#LogicP
from GUIp import *
from PyQt6 import *
import formulas
import sys
import csv

class Logic(QtWidgets.QMainWindow,Ui_MainWindow):
    """
    Class for the GUI
    """
    cfile = open('output.csv','w',newline='')
    writer = csv.writer(cfile)
    writer.writerow(['List','Function','Result'])
    cfile.close()
    def __init__(self):
        """
        Initialize the class, connect buttons to functions
        :return: None
        """
        super().__init__()
        self.setupUi(self)
        self.firstIn.textChanged.connect(lambda : self.update())
        self.AddB.clicked.connect(lambda : self.add())
        self.subtractB.clicked.connect(lambda : self.subtract())
        self.multiplyB.clicked.connect(lambda : self.multiply())
        self.divideB.clicked.connect(lambda : self.divide())
        self.chooseB.clicked.connect(lambda : self.choose())
        self.ClearB.clicked.connect(lambda : self.clear())
        self.textOut.setText('Choose a function to perform')
        self.list = []
    def update(self):
        """
        Update the list of numbers
        :return: None
        """
        try:
            self.list = [float(i) for i in self.firstIn.toPlainText().split()]
        except:
            self.textOut.setText('Input must be numeric')
    def add(self):
        """
        Add all positive numbers in list, display result, write to csv
        :return: None
        """
        self.update()
        self.textOut.setText(f'Sum of all positive numbers in list: \n{formulas.add(self.list)}')
        cfile = open('output.csv','a',newline='')
        writer = csv.writer(cfile)
        writer.writerow([self.list,"add positive numbers",formulas.add(self.list)])
        cfile.close()
    def subtract(self):
        """
        Subtract all negative numbers in list, display result, write to csv
        :return: None
        """
        self.update()
        self.textOut.setText(f'Difference of all negative numbers in list: \n{formulas.subtract(self.list)}')
        cfile = open('output.csv','a',newline='')
        writer = csv.writer(cfile)
        writer.writerow([self.list,"difference of negative numbers",formulas.subtract(self.list)])
        cfile.close()
    def multiply(self):
        """
        Multiply all numbers in list, display result, write to csv
        :return: None
        """
        self.update()
        self.textOut.setText(f'Product of all the non-zero numbers in the list: \n{formulas.multiply(self.list)}')
        cfile = open('output.csv','a',newline='')
        writer = csv.writer(cfile)
        writer.writerow([self.list,"product of non-zero numbers",formulas.multiply(self.list)])
        cfile.close()
    def divide(self):
        """
        Divide all numbers in list, display result, write to csv
        :return: None
        """
        self.update()
        self.textOut.setText(f'Dividing all the numbers in the list: \n{formulas.divide(self.list)}')
        cfile = open('output.csv','a',newline='')
        writer = csv.writer(cfile)
        writer.writerow([self.list,"quotient of numbers",formulas.divide(self.list)])
        cfile.close()
    def choose(self):
        """
        Choose a number at random from list, display result, write to csv
        :return: None
        """
        self.update()
        self.textOut.setText(f'Choosing random number from list: \n{formulas.choose(self.list)}')
        cfile = open('output.csv','a',newline='')
        writer = csv.writer(cfile)
        writer.writerow([self.list,"random number",formulas.choose(self.list)])
        cfile.close()
    def clear(self):
        """
        Clear the text box
        :return: None
        """
        self.firstIn.setText('')
        self.textOut.setText('Choose a function to perform')
def main():
    """
    Main function
    :return: None
    """
    app = QtWidgets.QApplication([])
    window = Logic()
    window.show()
    app.exec()
   
if __name__ == '__main__':
    main()