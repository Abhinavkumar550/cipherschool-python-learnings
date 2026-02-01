#file=open("city.txt","w")
with open("city.txt","w") as file:
    data=file.write("up: Kanpur\n")
    data=file.write("bihar: patna\n")
#i=0
file=open("city.txt","r")
#for line in file:
    #print(line)
    #i+=1
#print(i)
#data=file.readlines()
#print(len(data))
#data=file.read()
#print(data.upper())
#print(len(data))
data=file.read()
#words=data.split()
#print("Total words in a file are: ",len(words))
#count=data.lower().count("Kanpur")
#print("Word count:",count)
#print(data[::-1])
print(data.replace("bihar","prem randwa mc bsdk uski mai awa"))

file.close()
