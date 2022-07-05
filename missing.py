import csv

xdr_endpoint_inventory = 'TrendMicro_EndpointInventory.csv'
a1_agent_list = 'Apex One Security Agent List.csv'

xdr_agents = set()
with open(xdr_endpoint_inventory, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        xdr_agents.add(row[0].lower())

with open(a1_agent_list, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        if row[1].lower() not in xdr_agents:
            print(', '.join(row))

