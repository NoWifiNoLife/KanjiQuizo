# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 08:10:55 2018

@author: MICHAEL
"""

import openpyxl, random
from openpyxl import load_workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter
#from tkinter import *
from tkinter import *

class MegaExcel(object):
    #general excel things that all will need
    def __init__ (self, name_of_workbook):
        self.name_of_workbook = name_of_workbook
        workbook = load_workbook(name_of_workbook)
        self.workbook = workbook
    
    def check(something):
        while something.lower() not in 'yn':
            something = input('please enter either y or n: ')
        if something.lower() == 'y':
            return True
        return False
    
    def getSheet(self, sheet_number):
        """assumes workbook is preloaded"""
        sheet_name = self.getWB().get_sheet_names()[sheet_number]
        sheet = self.getWB().get_sheet_by_name(sheet_name)
        return sheet

    def getWBName(self):
        return self.name_of_workbook
    
    def getWB(self):
        return self.workbook
    
"""test check"""
#print(MegaExcel.check('h')) ###works!###


class KanjiQuiz(MegaExcel):
    def __init__ (self, name):
        #inherit MegaExcel initialization method
        MegaExcel.__init__(self, name)
        
    def randomChoice(self, lower, upper, sheet):
        return self.getWb().get_sheet_by_name(str(sheet))

    
    def startKanjiQuiz():
        pass
    #does things specific to kanjiquiz excel i.e column and stuff 


def makingtheBase(low, high, history_log = []):
    try:
        wb = MegaExcel('HeisigKanji.xlsx')
        main = wb.getSheet(0)
        correct_incorrect_log = {}
        play = input('Do you want to continue? (y/n):')
        while MegaExcel.check(play):
            random_num = random.randint(low, high)
            while random_num in history_log:
                random_num = random.randint(low, high)
            history_log.append(random_num)
            print('What is ' + main['A%s' % random_num].value + ' ?')
            correct_incorrect = input('Correct? (y/n): ')
            if correct_incorrect.lower() == 'y':
                correct_incorrect_log[random_num] = correct_incorrect_log.get(random_num, [0,0])[0] + 1
            elif correct_incorrect.lower() == 'n':
                correct_incorrect_log[random_num] = correct_incorrect_log.get(random_num, [0,0])[1] + 1
            show_answer = input('Would you like to see the answer? (y/n):')
            if MegaExcel.check(show_answer):
                print('What is ' + main['B%s' % random_num].value + ' ?')
            play = input('Do you want to continue? (y/n):')
        return correct_incorrect_log, history_log
    except Exception:
        return history_log, 'error'
#wb = MegaExcel('HeisigKanji.xlsx')
#main = wb.getSheet(0)
"""Making the GUI"""
root = Tk()
topFrame = Frame(root)
midFrame = Frame(root)
botFrame = Frame(root)
topFrame.pack()
midFrame.pack()
botFrame.pack()


theLabel1 = Label(topFrame, text = main['A66'].value, font ='Times 100')
theLabel2 = Label(topFrame, text = 'Michael\'s KanjiQuiz', fg = 'green')
theLabel3 = Label(midFrame, text = 'Type \'y\' for correct or \'n\' for incorrect: ')

theLabel1.grid(row=1)
theLabel2.grid(row=0)
theLabel3.grid(row=0)

entry1 = Entry(midFrame)
entry1.grid(row=1)

def showAnswer(event):
    answer =  main['B66'].value
    print(answer)


button1 = Button(botFrame, text= 'Prev')
button2 = Button(botFrame, text= 'Next')
button3 = Button(botFrame, text= 'Menu')
button4 = Button(botFrame, text= 'Show Answer') #no parenthesis!

button4.bind("<Button-1>", showAnswer) #Button-1 means a left click on the button

button1.grid(row=0, column=1)
button2.grid(row=0, column=3)
button3.grid(row=0, column=2)
button4.grid(row= 0, column=4)

root.mainloop()


