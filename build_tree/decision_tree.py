from sklearn import tree
import numpy as np
import csv
def get_features_lables(file_name):

    labels = []
    with open(file_name, 'r') as train_file:

        rows = csv.reader(train_file)
        labels = []
        features = []
        for index,line in enumerate(rows):

            if index == 0:
                continue

            feature_line = list(line)


            if feature_line[2] == '2':
                labels.append(1) # tues egual a 1
            else:
                labels.append(0)

            feature_line.pop(2)

            features_temp = []

            for item in feature_line:

                if item != '':

                    features_temp.append(int(item))
                else:
                    features_temp.append(0)

            features.append(features_temp)

    return features, labels


def test_data(classifier, features_vector):

    result = classifier.predict(features_vector[0])

    labels = features_vector[1]

    total_correct = 0
    for index, item in enumerate(labels):

        if item == result[index]:
            total_correct += 1

    print('a precisao eh ' + str(total_correct / len(labels)))


features_vectors = get_features_lables('../data/train_data.csv')
X = np.array(features_vectors[0])
deads =0
for i in features_vectors[1]:
    if i == 1:
        deads += 1

print( ' numero de mortos ' + str(deads))
print('portencagem de mortos: ' + str(deads / len(features_vectors[1])))
print( 'total pessoas ' + str(len(features_vectors[1])) )

y = np.array(features_vectors[1])


print('------------ Gini | splitter best ---------------------')
clf = tree.DecisionTreeClassifier(criterion='gini', splitter='best')
clf = clf.fit(X,y)
test_data(clf, get_features_lables('../data/test_data.csv') )

print('------------ Gini | splitter random---------------------')
clf = tree.DecisionTreeClassifier(criterion='gini', splitter='random')
clf = clf.fit(X,y)
test_data(clf, get_features_lables('../data/test_data.csv') )

print('------------ Gini | splitter best | max_features = 20---------------------')
clf = tree.DecisionTreeClassifier(criterion='gini', splitter='best', max_features=20)
clf = clf.fit(X,y)
test_data(clf, get_features_lables('../data/test_data.csv') )


print('------------ Entropy | splitter best ---------------------')
clf = tree.DecisionTreeClassifier(criterion='entropy', splitter='best')
clf = clf.fit(X,y)
test_data(clf, get_features_lables('../data/test_data.csv') )

print('------------ Entropy | splitter random---------------------')
clf = tree.DecisionTreeClassifier(criterion='entropy', splitter='random')
clf = clf.fit(X,y)
test_data(clf, get_features_lables('../data/test_data.csv') )

print('------------ Entropy | splitter best | max_features = 20---------------------')
clf = tree.DecisionTreeClassifier(criterion='entropy', splitter='best', max_features=20)
clf = clf.fit(X,y)
test_data(clf, get_features_lables('../data/test_data.csv') )
