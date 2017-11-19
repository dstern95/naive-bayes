Readme Naive Bayes

runnable programs:
naivebayes.py
evaluate.py
getstats.py
---------------
naivebayes.py
to run: python3 naivebayes.py [trainingfile] [inputfile] [resultfile]

will use the training set to build conditional probabilties then make prediciton on the input file on what the last attribute should be. It writes down what it predicted along with the normalized probablity in the result text.
----------------
evaluate.py
to run:python3 evaluate.py [datafile]

will run naivebayes.py with leave-one-out cross validation it produces a inverted confusion matrix in confusionmatrix.txt and a file with the prediction the actual result and the probablities in allresults.txt

-----------------
getstats.py
to run:python3 getstats.py

Needs evaluate to have been run before it as it uses files generated. Uses the confusion matrix from confusionmatrix.txt to print out the TP,TN,FP,FN to make a table for each class along with printing the sensitivity and specificity. After that it will produce a labeled ROC curve one class at a time in matplotlib along with printing out the AUC values 

