# Ask in stackoverflow
# How to automatically catch the calendar data in tkinter whenever user chooses a date without using seperate button to fetch that data?

from tkinter import *
from functions import milkRecord, viewMilkRecord, expenseRecord, showNetIncome

default_color = '#d1fcf1'

class mainWindow:
    def __init__(self, root):
        # GUI
        self.root = root
        self.root.title('Diary Income Management System(Personal Use)')
        self.root.configure(background=default_color)

        # Global Heading
        self.globalTitle = Label(self.root, text='DAIRY INCOME MANAGEMENT SYSTEM', bg='black', fg='white', font=('Bold', '30'))
        
        # Main Frame Window
        self.mainframe = LabelFrame(self.root, bg=default_color, border=0)

        # Left Child Frame-----------------------------------------------------------------------
        self.leftFrame = LabelFrame(self.mainframe, bg=default_color, border=0)

        # SubChild Frames
        # Milk Frames
        self.milkframe = LabelFrame(self.leftFrame, bg=default_color)

        # Milk Frame's elements
        self.milkLabel1 = Label(self.milkframe, text = 'MILK RECORD', height=2, bg=default_color, font=('Georgia','12'))

        self.addButtonM = Button(self.milkframe, text='ADD RECORD', height = 2, width=15, border=1, command = lambda: self.subFunctions('Add'), bg=default_color)
        self.editButtonM = Button(self.milkframe, text='EDIT RECORD', height = 2, width=15, border=1, command = lambda: self.subFunctions('Edit'), bg=default_color)
        self.deleteButtonM = Button(self.milkframe, text='DELETE RECORD', height = 2, width=15, border=1, bg=default_color, command = lambda: self.subFunctions('Delete'))
        self.viewButtonM = Button(self.milkframe, text='VIEW RECORD', height = 2, width=15, border=1, bg=default_color, command = lambda: self.subFunctions('View'))
        
        # Expenses Frame
        self.expensesframe = LabelFrame(self.leftFrame, bg=default_color)

        # Expenses Frame's Elements
        self.expensesLabel1 = Label(self.expensesframe, text = 'EXPENSES RECORD', height=2, bg=default_color, font=('Georgia','12'))
        self.addButtonE = Button(self.expensesframe, text='ADD RECORD', height = 2, width=15, border=1, bg=default_color, command = lambda: self.subFunctions('Add', milk=False))
        self.editButtonE = Button(self.expensesframe, text='EDIT RECORD', height = 2, width=15, border=1, bg=default_color, command = lambda: self.subFunctions('Edit', milk=False))
        self.deleteButtonE = Button(self.expensesframe, text='DELETE RECORD', height = 2, width=15, border=1, bg=default_color, command = lambda: self.subFunctions('Delete', milk=False))
        self.viewButtonE = Button(self.expensesframe, text='VIEW RECORD', height = 2, width=15, border=1, bg=default_color, command = lambda: self.subFunctions('View', milk=False))
        
        self.netIncomeButton = Button(self.leftFrame, text = 'SHOW NET INCOME', width=20, height=4, bg=default_color, command = lambda: self.subFunctions('Net', milk=False))

        # Right Child Frame-------------------------------------------, -------------------------
        self.rightFrame = LabelFrame(self.mainframe, bg=default_color, text='GRAPHICAL INTERPRETATION', font=('Georgia','12'))
        
        # Milk Graph Section ......................................
        self.milkGraphTitle = Label(self.rightFrame, text='MILK STATUS', bg=default_color, font=('Georgia','12'))
        
        # Expenses Graph Section ......................................
        self.expensesGraphTitle = Label(self.rightFrame, text='EXPENSES STATUS', bg=default_color, font=('Georgia','12'))

        self.exitButton = Button(
            self.root, text='Exit', height = 2, width=20, command= self.root.quit, bg=default_color
            )

        showNetIncome.controlPanel(self, mainframe=self.root, ro=2)
        
    def placeGuiMain(self):
        self.globalTitle.grid(row=0, columnspan=50, padx=10)

        self.milkLabel1.grid(row=1, column=1, columnspan=2)

        self.addButtonM.grid(row=2, column=1, padx=10, pady=10)
                
        self.editButtonM.grid(row=2, column=2, padx=10, pady=10)
                
        self.deleteButtonM.grid(row=3, column=1, padx=10, pady=10)
                
        self.viewButtonM.grid(row=3, column=2, padx=10, pady=10)

        self.expensesLabel1.grid(row=1, column=1, columnspan=2)
                
        self.addButtonE.grid(row=2, column=1, padx=10, pady=10)
                
        self.editButtonE.grid(row=2, column=2, padx=10, pady=10)
                
        self.deleteButtonE.grid(row=3, column=1, padx=10, pady=10)
                
        self.viewButtonE.grid(row=3, column=2, padx=10, pady=10)

        self.milkframe.grid(row=1, column=1, pady=10)
                
        self.expensesframe.grid(row=2, column=1, pady=10)

        self.netIncomeButton.grid(row=3,column=1, pady=5)

        self.leftFrame.grid(row = 1, column = 1, padx=10, pady=10)

        self.milkGraphTitle.grid(row=2, column=1, pady=5)

        Label(self.rightFrame, text='GRAPH AREA1', width=100, bg=default_color).grid(row=3, column=1, pady=5)
                
        self.expensesGraphTitle.grid(row=4, column=1, pady=5)

        Label(self.rightFrame, text='GRAPH AREA2', width=100, bg=default_color).grid(row=5, column=1, pady=5)
                
        self.rightFrame.grid(row=1, column=2, padx=10, pady=10)
                
        self.mainframe.grid(row=1, pady=10, padx=10)

        self.exitButton.grid(row=2, column=1, padx=10, sticky='s')



    def subFunctions(self, title, milk=True):

        # Reserved frame for subfunctions
        mainframeTest = LabelFrame(self.root, bg=default_color, border=2)

        self.mainframe.grid_remove()
        self.exitButton.configure(text='Done ' + title + 'ing', command = lambda: self.back(mainframeTest))
        if title != 'View' and milk:
            self.milk = milkRecord(title, self.root, mainframeTest).placeGuiMilk()
        elif title == 'View' and milk:
            self.milk = viewMilkRecord(title, self.root, mainframeTest)
        elif not milk and title == 'Add' or title == 'Edit' or title == 'Delete' or title == 'View':
            self.expense = expenseRecord(title, self.root, mainframeTest)
        else:
            self.showNetIncome = showNetIncome(title, self.root, mainframeTest)

    def showGraph(self):
        def __init__(self):
            pass

    def back(self, mainframeTest):
        self.exitButton.configure(text='Exit', command = self.root.quit)
        mainframeTest.destroy()
        self.mainframe.grid()