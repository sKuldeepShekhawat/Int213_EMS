from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
from functools import partial
import sys
import time
import os
err="error"


#loading Database Files
if os.path.isfile('databases/E_id.dat'):
    pass
else:
    os.system("mkdir databases")
    f=open("databases/E_id.dat",'w')
    f.write('11915005')
    f.close();
    f=open("databases/database.dat",'w')
    f.close()
    print ("Files Created") 
try:
    f=open("databases/proDB.dat",'a')
    f.close();
except:
    f=open("databases/proDB.dat",'w')
    f.close();
try:
    f=open("databases/locDB.dat",'a')
    f.close();
except:
    f=open("databases/locDB.dat",'w')
    f.close();
try:
    f=open("databases/departDB.dat",'a')
    f.close();
except:
    f=open("databases/departDB.dat",'w')
    f.close();
    print ("Files Created") 




#main home class
class final(QMainWindow):
    def __init__(self):
      super().__init__()
      self.setWindowTitle('Employee Management System.')
      self.setFixedSize(1050,920)

      #frames
      self.newdata=QFrame()
      self.deletedata=QFrame()
      self.statusTrack=QFrame()
      self.About=QFrame()
      
      self.generalLayout = QVBoxLayout()#main layout
      
      #new layout
      self.newdataformlayout=QGridLayout()
      self.deleteDataLayout=QGridLayout()
      self.statusTrackLayout=QGridLayout()

      
      #extending subLayouts
      self.newdata.setLayout(self.newdataformlayout)
      self.deletedata.setLayout(self.deleteDataLayout)
      self.statusTrack.setLayout(self.statusTrackLayout)

      
      self._centralWidget = QWidget(self)
      self.setCentralWidget(self._centralWidget)
      self._centralWidget.setLayout(self.generalLayout)
      self.empc=0;
      self.pc=0;
      self.Cbutton()
      self.empMan()
      self.aboutlabels()
      self.label1()
      self.label2()
      self.label3()
      self.label4()
      self.label5()
      self.homeself()

      #adding subLayouts
      self.generalLayout.addWidget(self.newdata)
      self.generalLayout.addWidget(self.deletedata)
      self.generalLayout.addWidget(self.statusTrack)

      
      self.newdataform()
      self.deletedataform()
      self.labelC = QLabel(self)
      self.labelC.setText('')
      self.generalLayout.addWidget(self.labelC)
      self.newdata.hide()
      self.deletedata.hide()
      self.statusTrack.hide()
      
      

    def aboutlabels(self):
        Ayushlable="Ayush Gour\n 11905522"
        kuldeeplable="Kuldeep Singh\n 11915005"

        
        shadow1 = QGraphicsDropShadowEffect()
        shadow2 = QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(40)
        shadow2.setBlurRadius(45)
        
        #Ayush
        self.Ayush = QLabel(self)
        self.Ayush.setFixedSize(400,600)
        self.Ayush.setText(Ayushlable)
        self.Ayush.setFont(QFont("Arial", 15, QFont.Black))
        self.Ayush.setStyleSheet("background-color:rgb(235,155,155);color:white;\
                                                font-weight:bold;padding:20px")

        self.Ayush.setGraphicsEffect(shadow1)
        self.Ayush.move(40,100)

        #kuldeep
        self.Kuldeep = QLabel(self)
        self.Kuldeep.setFixedSize(400,600)
        self.Kuldeep.setText(kuldeeplable)
        self.Kuldeep.setFont(QFont("Arial", 15, QFont.Black))
        self.Kuldeep.setStyleSheet("background-color:skyblue;color:white;\
                                                font-weight:bold;padding:20px")

        self.Kuldeep.setGraphicsEffect(shadow2)  
        self.Kuldeep.move(600,100)

        
    def stat(self):
        labelLayout = QGridLayout()
        datalayout = QGridLayout()
        self.statHead={}
        self.tDic={}
        statHead={'Emp_ID':(0,0),
                  'Name':(0,1),
                  'Department':(0,2),
                  'Location':(0,3),
                  'ProjectName':(0,4),
                  'Manager':(0,5)}
        for lable,pos in statHead.items():
            self.statHead[lable] = QLabel(self)
            self.statHead[lable].setFixedSize(172,50)
            self.statHead[lable].setText(lable)
            self.statHead[lable].setFont(QFont('Arial',12))
            self.statHead[lable].setStyleSheet("background-color:orange;color:white;\
                                                font-weight:bold; \
                                                border:1px solid")

            
            labelLayout.addWidget(self.statHead[lable], pos[0], pos[1])
        self.statusTrackLayout.addLayout(labelLayout,0,0)
        file=open("databases/database.dat",'rt')
        data=file.read()
        data=list(data.split('|'))
        file.close()
        
        
        #0,1,2,5,4,7 agregate by 14
        for i in range(len(data)):
            data[i]=tuple(data[i].split(","))
            tDic={}
            
            try:
                tDic={data[i][0]:(i,0),
                      data[i][1]:(i,1),
                      data[i][2]:(i,2),
                      data[i][5]:(i,3),
                      data[i][4]:(i,4),
                      data[i][8]:(i,5)}
            except:
                pass
            for lable,pos in tDic.items():
                self.tDic[lable] = QLabel(self)
                self.tDic[lable].setFixedSize(172,50)
                self.tDic[lable].setText(lable)
                self.tDic[lable].setFont(QFont('Arial',7))
                self.tDic[lable].setStyleSheet("background-color:rgb(200,200,200);color:black;\
                                                    font-weight:bold; \
                                                    border:1px solid")

                
                datalayout.addWidget(self.tDic[lable], pos[0], pos[1])
            i=i+14
        self.statusTrackLayout.addLayout(datalayout,1,0)
        
                                               
    def empcount(self):
      self.empc=self.empc+1;
      database=open("databases/database.dat","rt")
      string=database.read()
      self.empc=string.count("e_id:")
      tstr='Total Employees:\n'+str(self.empc)
      self.settext(self.labelA,tstr)
      database.close()
      print("employee:",self.empc)
      return str(self.empc)
    def pcount(self):
      file=open("databases/proDB.dat","rt")
      string=file.read()
      self.pc=string.count("@")
      tstr='Total Projects:\n'+str(self.pc)
      file.close()
      print("project:",self.pc)
      self.settext(self.labelB,tstr)
      return str(self.pc)
    def loccount(self):
      file=open("databases/locDB.dat","rt")
      string=file.read()
      self.lc=string.count("@")
      tstr='Locations:\n'+str(self.lc)
      file.close()
      print("location:",self.lc)
      self.settext(self.labelE,tstr)
      return str(self.lc)
    def depcount(self):
      file=open("databases/departDB.dat","rt")
      string=file.read()
      self.depc=string.count("@")
      tstr='Departments:\n'+str(self.depc)
      file.close()
      print("department:",self.depc)
      self.settext(self.labelD,tstr)
      return str(self.depc)

    
    def settext(self,instance,text):
      instance.setText(text)
    def label1(self):
      shadow = QGraphicsDropShadowEffect() 
      shadow.setBlurRadius(15)
      self.labelA = QLabel(self)
      fstring='Total Employees:\n'
      self.labelA.setText(fstring)
      self.labelA.setFont(QFont("Arial", 15, QFont.Black))
      self.labelA.setStyleSheet("background:rgb(235,155,155);padding:20px;color:white;")
      self.labelA.setFixedSize(410,100)
      self.labelA.move(12, 70)
      self.labelA.setGraphicsEffect(shadow)
    def label2(self):
      shadow = QGraphicsDropShadowEffect() 
      shadow.setBlurRadius(15)
      self.labelB = QLabel(self)
      fstring='Total Projects:\n'
      self.labelB.setText(fstring)
      self.labelB.setFont(QFont("Arial", 15, QFont.Black))
      self.labelB.setStyleSheet("background:rgb(155,195,155);padding:20px;color:hue")
      self.labelB.setFixedSize(410,100)
      self.labelB.move(425, 70)
      self.labelB.setGraphicsEffect(shadow)
    def label3(self):
      shadow = QGraphicsDropShadowEffect() 
      shadow.setBlurRadius(15)
      self.labelD = QLabel(self)
      self.labelD.setText('Departments:\n')
      self.labelD.setFont(QFont("Arial", 15, QFont.Black))
      self.labelD.setStyleSheet("background:lightgreen;padding:20px;color:darkgreen")
      self.labelD.setFixedSize(410,100)
      self.labelD.move(12, 175)
      self.labelD.setGraphicsEffect(shadow)
    def label4(self):
      shadow = QGraphicsDropShadowEffect() 
      shadow.setBlurRadius(15)
      self.labelE = QLabel(self)
      self.labelE.setText('Locations:\n')
      self.labelE.setFont(QFont("Arial", 15, QFont.Black))
      self.labelE.setStyleSheet("background:skyblue;padding:20px;color:white")
      self.labelE.setFixedSize(410,100)
      self.labelE.move(425, 175)
      self.labelE.setGraphicsEffect(shadow)
    def label5(self):
      shadow = QGraphicsDropShadowEffect() 
      shadow.setBlurRadius(15)
      self.labelF = QLabel(self)
      self.desk=QLabel(self)
      self.desk.setText('DESK')
      self.labelF.setText('HR')
      self.desk.setFont(QFont("Arial", 10, QFont.Black))
      self.labelF.setFont(QFont("Arial", 45, QFont.Black))
      self.labelF.setStyleSheet("background:orange;padding:20px;color:white")
      self.labelF.setFixedSize(200,205)
      self.labelF.move(840, 70)
      self.desk.move(915,199)
      self.labelF.setGraphicsEffect(shadow)
    def Cbutton(self):
        self.btn = {}
 
        buttonsLayout = QGridLayout()
 
        btn = {
            'LogOut': (0, 0),
            'Employee Management': (0,1),
            'Status Track':(0,2),
            'About':(0,3),
            'Home':(0,4)
            }
    
 
        for btnText, pos in btn.items():
            self.btn[btnText] = QPushButton(btnText)
            self.btn[btnText].setFixedSize(200, 50)
            self.btn[btnText].setStyleSheet("background-color : rgb(55,55,55); \
                                                 font-weight:bold; color:white;")
            buttonsLayout.addWidget(self.btn[btnText], pos[0], pos[1])
 
        self.generalLayout.addLayout(buttonsLayout)

    def empMan(self):
        self.empbtn = {}
 
        self.buttonsLayoutemp = QGridLayout()
 
        empbtn = {
            'New Joining': (1,1),
            'Terminate':(1,2),
            }
    
 
        for btnText, pos in empbtn.items():
            self.empbtn[btnText] = QPushButton(btnText)
            self.empbtn[btnText].setFixedSize(255, 80)
            self.empbtn[btnText].setFont(QFont('Arial', 15)) 
            self.empbtn[btnText].setStyleSheet("background-color : rgb(35,35,35); \
                                                 font-weight:bold; color:white;")
            
            self.buttonsLayoutemp.addWidget(self.empbtn[btnText], pos[0], pos[1])
        self.generalLayout.addLayout(self.buttonsLayoutemp)
        





    def newdataform(self):
        self.form_data={}
        self.form_text={}
        form_data={
              ('Full-Name','nameDisplay'):('Full_Name',0),
              ('Department Assigned','Ddisplay'):('department',1),
              ('Salary per Annum','S_Display'):('salary',2),
              ('Project Name','ProDisplay'):('P_name',3),
              ('Office Location','locDisplay'):('P_no',4),
              ('Email Id','EDisplay'):('email',5),
              ('Position/Job Title','pdisplay'):('post',6),
              ('Manager Name','mdisplay'):('manager',7),
              ('Date Of Joining','dojDisplay'):('doj',8),
              ('Gender','gdisplay'):('gender',9),
              ('Contact No','C_display'):('c_text',10),
              ('Highest Education Aquired','eduDisplay'):('eduText',11),
              ('Address with pincode','addDisplay'):('address',12)
              
          }

        for atrtext, pos in form_data.items():
            self.form_data[pos[0]] = QLabel(atrtext[0],self)
            self.form_data[pos[0]].setFont(QFont("Arial", 10, QFont.Black))
            self.form_text[atrtext[1]] = QLineEdit()
            self.form_text[atrtext[1]].setFixedSize(630,40)
            self.form_text[atrtext[1]].move(self.rect().center())
            f = self.form_text[atrtext[1]].font()
            f.setPointSize(12) # sets the size to 12
            self.form_text[atrtext[1]].setFont(f)
            self.form_text[atrtext[1]].setAlignment(Qt.AlignLeft)
            self.form_text[atrtext[1]].setReadOnly(0)
            self.newdataformlayout.addWidget(self.form_data[pos[0]],pos[1],0)
            self.newdataformlayout.addWidget(self.form_text[atrtext[1]],pos[1],1)
        self.addnewdatabtn=QPushButton("ADD New Employee")
        self.addnewdatabtn.setFixedSize(255, 70)
        self.addnewdatabtn.setFont(QFont('Arial', 12)) 
        self.addnewdatabtn.setStyleSheet("background-color : rgb(135,35,35); \
                                                 font-weight:bold; color:white;")
        self.newdataformlayout.addWidget(self.addnewdatabtn,14,1)
        




    def deletedataform(self):
        self.deleteidfield=QLineEdit()
        self.deleteidfield.setText('11915006')
        self.deletefieldlabel=QLabel("Enter Emp_ID to be terminated")
        self.deletefieldlabel.setFont(QFont("Arial", 10, QFont.Black))
        self.deleteidfield.setFixedSize(630,40)
        f = self.deleteidfield.font()
        f.setPointSize(12) # sets the size to 12
        self.deleteidfield.setFont(f)
        self.deletedatabtn=QPushButton("Terminate Employee")
        self.deletedatabtn.setFixedSize(255, 70)
        self.deletedatabtn.setFont(QFont('Arial', 12))
        self.deleteDataLayout.addWidget(self.deleteidfield,0,1)
        self.deleteDataLayout.addWidget(self.deletefieldlabel,0,0)
        self.deletedatabtn.setStyleSheet("background-color : rgb(135,35,35); \
                                                 font-weight:bold; color:white;")
        self.deleteDataLayout.addWidget(self.deletedatabtn,14,1)
        self.itemPresenceflag=QLabel("Status Return will be seen here")
        self.deleteDataLayout.addWidget(self.itemPresenceflag,12,1)
    def terminate(self):
        file=open('databases/database.dat','r');
        data=file.read()
        data=list(data.split("|"))
        E_id=self.deleteidfield.text();
        TE_id="e_id:"+E_id;
        index=-1
        try:
	#search for the item
            for i in range(len(data)):
                if data[i].count(TE_id)>0:    
                    index = i
                    indexData=data[i]
                    print(indexData)
            
        except:
            index=-1
        
        if index>=0:
            self.itemPresenceflag.setText("Id found and deleted successfully...")
            data.remove(indexData)
                
        else:
            self.itemPresenceflag.setText("Element Not found")
        file=open("databases/database.dat","w");
        for i in data:
            file.write(i+"|")
        file.close()
        self.depcount()
        self.loccount()
        self.pcount()
        self.empcount()
            
    def homeemp(self):
        self.labelA.setHidden(1);
        self.labelB.setHidden(1)
        self.labelD.setHidden(1);
        self.labelE.setHidden(1)
        self.labelF.setHidden(1)
        self.desk.setHidden(1)
        self.newdata.hide()
        self.statusTrack.hide()
        self.deletedata.hide()
        self.Ayush.setHidden(1);
        self.Kuldeep.setHidden(1);
        for btnText, pos in self.empbtn.items():
            self.empbtn[btnText].setHidden(0)
    def homestat(self):
        self.statusTrack.setParent(None)
        self.statusTrack=QFrame()
        self.statusTrackLayout=QGridLayout()
        self.statusTrack.setLayout(self.statusTrackLayout)
        self.generalLayout.addWidget(self.statusTrack)

        
        self.labelA.setHidden(1);
        self.labelB.setHidden(1)
        self.labelD.setHidden(1);
        self.labelE.setHidden(1)
        self.labelF.setHidden(1)
        self.desk.setHidden(1)
        self.newdata.hide()
        self.deletedata.hide()
        self.Ayush.setHidden(1);
        self.Kuldeep.setHidden(1);
        self.statusTrack.show()
        self.stat()
      
        for btnText, pos in self.empbtn.items():
            self.empbtn[btnText].setHidden(1)
    def homeattend(self):
        
        self.labelA.setHidden(1);
        self.labelB.setHidden(1)
        self.labelD.setHidden(1);
        self.labelE.setHidden(1)
        self.labelF.setHidden(1)
        self.desk.setHidden(1)
        self.deletedata.hide()
        self.Ayush.setHidden(0);
        self.Kuldeep.setHidden(0);
        self.newdata.hide()
      
        self.statusTrack.hide()
        for btnText, pos in self.empbtn.items():
            self.empbtn[btnText].setHidden(1)
    def homeself(self):
        self.labelA.setHidden(0);
        self.labelB.setHidden(0)
        self.labelD.setHidden(0);
        self.labelE.setHidden(0)
        self.labelF.setHidden(0)
        self.desk.setHidden(0)
        self.newdata.hide()
        self.deletedata.hide()
        self.Ayush.setHidden(1);
        self.Kuldeep.setHidden(1);
        self.statusTrack.hide()
        for btnText, pos in self.empbtn.items():
            self.empbtn[btnText].setHidden(1)
    def Logout(self):
      self.close();
    
    def joiningform(self):
      self.newdata.show()
      self.deletedata.hide()
    def modDetail(self):
      self.newdata.hide()
      self.deletedata.hide()
    def Terminate(self):
      self.newdata.hide()
      self.deletedata.show()
    def Anew(self):
      self.newdata.hide()
      self.deletedata.hide()
    def newE_id(self):
      e_idFile=open("databases/E_id.dat",'r+t');
      e_id=e_idFile.read();
      inte_id=int(e_id);
      newone=inte_id+1;
      e_idFile.seek(0)
      e_idFile.truncate()
      print("new id:",newone,end=" ")
      e_idFile.write(str(newone));
      e_idFile.close()
      return str(newone)
    
    def appendToBase(self):
      basefile=open("databases/database.dat","r+");
      departfile=open("databases/departDB.dat","r+");
      locfile=open("databases/locDB.dat","r+");
      basefiledata=basefile.read()
      email=self.form_text["EDisplay"].text();
      if basefiledata.count(email)==0:
          basefile.write("e_id:"+self.newE_id()+",")
          for i in self.form_text:
            text=self.form_text[i].text()
            basefile.write(text+",")
          basefile.write("|")
          print("inserted")
      else:
          print("record already exist")
      basefile.close()
      projectfile=open("databases/proDB.dat","r+");
      project_name=self.form_text["ProDisplay"].text()
      proData=projectfile.read()
      if proData.count(project_name)==0:
          projectfile.write(project_name+"@\n");
          print("project database modified")
      projectfile.close()
      department_name=self.form_text["Ddisplay"].text()
      departData=departfile.read()
      if departData.count(department_name)==0:
          departfile.write(department_name+"@\n");
          print("department database modified")
      departfile.close()
      location_name=self.form_text["locDisplay"].text()
      locData=locfile.read()
      if locData.count(location_name)==0:
          locfile.write(location_name+"@\n");
          print("delocation database modified")
      locfile.close()

      self.depcount()
      self.loccount()
      self.pcount()
      self.empcount()
   

      















       
class logscr(QMainWindow):
  def __init__(self,obj):
    super().__init__()
    self.home=obj
    self.setWindowTitle('Employee Management System.')
    self.setFixedSize(450,520)
    self.generalLayout = QVBoxLayout()
    self._centralWidget = QWidget(self)
    self.setCentralWidget(self._centralWidget)
    self._centralWidget.setLayout(self.generalLayout)
    
    self.img()
    self.label_1 = QLabel('Employee ID', self) 
    self.generalLayout.addWidget(self.label_1)
    self.t1()
    self.label_2 = QLabel('Employee Name', self)
    self.generalLayout.addWidget(self.label_2)
    self.t2()
    self.inButton()
    
  def img(self):
    def logo(self):
      self.label = QLabel(self)
      self.pixmap = QPixmap('login1.png')
      self.img=self.label.setPixmap(self.pixmap)  
      self.label.resize(self.pixmap.width(),self.pixmap.height())
      self.generalLayout.addWidget(self.label)
    self.logo()
    self.label = QLabel(self)
    self.pixmap = QPixmap('image2.png')
    self.img=self.label.setPixmap(self.pixmap)  
    self.label.resize(self.pixmap.width(),self.pixmap.height())
    self.generalLayout.addWidget(self.label)
  def logo(self):
    self.label = QLabel(self)
    self.pixmap = QPixmap('login1.png')
    self.img=self.label.setPixmap(self.pixmap)  
    self.label.resize(self.pixmap.width(),self.pixmap.height())
    self.generalLayout.addWidget(self.label)
  def t1(self):
        self.display = QLineEdit()
        self.display.setFixedSize(430,40)
        self.display.move(self.rect().center())
        f = self.display.font()
        f.setPointSize(12) # sets the size to 27
        self.display.setFont(f)
        self.display.setAlignment(Qt.AlignLeft)
        self.display.setReadOnly(0)
 
        self.generalLayout.addWidget(self.display)
  def t2(self):
        self.display1 = QLineEdit()
        self.display1.setFixedSize(430,40)
        f = self.display1.font()
        f.setPointSize(12) # sets the size to 27
        self.display1.setFont(f)
        self.display1.setAlignment(Qt.AlignLeft)
        self.display1.setReadOnly(0)
 
        self.generalLayout.addWidget(self.display1)

  def inButton(self):
        self.buttons = {}
 
        buttonsLayout = QGridLayout()
 
        buttons = {
            'Login': (0, 0),
            'Clear': (0,1)
            }
 
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(150, 50)
            self.buttons[btnText].setStyleSheet("background-color : rgb(55,55,55); \
                                                 font-weight:bold; color:white;")
            buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
 
        self.generalLayout.addLayout(buttonsLayout)
  def clearDisplay(self):
        self.display.setText('')
        self.display1.setText('')
  def login(self):
      E_id=self.display.text();
      name=self.display1.text();
      if E_id=='E1234' and name=='admin':
        print('welcome {}'.format(name));
        self.close()
        self.home.appendToBase()
        self.home.show()
      else:
        print("UnAuthorised: You are not allowed to go through...");
class PyCalcCtrl:
    def __init__(self, model, view, home):
        self._evaluate = model
        self._home=home
        self._view = view
        self._connectSignals()
 
    def _connectSignals(self):
        self._view.buttons["Login"].clicked.connect(self._view.login)       
        self._view.buttons["Clear"].clicked.connect(self._view.clearDisplay)
        #command for home page
        #command for home page
        self._home.btn["LogOut"].clicked.connect(self._home.Logout)
        self._home.btn["About"].clicked.connect(self._home.homeattend)
        self._home.btn["Status Track"].clicked.connect(self._home.homestat)
        self._home.btn['Employee Management'].clicked.connect(self._home.homeemp)
        self._home.btn['Home'].clicked.connect(self._home.homeself)
        self._home.empbtn['New Joining'].clicked.connect(self._home.joiningform)
        self._home.empbtn['Terminate'].clicked.connect(self._home.Terminate)
        self._home.addnewdatabtn.clicked.connect(self._home.appendToBase)
        self._home.deletedatabtn.clicked.connect(self._home.terminate)







        
def evaluateExpression(expression):
    try:
        result = str(eval(expression, {}, {}))
 
    except Exception:
        result = err
 
    return result

def main():
    pycalc = QApplication(sys.argv)
    pycalc.setStyle('Fusion')
    home=final()
    view = logscr(home)
 
 
 
    view.show()
 
    model = evaluateExpression
    PyCalcCtrl(model=model, view=view, home=home)
 
    sys.exit(pycalc.exec_())
 
if __name__ == "__main__":
    main()


