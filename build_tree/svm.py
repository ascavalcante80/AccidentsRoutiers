import csv
import pickle
from sklearn import svm
import numpy as np


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
    correct_dead = 0
    deads = 0
    for index, item in enumerate(labels):

        if item == result[index]:
            total_correct += 1

        if result[index]== 1 and item ==1:
            correct_dead += 1

        if item == 1:
            deads +=1

    print('a precisao eh ' + str(total_correct / len(labels)))
    print('usando metodo score' + str(classifier.score(features_vectors[0], features_vectors[1])))
    print(' total de mortos no test : ' + str(deads))
    print('total classificados como mortos: ' + str(correct_dead))
    print(' porcentagem correcta de classficada com morta:' + str(correct_dead/deads))

try:
    features_vectors = pickle.load(open('features.pk', 'rb'))
except FileNotFoundError:
    features_vectors = get_features_lables('../data/train_data.csv')
    pickle.dump(features_vectors, open('features.pk', 'wb'))


X = np.array(features_vectors[0])
deads =0
for i in features_vectors[1]:
    if i == 1:
        deads += 1

# print( ' numero de mortos ' + str(deads))
# print('portencagem de mortos: ' + str(deads / len(features_vectors[1])))
# print( 'total pessoas ' + str(len(features_vectors[1])) )

y = np.array(features_vectors[1])
features_test = get_features_lables('../data/test_data.csv')


print('------------ SVM ---------------------')
clf = svm.SVC()
clf = clf.fit(X,y)
test_data(clf,  features_test)
# print('------------ Estimators 30 ---------------------')
# clf = RandomForestClassifier(n_estimators=30, )
# clf = clf.fit(X,y)
# test_data(clf,  features_test)
# print('------------ Estimators 20 ---------------------')
# clf = RandomForestClassifier(n_estimators=20, )
# clf = clf.fit(X,y)
# test_data(clf,  features_test)
# print('------------ Estimators 10 ---------------------')
# clf = RandomForestClassifier(n_estimators=10, )
# clf = clf.fit(X,y)
# test_data(clf,  features_test)
#
# print('------------ Estimators 40 | entropy ---------------------')
# clf = RandomForestClassifier(n_estimators=40, criterion='entropy')
# clf = clf.fit(X,y)
# test_data(clf,  features_test)
# print('------------ Estimators 30 ---------------------')
# clf = RandomForestClassifier(n_estimators=30, criterion='entropy')
# clf = clf.fit(X,y)
# test_data(clf,  features_test)
# print('------------ Estimators 20 ---------------------')
# clf = RandomForestClassifier(n_estimators=20, criterion='entropy')
# clf = clf.fit(X,y)
# test_data(clf,  features_test)
# print('------------ Estimators 10 ---------------------')
# clf = RandomForestClassifier(n_estimators=10, criterion='entropy')
# clf = clf.fit(X,y)
# test_data(clf,  features_test)
#
