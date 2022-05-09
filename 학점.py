acnt = bcnt = 0
_ = input()
for sex in input():
    if sex == 'A':
        acnt+=1
    elif sex == 'B':
        bcnt+=1

if acnt == bcnt:
    print('Tie')
else:
    print('B' if bcnt > acnt else 'A')