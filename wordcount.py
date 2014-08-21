#!/usr/bin/python

import sys, getopt

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'wordcount.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'wordcount.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            file=open(inputfile,"r+")
            wordcount={}
            totalwords = 0
            for word in file.read().split():
                totalwords += 1
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
            for k,v in wordcount.items():
                print k, v
            print 'Total words: ' + str(totalwords) 

if __name__ == "__main__":
   main(sys.argv[1:])
