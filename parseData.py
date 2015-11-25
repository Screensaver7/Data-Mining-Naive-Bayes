import sys
import gzip
import json

def parse(filename):
    f = gzip.open(filename, 'r')
    entry = {}
    for l in f:
        l = l.strip()
        l = unicode(l, errors = 'replace')
        colonPos = l.find(':')
        if colonPos == -1:
            yield entry
            entry = {}
            continue
        eName = l[:colonPos]
        rest = l[colonPos+2:]
        entry[eName] = rest
    yield entry

for e in parse("finefoods.txt.gz"):
    #print json.dumps(e)
    
    ##product/productId
    ##review/userId
    ##review/profileName
    ##review/helpfulness
    ##review/score
    ##review/time
    ##review/summary
    ##review/text
    print e['review/profileName']
