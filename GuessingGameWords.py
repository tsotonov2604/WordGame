#Tsvety Sotonov
#Problem 3
import random 
def wordGame():
    fname = "The_Tempest.txt"
    infile = open(fname,'r')
    s = infile.read()
    infile.close()
    words = s.split()
    word1=(random.choice(words))
    word2=(random.choice(words))
    print("Which word did the writer use more often",'"'+str(word1)+'"',"or",'"'+str(word2)+'"'+"?")
    input()
    numword1=s.count(word1)
    numword2=s.count(word2)
    if numword1 > numword2:
        print("you are correct")
    else:
        print("you are incorrect")
    return 
