import random
import time
from tkinter import *
from tkinter import filedialog

class Application:
    def __init__(self):
        self.list_objects = []
        self.timer = False
        self.start_time = 0
        self.level = 0
        self.direction = True
        self.jump = 0
        self.question_number = 0
        self.temp_question = -1, -1
        self.create_widgets()

    def create_widgets(self):
        self.root = Tk()
        self.root.title('one-FROM-two')
        self.root.geometry('375x367+50+50')
        self.root.resizable(False, False)
        self.root.configure(background='white')
        self.fnt1 = ('Consolas','18')
        self.fnt2 = ('Consolas','10')
        self.fnt3 = ('Arial','10')
        self.create_frame1()
        self.create_frame2()
        self.mess_lab = Label(self.root, font=self.fnt3, bg='black', fg='#00FF00')
        self.mess_lab['text'] = "Add subjects to the text field with keybord or from the file!"
        self.mess_lab.place(x=5, y=5, width=365, height=35)

    def create_frame1(self):
        self.frame1 = Frame(self.root, bg='#d7edff', bd=5, height=66, width=365)
        self.frame1.place(x=5, y=44)
        Label(self.frame1, text="or", font=self.fnt1, bg='#d7edff').place(x=160, y=13)
        # buttons
        self.option_but1 = Button(self.frame1, text='one', font=self.fnt1, bd=5, command=self.choose1)
        self.option_but1['state'] = DISABLED
        self.option_but1.place(x=2, y=1, width=150)
        self.option_but2 = Button(self.frame1, text='two', font=self.fnt1, bd=5, command=self.choose2)
        self.option_but2['state'] = DISABLED
        self.option_but2.place(x=198, y=1, width=155)

    def create_frame2(self):
        self.frame2 = Frame(self.root, bg='#ffffe0', bd=5, height=247, width=365)
        self.frame2.place(x=5, y=115)
        # labels
        self.quest_num_lab = Label(self.frame2, text="Number of the question: 0", font=self.fnt2, bg='#ffffe0')
        self.quest_num_lab.place(x=125, y=5)
        self.count_elem_lab = Label(self.frame2, text="Count of elements: 0", font=self.fnt2, bg='#ffffe0')
        self.count_elem_lab.place(x=125, y=25)
        self.count_posb_quest_lab = Label(self.frame2, text="Count of possible questions: 0", font=self.fnt2, bg='#ffffe0')
        self.count_posb_quest_lab.place(x=125, y=45)
        self.time_lab = Label(self.frame2, text="Time: 00:00:00.0", font=self.fnt2, bg='#ffffe0')
        self.time_lab.place(x=125, y=65)
        # text field
        self.options_txt = Text(self.frame2, height=15, width=15, font=self.fnt2, bd=0)
        self.options_txt.place(x=5, y=5)
        self.border_for_txt = Frame(self.frame2, width=115, height=235, borderwidth=30)
        self.border_for_txt['bg'] = 'red'
        self.border_for_txt.lower()
        self.border_for_txt.place(x=1, y=1)
        # buttons
        self.start_but = Button(self.frame2, text='START', font=self.fnt1, command=self.start)
        self.start_but['state'] = DISABLED
        self.start_but.place(x=125, y=154, width=229)
        self.add_from_text_but = Button(self.frame2, text="Add", font=self.fnt2, command=self.add_from_text)
        self.add_from_text_but.place(x=125, y=210, width=96)
        self.add_from_file_but = Button(self.frame2, text="Add from file", font=self.fnt2, command=self.add_from_file)   
        self.add_from_file_but.place(x=229, y=210, width=125)

    def add_from_text(self):
        self.option_but1['state'] = DISABLED
        self.option_but1['text'] = 'Option 1'
        self.option_but2['state'] = DISABLED
        self.option_but2['text'] = 'Option 2'
        self.start_but['state'] = NORMAL
        self.timer = False
        self.list_objects = []
        list_objects_view = []
        lines_text = self.options_txt.get('1.0', END).strip(' \n').split('\n')
        if lines_text:
            for subj in lines_text:
                tmp = subj.strip().lower().title()
                self.list_objects.append( [tmp, 0] )
                list_objects_view.append( tmp )
            random.shuffle( self.list_objects )
            list_objects_view.sort()
            list_objects_view = '\n'.join(list_objects_view)
            self.options_txt.delete('1.0', END) 
            self.options_txt.insert('1.0', list_objects_view)
            print('List download from text field is done:', self.list_objects, sep='\n')
        else:
            print('Text field is empty...')

    def add_from_file(self):
        self.option_but1['state'] = DISABLED
        self.option_but1['text'] = 'Option 1'
        self.option_but2['state'] = DISABLED
        self.option_but2['text'] = 'Option 2'
        self.start_but['state'] = NORMAL
        self.timer = False
        self.list_objects = []
        fn = filedialog.askopenfilename(filetypes = [('*.txt files', '*.txt')])
        if fn:
            fin = open(fn, 'r')
            lines_file = fin.read().strip(' \n').split('\n')
            print(1,lines_file)
            fin.close()
            if lines_file == ['']:
               print('File is empty...')
            elif len(lines_file) < 2:
                print("Count of the elements less then 2...")
            else:
                list_objects_view = []
                for subj in lines_file:
                    tmp = subj.strip().lower().title()
                    self.list_objects.append( [tmp, 0] )
                    list_objects_view.append( tmp )
                random.shuffle( self.list_objects )
                list_objects_view.sort()
                list_objects_view = '\n'.join(list_objects_view)
                self.options_txt.delete('1.0', END) 
                self.options_txt.insert('1.0', list_objects_view)
                self.count_elem_lab['text'] = self.count_elem_lab['text'][:19] + str(len(self.list_objects))
                self.count_posb_quest_lab['text'] = self.count_posb_quest_lab['text'][:29] + \
                                           str(len(self.list_objects)*(len(self.list_objects)-1)//2)
                print('List download from file is done:', self.list_objects, sep='\n')

    def update_time(self):
        if self.timer:
            time_passed = int(time.time()*10) - self.start_time
            milisec = str(time_passed % 10)
            time_passed //= 10
            seconds = str(time_passed % 60).zfill(2)
            time_passed //= 60
            minutes = str(time_passed % 60).zfill(2)
            hours = str(time_passed // 60).zfill(2)
            time_passed_str = '{0}:{1}:{2}.{3}'.format(hours, minutes, seconds, milisec)
            self.time_lab['text'] = self.time_lab['text'][:6] + time_passed_str
            self.root.after(100, self.update_time)
        else:
            self.time_lab['text'] = 'Time: 00:00:00.0'

    def start(self):
        if len(self.list_objects) > 1:
            self.option_but1['state'] = NORMAL
            self.option_but2['state'] = NORMAL
            self.start_but['state'] = DISABLED

            self.start_time = int(time.time()*10)
            self.timer = True
            self.update_time()
            
            self.level = 0
            self.jump = 0
            self.direction = True
            self.question_number = 0
            self.temp_question = -1, -1
            self.human_sort()
            self.quest_num_lab['text'] = self.quest_num_lab['text'][:24] + str(self.question_number)
        else:
            print("I don't see the reason to start!")

    def on_level_count(self):
        count = 0
        for el in self.list_objects:
            if el[1] == self.level: count += 1
        return count

    def find_next_pair(self):
        one, two = self.temp_question
        for i in range( two+1, len(self.list_objects) ):
            if self.list_objects[i][1] == self.level:
                one = i
                for j in range( one+1, len(self.list_objects) ):
                    if self.list_objects[j][1] == self.level:
                        two = j
                        break
                break
        self.temp_question = one, two
        self.option_but1['text'] = self.list_objects[one][0]
        self.option_but2['text'] = self.list_objects[two][0]

    def human_sort(self, winner=None, loser=None):
        if winner != None and loser != None:
            self.question_number += 1
            self.list_objects[winner][1] += 1
            self.list_objects[loser][1] -= 1
            print(self.list_objects[winner], self.list_objects[loser])
            while self.on_level_count() < 2:
                if self.jump >= len(self.list_objects) * 2 - 1:
                    print('Sorting is done!')
                    self.option_but1['state'] = DISABLED
                    self.option_but1['text'] = 'Option 1'
                    self.option_but2['state'] = DISABLED
                    self.option_but2['text'] = 'Option 2'
                    self.list_objects.sort(key = lambda x: x[1], reverse=True)
                    print(''.join([str(i+1)+'. '+str(el[0])+'\n' for i, el in enumerate(self.list_objects)]))
                    break
                elif self.direction:
                    if self.level < max(self.list_objects, key = lambda x: x[1])[1]:
                        self.level += 1
                    else:
                        self.level -= 1
                        self.direction = False
                    self.jump += 1
                    self.temp_question = -1, -1
                else:
                    if self.level > min(self.list_objects, key = lambda x: x[1])[1]:
                        self.level -= 1
                    else:
                        self.level += 1
                        self.direction = True
                    self.jump += 1
                    self.temp_question = -1, -1
            else:
                self.find_next_pair() 
        else:
            self.question_number += 1
            self.find_next_pair()
            print(self.temp_question)
                
    def choose1(self):
        self.human_sort(self.temp_question[0], self.temp_question[1])
        self.quest_num_lab['text'] = self.quest_num_lab['text'][:24] + str(self.question_number)

    def choose2(self):
        self.human_sort(self.temp_question[1], self.temp_question[0])
        self.quest_num_lab['text'] = self.quest_num_lab['text'][:24] + str(self.question_number)


if __name__ == '__main__':
    app = Application()
    app.root.mainloop()
