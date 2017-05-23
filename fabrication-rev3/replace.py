#!/usr/bin/python
#
# This is a program to take two Macrofab XYRS files and if the X, Y coordinates in the A file do not match the B file, it will auto correct.
# parts that are not in the B file but are in the A file will not be copied over. We'll let Macrofab read the kicad file and figure that out. 
#

# file with good placement
a = open("rev9_bom.xyrs")
# file with old placement
b = open("rev3_bom.xyrs")

partsa = {}
partsb = {}

# load parts into hashes
for line in a:
    parts = line.split()
    partsa[parts[0]] = line.rstrip()
    
for line in b:
    parts = line.split()
    partsb[parts[0]] = line.rstrip()

for k in partsa.keys():
    cols_a = partsa[k].split()
    try:
        cols_b = partsb[k].split()
    except KeyError:
        print "part missing:"
        print partsa[k]
        continue
        
    if cols_a[1] != cols_b[1] or cols_a[2] != cols_b[2] or cols_a[3] != cols_b[3]:
        print "--------------------------error!---------------------"
        print "in A:"
        print partsa[k]
        print "in B:"
        print partsb[k]
        # to correct this, we will take placement data from (A) which is the new, good file
        # and we will move that data to (B)

        cols_b[1] = cols_a[1]
        cols_b[2] = cols_a[2]
        cols_b[3] = cols_a[3]

        partsb[k] = '\t'.join(cols_b)
        print "fix:"
        print partsb[k]



o = open("out.xyrs","w")
for k in partsb.keys():
    cols = partsb[k].split()
    for i in range(0, 14):
        try:
            print >>o, cols[i], "\t",
        except IndexError:
            print >>o, "\t",
    print >>o
        

