# def f(n):
# 	if n <= 1: return 0
# 	if n == 2 or n == 3: return 1
# 	else:
# 		return n//2 + f(n//2) + f(n//2) + f((n//2+1)//2)

import random
import time
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class Application:
    def __init__(self):
        self.list_objects = []
        self.timer = False
        self.start_time = 0
        self.time_passed = 0
        self.level = 0
        self.direction = True
        self.jump = 0
        self.question_number = 0
        self.temp_question = -1, -1
        self.list_of_question_count = {20:74, 19:63, 18:57, 17:53, 16:48, 15:39,
                                      14:39, 13:36, 12:32, 11:27, 10:21, 9:19,
                                      8:15, 7:12, 6:9, 5:6, 4:4, 3:1, 2:1}
        self.create_widgets()

    def create_widgets(self):
        self.root = Tk()
        self.root.title('Blitz')
        self.root.geometry('375x460+50+50')
        self.root.resizable(False, False)
        self.root.configure(background='white')
        self.fnt1 = ('Consolas', '18')
        self.fnt2 = ('Consolas', '10')
        self.fnt3 = ('Arial', '10')
        self.fnt4 = ('Arial', '12')
        self.create_frame_choice()
        self.create_frame_view()
        self.create_frame_register()
        self.mess_lab = Label(self.root, font=self.fnt3, bg='black', fg='#00FF00')
        self.mess_lab['text'] = "Add subjects to the text field with keyboard or from the file!"
        self.mess_lab.place(x=5, y=5, width=365, height=35)

    def create_frame_choice(self):
        self.frame_choice = Frame(self.root, bg='#d7edff', bd=5, height=66, width=365)
        self.frame_choice.place(x=5, y=44)
        Label(self.frame_choice, text="or", font=self.fnt1, bg='#d7edff').place(x=160, y=13)
        # buttons
        self.option_but1 = Button(self.frame_choice, text='one', font=self.fnt1, bd=5, command=self.choose1)
        self.option_but1['state'] = DISABLED
        self.option_but1.place(x=2, y=1, width=150)
        self.option_but2 = Button(self.frame_choice, text='two', font=self.fnt1, bd=5, command=self.choose2)
        self.option_but2['state'] = DISABLED
        self.option_but2.place(x=198, y=1, width=155)

    def create_frame_register(self):
        self.frame_register = Frame(self.root, bg='#d0ffd0', bd=5, height=55, width=365)
        self.frame_register.place(x=5, y=114)
        Label(self.frame_register, font=self.fnt4, bg='#d0ffd0',
              text='First name:                 Second name:          Class:').place(x=0, y=0)
        self.first_name_ent = Entry(self.frame_register, font=self.fnt4, width=13)
        self.first_name_ent.place(x=0, y=22)
        self.first_name_ent.insert(END, 'Вася')
        self.second_name_ent = Entry(self.frame_register, font=self.fnt4, width=13)
        self.second_name_ent.place(x=145, y=22)
        self.second_name_ent.insert(END, 'Пупкин')
        class_list = ['8А', '8Б', '9А', '9Б', '9В', '10А', '11А']
        self.class_combobox = ttk.Combobox(self.frame_register, values=class_list,
                                           state='readonly', width=8)
        self.class_combobox.place(x=283, y=22)
        self.class_combobox.set(class_list[0])

    def create_frame_view(self):
        self.frame_view = Frame(self.root, bg='#ffffe0', bd=5, height=280, width=365)
        self.frame_view.place(x=5, y=174)
        # labels
        self.quest_num_lab = Label(self.frame_view, font=self.fnt2, bg='#ffffe0')
        self.quest_num_lab['text'] = "Number of the question: _"
        self.quest_num_lab.place(x=125, y=0)
        self.count_elem_lab = Label(self.frame_view, font=self.fnt2, bg='#ffffe0')
        self.count_elem_lab['text'] = "Count of elements: _"
        self.count_elem_lab.place(x=125, y=20)
        self.count_quest_lab = Label(self.frame_view, font=self.fnt2, bg='#ffffe0')
        self.count_quest_lab['text'] = "Left a questions: _"
        self.count_quest_lab.place(x=125, y=40)
        self.count_posb_quest_lab = Label(self.frame_view, font=self.fnt2, bg='#ffffe0')
        self.count_posb_quest_lab['text'] = "Count of possible questions: _"
        self.count_posb_quest_lab.place(x=125, y=60)
        self.time_lab = Label(self.frame_view, font=self.fnt2, bg='#ffffe0')
        self.time_lab['text'] = "Time: __:__:__._"
        self.time_lab.place(x=125, y=80)
        # text field
        self.options_txt = Text(self.frame_view, height=15, width=15, font=self.fnt2, bd=0)
        self.options_txt.place(x=5, y=5)
        self.border_for_txt = Frame(self.frame_view, width=115, height=235, borderwidth=30)
        self.border_for_txt['bg'] = 'red'
        self.border_for_txt.lower()
        self.border_for_txt.place(x=1, y=1)
        # buttons
        self.start_but = Button(self.frame_view, text='START', font=self.fnt1, command=self.start)
        self.start_but['state'] = DISABLED
        self.start_but.place(x=125, y=187, width=229)
        self.clear_but = Button(self.frame_view, text="Clear", font=self.fnt2, command=self.clear_text_field)
        self.clear_but.place(x=1, y=243, width=115)
        self.add_from_text_but = Button(self.frame_view, text="Add", font=self.fnt2, command=self.add_from_text)
        self.add_from_text_but.place(x=125, y=243, width=96)
        self.add_from_file_but = Button(self.frame_view, text="Add from file", font=self.fnt2, command=self.add_from_file)
        self.add_from_file_but.place(x=229, y=243, width=125)

    def stop_answer_question(self):
        self.timer = False
        self.start_time = 0
        self.time_passed = 0
        self.time_lab['text'] = "Time: __:__:__._"
        self.list_objects = []
        self.question_number = 0
        self.border_for_txt['bg'] = 'red'
        self.quest_num_lab['text'] = "Number of the question: _"
        self.count_elem_lab['text'] = "Count of elements: _"
        self.count_quest_lab['text'] = "Left a questions: _"
        self.count_posb_quest_lab['text'] = "Count of possible questions: _"
        self.mess_lab['text'] = "Add subjects to the text field with keyboard or from the file!"
        self.option_but1['state'] = DISABLED
        self.option_but1['text'] = 'one'
        self.option_but2['state'] = DISABLED
        self.option_but2['text'] = 'two'

    def clear_text_field(self):
        self.stop_answer_question()
        self.options_txt.delete('1.0', END)
        self.start_but['state'] = DISABLED

    def add_from_text(self):
        self.stop_answer_question()
        lines_text = [el.strip() for el in self.options_txt.get('1.0', END).strip(' \n').split('\n') if el != '']
        if not lines_text:
            print('File is empty...')
        elif len(lines_text) < 2:
            print("Count of the elements less then 2...")
        elif len(lines_text) > 20:
            print("Count of the elements more then 20...")
        else:
            list_objects_view = []
            for subj in lines_text:
                tmp = subj.lower().title()
                self.list_objects.append([tmp, 0])
                list_objects_view.append(tmp)
            random.shuffle(self.list_objects)
            list_objects_view.sort()
            list_objects_view = '\n'.join(list_objects_view)
            self.options_txt.delete('1.0', END)
            self.options_txt.insert('1.0', list_objects_view)
            self.border_for_txt['bg'] = 'blue'
            self.count_elem_lab['text'] = "Count of elements: {0}".format(len(self.list_objects))
            self.count_quest_lab['text'] = "Left a questions: {0}".format(
                self.list_of_question_count[len(self.list_objects)])
            count_posb_quest = len(self.list_objects) * (len(self.list_objects) - 1) // 2
            self.count_posb_quest_lab['text'] = "Count of possible questions: {0}".format(count_posb_quest)
            self.mess_lab['text'] = "List download from file is done! Now press the START"
            self.start_but['state'] = NORMAL
            print(self.list_objects)

    def add_from_file(self):
        self.stop_answer_question()
        fn = filedialog.askopenfilename(filetypes=[('*.txt files', '*.txt')])
        if fn:
            fin = open(fn, 'r')
            lines_file = [el.strip() for el in fin.read().strip(' \n').split('\n') if el != '']
            fin.close()
            if not lines_file:
                print('File is empty...')
            elif len(lines_file) < 2:
                print("Count of the elements less then 2...")
            else:
                list_objects_view = []
                for subj in lines_file:
                    tmp = subj.lower().title()
                    self.list_objects.append([tmp, 0])
                    list_objects_view.append(tmp)
                random.shuffle(self.list_objects)
                list_objects_view.sort()
                list_objects_view = '\n'.join(list_objects_view)
                self.options_txt.delete('1.0', END)
                self.options_txt.insert('1.0', list_objects_view)
                self.border_for_txt['bg'] = 'blue'
                self.count_elem_lab['text'] = "Count of elements: {0}".format(len(self.list_objects))
                self.count_quest_lab['text'] = "Left a questions: {0}".format(
                    self.list_of_question_count[len(self.list_objects)])
                count_posb_quest = len(self.list_objects) * (len(self.list_objects) - 1) // 2
                self.count_posb_quest_lab['text'] = "Count of possible questions: {0}".format(count_posb_quest)
                self.mess_lab['text'] = "List download from file is done! Now press the START"
                self.start_but['state'] = NORMAL
                print(self.list_objects)

    def update_time(self):
        def time_str(t):
            milisec = str(t % 10)
            seconds = str(t // 10 % 60).zfill(2)
            minutes = str(t // 600 % 60).zfill(2)
            hours = str(t // 36000).zfill(2)
            return '{0}:{1}:{2}.{3}'.format(hours, minutes, seconds, milisec)
        if self.timer:
            self.time_passed = int(time.time()*10) - self.start_time
            self.time_lab['text'] = self.time_lab['text'][:6] + time_str(self.time_passed)
            self.root.after(100, self.update_time)

    def start(self):
        if len(self.list_objects) < 2:
            print("Count of the objects less then 2!")
        elif not (self.second_name_ent.get() or self.first_name_ent.get() or self.class_combobox.get()):
            print("Enter your first name, second name and choose your class!")
        else:
            print(self.second_name_ent.get(),
                  self.first_name_ent.get(),
                  self.class_combobox.get())
            self.option_but1['state'] = NORMAL
            self.option_but2['state'] = NORMAL
            self.start_but['state'] = DISABLED
            self.mess_lab['text'] = "Answer the questions below"
            self.print_list_in_process()

            self.start_time = int(time.time() * 10)
            self.timer = True
            self.update_time()

            self.level = 0
            self.jump = 0
            self.direction = True
            self.question_number = 0
            self.temp_question = -1, -1
            self.human_sort()
            self.quest_num_lab['text'] = "Number of the question: {0}".format(self.question_number)

    def on_level_count(self):
        count = 0
        for el in self.list_objects:
            if el[1] == self.level:
                count += 1
        return count

    def find_next_pair(self):
        one, two = self.temp_question
        for i in range(two + 1, len(self.list_objects)):
            if self.list_objects[i][1] == self.level:
                one = i
                for j in range(one + 1, len(self.list_objects)):
                    if self.list_objects[j][1] == self.level:
                        two = j
                        break
                break
        self.temp_question = one, two
        self.option_but1['text'] = self.list_objects[one][0]
        self.option_but2['text'] = self.list_objects[two][0]

    def human_sort(self, winner=None, loser=None):
        if winner is not None and loser is not None:
            self.question_number += 1
            self.list_objects[winner][1] += 1
            self.list_objects[loser][1] -= 1
            while self.on_level_count() < 2:
                if self.jump >= len(self.list_objects) * 2 - 1:
                    self.mess_lab['text'] = "Sorting is done!"
                    self.border_for_txt['bg'] = 'green'
                    self.timer = False
                    self.option_but1['state'] = DISABLED
                    self.option_but1['text'] = 'one'
                    self.option_but2['state'] = DISABLED
                    self.option_but2['text'] = 'two'
                    self.list_objects.sort(key=lambda x: x[1], reverse=True)
                    self.options_txt.delete('1.0', END)
                    self.options_txt.insert('1.0', ''.join([str(i + 1) + '. ' + str(el[0]) + '\n'
                                                            for i, el in enumerate(self.list_objects)]))
                    break
                elif self.direction:
                    if self.level < max(self.list_objects, key=lambda x: x[1])[1]:
                        self.level += 1
                    else:
                        self.level -= 1
                        self.direction = False
                    self.jump += 1
                    self.temp_question = -1, -1
                else:
                    if self.level > min(self.list_objects, key=lambda x: x[1])[1]:
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

    def print_list_in_process(self):
        self.options_txt.delete('1.0', END)
        lst = []
        for title, level in sorted(self.list_objects, key=lambda x: x[1]):
            lst.append('{0:2d} {1}'.format(level, title))
        self.options_txt.insert('1.0', '\n'.join(lst))

    def choose1(self):
        self.human_sort(self.temp_question[0], self.temp_question[1])
        self.quest_num_lab['text'] = "Number of the question: {0}".format(self.question_number)
        self.count_quest_lab['text'] = "Left a questions: {0}".format(
            self.list_of_question_count[len(self.list_objects)]-self.question_number)
        if self.timer:
            self.print_list_in_process()

    def choose2(self):
        self.human_sort(self.temp_question[1], self.temp_question[0])
        self.quest_num_lab['text'] = "Number of the question: {0}".format(self.question_number)
        self.count_quest_lab['text'] = "Left a questions: {0}".format(
            self.list_of_question_count[len(self.list_objects)] - self.question_number)
        if self.timer:
            self.print_list_in_process()

if __name__ == '__main__':
    app = Application()
    app.root.mainloop()