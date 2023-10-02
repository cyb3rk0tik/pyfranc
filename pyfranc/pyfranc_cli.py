# -*- coding: utf-8 -*
#!/usr/bin/env python3

from argparse import ArgumentParser
from pyfranc import franc
from pyfranc import iso639

def main():
    parser = ArgumentParser(description = f'CLI to detect the language of text.')
    parser.add_argument("-v", "--version",
                        dest="version", action="store_true", default=False,
                        help="Print version number.")                         
 
    parser.add_argument("-s", "--string", 
                        dest="string", type=str,
                        help="Input string.") #, required=True                        
                        
    parser.add_argument("-t", "--top",
                        dest="top", default=5, type=int, 
                        help="Print top results.")
                        
    parser.add_argument("-m", "--minlength",
                        dest="minlength", default=10, type=int, 
                        help="Minimum string length  to accept.")
                        
    parser.add_argument("-w", "--whitelist", "-o", "--only", nargs="*",  
                        dest="whitelist", default=[], 
                        help="Allow languages.")
                        
    parser.add_argument("-b", "--blacklist", "-i", "--ignore", nargs="*",
                        dest="blacklist", default=[], 
                        help="Disallow languages.")
                        
    parser.add_argument("-a", "--all",
                        dest="all", action="store_true", default=False,
                        help="Print all raw results.")
                        
    parser.add_argument("-f", "--full",
                        dest="full", action="store_true", default=False,
                        help="Print full name of language (with lang code).")
                        
    parser.add_argument("-p", "--percentage",
                        dest="perc", action="store_true", default=False,
                        help="Print relative match value (in percent).")                         
                                 
    args = parser.parse_args()

    code_name = iso639.code_to_name
  
    if args.version:
        from pyfranc import __version__
        print(__version__)
        
    if args.string:
        result = franc.lang_detect(value = args.string, minlength = args.minlength, whitelist = args.whitelist, blacklist = args.blacklist)
        if args.all: 
            print(result)
            quit()
        for top in result[:args.top]:
            if args.full: 
                if top[0] == 'und': top[0] = 'Undetermined (und)'
                else: top[0] = code_name[top[0]] + ' (' + top[0] + ')'
            if not args.perc:
                print(top[0] + ' : ' + str(top[1]))
            else:
                print(top[0] + ' : ' + str(round(100 / sum(v for name, v in result[:args.top]) * top[1])) + '%')

if __name__ == "__main__":
    main()
