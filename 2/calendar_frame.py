from tkinter import *
from tkinter import ttk
import datetime
import calendar
import time

class Date(ttk.Frame):
    date = None
    active = True
    weekend = False
    label_style = None

    activo ="#000000"
    inactivo ="#C2C2C2"
    finde ="#FF6157"
    
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=76, height=61, borderwidth=0.5, relief='groove')
        self.label_style= ttk.Label(self, text="", font=('Arial', 28, 'bold'), width=2, anchor=E, foreground=self.inactivo)
        self.label_style.place(x=37, y=22)


    def set_date(self,value=None):
        if value == None:
            return self.date
        if self.weekend == True:
            if self.active:
                self.label_style.config(foreground=self.finde)
            else:
                self.__weekend__ = False
                self.label_style.config(foreground=self.inactivo)         
        else:
            self.date = value
            self.set_active(True)
            self.label_style.config(text=self.date.day)

    

    def set_active(self, value=None):
        if value == None:
            return self.active
        elif value == True:
            if self.weekend:
                self.label_style.config(foreground=self.finde)
            else:
                self.label_style.config(foregroung=self.activo)
        else:
            self.active = False
            self.label_style.config(foreground=self.inactivo)

    
    


class Calendar(ttk.Frame):
   

    def __init__(self, parent, **args): #el frame que cubre la ventana
        self.year = datetime.date.today().year
        self.month = datetime.date.today().month
        ttk.Frame.__init__(self,parent, width = 532, height = 422)
        self.header()
        self.days_label()
        self.set_monthdateName(self.year,self.month)
        self.weeks()
        # date = Date()
       

    def weeks(self):
        self.cal = [day for day in calendar.monthcalendar(int(self.year),int(self.month))]
        print(self.cal)
        for week in range(len(self.cal)):
            for dayWeek in range(7):
                total = week + dayWeek * 7
                label_daysweek = ttk.Frame(self, width=76, height=55)
                label_daysweek.pack_propagate(0)
                ttk.Label(label_daysweek, text=self.cal[week][dayWeek],font=('Arial', 28,'bold'), anchor=CENTER, borderwidth=0.5,relief='groove').pack(fill=BOTH, expand=1)
                label_daysweek.place(x=dayWeek*76, y=61+55*week)


    def days_label(self):
        days = ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo')
        for i in range(7):
            label_days = ttk.Frame(self, width = 76, height=14) #el frame de los dias
            label_days.pack_propagate(0)
            ttk.Label(label_days, text=days[i], font=('Arial', 11), anchor=CENTER, borderwidth=0.5, relief='groove').pack(fill=BOTH, expand=1)
            label_days.place(x=i*76, y=45) #532/7= 76 #los duadraditos

    



    def set_monthdateName(self, year, month):
        self.weeks()
        str1 = calendar.month(year,month)
        self.label.configure(text=str1)


    def set_monthdate(self,x):
        if x == -1:
            self.month -= 1
            if self.month == 0:
                self.month = 12
                self.year -= 1
                # if self.month in meses:
            return self.set_monthdateName(self.year,self.month)
        elif x == +1:
            self.month += 1
            if self.month == 13:
                self.month = 1
                self.year += 1
            return self.set_monthdateName(self.year,self.month)
        elif x == -12:
            self.year -= 1
            if self.year == self.year - 1:
                self.year = self.year
                self.month = self.month - 12
            return self.set_monthdateName(self.year,self.month)       
        elif x == +12:
            self.year += 1
            if self.year == self.year + 1:
                self.year = self.year
                self.month = self.month + 12
            return self.set_monthdateName(self.year,self.month)
        else:
            pass

    
    def header(self):
    
        self.header = ttk.Frame(self, width=532, height=45,borderwidth=0.5, relief='groove')
        self.header.place(y=0, x=0)    #el frame donde estan los botones
        ##MES EN CURSO##
        self.label = ttk.Label(self.header, text="", width=15, anchor=CENTER, font=('Arial', 28, 'bold'))
        self.label.place(x=146, y=0) #label del mes
        ##BOTONES##           
        self.botonYearBack = ttk.Button(self.header, text = '<<', width=2,command=lambda: self.set_monthdate(-12))
        self.botonYearBack.place(x = 24, y = 8)
        self.botonYearNext = ttk.Button(self.header, text = '>>', width=2,command=lambda: self.set_monthdate(+12))
        self.botonYearNext.place(x = 462, y = 8)
        self.botonMonthNext = ttk.Button(self.header, text = '>', width=2,command=lambda: self.set_monthdate(+1))
        self.botonMonthNext.place(x = 408, y = 8)
        self.botonMonthBack = ttk.Button(self.header, text = '<', width=2,command=lambda: self.set_monthdate(-1))
        self.botonMonthBack.place(x = 78, y = 8)


class MainApp(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("Calendario")
        self.geometry("532x422")

        self.calendar = Calendar(self)
        self.calendar.place(x=0, y=0)

    def start(self):
        self.mainloop()

if __name__ == '__main__':
    ap = MainApp()
    ap.start()