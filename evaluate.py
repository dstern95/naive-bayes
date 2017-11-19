import os
import sys
import matplotlib.pyplot as plt
import numpy as np

def createtraining(attributelines,datalines):
    trainfile = open('training.txt','w')
    for line in attributelines:
        trainfile.write(line)
    ln = '@data \n'
    trainfile.write(ln)
    for line in datalines:
        trainfile.write(line)
    trainfile.close()
    

def main():
    origfile = open(sys.argv[1],'r')
    attributelines =[]
    datalines = []
    data = False
    datalist= []
    for line in origfile:
        if '@attribute' in line:
            attributelines.append(line)
        if data == True and '%' not in line:
            ln = line
            ln=ln.replace('\n','')
            ln=ln.split(',')
            datalist.append(ln)
            datalines.append(line)
        if '@data' in line:
            data = True
    origfile.close()
    createtraining(attributelines,datalines)
    tp =0
    tn =0
    fp = 0
    fn =0
    tot = 0
    confusionmatrix = []
    confusionkey = {}
    predattribute = []

    #get the attributes for the predicted attribute
    line = attributelines[-1]
    ln = line.split('{')
    ln2=ln[-1].replace('\n','')
    ln2=ln2.replace('{','')
    ln2=ln2.replace('}','')
    ln2 = ln2.replace(' ','')
    predattribute = ln2.split(',')
    n= 0
    predictionname =['prediction','actual']

    for item in predattribute:
        itemlist = []
        for i in range(len(predattribute)):
            itemlist.append(0)
        confusionmatrix.append(itemlist)
        confusionkey[item] = n
        n+=1
        predictionname.append(item)

            
    percentdata= []
    percentdata.append(predictionname)
    
    for i in range(len(datalines)):
        tlist = []
        for x in range(len(datalines)):
            if x != i:
                tlist.append(datalines[x])
        createtraining(attributelines,tlist)
        valfile = open('validation.txt','w')
        ln = '@data \n'
        valfile.write(ln)
        valfile.write(datalines[i])
        valfile.close()
        os.system('Python3 naivebayes.py training.txt validation.txt result.txt')
        #print('opening')
        results = open('result.txt','r')
        results.readline()
        result = results.readline()
        result = result.split('\t')
        


        #print(list(result[1]),list(datalist[i][-1]))
        if result[1] == datalist[i][-1]:
            
            tp +=1
        else:
            fp += 1
        confusionmatrix[confusionkey[result[1]]][confusionkey[datalist[i][-1]]] += 1
        result.pop(0)
        result.insert(1,datalist[i][-1])
        percentdata.append(result)
        #print(result)
        tot +=1
    print(tp)
    print(fp)
    print(tp/tot)

    f1 = open('confusionmatrix.txt','w')
    f1.write(attributelines[-1])
    for item in confusionmatrix:
        line = ''
        for item2 in item:
            line += str(item2)
            line +='\t'
        line+='\n'
        f1.write(line)
    f1.close()
    f2 = open('allresults.txt','w')
    for i in range(len(percentdata)):
        line = ''
        for item in percentdata[i]:
            line +='\t'
            line+= str(item)
        if i == 0:
            line+='\n'
        
    
        f2.write(line)
    f2.close()
    #print('plotting')
    #plt.plot(fp/tot,tp/tot)
    #plt.show()
    #auc = np.trapz(fp/tot,tp/tot)
    #print(auc)

    
main()
