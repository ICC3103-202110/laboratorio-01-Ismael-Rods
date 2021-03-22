from random import shuffle
from tabulate import tabulate
def shuffle_card_list(n):
    i=1
    list=[]
    for g in range(n):
        list.append(i)
        list.append(i)
        i+=1
    shuffle(list)
    return(list)

def cens_list(n):
    list=[]
    for g in range(n):
        list.append('*')
        list.append('*')
    return list
def generate_board(list1,row_amount):
    l=[]
    x=0
    y=10
    u=0
    for i in range(row_amount):
        g=list1[x:y]
        g.insert(0,u)
        l.append(g)
        u+=1
        x+=10
        y+=10
    print(tabulate(l,headers=['r/c ','1','2','3','4','5','6','7','8','9','10']))

n= int(input('Enter number of cards to play:'))
row_amount=int(input('Enter the number of rows on your board, thinking about the number of pairs and consider 10 columns\nFor Example: 20 pairs = 4 rows: '))

#P1=0
#P2=0
#print(shuffle_card_list(20))
print(generate_board(shuffle_card_list(n),row_amount))

print(generate_board(cens_list(n),row_amount))