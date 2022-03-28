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

def topUsers(data):
    usersDict = {}
    top10User = []
    for tweet in data:
        if (tweet["user"]["username"] in usersDict.keys()):
            usersDict[tweet["user"]["username"]] += 1
        else:
            usersDict[tweet["user"]["username"]] = 1
   
    usersDict = {k: v for k, v in sorted(usersDict.items(), key=lambda item: item[1], reverse=True)}

    aux = 0
    for user in usersDict:
        if aux < 9:
            top10User.append([user, usersDict[user]])
        else:
            break
        aux += 1

    for i in top10User:
        print("User: "+ i[0] + " - Tweets: " + str(i[1]))

    return(top10User)

def main():
    data = readJson()
    top10Rt = TopTweets(data)
    top10User = topUsers(data)

main()
