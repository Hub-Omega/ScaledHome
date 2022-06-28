# IMPORTS
import time
from adafruit_servokit import ServoKit
import sys
import os
import csv
import RPi.GPIO as GPIO
from datetime import datetime
from time import strftime
import pdb
from collections import defaultdict
import pandas as pd

kit = ServoKit(channels=16)

# The Home class holds all of the rooms, appliances, doors, and windows in the
# house and acts as a hub for large scale commands like opening and closing all
# the windows and doors.
class Home:
    name = 'SmartHomeModel'
    def __init__(self, rooms, appliances, doors, windows, sun):
        self.rooms = rooms
        self.appliances = appliances
        self.doors = doors
        self.windows = windows
        self.sun = sun 


    # These next few functions returns a list of the names of the different
    # objects in the house. This is used later to create the column names
    # for the output csv file.
    def getRooms(self):
        rL = []
        for r in self.rooms:
            rL.append(r.name)
        return rL


    def getApps(self):
        aL = []
        for a in self.appliances:
            aL.append(a.name)
        return aL


    def getDoors(self):
        dL = []
        for d in self.doors:
            dL.append(d.name)
        return dL


    def getWindows(self):
        wL = []
        for w in self.windows:
            wL.append(w.name)
        return wL

    def getSun(self):
        sL = []
        for s in self.sun:
            sL.append(s.name)
        return sL


    # These next two functions returns the nicknames of the doors and windows.
    # These abbreviations are used in the input file to denote which hinge is
    # being referred to and shorten the strings used in string comparisons.
    def getDoorNicknames(self):
        dN = []
        for d in self.doors:
            dN.append(d.nickname)
        return dN


    def getWindowNicknames(self):
        wN = []
        for w in self.windows:
            wN.append(w.nickname)
        return wN


    # This function outputs the states of all the objects in the house (except
    # the rooms as they don't have states).
    def getStates(self):
        states = []
        states.append(format(datetime.now(), '%H:%M:%S'))
        # get appliance states
        for a in self.appliances:
            states.append(a.getState())
        # get door states
        for d in self.doors:
            states.append(d.getState())
        # get window states
        for w in self.windows:
            states.append(w.getState())
            # get sun states
        for s in self.sun:
            states.append(s.getState())
        return states


    # The next few functions add different things to the house so it can be built
    # in the controlTower class.
    def addRoom(self, newRoom):
        self.rooms.append(newRoom)


    def addWindow(self, newWindow):
        self.windows.append(newRoom)


    def addDoor(self, newDoor):
        self.doors.append(newDoor)


    def addAppliance(self, newApp):
        self.appliances.append(newApp)

    def addSun(self, newSun):
        self.sun.append(newSun)


    # These next few functions control large scale operations of the house.
    def openWindows(self):
        print('opening all windows...')
        for w in self.windows:
            w.openHinge()


    def closeWindows(self):
        print('closing all windows...')
        for w in self.windows:
            w.closeHinge()


    def openDoors(self):
        print('opening all doors...')
        for d in self.doors:
            d.openHinge()


    def closeDoors(self):
        print('closing all doors...')
        for d in self.doors:
            d.closeHinge()


    def openEverything(self):
        print('opening everything...')
        self.openWindows()
        self.openDoors()


    def closeEverything(self):
        print('closing everything...')
        self.closeWindows()
        self.closeDoors()


    def turnEverythingOn(self):
        print('turning on all appliances...')
        for a in self.appliances:
            a.turnOn()


    def turnEverythingOff(self):
        print('turning off all appliances...')
        for a in self.appliances:
            a.turnOff()


    # toString function
    def __str__(self):
        output = "Home: " + name + "\n\t**Rooms**"
        for r in rooms:
            output += "\n" + r
        output += "\n\t**Appliances**"
        for ap in appliances:
            output += "\n\t~" + ap


# The Room class acts as an organizational vehicle for the house. It contains all
# the doors and windows associated with an individual room in the house.
class Room:

    # Rooms only have a name, a door list, and a window list. There is no associated
    # nickname with a room since it is currently only being used as an
    # organizatioal tool.
    def __init__(self, name, door_list, window_list):
        self.name = name
        self.door_list = door_list
        self.window_list = window_list


    # These two functions add doors and windows to each room.
    def addRoom(self, newRoom):
        self.door_list.append(newRoom)


    def addWindow(self, newWindow):
        self.window_list.append(newWindow)


    # toString function.
    def __str__(self):
        output = "\t~Room: " + name + "\n\t\t**Doors**"
        for door in door_list:
            output += "\n\t\t-" + door
        output += "\n\t\t**Windows**"
        for window in window_list:
                output += "\n\t\t-" + window
        return output



class sunMotor:
    def __init__(self,name,pin1,pin2,enable, duty):
        self.name = name
        self.pin1 = int(pin1)
        self.pin2 = int(pin2)
        self.enable = int(enable)
        self.duty = int(duty)
        self.state = 0

    def getState(self):
        return self.state


# The Motor class is a parent class for all the objects in the house that can be
# controlled (i.e. doors, windows, and appliances).
class Motor:
    # Every motor has a name (to be used when printing the well known name of the
    # object), a nickname (to be used in the input file), a pin (to refer to
    # a specific pin on the RaspberryPi board), and a state (to determine if the
    # motor is open/on or closed/off).
    def __init__(self, name, nickname, pin):
        self.name = name
        self.nickname = nickname
        self.pin = int(pin)
        self.state = 0


    def getState(self):
        return self.state


    # toString function
    def __str__(self):
        out = "This is a " + self.name + " with the pin number " + str(self.pin) + "."
        return out


# The Hinge class is for the doors and windows of the house. It controls the
# opening and closing mechanism.
class Hinge(Motor):

    def __init__(self, name, nickname,  pin):
        super().__init__(name, nickname, pin)
        # This sets the opening angles of each pin
        if self.pin == 2 or self.pin == 13:
            self.openingAngle = 150
        elif self.pin == 15:
            self.openingAngle = 147
        else:
            self.openingAngle = 180
        # This sets the closing angle of each pin
        if self.pin == 10:
            self.closingAngle = 65
        elif self.pin == 12:
            self.closingAngle = 50
        elif self.pin == 15:
            self.closingAngle = 58
        elif pin == 6 or pin == 5:
            self.closingAngle = 55
        else:
            self.closingAngle = 60

    # These functions open and close the hinge.
    def openHinge(self):
        print('opening ' + self.name + '...')
        kit.servo[self.pin].angle = self.openingAngle
        self.state = 1


    def closeHinge(self):
        print('closing ' + self.name + '...')
        kit.servo[self.pin].angle = self.closingAngle
        self.state = 0


class Sun(sunMotor):
    def __init__(self,name,pin1,pin2,enable,duty):
        super().__init__(name, pin1, pin2, enable, duty)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin1, GPIO.OUT)
        GPIO.setup(pin2, GPIO.OUT)
        GPIO.setup(enable, GPIO.OUT)
        GPIO.output(pin1,GPIO.LOW)
        GPIO.output(pin2,GPIO.LOW)
        self.p = GPIO.PWM(enable, 1000)
        self.p.start(duty)

     # These functions turn the appliance on and off.
    def turnOn(self):
        print('turning on ' + self.name + '...')
        GPIO.output(self.pin1, GPIO.HIGH)
        self.state = 1

    def turnOff(self):
        print('turning off ' + self.name + '...')
        GPIO.output(self.pin1, GPIO.LOW)
        self.state = 0



# The Appliance class is for the appliances in the house that control the
# temperature (i.e. the heater, lamp, etc.). It controls the on and off
# mechanism.
class Appliance(Motor):
    # The appliance names and the appliance nicknames are the same thing.
    def __init__(self, name, pin):
        super().__init__(name, name, pin)
        GPIO.setup(self.pin, GPIO.OUT)


    # These functions turn the appliance on and off.
    def turnOn(self):
        print('turning on ' + self.name + '...')
        GPIO.output(self.pin, GPIO.HIGH)
        self.state = 1


    def turnOff(self):
        print('turning off ' + self.name + '...')
        GPIO.output(self.pin, GPIO.LOW)
        self.state = 0

# The ControlTower class is where everything is built and controlled from.
class ControlTower():
    def convertToSimulationTime(self, time: str) -> float:
        '''
        The simulated time : real time ratio in seconds is 1:45 
        The format for real time (time read in) is in 24 hour format, HH:MM 
        The digits before the ':' are the hours, the following digits are the minutes
        Starts day from 00:00
        '''
        militaryTime = time.split(':')
        parse = [int(digit) for digit in militaryTime]
        total_time = (parse[0]*3600 + parse[1]*60) // 45
        return total_time
        # print(convertToSimulationTime("20:45"))
    

    def parse(self, csv):
        df = pd.read_csv(csv)
        column_names = ["object", "time"]
        new_df = pd.DataFrame(columns = column_names)
        for index, row in df.iterrows():
            new_df.loc[len(new_df.index)] = [row['objects'], row['on_time']]
            new_df.loc[len(new_df.index)] = [row['objects'], row['off_time']]
        

        for index, row in new_df.iterrows():
            new_df.at[index,'time'] = self.convertToSimulationTime(new_df.at[index,'time'])
        new_df.sort_values(by=['time'], inplace=True)
        return new_df

    def parseDict(self, df):
        events = defaultdict(list)
        [events[row['time']].append(row['object']) for index, row in df.iterrows()]
        return events

    def time_to_switch(self, events):
        start_time = time.time()
        while(len(events) > 0):
            curr_time = int(time.time() - start_time)
            if curr_time in events.keys():
                self.switchState(events[curr_time])
                events.pop(curr_time)

    def switchState(self, list_of_objects):
        for object in list_of_objects:
            if (object.getState()):
                object.turnOff
            else:
                object.turnOn



    def main(self, inFile, outFile):
        # *** BUILDING THE HOUSE ***
        # --appliances--
        # no nickname needed, just use regular name when writing the test file
        lamp = Appliance("lamp", 5)
        heater = Appliance("heater", 6)
        fan = Appliance("fan", 18)
        ac = Appliance("ac", 13)
        applianceDict = {'lamp': lamp, 'heater':heater, 'fan':fan, 'ac':ac}

        #motor1 drives the lamp back and forth. motor 2 controls the angle of the lamp
        #Each motor has 2 pins and an enable connected to the motor driver then to the breadboard.
        motor1 = Sun("motor1",19,16,20,90)
        motor2 = Sun("motor2",25,24,17,30)
        sunDict = {'motor1':motor1, 'motor2':motor2}

        # --doors--
        # nicknaming convention: d + the initials of the door name. Example: db2b
        #                       is the -D-oor from -B-edroom -2- to the -B-athroom
        bed2_bath = Hinge("Bedroom 2 to Bathroom","db2b", 0)
        bed1_living = Hinge("Bedroom 1 to Living Room", "db1l", 1)
        living_kitchen = Hinge("Living Room to Kitchen", "dlk",  2)
        living_bath = Hinge("Living Room to Bathroom", "dlb", 3)
        bed1_bath = Hinge("Bedroom 1 to Bathroom", "db1b", 4)
        living_outside = Hinge("Living Room to Outside", "dlo", 5)
        bed1_outside = Hinge("Bedroom 1 to Outside", "db1o", 6)
        doorDict = {'db2b':bed2_bath, 'db1l':bed1_living, 'dlk':living_kitchen, 'dlb':living_bath,'db1b':bed1_bath,'dlo':living_outside,'db1o':bed1_outside}

        # --windows--
        # nicknaming convention: w + the initials of the door name. Example: wb1l
        #                        is the -W-indow in -B-edroom -1- on the -L-eft side
        #                        Each major room has a left and right window.                          
        bed1_left = Hinge("Bedroom 1 Left Window", "wb1l", 8)
        living_left = Hinge("Living Room Left Window", "wll",  9)
        bed2_right = Hinge("Bedroom 2 Right Window", "wb2r", 10)
        kitchen_right = Hinge("Kitchen Right Window", "wkr", 11)
        bed2_back = Hinge("Bedroom 2 Back Window", "wb2b", 12)
        living_front = Hinge("Living Room Front Window", "wlf", 13)
        kitchen_front = Hinge("Kitchen Front Window", "wkf", 14)
        bed1_back = Hinge("Bedroom 1 Back Window", "wb1b", 15)
        windowDict = {'wb1l':bed1_left, 'wll':living_left,'wb2r':bed2_right,'wkr':kitchen_right,'wb2b':bed2_back,'wlf':living_front, 'wkf':kitchen_front,'wb1b':bed1_back}
        # --rooms--
        bed1 = Room("Bedroom 1", [bed1_living, bed1_bath, bed1_outside], [bed1_left, bed1_back])
        bed2 = Room("Bedroom 2", [bed2_bath], [bed2_right, bed2_back])
        bath = Room("Bathroom", [bed2_bath, living_bath, bed1_bath], [])
        living = Room("Living Room", [bed1_living, living_kitchen, living_bath, living_outside], [living_left, living_front])
        kitchen = Room("Kitchen", [living_kitchen], [kitchen_right, kitchen_front])
        roomDict = {'Bedroom 1':bed1,'Bedroom 2':bed2, 'Bathroom':bath,'Living Room':living,'Kitchen':kitchen}

        # a dictionary for every object to be able to look them up when reading the Scenario file
        allObjects = {'lamp': lamp, 'heater':heater, 'fan':fan, 'ac':ac,'motor1':motor1, 'motor2':motor2,'db2b':bed2_bath, 'db1l':bed1_living, 'dlk':living_kitchen, 'dlb':living_bath,'db1b':bed1_bath,'dlo':living_outside,'db1o':bed1_outside,'wb1l':bed1_left, 'wll':living_left,'wb2r':bed2_right,'wkr':kitchen_right,'wb2b':bed2_back,'wlf':living_front, 'wkf':kitchen_front,'wb1b':bed1_back}        
        # --house--
        scaledHome = Home(roomDict, applianceDict, doorDict, windowDict, sunDict)

        # *** CONTROLLING THE HOUSE ***
        #bed1_left.openHinge()
        #time.sleep(5)
        #bed1_left.closeHinge()

        #fan.turnOn()
        #time.sleep(5)
        #lamp.turnOff()

        #scaledHome.openEverything()
        #time.sleep(5)
        #scaledHome.closeEverything()

        df = self.parse('Scenario1.csv')
        events = self.parseDict(df)
        self.time_to_switch(events)


        #print(scaledHome.getDoors())

        # Make sure to have GPIO.cleanup() at the end of the program to reset
        # all of the appliances before the program terminates.
        GPIO.cleanup()
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(6,GPIO.OUT)
        # GPIO.setup(13,GPIO.OUT)
        # p1=GPIO.PWM(en1,1000)
        # p2=GPIO.PWM(en2,1000)
        # p1.start (30)
        # p2.start (30)


 

if __name__ == "__main__":
    #inFile = "simulation_1_charlotte.txt"
    #outFile = "appliance_and_motor_states1_charlotte.csv"

    #inFile = "lamp_simulation.txt"
    #outFile = "appliance_and_motor_states4.csv"

    # inFile = "simulation3.txt"
    # outFile = "appliance_and_motor_states3.csv"

    # inFile = "simulation4.txt"
    # outFile = "appliance_and_motor_states4.csv"

    start = ControlTower()
    inFile = "Scenario.txt"
    outFile = "demo_sim.csv"
    start.main(inFile, outFile)
