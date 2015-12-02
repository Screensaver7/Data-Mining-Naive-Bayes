import csv
import math

def openCSV(filename):
    #I don't if it should handle strings or not
    with open(filename,"r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        line = list(reader)

        #make the array column major 
        temp = [[0 for x in range(len(line))] for x in range(len(line[0]))]
        for i in range(len(line[0])):
            for j in range(len(line)):
                temp[i][j] = float(line[j][i])
                
        #I don't know if needed
        """
        for i in range(len(line)):
            line[i] = [float(x) for x in line[i]]
        """
        
        #TESTING PURPOSES
        for x in temp:
            print(x)
            
    return temp

#go to the link I email to understand why I did this to calculate the probability
def mean(listOfNum):
    return sum(listOfNum)/float(len(listOfNum))

def stddev(listOfNum):
    avg = mean(listOfNum)
    return math.sqrt(sum([pow(x-avg,2) for x in listOfNum])/float(len(listOfNum)-1))

def gaussianPdf(listOfNum,x):
    avg = mean(listOfNum)
    standDev = stddev(listOfNum)
    return (1/(standDev*math.sqrt(2*math.pi)))*math.pow(math.e,-1*math.pow((x-avg),2)/(2*standDev*standDev))

def main():
    data = openCSV("test.csv")
    classification = data[len(data)-1]

    #TESTING PURPOSES
    test = [1,2,3,4]
    avg = mean(test)
    dev = stddev(test)
    prob = gaussianPdf(test,3)
    print(avg)
    print(dev)
    print(prob)

main()
