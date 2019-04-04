from datetime import datetime
from prettytable import PrettyTable
def Stage1():
    act = input("\nHow many activities do you have to do: ")
    print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    acts = act.lower()
    if acts == "4" or acts == "four":
        Stage24()
    elif acts == "3" or acts == "three":
        Stage23()
    elif acts == "2" or acts == "two":
        Stage22()
    elif acts == "5" or acts == "five":
        Stage25()
    elif acts == "6" or acts == "six":
        Stage26()
    else:
        print("\nInvalid input, press enter to try again")
        input()
        Stage1()


def TimeTable():
    l = ['a','b','c']
    l1 = ['1','2','3']
    table = PrettyTable(['l', 'l1'])
    for x in range(0,3):
        table.add_row([l[x], l1[x]])
    print(table)



def Stage24():
        print("Enter your working working hours (In 00:00 format - 24 hours clock)")
        s = input("Start Time: ")
        e = input("End Time: ")
        if s != "16:30":
            print("Invalid input. Press enter to restart. ")
            input()
            Stage24()
        print("\nName your activities")
        a1 = input("Activity 1: ")
        a2 = input("Activity 2: ")
        a3 = input("Activity 3: ")
        a4 = input("Activity 4: ")
        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print("\n")
        print("Prioritize your activities on a scale of 1 - 4 (1 being the highest and 4 being the lowest)")
        p1 = input("Prioritize - '" + str(a1) + "': ")
        p2 = input("Prioritize - '" + str(a2) + "': ")
        p3 = input("Prioritize - '" + str(a3) + "': ")
        p4 = input("Prioritize - '" + str(a4) + "': ")
        if p1 == "5":
            print("Invalid input. Press enter to restart. ")
            input()
            Stage24()
        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        v = input("\nWhich activity do you want to spend the most time on: ")
        n = input("Which activity do you want to spend the least time on: ")
        print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print("\n\n")
        Time = ['16:30 - 17:30','17:30 - 19:00','19:00 - 19:30', '19:30 - 20:30']
        Activity = ['Math Homework','Summative Assessment Revision','Football', 'Personal Project']
        table = PrettyTable(['Time', 'Activity'])
        for x in range(0,4):
            table.add_row([Time[x], Activity[x]])
        print(table)
        print("\nThis is your timetable. You are free to make changes, however this can be the basis for your timetable. Make sure to use your time productively.")
        print ("\n\n")
        end = input("Do you want to retry the program. Enter yes or no: ")
        if end.lower() == "no":
            print("Enter to confirm exit")
            input()
        elif end.lower() == "yes":
            print("\n\n\n\n\n\n\n")
            Stage1()
    
def WorkingHours():
    print("Enter your working hours in a 24 hours format (00:00)")
    Start = input("What is your starting time:")
    End = input("What is your ending time")

def Stage22():
    print("\nName your activities")
    a1 = input("Activity 1: ")
    a2 = input("Activity 2: ")
    print("\n")
    print("Prioritize your activities on a scale of 1 - 2 (1 being the highest and 2 being the lowest)")
    p1 = input("Prioritize - '" + str(a1) + "': ")
    p2 = input("Prioritize - '" + str(a2) + "': ")


def Stage23():
    print("\nName your activities")
    a1 = input("Activity 1: ")
    a2 = input("Activity 2: ")
    a3 = input("Activity 3: ")
    print("\n")
    print("Prioritize your activities on a scale of 1 - 3 (1 being the highest and 3 being the lowest)")
    p1 = input("Prioritize - '" + str(a1) + "': ")
    p2 = input("Prioritize - '" + str(a2) + "': ")
    p3 = input("Prioritize - '" + str(a3) + "': ")

def Stage25():
    print("\nName your activities")
    a1 = input("Activity 1: ")
    a2 = input("Activity 2: ")
    a3 = input("Activity 3: ")
    a4 = input("Activity 4: ")
    a5 = input("Activity 5: ")
    print("\n")
    print("Prioritize your activities on a scale of 1 - 5 (1 being the highest and 5 being the lowest)")
    p1 = input("Prioritize - '" + str(a1) + "': ")
    p2 = input("Prioritize - '" + str(a2) + "': ")
    p3 = input("Prioritize - '" + str(a3) + "': ")
    p4 = input("Prioritize - '" + str(a4) + "': ")
    p5 = input("Prioritize - '" + str(a5) + "': ")

def Stage26():
    print("\nName your activities")
    a1 = input("Activity 1: ")
    a2 = input("Activity 2: ")
    a3 = input("Activity 3: ")
    a4 = input("Activity 4: ")
    a5 = input("Activity 5: ")
    a6 = input("Activity 6: ")
    print("\n")
    print("Prioritize your activities on a scale of 1 - 6 (1 being the highest and 6 being the lowest)")
    p1 = input("Prioritize - '" + str(a1) + "': ")
    p2 = input("Prioritize - '" + str(a2) + "': ")
    p3 = input("Prioritize - '" + str(a3) + "': ")
    p4 = input("Prioritize - '" + str(a4) + "': ")
    p5 = input("Prioritize - '" + str(a5) + "': ")
    p6 = input("Prioritize - '" + str(a6) + "': ")

def Program():

    Stage1()

Program()
