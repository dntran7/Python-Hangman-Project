import random
from getpass import _raw_input

print("Welcome to Guess the Word!")
wordlist = open('D:\\workspace\\ok\\wordlist.txt',"r")
class Word:
    def printlist(self):
        print (wordlist.read())
    def getrandomword(self):
        randomnum = random.randint(1,126)
        for a in range(1,randomnum):
            randomword = str(wordlist.readline()).lower()
        return randomword

class Slot:
    def getSlotList(self,randomword):
        slotlist = []
        length = len(randomword)-1
        for char in range(0,length):
            slotlist.append("_")
        return slotlist
    def getFullSlot(self,randomword):
        slotlist=[]
        length = len(randomword)-1
        for char in range(0,length):
            slotlist.append(randomword[char])
        return slotlist
    def getPrintedSlot(self,slotlist):   
        slot = (" ".join(slotlist))
        print(slot)
a = Word()   
b= Slot()
gamecontinue=True
ranword = a.getrandomword()
'''print (ranword)'''
charnum = len(ranword)-1

print("The word consists of " + str(charnum) +" characters")
slotlist=b.getSlotList(ranword)
copyslotlist = b.getSlotList(ranword)
turns=5
alreadyanswers=[]
while (gamecontinue):
    b.getPrintedSlot(copyslotlist)
    answer = _raw_input("Please guess a character: ")
    isitanum=False
    for num in range(0,10):
        if answer==str(num):
            print("Type in a character only!")
            isitanum=True
    if(len(answer)>1):
        print("Type in a character only!")
    elif ("".join(alreadyanswers)).find(answer)>-1:
        print("You've already tried that! try again")
    elif(isitanum==False):
        alreadyanswers.append(answer)
        result = ranword.find(answer)
        resultlist =[]
        if (result==-1):
            print("The word does not contain any", answer)
            turns = turns-1
            print ("You have", turns,"incorrect turns left")
        else:
            for character in range(0,len(ranword)):
                c = 0
                if ranword[character] == answer:
                    print ("The word contains " + str(answer) + " at slot #", character+1)
                    copyslotlist[character]=answer
                    c+=1
                if c>1:
                    for a in range(0,c):
                        copyslotlist[character]=answer
                        del slotlist[("".join(slotlist)).find(answer)]
                elif c==1:
                    copyslotlist[character]=answer
                    del slotlist[("".join(slotlist)).find(answer)]
    if turns==0:
        print("Game Over")
        print("The word was:")
        b.getPrintedSlot(b.getFullSlot(ranword))
        break    
    if slotlist==[]:
        print("You Won!")
        b.getPrintedSlot(copyslotlist)
        gamecontinue=False
        break
