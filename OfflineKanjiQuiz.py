# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 08:10:55 2018
@author: MICHAEL
"""

import openpyxl, random, datetime
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

def makingtheBase(low, high, history_log = []):
    try:
        txtlog = open('KanjiQuizLog.txt', 'a')
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
        txtlog.write('\n' + datetime.datetime.today().strftime('%Y-%m-%d') + ' ' \
                     + datetime.datetime.today().strftime('%T') + ' %s'% history_log)
        txtlog.close()
        return correct_incorrect_log, history_log
    except Exception:
        txtlog.write('\n' + datetime.datetime.today().strftime('%Y-%m-%d') + \
                     ' ' + datetime.datetime.today().strftime('%T') + 'Error occured. recording... %s'% history_log)
        txtlog.close()
        return history_log, 'error'
    
wb = MegaExcel('HeisigKanji.xlsx')
main = wb.getSheet(0)
"""Making the GUI"""

class kanjiQuiz(object):
    def __init__ (self, excel, high, low, master=root, flag = False, activeSheet=0):
        history_log = []
        self.high = high
        self.low = low
        self.history_log = history_log
        if flag:
            wb = MegaExcel(excel)
            main = wb.getSheet(activeSheet)
        topFrame = Frame(master)
        midFrame = Frame(master)
        botFrame = Frame(master)
        topFrame.pack()
        midFrame.pack()
        botFrame.pack()
        
        #text a.k.a lables
        theLabel1 = Label(topFrame, text = 'press start', font='Times 100')
        theLabel2 = Label(topFrame, text = 'Michael\'s KanjiQuiz', fg = 'green')
        theLabel3 = Label(midFrame, text = 'Type \'y\' for correct or \'n\' for incorrect: ')
        
        #text/label 
        theLabel1.grid(row=1)
        theLabel2.grid(row=0, column=1)
        theLabel3.grid(row=0)
        
        #Buttons
        button1 = Button(botFrame, text= 'Prev')
        button2 = Button(botFrame, text= 'Next')
        button3 = Button(botFrame, text= 'Menu')
        button4 = Button(botFrame, text= 'Show Answer') #no parenthesis!
        
        butnStart = Button(topFrame, text= 'Start')
        butnQuit = Button(topFrame, text= 'Quit')
        butnStart.grid(row=0, column=0)
        butnQuit.grid(row=0, column=2)
        
        #Button locis            
        button1.grid(row=0, column=1)
        button2.grid(row=0, column=3)
        button3.grid(row=0, column=2)
        button4.grid(row= 0, column=4)
        
        entry1 = Entry(midFrame)
        entry1.grid()

    def updateLabel(event):
        num = random.randint(250, 550)
        theLabel1['text'] = main['A%s' % num].value
        
        #Button binds
    def binds(self, master, function):
            button4.bind("<Button-1>", function) #Button-1 means a left click on the button
            

#        random.randint()
#        text = main['A%s' % num].value, font ='Times 100'

root = Tk()
topFrame = Frame(root, width=200, length=200)
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

history_log = [0, 66]
low, high = 250, 550
def showAnswer(event):
    n = history_log[-1]
    answer =  main['B%s' %  n].value
    theLabel1['text'] = answer 

def nextOne(event):
    random_num = random.randint(low, high)
    while random_num in history_log:
        random_num = random.randint(low, high)
    history_log.append(random_num)
    theLabel1['text'] = main['A%s' %  random_num].value    

button1 = Button(botFrame, text= 'Prev')
button2 = Button(botFrame, text= 'Next')
button3 = Button(botFrame, text= 'Menu')
button4 = Button(botFrame, text= 'Show Answer') #no parenthesis!

button4.bind("<Button-1>", showAnswer) #Button-1 means a left click on the button
button2.bind("<Button-1>", nextOne)

button1.grid(row=0, column=1)
button2.grid(row=0, column=3)
button3.grid(row=0, column=2)
button4.grid(row= 0, column=4)

root.mainloop()


