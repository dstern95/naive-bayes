import matplotlib.pyplot as plt
import numpy as np

def main():
    f1 =open('confusionmatrix.txt','r')
    f1.readline()
    cmatrix = []
    for line in f1:
        line= line.replace('\t\n','')
        line = line.split('\t')
        cmatrix.append(line)
    tp =0
    tn =0
    fp = 0
    fn = 0
    #print(cmatrix)

    f1.close()

        #gets the data for the roc graphs
    f2 = open('allresults.txt','r')
    l1 =f2.readline()
    l1 = l1.replace('\n','')
    l1=l1.split('\t')
    l1.pop(0)
    l1.pop(0)
    l1.pop(0)
    classes=l1
    scenerios = []
    for line in f2:
        line = line.replace('\n','')
        line = line.split('\t')
        line.pop(0)
        line.pop(0)
        scenerios.append(line)
    f2.close()
    

    #confusion matrix stuff
    for i in range(len(cmatrix)):
        tp =0
        tn =0
        fp = 0
        fn = 0
        for n in range(len(cmatrix)):
            for x in range(len(cmatrix)):
                if n == x and n==i:
                    tp+= int(cmatrix[n][x])
                elif n != x and n == i:
                    #print(cmatrix[n][x],n,x,i)

                    fp += int(cmatrix[n][x])
                elif i==x and i!=n:
                    #print(cmatrix[n][x],n,x,i)
                    fn+=int(cmatrix[n][x])
                else:

                    tn += int(cmatrix[n][x])

        print(classes[i])
        print('tp',tp)
        print('tn',tn)
        print('fp',fp)
        print('fn',fn)


        sensitivity = tp/(tp+fn)
        specificity = tn/(tn+fp)
        precision = tp/(tp+fp)
        accuracy = (tp+tn)/(tp+tn+fp+fn)
        print('sensitivity',sensitivity)
        print('specificity',specificity)
        #print('precision',precision)
        #print('accuracy',accuracy)



    #print(scenerios)
    totsenslist = []
    totspeclist =[]

    #no duplicates
    totsenslist2 = []
    totspeclist2 =[]
    for i in range(len(classes)):
        senslist =[]
        speclist = []

        #no duplicates
        senslist2 =[]
        speclist2 = []
        for nt in range(0,11,1):
            t = nt/10
            tp =0
            tn =0
            fp = 0
            fn =0
        
            for item in scenerios:
                if float(item[i+1])>= t:
                    if classes[i] == item[0]:
                        tp +=1
                    else:
                        fp += 1
                else:
                    if classes[i] == item[0]:
                        fn +=1
                    else:
                        tn+=1
            #print(t,tp+fp)
            sensitivity = tp/(tp+fn)
            specificity = tn/(tn+fp)
            senslist.append(sensitivity)
            speclist.append(1-specificity)
            if sensitivity not in senslist2 and (1-specificity) not in speclist2:
                senslist2.append((sensitivity))
                speclist2.append((1-specificity))

        senslist2.reverse()
        speclist2.reverse()
        totsenslist.append(senslist)
        totspeclist.append(speclist)
        totsenslist2.append(senslist2)
        totspeclist2.append(speclist2)



    #plt.figure(4)
    
    #grid = gridspeck.GridSpeck(len(class

    
    #s1='\t'.join(senslist2)
    #s2='\t'.join(speclist2)
    #print(s1)
    #print(s2)
    #senslist2.reverse()
    #speclist2.reverse()
    for i in range(len(classes)):
        

        plt.plot(totspeclist[i],totsenslist[i])
        plt.xlabel('1-specificity')
        plt.ylabel('sensitivity')
        plt.title(classes[i])
        plt.show()

        print(classes[i])
        auc = np.trapz(totsenslist2[i],totspeclist2[i])
        #auc = np.trapz(totspeclist2[i],totsenslist2[i])
        print("auc =",auc)
        

    

            

    #yrate.append(sensitivity)
    #xrate

    
    #print('plotting')


    #plt.plot(xrate, yrate)
    #plt.plot(.20,.30)
    #plt.show()
    #auc = np.trapz(xrate,yrate)
    #print(y)
    #print(x)
    #print(auc)
    
main()
