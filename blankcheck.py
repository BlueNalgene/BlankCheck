#!/usr/bin/python

import csv
import os
import sys
import getopt
import itertools as IT

def main(argv):
    found_i = False
    csvtrue = True
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print 'blankcheck.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'blankcheck.py -i <inputfile>'
            sys.ext()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            found_i = True
            if not inputfile[-4:] == ".csv":
                csvtrue = False
    if csvtrue and not found_i:
        print "This code requires an input file argument '-i'"
        sys.exit(2)
    elif found_i and not csvtrue:
        print "This code requires you use a .csv file"
        sys.exit(2)
    print 'Running with Input file: ', inputfile
    with open(inputfile, 'rb') as csvfile:
        reader = csv.reader(csvfile)
    
        # This skips the first line (headers) in the CSV
        first_row = next(reader)
        num_cols = len(first_row)
        i = 2
        collist = []
        while i <= num_cols:
            collist.append("tmp" + str(i))
            i += 2
        csvfile.seek(0)   
        j = 2
        tempname = 'tmp' + str(j)
        f = open(tempname, 'wb')
        while j <= num_cols:
            f = open(tempname, 'wb')
            i = 1
            for row in reader:
                if not row[j-2] == '' and not row[j-1] == '' and not row[j-2] == ' ' and not row[j-1] == ' ':
                    f.write(row[j-2] + "," + row[j-1] + "\n")
                    i += 1
                else:
                    i += 1
            j += 2
            csvfile.seek(0)
            tempname = 'tmp' + str(j)
            
    print collist
    handles = [open(filename, 'rb') for filename in collist]    
    readers = [csv.reader(f, delimiter=',') for f in handles]
                
    with  open('combined.csv', 'wb') as h:
        writer = csv.writer(h, delimiter=',', lineterminator='\n', )
        for rows in IT.izip_longest(*readers, fillvalue=['']*2):
            combined_row = []
            for row in rows:
                row = row[:2] # select the columns you want
                if len(row) == 2:
                    combined_row.extend(row)
                else:
                    combined.extend(['']*2)
            writer.writerow(combined_row)
    
    k = 0
    num_cols = num_cols / 2 - 1
    while k <= num_cols:
        os.remove(collist[k])
        k += 1

    
if __name__ == "__main__":
   main(sys.argv[1:])
   
