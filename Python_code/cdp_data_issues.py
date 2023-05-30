import re
import csv
import logging
import argparse
import sys

if __name__== "__main__" :

    parser=argparse.ArgumentParser(description='command line argument for non-interactive execution.',formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-i','--inputfile',help='path of input file',required=True)
    parser.add_argument('-o', '--outputfile', help='path of output file', required=True)
    parser.add_argument('-c', '--columncount', help='Number of column to be extracted', required=True)

    args=parser.parse_args()
    inputfile=args.inputfile
    outputfile=args.outputfile
    columncount=args.columncount



    try:
        CSV_SPLIT_RE =re.compile(r'''
        (
        [^,"]*?  #Either a series of non-double quote charcter
        |        #or
        "        #double quotes followed by
        [^"]*(?:"[^,"]*"[^"]*)* # Match either a non-qiote,or 2 consequent double qotes inside double quotation mark
        "        #Followed by closing double quote
        )
        (?:,|$)  #Followed by a commna or the end of string
        ''',re.VERBOSE)

        inputfile=open(args.inputfile)
        Data=inputfile.readlines()
        print(Data)
        for line in Data:
            quoted_values=CSV_SPLIT_RE.findall(line.rstrip('\r\n')) if line.rstrip('\r\n').endswith(
                ',') else CSV_SPLIT_RE.findall(line.rstrip('\r\r'))
            print(quoted_values[2])
            find_row=quoted_values[0:3]
            print(find_row)
            s=','.join(find_row)
            print(s)
            with open(outputfile,"w") as f:
                f.write("{}\n".format(s))
    except Exception as e:
        print(e)


