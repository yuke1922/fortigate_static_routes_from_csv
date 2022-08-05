import csv
import os

os.system('clear')
os.system('rm -rf ./script.txt')

input_file = "source.csv"
outputfile = "script.txt"
string = ""
with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        prefix = row['prefix']
        prefixlen = str(row['prefixlen'])
        gw = str(row['gateway'])
        device = str(row['device'])

        current_string = "config router static\nedit 0\nset dst " + prefix + "/" + prefixlen + "\nset gateway " + gw + "\nset device " + device + "\nnext\nend\n\n"
        string += current_string

outfile = open(outputfile, 'w')
outfile.write(string)
outfile.close()