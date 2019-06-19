import rpyc
import sys
import os
import time

def create_number_collection(n):
    collection = []
    for i in range(0, n):
        collection.append(i)
    return collection

start = time.time()
if len(sys.argv) < 3:
   exit("Usage {} SERVER".format(sys.argv[0]))
 
server = sys.argv[1]

n = int(sys.argv[2])
 
connection = rpyc.connect(server,18861)

number_collection = create_number_collection(n)

print(connection.root.get_sum(number_collection))
end = time.time()
print("Resultado no cliente: {}".format(end-start))
