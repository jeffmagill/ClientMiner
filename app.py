import sys
import os

print ("Opening file: ", sys.argv[1])

#TODO huge security vulnerability here. prevent "../" for starters
path = os.environ["MINING_BASE_PATH"] + sys.argv[1]

with open(path, 'r') as content_file:
    content = content_file.read()
    print (content)
