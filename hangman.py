import random

print("Welcome to hangman! You will have 10 attempts at guessing the word.\n")
print("_", end=" ")
print("_", end=" ")
print("_", end=" ")
print("_", end=" ")
print("_")

l1="_"
l2="_"
l3="_"
l4="_"
l5="_"


n1=""
n2=""
n3=""
n4=""
n5=""
counter = 0
wordlist=["night","fried","shelf","frame"]
x=random.choice(wordlist)

while counter<10:
    userguess=str(input("Please type in a letter\n"))
   

    if x=="shelf":
        n1="s"
        n2="h"
        n3="e"
        n4="l"
        n5="f"
    
    if x=="frame":
        n1="f"
        n2="r"
        n3="a"
        n4="m"
        n5="e"

    if x=="fried":
        n1="f"
        n2="r"
        n3="i"
        n4="e"
        n5="d"
    
    if x=="night":
        n1="n"
        n2="i"
        n3="g"
        n4="h"
        n5="t"
 


    if userguess==n1:
        l1= l1.replace(l1,userguess)
    if userguess==n2:
        l2 = l2.replace(l2,userguess)
    if userguess==n3:
        l3= l3.replace(l3,userguess)
    if userguess==n4:
        l4 = l4.replace(l4,userguess)
    if userguess==n5:
        l5 = l5.replace(l5,userguess)

    print(l1, end = " ")
    print(l2, end = " ")
    print(l3, end = " ")
    print(l4, end = " ")
    print(l5, end = "\n")

      
    if l1!= "_" and l2!="_" and l3!="_" and l4!="_" and l5!="_":
        print("Congrats!")
        break
    counter = counter + 1
  
if l1== "_" or l2=="_" or l3=="_" or l4=="_" or l5=="_":
    print("You ran out of guesses")


























'''
def split(x):
    return list(x)
splitword=split(x)
'''  


