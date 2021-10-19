# Pyfranc
Text language detection basic on trigrams.
Support [403](https://github.com/wooorm/franc/blob/main/packages/franc-all/readme.md#support) language from [franc-all](https://github.com/wooorm/franc/tree/main/packages/franc-all)

## Install

This package is tested in Python 3.8, but should work on the whole 3rd revision of Python.

[pip](https://pip.pypa.io/en/stable/installation/):

```python
pip install pyfranc
```

## Use
### How library

```python
from pyfranc import franc

franc.land_detect('Alle menslike wesens word vry')[0][0] # 'afr'
franc.lang_detect('এটি একটি ভাষা একক IBM স্ক্রিপ্ট')[0][0]  # 'ben'
franc.lang_detect('Alle menneske er fødde til fridom')[0][0] # 'nno'
franc.lang_detect('')[0][0] # 'und'

# You can change what’s too short (default: 10):
franc.lang_detect('the')[0][0] # 'und'
franc('the', minlength=3)[0][0] # 'sco'

[0][0] has taken first value (iso code lang) in first element in output array.
```

#### `whitelist`

```python
franc.lang_detect('Considerando ser essencial que os direitos humanos', whitelist = ['por', 'spa'])
# [['por', 1], ['spa', 0.6034146900423971]]
```

#### `blacklist`

```python
franc.lang_detect('Considerando ser essencial que os direitos humanos', blacklist = ['src', 'glg'])

#[['por', 1],
# ['ina', 0.6211756617394293], 
# ['spa', 0.6034146900423971], 
# ['ast', 0.5628509224246592], 
# ['oci', 0.5583820327718574]
# ... 310 more items]
```

### How CLI
CLI to detect the language of text.

```
usage: pyfranc_cli [-h] --string STRING [--top TOP] [--minlength MINLENGTH]
                   [--whitelist [WHITELIST [WHITELIST ...]]]
                   [--blacklist [BLACKLIST [BLACKLIST ...]]] [--percentage]

optional arguments:
  -h, --help            	show this help message and exit
  -s, --string 		string	Input string.
  -t, --top   		int  	Print top results (Default: 5)).
  -m, --minlength 	int		Minimum string length to accept (Default: 10).
  -w, --whitelist   [WHITELIST [WHITELIST ...]]
							Allow languages.
  -b, --blacklist   [BLACKLIST [BLACKLIST ...]]
							Disallow languages.
  -p, --percentage  bool     	Print relative match value (in percent).
```
					
usage:
```	
# output language
$ pyfranc_cli -t1 -s "Alle menslike wesens word vry"
# 'afr' : 1.0

# output language from stdin (expects utf8)
$ echo "এটি একটি ভাষা একক IBM স্ক্রিপ্ট" | pyfranc_cli -t 1 -s $0
# 'ben' : 1.0

# ignore certain languages
$ pyfranc_cli --blacklist por glg "O Brasil caiu 26 posições"
# 'vec' : 1.0

# output language from stdin with only
$ echo "Alle mennesker er født frie og" | pyfranc_cli -t 1 --whitelist nob dan -s $0
# 'nob' : 1.0'
```

## Derivation

Pyfranc is a outright port from [Franc](https://github.com/wooorm/franc) (JavaScript, MIT), 
[trigram-utils](https://github.com/wooorm/trigram-utils) (JavaScript, MIT),  [collapse-white-space](https://github.com/wooorm/collapse-white-space)
(JavaScript, MIT), and [n-gram](https://github.com/words/n-gram) (JavaScript, MIT). 
All this by [Titus Wormer](https://github.com/wooorm).

## License

[MIT](https://github.com/cyb3rk0tik/pyfranc/blob/main/LICENSE) © [cyb3rk0tik](https://github.com/cyb3rk0tik)

