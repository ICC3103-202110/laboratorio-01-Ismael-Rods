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
    print(tabulate(l,headers=['r/c ','0','1','2','3','4','5','6','7','8','9']))

def turno_p1():
    print('Player 1 turn!')
    generate_board(game_board,row_amount)
    print('Select a card!')
    x=int(input('Enter coordinates (x,y)!\nFor example: (1,1) = 11 : '))
    game_board[x]=deck[x]
    generate_board(game_board,row_amount)
    print('Select the second card!')
    x2=int(input('Enter coordinates (x,y)!\nFor example: (1,1) = 11 : '))
    game_board[x2]=deck[x2]
    generate_board(game_board,row_amount)
    if deck[x]==deck[x2]:
        True
    else:
        False
def turno_p2():
    print('Player 2 turn!')
    generate_board(game_board,row_amount)
    print('Select a card!')
    x=int(input('Enter coordinates (x,y)!\nFor example: (1,1) = 11 : '))
    game_board[x]=deck[x]
    generate_board(game_board,row_amount)
    print('Select the second card!')
    x2=int(input('Enter coordinates (x,y)!\nFor example: (1,1) = 11 : '))
    game_board[x2]=deck[x2]
    generate_board(game_board,row_amount)
    if deck[x]==deck[x2]:
        True
    else:
        False

print('Welcome!')
P1=0
P2=0
n= int(input('Enter number of cards to play:'))
row_amount=int(input('Enter the number of rows on your board, thinking about the number of pairs and consider 10 columns\nFor Example: 20 pairs = 4 rows: '))
deck=shuffle_card_list(n)
generate_board(deck,row_amount)
print('\n')
game_board=cens_list(n)

list=[]
for g in range(n):
    list.append('')
    list.append('')
generate_board(list,row_amount)
print(list)