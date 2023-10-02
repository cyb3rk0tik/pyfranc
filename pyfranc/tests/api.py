from fixtures import fixtures
from pyfranc import franc
import unittest

languageA = 'pol'
languageB = 'eng'
fixtureB = fixtures[languageB]['fixtures']
hebrew = 'הפיתוח הראשוני בשנות ה־80 התמקד בגנו ובמערכת הגרפית'

class TestFrancAPI(unittest.TestCase):
    def test_franc_single(self):
        self.assertEqual(type(franc.lang_detect('XYZ')[0][0]), str, msg = 'should return a string')
        
        self.assertEqual(franc.lang_detect('XYZ')[0][0], 'und', msg = 'should return "und" on an undetermined value')
        
        self.assertEqual(franc.lang_detect('the the the the the ')[0], 'sco', msg = 'should work on weird values')

        # Inspired by lifthrasiir on hackernews:
        # https://news.ycombinator.com/item?id=8405672 
        self.assertEqual(franc.lang_detect(''.join([
        '한국어 문서가 전 세계 웹에서 차지하는 비중은 2004년에 4.1%로, 이는 영어(35.8%), ',
        '중국어(14.1%), 일본어(9.6%), 스페인어(9%), 독일어(7%)에 이어 전 세계 6위이다. ',
        '한글 문서와 한국어 문서를 같은것으로 볼 때, 웹상에서의 한국어 사용 인구는 전 세계 ',
        '69억여 명의 인구 중 약 1%에 해당한다.'
        ]))[0][0], 'kor', msg = 'should work on unique-scripts with many latin characters (1)')

        self.assertEqual(franc.lang_detect(''.join([
        '現行の学校文法では、英語にあるような「目的語」「補語」などの成分はないとする。',
        '英語文法では "I read a book." の "a book" はSVO文型の一部をなす目的語であり、',
        'また、"I go to the library." の "the library" ',
        'は前置詞とともに付け加えられた修飾語と考えられる。'
        ]))[0][0], 'jpn', msg = 'should work on unique-scripts with many latin characters (2)')

        self.assertEqual(franc.lang_detect('すべての人は、生命、自由及び身体の安全に対する権利を有する。')[0][0], 'jpn', msg = 'should detect Japanese even when Han ratio > 0.5 (udhr_jpn art 3) (1)')

        self.assertEqual(franc.lang_detect(''.join([
        'すべての人は、憲法又は法律によって与えられた基本的権利を侵害する行為に対し、',
        '権限を有する国内裁判所による効果的な救済を受ける権利を有する。'
        ]))[0][0], 'jpn', msg = 'should detect Japanese even when Han ratio > 0.5 (udhr_jpn art 8) (2)')

        self.assertEqual(franc.lang_detect(''.join([
        '成年の男女は、人種、国籍又は宗教によるいかなる制限をも受けることなく、婚姻し、',
        'かつ家庭をつくる権利を有する。成年の男女は、婚姻中及びその解消に際し、',
        '婚姻に関し平等の権利を有する。婚姻は、婚姻の意思を有する両当事者の自由かつ完全な合意によってのみ成立する。',
        '家庭は、社会の自然かつ基礎的な集団単位であって、社会及び国の保護を受ける権利を有する。'
        ]))[0][0], 'jpn', msg = 'should detect Japanese even when Han ratio > 0.5 (udhr_jpn art 16) (3)')

        self.assertNotEqual(franc.lang_detect(fixtureB, blacklist = [franc.lang_detect(fixtureB)[0]]), franc.lang_detect(fixtureB), msg = 'should accept `ignore`')

        self.assertEqual(franc.lang_detect(fixtures['aii']['fixtures'], blacklist = ['aii'])[0][0], 'und', msg =  'should support `ignore` if the script can only be in that language')
        
        self.assertEqual(franc.lang_detect(fixtureB, whitelist = [languageA])[0], languageA, msg =  'should accept `only`')

        self.assertEqual(franc.lang_detect(hebrew, whitelist = ['eng'])[0], 'und', msg = 'should accept `only` for different scripts')

        self.assertEqual(franc.lang_detect('the', minlength = 3)[0], 'sco', msg = 'should accept `minLength` (1)' )

        self.assertEqual(franc.lang_detect('the', minlength = 4)[0][0], 'und', msg = 'should accept `minLength` (2)' )

        self.assertEqual(franc.lang_detect('987 654 321')[0][0], 'und', msg = 'should return `und` for generic characters')

    def test_franc_all(self): 
        self.assertEqual(franc.lang_detect('XYZ'), [['und', 1]], msg = 'should return an array containing language--probability tuples')

        self.assertEqual(franc.lang_detect('פאר טסי'), [['und', 1]], msg = 'should return `[["und", 1]]` without matches (1)')
               
        self.assertEqual(franc.lang_detect('פאר טסי', minlength = 3),[['heb', 0], ['ydd', 0]], msg = 'should return `[["und", 1]]` without matches (2)')

        self.assertEqual(franc.lang_detect('xyz'),[['und', 1]], msg = 'should return `[["und", 1]]` without matches (3)')

        # not equal because missing 1 (value) argument
#        self.assertEqual(franc.lang_detect(), 'und', msg = 'should return "und" on a missing value')

        self.assertEqual(franc.lang_detect('987 654 321'),[['und', 1]], msg = 'should return `[["und", 1]]` for generic characters')
        
        self.assertEqual(franc.lang_detect('the the the the the ')[:2],[['sco', 1.0],['eng', 0.9889001009081736]], msg = 'should work on weird values')
         
        self.assertEqual(franc.lang_detect(fixtureB)[0] in franc.lang_detect(fixtureB, blacklist = [franc.lang_detect(fixtureB)[0][0]]), False, msg = 'should accept `ignore`')

        self.assertEqual(franc.lang_detect(fixtureB, whitelist = [languageA]), [[languageA, 1]], msg = 'should accept `only`')       

        self.assertEqual(franc.lang_detect(hebrew, whitelist = [eng]), [['und', 1]], msg = 'should accept `only` for different scripts')       

        self.assertEqual(franc.lang_detect('the'[0:3], minlength=3)[:2],[['sco', 1.0],['eng', 0.9988851727982163]], msg = 'should accept `minLength` (1)')

        self.assertEqual(franc.lang_detect('the', minlength=4),[['und', 1]], msg = 'should accept `minLength` (2)') 

    def test_algorithm(self): 
        ignore = ['bos', 'prs']

        for code in fixtures:
            info = fixtures[code]
            if info['iso6393'] in ignore: continue 
            self.assertEqual(franc.lang_detect(info['fixtures'])[0][0], info['iso6393'], msg = info['fixtures'].replace('\n', '\n\n')[0:21] + '... (' + info['iso6393'] + ')')

if __name__ == '__main__':
    if languageA != franc.lang_detect(fixtureB)[0][0]: print('a and b should not be equal...')
    unittest.main()
    