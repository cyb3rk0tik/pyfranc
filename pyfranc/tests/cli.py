import unittest
import subprocess
from pyfranc import franc
from fixtures import fixtures

languageA = 'pol'
languageB = 'eng'
fixtureB = fixtures[languageB]['fixture']
hebrew = 'הפיתוח הראשוני בשנות ה־80 התמקד בגנו ובמערכת הגרפית'

class TestFrancCLI(unittest.TestCase):
    def test_cli(self):
        cli = 'pyfranc_cli'
        
        af = 'Alle menslike wesens word vry'
        no = 'Alle mennesker er født frie og'
        ptBr = 'O Brasil caiu 26 posições'

        # Version.
        from pyfranc import __version__
        self.assertEqual(subprocess.Popen([cli, '-v'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8'), __version__ + '\r\n',msg = '-v')
        
        self.assertEqual(subprocess.Popen([cli, '--version'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8'), __version__ + '\r\n',msg = '--version')

        # Help.
        h = subprocess.Popen([cli, '--h'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
        self.assertRegex(h, r'CLI to detect the language of text.', msg = '-h')

        help = subprocess.Popen([cli, '--h'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
        self.assertRegex(help, r'CLI to detect the language of text.', msg = '--help')

        # Main.
        self.assertEqual(subprocess.Popen([cli, '-s', af, '-t', '1'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8'), 'afr : 1.0\r\n', msg = 'argument')

        self.assertEqual(subprocess.Popen([cli, '-s', af, '-t', '2'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8').replace('\r\n', ' '), 'afr : 1.0 nld : 0.7419425564569173 ', msg = 'multiple argument')
 
        # Only.
        self.assertEqual(subprocess.Popen([cli, '-s', no, '-o', 'nob', 'dan', '-t', '1'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8'), 'nob : 1.0\r\n', msg = '-o')

        self.assertEqual(subprocess.Popen([cli, '-s', no , '--only', 'nob', 'dan', '-t', '1'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8'), 'nob : 1.0\r\n', msg = '--only')

        self.assertEqual(subprocess.Popen([cli, '-s', no, '-w', 'nob', 'dan', '-t', '1'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8'), 'nob : 1.0\r\n', msg = '-w')
        
        self.assertEqual(subprocess.Popen([cli, '-s', no , '--whitelist', 'nob', 'dan', '-t', '1'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8'), 'nob : 1.0\r\n', msg = '--whitelist')       
        
        # Ignore.
        self.assertEqual(subprocess.Popen([cli, '-s', '"' + ptBr + '"', '-i', 'por','glg', '-t', '1'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8'), 'lad : 1.0\r\n', msg = '-i')
        
        self.assertEqual(subprocess.Popen([cli, '-s', '"' + ptBr + '"', '--ignore', 'por','glg', '-t', '1'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8'), 'lad : 1.0\r\n', msg = '--ignore')
        
        self.assertEqual(subprocess.Popen([cli, '-s', '"' + ptBr + '"', '-b', 'por','glg', '-t', '1'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8'), 'lad : 1.0\r\n', msg = '-b')
        
        self.assertEqual(subprocess.Popen([cli, '-s', '"' + ptBr + '"', '--blacklist', 'por','glg', '-t', '1'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8'), 'lad : 1.0\r\n', msg = '--blacklist')

        # Min.
        self.assertEqual(subprocess.Popen([cli, '-s', 'the', '-m', '3', '-t', '1'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8'), 'sco : 1.0\r\n', msg = '-m')

        self.assertEqual(subprocess.Popen([cli, '-s', 'the', '-m', '4'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8'), 'und : 1\r\n', msg = '-m (unsatisfied)')

        self.assertEqual(subprocess.Popen([cli, '-s', 'the', '--minlength', '3', '-t', '1'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8'), 'sco : 1.0\r\n', msg = '--minlength')

        self.assertEqual(subprocess.Popen([cli, '-s', 'the', '--minlength', '4'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8'), 'und : 1\r\n', msg = '--minlength (unsatisfied)')
        
        # All.
        self.assertEqual(re.findall('\[(\'[a-zA-Z_]*\', [.0-9]*)]', subprocess.Popen([cli, '-a', '-s', af], stdout=subprocess.PIPE).communicate()[0].decode('utf-8'))[0:3], ["'afr', 1.0", "'nld', 0.7419425564569173", "'fry', 0.6610392457794343"], msg = '-a')
 
        self.assertEqual(re.findall('\[(\'[a-zA-Z_]*\', [.0-9]*)]', subprocess.Popen([cli, '--all', '-s', af], stdout=subprocess.PIPE).communicate()[0].decode('utf-8'))[0:3], ["'afr', 1.0", "'nld', 0.7419425564569173", "'fry', 0.6610392457794343"], msg = '--all')
         

if __name__ == '__main__':
    unittest.main()
    