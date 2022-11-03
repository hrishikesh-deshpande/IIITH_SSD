import csv
from statistics import mean

headers = []
table = []

with open('lab_11_data.csv') as csvFile:
    csvReader = csv.reader(csvFile)
    headers = next(csvReader)
    # print(headers)

    for row in csvReader:
        table.append(dict(list(zip(headers, row))[:-6:]))


table = list(filter(lambda x: float(
    x["% Chng"].replace(',', '')) >= -3, table))


def avg(col):
    return mean(map(lambda x: float(x[col].replace(',', '')), table))


# print("Averages of 'Open', 'High', 'Low' Columns are : ",
#       avg("Open"), ",", avg("High"), ",", avg("Low"))
with open('avg_output.txt', "w") as f:
    f.writelines([str(avg("Open")), '\n', str(
        avg("High")), '\n', str(avg("Low")), '\n'])

while(True):
    c = input("\nEnter a character between A-Z to search, EXIT to exit. : ")
    if(c == 'EXIT'):
        break
    if(len(c) != 1 or ord(c) < ord('A') or ord(c) > ord('Z')):
        print('Invalid Input')
        continue

    print(', '.join(headers[:-6:]))
    rows = list(filter(lambda x: x["Symbol"][0] == c, table))
    for row in rows:
        print(', '.join(row.values()))

with open('stock_output.txt', 'w', newline='') as outputTxt:
    txtWriter = csv.writer(outputTxt)
    # txtWriter.writerow(headers[:-6:])
    txtWriter.writerows(map(lambda x: x.values(), table))
