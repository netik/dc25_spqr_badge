#!/usr/bin/python
import csv

state=0

row={}
comps={}

def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z

with open('scrape', 'r+') as f:
    lines = f.readlines()
    i=0
    while i < len(lines):
        line = lines[i]
        if line.startswith(' SEARCH FOR PARTS'):
            state = 1
            if i+3 > len(lines):
                i=i+1
                continue
                
            row['part']=lines[i+1].lstrip().rstrip()
            row['value']=lines[i+5].lstrip().rstrip()
            row['description']=lines[i+7].lstrip().rstrip()
            row['components']=lines[i+9].lstrip().rstrip()
            i = i + 3

        if line.startswith("PARTS$"):
            row['partcost'] = line.replace('PARTS$','').lstrip().rstrip()

        if line.startswith("LABOR$"):
            row['laborcost'] = line.replace('LABOR$','').lstrip().rstrip()

        if line.startswith('MARKETCONSIGNINVENTORY'):
            # link comps
            for comp in row['components'].split():
                comps[comp] = row
                
            # print record
            print row
            row = {}
            state = 0
        i=i+1

f.close()

with open('bom.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['reference_designator', 'qty', 'mpn','value','description', "partcost","laborcost"])
#    writer = csv.DictWriter(csvfile, fieldnames=['reference_designator', 'qty', 'mpn','value','description'])
    writer.writeheader()
    for comp in sorted(comps.keys()):
        writer.writerow({'reference_designator' : comp,
                         'qty' : 1 ,
                         'mpn' : comps[comp]['part'],
                         'value' : comps[comp]['value'],
                         'description' : comps[comp]['description'],
                         'partcost' : comps[comp]['partcost'],
                         'laborcost' : comps[comp]['laborcost'],
        })

    
#        writer.writerow({'reference_designator' : comp,
#                               'qty' : 1 ,
#                               'mpn' : comps[comp]['part'],
#                               'value' : comps[comp]['value'],
#                               'description' : comps[comp]['description']})

    

