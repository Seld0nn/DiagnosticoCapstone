

a = "http://www.masrawy. com/Sports/Sports_News/details/2014/9/5/ 338281#HPOFEATURE\n#ss\nddd\n#ddd jaaja ksks #sfsfsf\n#ggdg#hdhhd"
b = "Hey guys! tackoverflow really rocks rocks announcement"

b = {tag.strip("#") for tag in b.split() if tag.startswith("#")}
a = {tag.strip("#") for tag in a.split() if tag.startswith("#")}

print(a)
print(len(b))
#for i in a:
 #   print (i)
  #  print (type (i)) 
for i in b: 
    print(i)