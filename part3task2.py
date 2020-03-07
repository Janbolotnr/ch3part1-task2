#from random import randint

player1 = input('player1 chose: kamen(k), nojnicu(n) ili bumaga(b)?')
player2 = input('player2 chose: kamen(k), nojnicu(n) ili bumaga(b)?')


if player1 == player2:
    print('draw')
elif player1 == 'k' and player2  == 'n':
    print('player1 win!!!')
elif player1 == 'k' and player2 == 'b':
    print('player2 win!!!')  
elif player1 == 'n' and player2 == 'b':
    print('player1 win!!!') 
elif player1 == 'n' and player2 == 'k':
    print('player2 win!!!')
elif player1 == 'b' and player2 == 'k':
    print('player1 win!!!')     
elif player1 == 'b' and player2 == 'n':
    print('player2 win!!!')   
else:
     print("Your chose error")              


