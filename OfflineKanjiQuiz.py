# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 08:10:55 2018

@author: MICHAEL
"""

import openpyxl, random
from openpyxl import load_workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter


class MegaExcel(object):
    #general excel things that all will need
    def __init__ (self, name_of_workbook):
        self.name_of_workbook = name_of_workbook
    
    def activatewb(self, name):
        name = load_workbook(get_wb_name(self))
        return name
    
    def check(something):
        while something.lower() not in 'yn':
            something = input('please enter either y or n: ')
        if something.lower() == 'y':
            return True
        return False

    #some simple getters
    def get_wb_name(self):
        """return a str"""
        return self.name_of_workbook
    
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

wb = load_workbook('HeisigKanji.xlsx')
first_sheet = wb.get_sheet_names()[0]
main = wb.get_sheet_by_name(first_sheet)

def makingtheBase(low, high):
    history_log = []
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
    return correct_incorrect_log
a = makingtheBase(300,502)

