import csv
import json
import time


dict = {}

def timeFormatter(str):
    mytime = time.strptime(str, "%m/%d/%y %H:%M")
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", mytime)

with open('data.csv', newline = '') as csvfile:
    datastream = csv.reader(csvfile, delimiter=',', quotechar='|')
    counter = 0
    for row in datastream:
        if counter > 0:
            dict[row[0]] = {}
            dict[row[0]]["agent_id"] = row[0]
            dict[row[0]]["agent_name"] = row[1]
            dict[row[0]]["start"] = timeFormatter(row[2])
            dict[row[0]]["end"] = timeFormatter(row[3])
        counter += 1

jsonify = json.dumps(dict, indent=4)
print(jsonify)
