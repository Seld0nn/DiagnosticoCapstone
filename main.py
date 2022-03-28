import re
import json

def readJson():
    data = [json.loads(line) for line in open('data.json', 'r')]  
    return data

def TopTweets(data):
    top10RtArray = [0]*10
    top10RtObject = []
    for tweet in data:
        if tweet["retweetCount"] > top10RtArray[0]:
                top10RtObject.append(tweet)
                for object in top10RtObject:
                    if top10RtArray[0] == object["retweetCount"]:
                        top10RtObject.remove(object)
                
                top10RtArray[0] = tweet["retweetCount"]
                top10RtArray.sort()

    top10RtObject.sort(key=lambda x: x["retweetCount"], reverse=True)
    for i in top10RtObject:
        print(str(i["retweetCount"]) + "  " + i["user"]["username"] + "  " + i["url"])
    return top10RtObject


def main():
    data = readJson()
    top10Rt = TopTweets(data)
 

main()
