#This is an example of using SciKit-Learn to match data with features and labels.
#You can try to match height, years old and weight
from sklearn import tree


#Features file example [height, years old, weight]
with open('features') as ins:
    ins = ins.read().splitlines()
    features = []
    for line in ins:
        line = line.split(",")
        features.append(line)

print (features) #Show data imported from the file

#Labels has names of the features match
with open('labels') as ins:
    ins = ins.read().splitlines()
    labels = []
    for line in ins:
        labels.append(line)

print (labels) #Show data imported from the file

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print ("Insert Informations: ")
print ("Height: ")
height = input()
print ("Years: ")
years = input()
print ("Weight: ")
weight = input()

print (clf.predict([[height, years, weight]]))
print (clf.score(features, labels))