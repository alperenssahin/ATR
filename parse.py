import serial
import sys

from ast import literal_eval
ser = serial.Serial('/dev/ttyUSB%s' % sys.argv[1], 9600)
ser.baudrate = 9600

def parseATR(str):
        input = []
        list = []
        dic = {}
        st = ""
        if str[0] != "+":
                return False
        for s in str:
                if s == "+":
                        input = []
                        st = ""
                        continue
                elif s == "*":
                        st = st.join(input)
                        list = st.split('|')
                        dic[list[0]] = list[1]
                        continue
                else:
                        input.append(s)
        return dic


while True:

        read = ser.readline()
        read = read[:-1].decode()
        data = parseATR(read)
        if not data:
                continue
        print(read)
        print(data)
        print(data["sensor1"])
        print(data["Sensor2"])

