import random
arrylist = ['sheep', 'dogs', 'hamsters']
for i in range(3):
    choice = input("What other animals should be added to the list? ")
    arrylist.append(choice)
# print(arrylist)
for i in range(len(arrylist)):
    print(arrylist[i])
# number = random.randint(0,5)
# print(arrylist[number])

print(random.choice(arrylist))