from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QDesktopWidget, QLineEdit, QHBoxLayout, QMessageBox
import sys
from PySide2.QtGui import QIcon, QPixmap




import sys
import matplotlib



from PySide2.QtWidgets import QMainWindow, QApplication

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import sys
from PySide2.QtWidgets import QApplication, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide2.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np





class Window(QWidget):
    func = ""
    valid = True
    check2 = True
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graph Calculator")  
        self.setGeometry(600,600,600,500)
        self.SetappIcon()
        self.setMainIcon()
        self.button()
        self.center()
        self.GUI()

    def SetappIcon(self):
        icon = QIcon("icon.png")
        self.setWindowIcon(icon) 

    def setMainIcon(self):
        label = QLabel(self)

        # Load the image using QPixmap
        pixmap = QPixmap("icon.png")

        # Set the pixmap to the label
        label.setPixmap(pixmap)

        # Resize the label to fit the image
        label.resize(pixmap.width(), pixmap.height())

        # Set the position of the label within the main window
        label.move(470, 5)


    def button(self):
        self.btn = QPushButton("graph", self)
        self.btn.resize(80,30)
        self.btn.move(510,400)

    def center(self):
        cen = self.frameGeometry()
        centerpoint = QDesktopWidget().availableGeometry().center()
        cen.moveCenter(centerpoint)
        self.move(cen.topLeft())

    def GUI(self):
        # Create a label
        layout = QVBoxLayout()
        label = QLabel("Enter your function:", self)

        self.func_text_box = QLineEdit(self)
        self.func_text_box.setFixedWidth(200)
        self.func_text_box.move(20,170)
        layout.addWidget(label)
        layout.addWidget(self.func_text_box)
        
        
        
        label2 = QLabel("Enter x Min:", self)
        label2.move(20, 200)
        self.x_min_text_box = QLineEdit(self)
        self.x_min_text_box.setFixedWidth(200)
        self.x_min_text_box.move(20,220)
        layout.addWidget(label2)
        layout.addWidget(self.x_min_text_box)

        label3 = QLabel("Enter x Max:", self)
        label3.move(20, 250)
        self.x_max_text_box = QLineEdit(self)
        self.x_max_text_box.setFixedWidth(200)
        self.x_max_text_box.move(20,270)
        layout.addWidget(label3)
        layout.addWidget(self.x_max_text_box)
        layout.addWidget(self.btn)
        self.btn.clicked.connect(self.GetInput)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        
        layout.addWidget(self.canvas)

        

        # Set the layout for the QWidget
        self.setLayout(layout)

    def GetInput(self):
        self.userInput = self.func_text_box.text()
        try:
            self.min_x = int(self.x_min_text_box.text())
            self.max_x = int(self.x_max_text_box.text())
        except ValueError:
            self.check2 = False
            

        
        check = self.validate_input()
        if not check or not self.check2:
            Messagebox = QMessageBox.warning(self, "Wrong Input", "Please Enter right input")
            self.func = ""
            self.userInput = ""
            self.min_x = None
            self.max_x = None
            self.func = ""
            self.valid = False
            self.check2 = True
            self.figure.clear()

        else:
            for i in self.userInput:
                if i != "^":
                    self.func+=i
                elif i == "^":
                    self.func+="**"

            self.func = self.func[2:]

            self.plot()
            self.func = ""
            self.userInput = ""
            self.min_x = None
            self.max_x = None
            self.figure.clear()

        

    def plot(self):
    
        
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        if self.func.isnumeric():
            ax.axhline(y = self.func, color = 'r', linestyle = '-')
            self.canvas.draw()
            return

        
        x = np.linspace(self.min_x, self.max_x, 50)  # Assuming x values from 0 to 9
        y = eval(self.func)# Evaluate the user input expression for y values

        # Plot the data
        ax.plot(x, y)

        # Set labels and title
       

        # Redraw the canvas
        self.canvas.draw()      

        
        
    
        



           


            

    def validate_input(self):

        if len(self.userInput) < 3:
            return False
        
        if (self.userInput[-1] == "-" or self.userInput[-1] == "+" or self.userInput[-1] == "/" or self.userInput[-1] == "^"):
            return False
        
        self.userInput = self.userInput.lower()
        
        if self.userInput[0]!= "y" or self.userInput[1] != "=": # doesn't start with y=
            return False
        
        
        for i in self.userInput: #check any wrong character not included in our calculator
            if i != "x" and i != "y" and i != "=" and (not i.isdigit()) and i!= "*" and i!="/" and i!="^" and i!="-" and i!="+":
                return False
            
        for i in range(len(self.userInput)): 
            if i == len(self.userInput)-1:
                if self.userInput[i] == "=":
                    return False
            if i > 1 and self.userInput[i] == "=":
                return False

            if self.userInput[i] == "=":  #check if after "=" there is a number or "x" or "-" or "+"
                if (not self.userInput[i+1].isdigit()) and self.userInput[i+1] != "x" and self.userInput[i+1] != "+" and self.userInput[i+1] != "-":
                    return False
            if self.userInput[i] == "-": #using any operator except - or + after - is considered an error
                if self.userInput[i+1] == "*" or self.userInput[i+1] == "^" or self.userInput[i+1] == "/":
                    return False
                
            if self.userInput[i] == "/" or self.userInput[i] == "^" or self.userInput[i] == "*": #using any two operators successively is conisdered an error 
                if self.userInput[i+1] == self.userInput[i]:
                    return False
                if self.userInput[i] == "/" and (self.userInput[i+1] == "+" or  self.userInput[i+1] == "*" or self.userInput[i+1] == "^"):
                    return False
                if self.userInput[i] == "^" and (self.userInput[i+1] == "/" or  self.userInput[i+1] == "*" or self.userInput[i+1] == "+"):
                    return False
                if self.userInput[i] == "*" and (self.userInput[i+1] == "/" or  self.userInput[i+1] == "^" or self.userInput[i+1] == "+"):
                    return False
                
            if self.userInput[i].isdigit(): #making sure that there is an operator after any digit or another digit
                if self.userInput[i+1] != "+" and self.userInput[i+1] != "-" and self.userInput[i+1] != "/" and self.userInput[i+1] != "^" and self.userInput[i+1] != "*" and not(self.userInput[i+1].isdigit()):
                    return False 
                
                
                
            

                
        
        return True




        


        
    


myApp = QApplication(sys.argv)
window = Window()
window.show()
myApp.exec_()
sys.exit(0)


