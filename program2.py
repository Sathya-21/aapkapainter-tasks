input_list=[1,2,3,2,1]
score={'p1':0,'p2':0}
#assuming strike starts with player1
strike='p1'
for i in input_list:
    score[strike]=score[strike]+i
    if(i%2 == 0):
        #no change in strike
        pass
    else:
        if(strike == 'p1'):
            strike='p2'
        else:
            strike='p1'
print("\n score of palyer1",score['p1'])
print("\n score of palyer2",score['p2'])
