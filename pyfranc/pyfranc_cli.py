# -*- coding: utf-8 -*
#!/usr/bin/env python3

from argparse import ArgumentParser
from .franc import *

def main():
    parser = ArgumentParser()
    parser.add_argument("-s", "--string", 
                        dest="string", type=str, required=True,
                        help="Input string.")                         
                        
    parser.add_argument("-t", "--top",
                        dest="top", default=5, type=int, 
                        help="Print top results.")
                        
    parser.add_argument("-m", "--minlength",
                        dest="minlength", default=10, type=int, 
                        help="Minimum string length  to accept.")
                        
    parser.add_argument("-w", "--whitelist", nargs="*",  
                        dest="whitelist", default=[], 
                        help="Allow languages.")
                        
    parser.add_argument("-b", "--blacklist", nargs="*",
                        dest="blacklist", default=[], 
                        help="Disallow languages.")
                        
    parser.add_argument("-p", "--percentage",
                        dest="perc", action="store_true", default=False,
                        help="Print relative match value (in percent).")                           
                                 
    args = parser.parse_args()

    if args.string:
        result = lang_detect(value = args.string, minlength = args.minlength, whitelist = args.whitelist, blacklist = args.blacklist)
        for top in result[:args.top]:
            if not args.perc:
                print(top[0] + ' : ' + str(top[1]))
            else:
                print(top[0] + ' : ' + str(round(100 / sum(v for name, v in result[:args.top]) * top[1])) + '%')

if __name__ == "__main__":
    main()
