import os
import csv
import matplotlib.pyplot as plt
from datetime import datetime

dataset_act = [] # actual values ("Aktueller Wert")
dataset_init = [] # init values ("Einstandswert")
dates = [] # date substrings of filenames
filenames_sorted = [] # sorted filenames with paths
initvalue = 0 # initvalue index inside csv files
actvalue = 0 # actvalue index inside csv files

# Startup + path input
print("This is a simple program that lists the content of one folder and the values of all files of that directory.")

print("Use default path? Y/N")
decision = input()
if decision == "N" or decision == "n":
    print("Please insert the folder path:")
    path = input() + "/"
else:
    if decision == "Y" or decision == "y":
        path = "C:/Users/Thomas/Meine Ablage/Privat/Flatex/"
        isdir = os.path.isdir(path)
        if isdir is False:
            # If the user input is no path, abort
            print("Your path is invalid - abort execution.")
        else:
            # Get content of path, sort it by date string and save it as full paths into filenames_sorted
            content = os.listdir(path)
            for i in content:
                dates.append(i[13:23])
            dates.sort(key=lambda date: datetime.strptime(date, "%d.%m.%Y"))
            for i in dates:
                filenames_sorted.append(path + "Depotbestand_" + i + ".csv")

            # In every csv file at path, search for actvalue and initvalue. Append datasets with actvalue/initvalue
            for item in filenames_sorted:
                file = open(item)
                file_object = csv.reader(file, delimiter=';')
                value = next(file_object)
                for i, cell in enumerate(value):
                    if value[i] == "Aktueller Wert":
                        actvalue = i
                        initvalue = i + 2
                value = next(file_object)
                dataset_act.append(float(value[actvalue].replace(',', '.')))
                dataset_init.append(float(value[initvalue].replace(',', '.')))

            # Plot datasets and show plot
            plt.plot(dates, dataset_act, color='b', label='Aktueller Wert')
            plt.plot(dates, dataset_init, color='r', label='Einstandswert')
            plt.xlabel("Datum")
            plt.ylabel("[€]")
            plt.title("Depotentwicklung")
            plt.legend()
            plt.grid()
            plt.xticks(rotation=90)
            plt.tight_layout()
            plt.show()
            print("Execution finished.")
    else:
        print("Invalid answer. Abort program.")