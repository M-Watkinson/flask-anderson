import csv

def convert_to_dict(filename):
    datafile = open(filename, newline='')
    my_reader = csv.DictReader(datafile)
    list_of_dicts = []
    for row in my_reader:
        list_of_dicts.append( dict(row) )
    datafile.close()
    return list_of_dicts

character_data = convert_to_dict("characters.csv")
