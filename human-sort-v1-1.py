import random
import time
from tkinter import *
from tkinter import filedialog

def on_level_count(level):
    count = 0
    for el in list_objects:
        if el[1] == level: count += 1
    return count

def human_sort(winner=None, loser=None):
    global list_objects
    level = 0
    direction = True
    jump = 0
    question_number = 0
    if winner and loser:
        pass
    else:
        if on_level_count(level) > 1:
            question_number += 1
            jump = 0
            one, two = -1, -1
            for i in range( two+1, len(list_objects) ):
                if list_objects[i][1] == level:
                    one = i
                    for j in range( one+1, len(list_objects) ):
                        if list_objects[j][1] == level:
                            two = j
                            break
                    break
            yield list_objects[one][0], list_objects[two][0]

def human_sort1():
    global list_objects
    level = 0
    direction = True
    jump = 0
    question_number = 0
    while True:
        if on_level_count(level) > 1:
            question_number += 1
            jump = 0
            one, two = -1, -1
            for i in range( two+1, len(list_objects) ):
                if list_objects[i][1] == level:
                    one = i
                    for j in range( one+1, len(list_objects) ):
                        if list_objects[j][1] == level:
                            two = j
                            break
                    break
            option_but1['text'] = list_objects[one][0]
            option_but2['text'] = list_objects[two][0]
            print(question_number,') ',list_objects[one][0], ' or ', list_objects[two][0],'?',sep='',end='')
            print('  -> ', end='',sep='')
            while True:
                answ = input()
                if answ == '1': list_objects[one][1] += 1; list_objects[two][1] -= 1; break
                elif answ == '2': list_objects[one][1] -= 1; list_objects[two][1] += 1; break
        else:
            if jump >= len(list_objects) * 2 - 1: break
            if direction == True:
                if level < max(list_objects, key = lambda x: x[1])[1]: level += 1
                else: level -= 1; direction = False;
                jump += 1
            else:
                if level > min(list_objects, key = lambda x: x[1])[1]: level -= 1
                else: level += 1; direction = True
                jump += 1
    return list_objects

def print_list(li):
    print('-------------------------------------\nYour preferences:')
    i = 1
    for el in sorted(li, key=lambda x: x[1], reverse=True):
        print(i,'. ',el[0],sep=''); i += 1

def choose1():
    quest_num_lab['text'] = quest_num_lab['text'][:24] + str(int(quest_num_lab['text'][24:])+1)

def choose2():
    quest_num_lab['text'] = quest_num_lab['text'][:24] + str(int(quest_num_lab['text'][24:])-1)

def add_from_text():
    option_but1['state'] = DISABLED
    option_but2['state'] = DISABLED
    global list_objects, timer
    timer = False
    list_objects = []
    for subj in options_txt.get('1.0', END).split('\n'):
        if subj:
            list_objects.append( [subj.strip().lower().title(), 0] )
    random.shuffle(list_objects)
    if list_objects: print('list download from text field is done:', list_objects, sep='\n')
    else: print('list is empty:', list_objects)
    
def add_from_file():
    option_but1['state'] = DISABLED
    option_but2['state'] = DISABLED
    global list_objects, timer
    timer = False
    list_objects = []
    fn = filedialog.askopenfilename(filetypes = [('*.txt files', '*.txt')])
    if fn:
        fin = open(fn,'r')
        lines_file = fin.readlines()
        fin.close()
        for el in lines_file:
            list_objects.append( [el[:-1], 0] )
        random.shuffle(list_objects)
        lines_file.sort()
        list_objects_view = ''.join(lines_file)
        options_txt.delete('1.0', END) 
        options_txt.insert('1.0', list_objects_view)
        count_elem_lab['text'] = count_elem_lab['text'][:19] + str(len(list_objects))
        count_posb_quest_lab['text'] = count_posb_quest_lab['text'][:29] + \
                                       str(len(list_objects)*(len(list_objects)-1)//2)
    if list_objects: print('List download from file is done:', list_objects, sep='\n')
    else: print('List is empty:', list_objects)

def start():
    global list_objects, start_time, timer
    if len(list_objects) > 1:
        option_but1['state'] = NORMAL
        option_but2['state'] = NORMAL
        start_time = int(time.time()*10)
        timer = True
        update_time()
        human_sort()
    else:
        print("I don't see the reason to start!")


def update_time():
    if timer:
        time_passed = int(time.time()*10) - start_time
        milisec = str(time_passed % 10)
        time_passed //= 10
        seconds = str(time_passed % 60).zfill(2)
        time_passed //= 60
        minutes = str(time_passed % 60).zfill(2)
        hours = str(time_passed // 60).zfill(2)
        time_passed_str = '{0}:{1}:{2}.{3}'.format(hours, minutes, seconds, milisec)
        time_lab['text'] = time_lab['text'][:6] + time_passed_str
        root.after(100, update_time)
    else:
        time_lab['text'] = 'Time: 00:00:00.0'
        
# ---=== MAIN ===--- #

root = Tk()
root.title(u'one-FROM-two')
root.geometry('375x345+50+50')
root.resizable(False, False)
fnt1 = ('Arial','18')
fnt2 = ('Arial','10')

frame1 = Frame(root, bg='grey', bd=5, height=65, width=365,highlightbackground='red')
frame1.place(x=5, y=5)
or_lab = Label(frame1, text="or", font=fnt1, bg='grey')
or_lab.place(x=163, y=13)
option_but1 = Button(frame1,text="Вариант 1", font=fnt1, width=10, state=DISABLED, command=choose1)
option_but2 = Button(frame1,text="Вариант 2", font=fnt1, width=10, state=DISABLED, command=choose2)
option_but1.place(x=5, y=5)
option_but2.place(x=200, y=5)

frame2 = Frame(root, bg='#ffffe0', bd=5, height=265, width=365)
frame2.place(x=5, y=75)
quest_num_lab = Label(frame2, text="Number of the question: 0", font=fnt2, bg='#ffffe0')
quest_num_lab.place(x=125, y=5)
count_elem_lab = Label(frame2, text="Count of elements: 0", font=fnt2, bg='#ffffe0')
count_elem_lab.place(x=125, y=25)
count_posb_quest_lab = Label(frame2, text="Count of possible questions: 0", font=fnt2, bg='#ffffe0')
count_posb_quest_lab.place(x=125, y=45)
time_lab = Label(frame2, text="Time: 00:00:00.0", font=fnt2, bg='#ffffe0')
time_lab.place(x=125, y=65)
options_txt = Text(frame2, height=15, width=15, font=fnt2, wrap=WORD)
options_txt.place(x=5, y=5)
add_from_file_but = Button(frame2, text="Добавить из файла", font=fnt2, command=add_from_file)
add_from_text_but = Button(frame2, text="Добавить", font=fnt2, command=add_from_text)
add_from_text_but.place(x=125, y=222, width=90)
add_from_file_but.place(x=225, y=222, width=125)
start_but = Button(frame2, text='Start', font=fnt1, command=start)
start_but.place(x=125, y=160, width=225)

list_objects = []
timer = False
#li = DataInputFile()
#li = HumanSort(li)
#PrintList(li)

root.mainloop()
