import csv

__author__ = 'alexandre cavalcante'

"""
    This script builds an unique CSV file using the data coming from different CSV files.
"""

data_folder = '../data/'
all_data = {}
fatal = 0
for year in range(2005,2016):

    usager_data = None
    vehicule_dic = {}
    caracteristiques_dic = {}
    lieux_dic = {}

    with open(data_folder + 'usagers_' + str(year) + '.csv') as usager_file:
        usager_data = [line for line in csv.reader(usager_file)]

    with open(data_folder + 'caracteristiques_' + str(year) + '.csv', encoding='iso-8859-1') as caracteristiques_file:

        for line in csv.reader(caracteristiques_file):
            caracteristiques_dic[line[0]] = line[1:]

    with open(data_folder + 'vehicules_' + str(year) + '.csv') as vehicules_file:
        for line in csv.reader(vehicules_file):
            vehicule_dic[line[0]] = line[1:]

    with open(data_folder + 'lieux_' + str(year) + '.csv') as lieux_file:
        for line in csv.reader(lieux_file):
            lieux_dic[line[0]] = line[1:]

    for index, row in enumerate(usager_data):

        if row[3] == '2':
            fatal +=1

        if index == 0:
            continue
        try:
            all_data [row[0]]= caracteristiques_dic[row[0]] + vehicule_dic[row[0]] + lieux_dic[row[0]]

        except KeyError:
            pass

print(str(fatal))
print(str(len(all_data)))



