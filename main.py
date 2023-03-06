from DBCon import DBconn

from contextlib import redirect_stderr
from pydoc import render_doc
from flask import Flask,render_template,request,redirect,session
import os
import sys

class ResgisterLogin:
    def __init__(self):
        self.db=DBconn()
        self.userchoice()
        
    def userchoice(self):
         x = input('''Enter 
         1 for Login
         2 for Register 
         3.Exit
         ''')
         if x=='1':
             self.login()
         elif x=='2':
             self.register()
         else:
             print("Logged out")
             sys.exit(30)

    def register(self):
        name=input("Enter name: ")
        email=input("Enter email: ")
        password=input("enter password: ")

        response = self.db.register(name,email,password)

        if response:
            print("{} Registered successfully".format(name))
        else:
            print("Please verify connection")
        self.userchoice()
    def login(self):
        email = input("Enter email: ")
        password = input("enter password: ")

        info1=self.db.login(email,password)

        if info1:
            print("{} logged in successfully".format(info1[0][1]))
            self.login_menu()
        else:
            print("Invalid username/password data")
            print("Try to enter data again")
            self.login()

    def login_menu(self):
        y = input('''Enter 
                 1 for see profile
                 2 for Edit profile 
                 3 for delete profile
                 4 for exit
                 ''')

        if y=='4':
            sys.exit(0)







s=ResgisterLogin()