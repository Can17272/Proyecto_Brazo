import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, ObjectProperty, ListProperty
from kivy.config import Config
from kivy.clock import Clock
from styles.common import *
import serial
import struct
import time
Config.set('graphics', 'width', 640)
Config.set('graphics', 'height', 640)
ser = serial.Serial(port='COM11', baudrate=2400, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS, timeout=0)


class MainWid(BoxLayout):
    tpuerto1 = ObjectProperty()
    title = StringProperty("Controlador Garra")
    subtitle = StringProperty("Peter Yau; 17914 \n Daniel Cano; 17272")
    text = StringProperty("ola k ")
    valorescrito = StringProperty()
    rec1 = []
    rec2 = []
    rec3 = []
    numero = StringProperty()
    #man1 = 0
    #man2 = 0
    #man3 = 0
#-------------------------------Mandar-------------------------------------------
    def mandar1(self):
        for man1 in self.rec1:
            ser.write(bytes([int(man1)]))
            print(bytes([int(man1)]))
        self.rec1.clear()
    def mandar2(self):
        for man2 in self.rec2:
            ser.write(bytes([int(man2)]))
            print(man2)
        self.rec1.clear()
    def mandar3(self):
        for man3 in self.rec3:
            ser.write(bytes([int(man3)]))
            print(man3)
        self.rec1.clear()
#-------------------------------Recibir Datos-------------------------------------

    def Serial1(self):
        self.valorescrito=self.tpuerto1.text
        x=int(self.valorescrito, base=0)
       # x=x/0.1  
        ser.flushInput()
        
        while x>0:
            time.sleep(1)
            b=ser.read(4)
            #b=int(b,0)
            #print ("hola")
            self.rec1.extend(b)
            #self.rec1.extend([13,15,17])
           
            x=x-1
        self.numero=("Datos Guardados")
        print(self.rec1)
        
        
    def Serial2(self):
        self.valorescrito=self.tpuerto1.text
        y=int(self.valorescrito, base=0)
        #y=y
        ser.flushInput()
        
        while y>0:
            time.sleep(1)
            print ("hola1")
            a=ser.read(4)
            #a=ord(a)
            self.rec2.extend(a)
            #self.rec1.extend([13,15,17])
            y=y-1
        self.numero = ("Datos Guardados")
        print(self.rec2)
        ser.close()
        
    def Serial3(self):
        self.valorescrito=self.tpuerto1.text
        z=int(self.valorescrito, base=0)
        #z=z*10        
        ser.flushInput()
        
        while z>0:
            time.sleep(1)
            c=ser.read(4)
            #print ("hola2")
            self.rec1.extend(c)
            #self.rec1.extend([13,15,17])
            z=z-1
        self.numero=("Datos Guardados")
        print(self.rec3)
        ser.close()
#---------------------------------------------------------------------------------------    


class MainApp(App):
    title = "Proyecto 3"

    def build(self):
        return MainWid()


if __name__ == "__main__":
    MainApp().run()
