import sqlite3
import sys


import recognation
from PyQt4 import QtGui
def create1():

    try:
        c.execute("""CREATE TABLE IA1_1
                 (nom TEXT, prenom TEXT, pre REAL)""")
    except:
        pass

    try:
        c.execute("""CREATE TABLE IA1_2
                 (nom TEXT, prenom TEXT, pre REAL)""")
    except:
        pass
    try:
        c.execute("""CREATE TABLE IA2_1
                 (nom TEXT, prenom TEXT, pre REAL)""")
    except:
        pass
    try:
        c.execute("""CREATE TABLE IA2_3
                 (nom TEXT, prenom TEXT, pre REAL)""")
    except:
        pass
    try:
        c.execute("""CREATE TABLE IA3_1
                 (nom TEXT, prenom TEXT, pre REAL)""")
    except:
        pass
    try:
        c.execute("""CREATE TABLE IA3_2
                 (nom TEXT, prenom TEXT, pre REAL)""")
    except:
        pass
    try:
        c.execute("""CREATE TABLE GTE1_1
                 (nom TEXT, prenom TEXT, pre REAL)""")
    except:
        pass
    try:
        c.execute("""CREATE TABLE GTE2_1
                 (nom TEXT, prenom TEXT, pre REAL)""")
    except:
        pass
    try:
        c.execute("""CREATE TABLE GTE3_1
                 (nom TEXT, prenom TEXT, pre REAL)""")
    except:
        pass
    try:
        c.execute("""CREATE TABLE MEC1_1
                 (nom TEXT, prenom TEXT, pre REAL)""")
    except:
        pass
    try:
        c.execute("""CREATE TABLE MEC1_1
                 (nom TEXT, prenom TEXT, pre REAL)""")
    except:
        pass
    try:
        c.execute("""CREATE TABLE MEC1_1
                 (nom TEXT, prenom TEXT, pre REAL)""")
    except:
        pass
    try:
        c.execute("""CREATE TABLE MEC1_1
                 (nom TEXT, prenom TEXT, pre REAL)""")
    except:
        pass



def insert2(cl,n,p):
    a=dernierID(cl)
    a=a+1
    c.execute("""SELECT nom FROM {} WHERE (nom = ? AND prenom = ?) """.format(cl),(n,p) )
    entry=c.fetchall()
    #print(entry)
    if entry.__len__()==0:
        c.execute("""INSERT INTO {}
                          values(?, ?, ?)""".format(cl), [n, p,a])
        conn.commit()
        print ('added successfully')
        ddd = recognation.setPics()
        ddd.start(cl,n,p,a)


        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText("Added Successfully")
        msg.setWindowTitle("Added")
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        msg.show()
        msg.exec_()
    else:
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Warning)
        msg.setText("Student already exisit !")
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        msg.show()
        msg.exec_()
def efface(cl,n,p):
    c.execute("""SELECT nom FROM {} WHERE (nom = ? AND prenom=?)""".format(cl), (n,p))
    entry = c.fetchall()
    # print(entry)
    if entry.__len__() == 0:
        print("l'eleve n'existe pas dans la liste!  ")
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Warning)
        msg.setText("Student not found !")
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        msg.show()
        msg.exec_()
    else:
        c.execute("""DELETE FROM {} WHERE
                                     (nom=? AND prenom=?)""".format(cl), [n, p])

        print('operation executee avec succes')
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        msg.setText("Deleted Successfully")
        msg.setWindowTitle("Added")
        msg.setStandardButtons(QtGui.QMessageBox.Ok)
        msg.show()
        msg.exec_()

def dernierID(u):


    recs = c.execute("""SELECT * FROM {} """.format(u))
    conn.commit()
    data = c.fetchall()
    if (data.__len__()==0):
        i=0

    else:
        i=data[data.__len__()-1][2]
        i=int(i)
    return i

def etudiantParID(u,id):
    recs = c.execute("""SELECT * FROM {} WHERE pre = ?""".format(u),(id,))
    conn.commit()
    dataa=c.fetchall()
    return (str(dataa[0][0])+" "+str(dataa[0][1]))
def supp():
    c.execute("""DELETE FROM IA1_1  """)
    c.execute("""DELETE FROM IA1_2  """)
    c.execute("""DELETE FROM EI1_1  """)
    c.execute("""DELETE FROM MEC1_1  """)
    conn.commit()











conn = sqlite3.connect('tabbb.db')
c = conn.cursor()




