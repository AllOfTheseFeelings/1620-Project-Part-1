#Part1
from GUILogic import *

def main():
    """
    Main function, pulls up GUI from GUILogic
    :return: None
    """
    cfile = open('output.csv','a',newline='')
    writer = csv.writer(cfile)
    app = QtWidgets.QApplication([])
    window = Logic()
    window.show()
    app.exec()
    cfile.close() #
   
if __name__ == '__main__':
    main()