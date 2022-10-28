import pyfirmata
import serial
from itertools import count
import configparser
import threading
import os
from roboreactmaster import Create_node_sub, Face_recognition, Speech_recognition, Speaking_languages, Create_i2c_Servo,Create_serial_Servo,Create_Servo_motor, Create_i2c_Servo,Create_serial_Servo,Create_Servo_motor, Create_i2c_Servo,Create_serial_Servo,Create_Servo_motor
Servo_control_5 = pyfirmata.ArduinoMega('/dev/I2C')
Servo_control_6 = pyfirmata.ArduinoMega('/dev/I2C')
Create_serial_Servo(5,Servo_control_5,['ATMega328p','Arduino2560','STM32F103C8TX','STM32F303K8TX'][2],0)
Create_serial_Servo(6,Servo_control_6,['ATMega328p','Arduino2560','STM32F103C8TX','STM32F303K8TX'][2],0)
def face_recog_1_function():
	Face_recognition("Face_db",0,'127.0.0.1',5080,'face_recog_1',0,65536,5081,'127.0.0.1')
def Speech_recognition_2_function():
	for Speech_recognition_2 in count(0):
		try:
			Speech_recognition('en','127.0.0.1',5060)
		except:
			pass
def tts_4_function():
	Speaking_languages("Hello I'm your robot","en","1.04",100)
def Servo_control_5_function():
	Create_i2c_Servo(5,"Servo_control_5",0,0)  #number_servo ,servo_name, angle, pin
def Servo_control_6_function():
	Create_i2c_Servo(6,"Servo_control_6",0,0)  #number_servo ,servo_name, angle, pin
t0 = threading.Thread(target=face_recog_1_function)
t1 = threading.Thread(target=Speech_recognition_2_function)
t2 = threading.Thread(target=tts_4_function)
t3 = threading.Thread(target=Servo_control_5_function)
t4 = threading.Thread(target=Servo_control_6_function)
t0.start()
t1.start()
t2.start()
t3.start()
t4.start()