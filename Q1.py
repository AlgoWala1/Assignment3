###Code to get all the words in the string
string = input("Enter a string:")
###Add a space at the end
string = string+" "
i = 0
j = string.find(" ")
###A list to store all the words(even duplicate)
worList = []
worList.append(string[i:j])
while j!=-1:
    i = j
    j = string.find(" ",i+1)
    worList.append(string[i+1:j])
###Code to count occurences and sinmultaneously check if word is repeated
###occ means occurences of a particular word
for i in range(0,len(worList)):
    occ = 0
    ###Check for repetitions
    isRepeat = False
    for k in range(i-1,-1,-1):
        if worList[k] == worList[i]:
            isRepeat = True
    if isRepeat:
        continue
    for j in range(i,len(worList)):
        if worList[i]==worList[j]:
            occ+=1
    print("Occurence of word ",worList[i],"is",occ)

