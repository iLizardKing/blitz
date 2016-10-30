import random

def DataInput():
    print('Введите элементы:')
    li = []
    i = 0
    while True:
        i += 1
        print(i,'. ',end='',sep='')
        el = input()
        if el == '': break
        li.append( [el, 0] )
    random.shuffle(li)
    return li

def DataInputFile():
    fin = open('human-sort.txt','r')
    li_f = fin.readlines()
    fin.close()
    li = []
    for el in li_f:
        li.append( [el[:-1], 0] )
    random.shuffle(li)
    return li

def onLevelCount(li, level):
    count = 0
    for el in li:
        if el[1] == level: count += 1
    return count

def HumanSort(li):
    print('-------------------------------------\nОтветьте на вопросы:')
    level = 0
    direction = True
    jump = 0
    qn = 0
    while True:
        if onLevelCount(li,level) > 1:
            qn += 1
            jump = 0
            one, two = -1, -1
            for i in range( two+1, len(li) ):
                if li[i][1] == level:
                    one = i
                    for j in range( one+1, len(li) ):
                        if li[j][1] == level:
                            two = j
                            break
                    break
            print(qn,') ',li[one][0], ' or ', li[two][0],'?',sep='',end='')
            answ = int(input('  -> '))
            if answ == 1: li[one][1] += 1; li[two][1] -= 1
            else: li[one][1] -= 1; li[two][1] += 1
        else:
            if jump >= len(li) * 2 - 1: break
            if direction == True:
                if level < max(li, key = lambda x: x[1])[1]: level += 1
                else: level -= 1; direction = False;
                jump += 1
            else:
                if level > min(li, key = lambda x: x[1])[1]: level -= 1
                else: level += 1; direction = True
                jump += 1
    return li

def PrintList(li):
    print('-------------------------------------\nВаши предпочтения:')
    i = 1
    for el in sorted(li, key=lambda x: x[1], reverse=True):
        print(i,'. ',el[0],sep=''); i += 1
        
        
# ---=== MAIN ===--- #
li = DataInput()
li = HumanSort(li)
PrintList(li)