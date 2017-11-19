import sys

def createPos(tot,attribute,poslist):
    slength = tot/len(attribute)
    i = 0
    position = 0
    for possibility in poslist:
        possibility.append(attribute[position])
        i+=1
        if i %slength == 0:
            position +=1
        if position == len(attribute):
            position = 0
    return poslist

def createCond(condproblist,scenerios,attributedictholder):
    for item in condproblist:
        i =0
        for line in scenerios:
            #
            if item[0] == line[item[2]] and item[1] == line[item[3]]:
                i+=1
        tot = attributedictholder[item[3]][item[1]]
        item[-1] = i/tot    
    return condproblist

def calcProb(attributeprediction,currentscenerio,condproblist,scenerios,attributedictholder,attributelist):

    #attributeprediction is the number pointing to the list of attributes that it could be when making the prediction
    predictionpercent= []
    for item in attributelist[attributeprediction]:
        pitem=attributedictholder[attributeprediction][item]/len(scenerios)
        i =0
        #print(pitem)
        for item2 in currentscenerio:
            if i != attributeprediction:
                for prob in condproblist:
                    if (prob[0] == item2 and prob[2] == i) and (prob[1] == item and attributeprediction == prob[3]):
                        #print(prob)
                        #print(pitem)
                        pitem = pitem*prob[-1]
            i+=1
        #print(pitem)
        predictionpercent.append(pitem)
    return predictionpercent
        
def main():
    training = sys.argv[1]
    trainfile = open(training,'r')
    attributelist = []
    scenerios = []
    data = False
    for line in trainfile:
        if "@attribute" in line:
            ln = line.split('{')
            ln2=ln[-1].replace('\n','')
            ln2=ln2.replace('{','')
            ln2=ln2.replace('}','')
            ln2 = ln2.replace(' ','')
            attributelist.append(ln2.split(','))

        if data == True and '%' not in line:
            line =line.replace('\n','')
            ln = line.split(',')
            scenerios.append(ln)
        if '@data' in line:
            data = True
    condproblist=[]
    attributedictholder =[]
    i =0 
    for attribute in attributelist:
        
        attributedict = {}

        for lattribute in attribute:
            n =0
            attributedict[lattribute] = 0
            for attribute2 in attributelist:
                for lattribute2 in attribute2:
                    if n != i:
                        prob=[lattribute,lattribute2,i,n,0]
                        condproblist.append(prob)
                n+=1
        attributedictholder.append(attributedict)            
        i +=1
    #print(len(condproblist))
    #print(condproblist)
    #print(len(attributedict))
    #print(len(scenerios))
    #print(scenerios)
    #print(attributedictholder[1])
    for line in scenerios:
        i =0

        for item in line:
            #print(item)
            #print(attributedictholder[i])
            attributedictholder[i][item] =attributedictholder[i][item]+1
            i+=1
    #print(attributedictholder[2])
    #print(condproblist)
    condproblist=createCond(condproblist,scenerios,attributedictholder)
    #print(condproblist)

    trainfile.close()


    ''' reading the input file and making predicitons'''

    
    inputfile = open(sys.argv[2],'r')

    predictionfile = open(sys.argv[3],'w')
    data = False
    inputscenerios = []
    for line in inputfile:

        if data == True and '%' not in line:
            line =line.replace('\n','')
            ln = line.split(',')
            if len(ln) == len(scenerios[0]):
                ln.pop()
            inputscenerios.append(ln)
        if '@data' in line:
            data = True
    inputfile.close()

    
    attributeprediction =len(scenerios[0])-1
    predheader = "prediction"
    for item in attributelist[-1]:
        predheader+='\t'
        predheader +=item
    predheader += '\n'
    predictionfile.write(predheader)

    n= 1
    for currentscenerio in inputscenerios:
        rlist=calcProb(attributeprediction,currentscenerio,condproblist,scenerios,attributedictholder,attributelist)
        line = str(n)+'.\t'
        pline=""
        n+=1
        maxprob=-1
        maxname=''
        equilizer = 0
        for i in range(len(rlist)):
            prob = rlist[i]
            equilizer+=prob
        for i in range(len(rlist)):
            prob = rlist[i]
            prob = prob/equilizer
            if prob>maxprob:
                maxprob = prob
                maxname = attributelist[-1][i]
            pline += '\t'
            pline += str(prob)
        line += maxname
        line += pline
        line +='\n'
        predictionfile.write(line)
    predictionfile.close()
    print('done')

main()
