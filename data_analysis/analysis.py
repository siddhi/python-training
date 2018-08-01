import pandas
import argparse

parser = argparse.ArgumentParser(description="Process city ratings")
parser.add_argument('--input', dest='inputfile', default='input.txt', help='File containing ratings data')
parser.add_argument('--output', dest='outputfile', default='output.csv', help='File to store results')
args = parser.parse_args()

data = pandas.read_csv(args.inputfile, header=None, sep=" ")
data.columns = ['Name', 'City', 'Rating']
print(data[ (data['Name'] == 'Sid') & (data['Rating'] > 70) ])

table = pandas.pivot_table(data, index='Name', columns='City', values='Rating')
table['Person Total'] = table.sum(axis=1)

city_totals = table.sum(axis=0)
city_totals.name = "City Totals"
table = table.append(city_totals)
print(table)

table.to_csv(args.outputfile)
