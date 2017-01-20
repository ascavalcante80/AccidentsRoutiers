import csv
import calendar

__author__ = 'alexandre cavalcante'

"""
    This script builds an unique CSV file using the data coming from different CSV files.
"""

data_folder = '../data/'
all_data = {}
fatal = 0
for year in range(2005,2006):

    usager_data = None
    vehicule_dic = {}
    caracteristiques_dic = {}
    lieux_dic = {}

    with open(data_folder + 'usagers_' + str(year) + '.csv') as usager_file:
        usager_data = [line for line in csv.reader(usager_file)]

    with open(data_folder + 'caracteristiques_' + str(year) + '.csv', encoding='iso-8859-1') as caracteristiques_file:

        for index, line in enumerate(csv.reader(caracteristiques_file)):

            if index == 0:
                continue

            # obtain the weekday (0, Monday 1 Tuesday, 2...)
            weekday = calendar.weekday(int(year),int(line[2]),int(line[3]))

            #cleaning data
            line[3] = weekday

            # converting hour in time codes
            """
                entre 0 e 7 madrugada - 0
                entre 8 e 12 manha    - 1
                entre 13 e 17 tarde   - 2
                entre 18 e 23 noite   - 3
            """
            hour = int(line.pop(4))
            code = 3
            if hour < 700:
                code = 0
            elif hour < 1200:
                code = 1
            elif hour < 1700:
                code = 2
            line[4] = code

            line.pop(10) # exclude city
            line.pop(10) # exclude adress
            line.pop(10) # exclude gps
            line.pop(10) # exclude latitude
            line.pop(10) # exclude longitude

            caracteristiques_dic[line[0]] = line[1:]

    with open(data_folder + 'vehicules_' + str(year) + '.csv') as vehicules_file:
        for line in csv.reader(vehicules_file):

            line.pop(1)
            line.pop(2)

            # todo como consertar o fato de que um acidente pode ter mais de um veiculo???

            vehicule_dic[line[0] + line[-1]] = line[1:]

    with open(data_folder + 'lieux_' + str(year) + '.csv') as lieux_file:
        for line in csv.reader(lieux_file):

            line.pop(3)
            line.pop(3)
            line.pop(5)
            line.pop(5)
            line.pop(8)
            line.pop(8)
            line.pop(11)

            lieux_dic[line[0]] = line[1:]

    for index, row_usager in enumerate(usager_data):

        if row_usager[3] == '2':
            fatal +=1

        if index == 0:
            continue
        try:
            all_data [row_usager[0]]= row_usager[1:] + caracteristiques_dic[row_usager[0]] + lieux_dic[row_usager[0]] + vehicule_dic[row_usager[0] + row_usager[-1]]
        except KeyError:
            print('eeerrro')
            pass


print(str(len(all_data)))
with open('all_data.csv', 'w') as new_data:

    for line in all_data.values():
        line.pop(10) # excluding vehicule code
        line.pop(34) # excluding vehicule code
        new_data.write(str(line))
        new_data.write('\n')



