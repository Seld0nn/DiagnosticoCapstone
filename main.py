import re
import json

def readJson():
    data = [json.loads(line) for line in open('data.json', 'r')]    
    return data

def TopTweets():
    pass

def main():
    data = readJson()
    
main()
