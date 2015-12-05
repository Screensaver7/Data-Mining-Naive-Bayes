## Naive Bayes with k-Fold Cross Validation
## Zhaozhuo Li, Joseph Wang
## CS484
## Input: # of folds
## Output: Classification errors
##
## Example: python naivebayes.py dataset.csv 5

import csv
import math
import operator
from random import sample, seed, randint
from sys import argv
from datetime import datetime

## Loads file into memory
def openCSV(filename, k):

    csvfile = open(filename,"r")
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    line = list(reader)
    #removes attrib names
    del line[0]
    col_count = len(line[0])
    row_count = len(line)
    size = row_count
    kparts = []
    #3 dimensional array
    #kparts[fold#][attribute][class label]
    for i in range(k):
        attribs = []
        for j in range(col_count - 1):
            lblclass = []
            for l in line:
                lblclass.append(l[col_count - 1])
            lblclass = set(lblclass)
            val = [[] for x in range(len(lblclass))]
            lblclass = dict(zip(lblclass, val))
            attribs.append(lblclass)
        kparts.append(attribs)

    #random sampling w\o replacement
    c = sample(range(0, row_count), row_count)
    test = randint(0, k - 1)
    #save test data
    testdata = []
    for i in range(row_count):
        l = line[i]
        #one partition saved for testing
        if (c[i]%k == test):
            testdata.append(l)
        else:
            for j in range(col_count - 1):
                #kparts[fold#][attribute][class label]
                kparts[c[i]%k][j][l[col_count-1]].append(float(l[j]))
    csvfile.close()
    #delete test data in training partition
    del kparts[test]
    return kparts, testdata

def mean(listOfNum):
    if (len(listOfNum) == 0): return 0
    return sum(listOfNum)/float(len(listOfNum))

def stddev(listOfNum):
    avg = mean(listOfNum)
    return math.sqrt(sum([pow(x-avg,2) for x in listOfNum])
                     /float(len(listOfNum)-1))

def gaussianPdf(avg, standDev ,x):
    return (1/(standDev*math.sqrt(2*math.pi)))*\
           math.pow(math.e,-1*\
           math.pow((x-avg),2)/\
           (2*standDev*standDev))

def main(arg):
    seed(datetime.now())
    data = openCSV(arg[0], int(arg[1]))
    test = data[1]
    data = data[0]
    cols_count = len(test[0])
    rows_count = len(test)
    keys = data[0][0].keys()
    train = []
    for attribs in range(cols_count - 1):
        train.append(dict(zip(keys, [[] for x in range(len(keys))])))
    #combine testing folds
    for parts in data:
        for i in range(cols_count - 1):
            for word in parts[i]:
                for array in parts[i][word]:
                    train[i][word].append(array)
    del data
    #calculate mean and stddev first
    for attrib in train:
        for key in keys:
            newval = [mean(attrib[key]), stddev(attrib[key])]
            attrib[key] = newval
    #test training
    count = 0
    for t in test:
        prob = dict(zip(keys, [[] for x in range(len(keys))]))
        for i in range(cols_count - 1):
            for k in keys:
                attrib_prob = gaussianPdf(train[i][k][0],
                                          train[i][k][1],
                                          float(t[i]))
                if (i == 0):
                    prob[k] = attrib_prob
                else:
                    prob[k] = prob[k] * attrib_prob
        total = sum(prob.values())
        for k in keys:
            prob[k] = prob[k] / total

        #best match, actual class
        if (max(prob.iteritems(), key=operator.itemgetter(1))[0] ==
            t[cols_count - 1]): count+=1
    #accuracy for one run
    return count/float(rows_count)

if __name__ == "__main__":
    results = []
    for i in range(int(argv[2])):
        print '%d...' % (i+1),
        results.append(main(argv[1:]))
    print '\nAccuracy: %.04f' % (sum(results)/float(len(results)))
