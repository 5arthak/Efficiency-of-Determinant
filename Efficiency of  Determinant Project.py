import numpy as np
import time
import sys
import os
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import *
from numpy import *


loop = True
diagonalSum = 0

def chosenGaussianElimination():

    getMatrixDeterminantGaussianElimination(matrix1)

def chosenRecursion():
    start = time.time()
    label14 = Label(root,text = "The determinant of matrix by recursive method is:"+ str(getMatrixDeterminantRecursion(matrix1)))
    delta3 = time.time() - start
    label15 = Label(root, text = "Time efficiency of calculating determinant using recursion is:"+str(delta3)+" seconds\n")
    label14.pack()
    label15.pack()

def chosenSpecialMatrix():

    getdeterminantbySpecialMatrix()

def restartProgram():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def leave():
    messagebox.showerror  ("Thanks","Thank You for using Determinant Calculator!")
    exit()

root = Tk()
theLabel = Label(root, text = "Determinant Calculator")
theLabel.pack(pady = 10)

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)

bottomFrame.pack(side = BOTTOM)

button1 = Button(topFrame, command = chosenSpecialMatrix,text = "Check for Special Matrix")
button2 = Button(topFrame, command = chosenGaussianElimination ,text = "Determinant by \"Gaussian Elimination\" ")
button3 = Button(topFrame, command = chosenRecursion, text = "Determinant by \"Recurrsion\"")
button4 = Button(topFrame, command = restartProgram,text = "Enter another matrix")
button5 = Button(topFrame, command = leave, text = "Exit!")
button1.pack(pady = 5)
button2.pack(pady = 5)
button3.pack(pady = 5)
button4.pack(pady = 5)
button5.pack(pady = 5)


numRows = simpledialog.askinteger("Input", "Enter Number of Rows: ")
numCols = simpledialog.askinteger("Input","Enter Number of Columns: ")
if numRows != numCols:
    messagebox.showerror ("Error","You entered an invalid matrix.\nPlease re-run a program and enter a valid square matrix ")
    messagebox.showerror  ("Thanks!","Thank You for using this program!")
    exit()
matrix1 = []
for i in range (0,numCols):
    matrix1.append([])
for i in range (0,numRows):
    for j in range(0,numCols):
        matrix1[i].append(j)
        matrix1[i][j] = 0
for i in range (0,numRows):
    for j in range (0, numCols):
        matrix1[i][j] = simpledialog.askinteger("Input",'Element for row:'+str(i+1)+'column'+str(j+1))
matrix2 = matrix(matrix1)
theLabel2 = Label(root, text = "The entered Matrix is:\n"+str(matrix2))
theLabel2.pack(pady = 10)

def islowertriangular(matrix1):
    for i in range(0, len(matrix1)):
        for j in range(i + 1, len(matrix1)):
            if(matrix1[i][j] != 0):
                    return False
    return True

def isuppertriangular(matrix1):
    for i in range(1, len(matrix1)):
        for j in range(0, i):
            if(matrix1[i][j] != 0):
                    return False
    return True

def diagonalSum(matrix2):
    size = len(matrix2[0])
    if size ==1:
        return matrix2[0][0]*2
    diagonalSum = 0
    for i in range(size):
        diagonalSum += matrix2[i][i]
        diagonalSum += matrix2[i][size-i-1]
    return diagonalSum

def getMatrixDeterminantGaussianElimination(matrix2):
    start = time.time()
    matrix3 = matrix2
    len1 = len(matrix2)
    len2 = len(matrix2[0])
    for i in range(min(len1, len2)):
        #print (map(lambda y: map(lambda x: "{0:.2f}".format(x), y), matrix2))
        for j in range(i + 1, len1):
            for k in range(i, len2):
                matrix3[j][k] = matrix2[j][k] - (matrix2[j][i] / matrix2[i][i]) * matrix2[i][k]
    matrix4 = matrix(matrix3)
    delta2 = time.time() - start
    theLabel3 = Label(root, text="The matrix after Gaussian elinimation is:\n"+str(matrix4))
    theLabel4 = Label(root, text='Determinant = Product of Matrix Diagonal ='+str(matrix4.diagonal().prod()))
    theLabel5 = Label(root, text="Time efficiency of calculating determinant by Gaussian elimination is:" + str(delta2) +" seconds\n")
    theLabel3.pack()
    theLabel4.pack()
    theLabel5.pack()

def getMatrixMinorRecursion(matrix2,i,j):
    return [row[:j] + row[j+1:] for row in (matrix2[:i]+matrix2[i+1:])]

def getMatrixDeterminantRecursion(matrix2):
    if len(matrix2) == 2:
        return matrix2[0][0]*matrix2[1][1]-matrix2[0][1]*matrix2[1][0]

    determinant = 0
    for k in range(len(matrix2)):
        determinant += ((-1)**k)*matrix2[0][k]*getMatrixDeterminantRecursion(getMatrixMinorRecursion(matrix2,0,k))
    return determinant

def getdeterminantbySpecialMatrix():
    start = time.time()
    heading1 = Label(root, text = "SPECIAL MATRIX METHOD")
    if (islowertriangular(matrix1) and isuppertriangular(matrix1)):
        label7 = Label(root, text = 'The entered matrix is a DIAGONAL MATRIX \nAnd the diagonal is:\n'+ str(diagonal(matrix2)))
        label8  = Label(root, text = 'Determinant = Product of Matrix Diagonal ='+str(matrix2.diagonal().prod()))
        label7.pack()
        label8.pack()
    elif islowertriangular(matrix1):
        label9 = Label(root,text = 'The entered matrix is a LOWER TRIANGULAR MATRIX \n And the diagonal is:'+str(diagonal(matrix2)))
        label10 = Label(root, text = 'Determinant = Product of Matrix Diagonal ='+str(matrix2.diagonal().prod()))
        label9.pack()
        label10.pack()
    elif isuppertriangular(matrix1):
        label11 = Label(root, text = 'The entered matrix is a UPPER TRIANGULAR MATRIX \n And the diagonal is:'+ str(diagonal(matrix2)))
        label12 = Label(root, text = 'Determinant = Product of Matrix Diagonal ='+str(matrix2.diagonal().prod()))
        label11.pack()
        label12.pack()
    else:
        label13 = Label(root, text = 'The entered matrix is not a special matrix!')
        label13.pack()
    delta1 = time.time() - start
    theLabel6 = Label(root, text="Time taken by the algorithm was:" + str(delta1) +" seconds\n")
    theLabel6.pack()


root.geometry('800x600')
root.mainloop()