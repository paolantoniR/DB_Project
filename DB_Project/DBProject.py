#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 18:02:08 2021

@author: giulianoamadei
"""

import mysql.connector



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Francesca.2013",
  database="examDB"
)

mycursor = mydb.cursor()

#with open('/Users/giulianoamadei/Desktop/test1.sql', 'r') as f:
    #with mydb.cursor() as cursor:
        #cursor.execute(f.read(), multi=True)
        #mydb.commit()

with open('Query1(NTW).sql', 'r') as sql_file:
    result_iterator = mycursor.execute(sql_file.read(), multi=True)
    print("This is the table of the number of medals won by each nation all time \n")
    print("('NOC', Team, Medal, Amount of Medals)\n")
    for res in result_iterator:
        result= mycursor.fetchall()
        for x in result:
            print(x)
        print('\n')
    
'''
with open('/Users/bearone/Desktop/progetto_DB/Query2(BETA).sql','r') as sql_file:
    result_iterator=mycursor.execute(sql_file.read(), multi=True)
    print("(NOC, Average Height, Average Weight)")
    for res in result_iterator:
        result=mycursor.fetchall()
        for x in result:
            column_names = [i[0] for i in mycursor.description]
            print(x)
        print('\n')


with open('/Users/bearone/Desktop/progetto_DB/test3.sql','r') as sql_file:
    result_iterator=mycursor.execute(sql_file.read(), multi=True)
    for res in result_iterator:
        result=mycursor.fetchall()
        for x in result:
            print(x)
  '''          




#mycursor.execute("select * from Seasons")
#myresult=mycursor.fetchall()
#print('Table Seasons:')
#for x in myresult:
    #print(x)
    
#mycursor.execute("select * from participants")
#myresult=mycursor.fetchall()
#print('Table Participants:')
#for x in myresult:
    #print(x)
    
    

#mycursor.execute(file("/user/giulianoamadei/desktop/practice script.sql").read())
#mycursor.execute("insert into participants(ID) select ID, Name, Sex, Age, height, Weight, Event, Medal from athlete_events")
#db.commit()

#mycursor.execute("select * from athlete_events")
#myresult=mycursor.fetchall()
#for x in myresult:
   #print(x)

#mycursor.execute("select * from seasons")
#for x in mycursor:
    #print(x)

#def executeScriptsFromFile(filename):
#    fd = open("/Users/giulianoamadei/desktop/practice script.sql", 'r')
#    sqlFile = fd.read()
#    fd.close()
#    sqlCommands = sqlFile.split(';')
#
#    for command in sqlCommands:
#        try:
#            if command.strip() != '':
#                cursor.execute(command)
#        except IOError,msg:
#            print "Command skipped: ", msg

#executeScriptsFromFile('/Users/giulianoamadei/desktop/practice script.sql')
#db.commit()