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
ser = serial.Serial(port='COM11', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS, timeout=0)


class MainWid(BoxLayout):
    tpuerto1 = ObjectProperty()
    title = StringProperty("Controlador Garra")
    subtitle = StringProperty("Peter Yau; 17914 \n Daniel Cano; 17272")
    text = StringProperty("ola k ")
    valorescrito = StringProperty()
    rec1 = []
    rec2 = [1,2,3,4,5,6]
    rec3 = [0,2,4,6,8,10]
    numero = StringProperty()
    #man1 = 0
    #man2 = 0
    #man3 = 0
#-------------------------------Mandar-------------------------------------------
    def mandar1(self):
        for man1 in self.rec1:
            ser.write(man1)
            print(man1)
        rec1.clear()
    def mandar2(self):
        for man2 in self.rec2:
            ser.write(man2)
            print(man2)
        rec1.clear()
    def mandar3(self):
        for man3 in self.rec3:
            ser.write(man3)
            print(man3)
        rec1.clear()
#-------------------------------Recibir Datos-------------------------------------------

    def Serial1(self):
        self.valorescrito=self.tpuerto1.text
        x=int(self.valorescrito, base=0)
        x=x*10      
        ser.flushInput()
        
        while x>0:
            time.sleep(0.1)
            #print ("hola")
            self.rec1.extend([ord(ser.read(4))])
            #self.rec1.extend([13,15,17])
            x=x-1
        self.numero=("Datos Guardados")
        print(self.rec1)
        ser.close()
        
    def Serial2(self):
        self.valorescrito=self.tpuerto1.text
        y=int(self.valorescrito, base=0)
        y=y*10
        ser.flushInput()
        
        while y>0:
            time.sleep(0.1)
            print ("hola1")
            a=ser.read(2)
            a=ord(a)
            self.rec2.extend([a])
            #self.rec1.extend([13,15,17])
            y=y-1
        self.numero = ("Datos Guardados")
        print(self.rec2)
        ser.close()
        
    def Serial3(self):
        self.valorescrito=self.tpuerto1.text
        z=int(self.valorescrito, base=0)
        z=z*10        
        ser.flushInput()
        
        while z>0:
            time.sleep(0.1)
            print ("hola2")
            self.rec1.extend([ser.read(4)])
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
