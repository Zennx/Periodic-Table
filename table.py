import os
import time

def clr(): #this is for resetting screen
    input ("Press enter to return.")
    os.system("cls")

def d1(): #elements
    print ("This is Hydrogen [H]")
    print ("Atomic Number: 1")
    print ("Atomic Weight: 1.00794")
    print ("Melting Point: 13.81 K (-259.34°C or -434.81°F)")
    print ("Boiling Point: 20.28 K (-252.87°C or -423.17°F)")
    print ("Density: 0.00008988 grams per cubic centimeter")
    print ("Phase at Room Temperature: Gas")
    print ("Element Classification: Non-metal")
    print ("Period Number: 1    Group Number: 1")
    clr()

def d2(): 
    print ("This is Helium [He]")
    print ("Atomic Number: 2")
    print ("Atomic Weight: 4.002602")
    print ("Melting Point: 0.95 K (-272.2°C or -458.0°F)")
    print ("Boiling Point: 4.22 K (-268.93°C or -452.07°F)")
    print ("Density: 0.0001785 grams per cubic centimeter")
    print ("Phase at Room Temperature: Gas")
    print ("Element Classification: Non-metal")
    print ("Period Number: 1    Group Number: 18    Group Name: Noble Gas")
    clr()

def d3(): 
    print ("This is Lithium [Li]")
    print ("Atomic Number: 3")
    print ("Atomic Weight: 6.941")
    print ("Melting Point: 453.65 K (180.50°C or 356.90°F)")
    print ("Boiling Point: 1615 K (1342°C or 2448°F)")
    print ("Density: 0.534 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 2    Group Number: 1    Group Name: Alkali Metal")
    clr()

def d4():
    print ("This is Beryllium [Be]")
    print ("Atomic Number: 4")
    print ("Atomic Weight: 9.0121831")
    print ("Melting Point: 1560 K (1287°C or 2349°F)")
    print ("Boiling Point: 2744 K (2471°C or 4480°F)")
    print ("Density: 1.85 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print("Period Number: 2    Group Number: 2    Group Name: Alkaline Earth Metal")

def d5():
    print ("This is Boron [B]")
    print ("Atomic Number: 5")
    print ("Atomic Weight: 10.811")
    print ("Melting Point: 2348 K (2075°C or 3767°F)")
    print ("Boiling Point: 4273 K (4000°C or 7232°F)")
    print ("Density: 2.37 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Semi-metal")
    print("Period Number: 2    Group Number: 13")

def d6():
    print ("This is Carbon [C]")
    print ("Atomic Number: 6")
    print ("Atomic Weight: 12.0107")
    print ("Melting Point: 3823 K (3550°C or 6422°F)")
    print ("Boiling Point: 4098 K (3825°C or 6917°F)")
    print ("Density: 2.2670 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Non-metal")
    print ("Period Number: 2    Group Number: 14")

def d7():
    print ("This is Nitrogen [N]")
    print ("Atomic Number: 7")
    print ("Atomic Weight: 14.00674")
    print ("Melting Point: 63.15 K (-210.00°C or -346.00°F)")
    print ("Boiling Point: 77.36 K (-195.79°C or -320.44°F)")
    print ("Density: 0.0012506 grams per cubic centimeter")
    print ("Phase at Room Temperature: Gas")
    print ("Element Classification: Non-metal")
    print ("Period Number: 2    Group Number: 15    Group Name: Pnictogen")

def d8():
    print ("This is Oxygen [O]")
    print ("Atomic Number: 8")
    print ("Atomic Weight: 15.9994")
    print ("Melting Point: 54.36 K (-218.79°C or -361.82°F)")
    print ("Boiling Point: 90.20 K (-182.95°C or -297.31°F)")
    print ("Density: 0.001429 grams per cubic centimeter")
    print ("Phase at Room Temperature: Gas")
    print ("Element Classification: Non-metal")
    print ("Period Number: 2    Group Number: 16    Group Name: Chalcogen")

def d9():
    print ("This is Fluorine [F]")
    print ("Atomic Number: 9")
    print ("Atomic Weight: 18.998403163")
    print ("Melting Point: 53.53 K (-219.62°C or -363.32°F)")
    print ("Boiling Point: 85.03 K (-188.12°C or -306.62°F)")
    print ("Density: 0.001696 grams per cubic centimeter")
    print ("Phase at Room Temperature: Gas")
    print ("Element Classification: Non-metal")
    print ("Period Number: 2    Group Number: 17    Group Name: Halogen")

def d10():
    print ("This is Neon [Ne]")
    print ("Atomic Number: 10")
    print ("Atomic Weight: 20.1797")
    print ("Melting Point: 24.56 K (-248.59°C or -415.46°F)")
    print ("Boiling Point: 27.07 K (-246.08°C or -410.94°F)")
    print ("Density: 0.0008999 grams per cubic centimeter")
    print ("Phase at Room Temperature: Gas")
    print ("Element Classification: Non-metal")
    print ("Period Number: 2    Group Number: 18    Group Name: Noble Gas")

def d11():
    print ("This is Sodium [Na]")
    print ("Atomic Number: 11")
    print ("Atomic Weight: 22.98976928")
    print ("Melting Point: 370.95 K (97.80°C or 208.04°F)")
    print ("Boiling Point: 1156 K (883°C or 1621°F)")
    print ("Density: 0.97 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 3    Group Number: 1    Group Name: Alkali Metal")

def d12():
    print ("This is Magnesium [Mg]")
    print ("Atomic Number: 12")
    print ("Atomic Weight: 24.305")
    print ("Melting Point: 923 K (650°C or 1202°F)")
    print ("Boiling Point: 1363 K (1090°C or 1994°F)")
    print ("Density: 1.74 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 3    Group Number: 2    Group Name: Alkaline Earth Metal")

def d13():
    print ("This is Aluminum [Al]")
    print ("Atomic Number: 13")
    print("Atomic Weight: 26.9815385")
    print ("Melting Point: 933.437 K (660.323°C or 1220.581°F)")
    print ("Boiling Point: 2792 K (2519°C or 4566°F)")
    print ("Density: 2.70 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 3    Group Number: 13")

def d14():
    print("This is Silicon [Si]")
    print ("Atomic Number: 14")
    print ("Atomic Weight: 28.0855")
    print ("Melting Point: 1687 K (1414°C or 2577°F)")
    print ("Boiling Point: 3538 K (3265°C or 5909°F)")
    print ("Density: 2.3296 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Semi-metal")
    print ("Period Number: 3    Group Number: 14")

def d15():
    print ("This is Phosphorus [P]")
    print ("Atomic Number: 15")
    print ("Atomic Weight: 30.973761998")
    print ("Melting Point: 317.30 K (44.15°C or 111.47°F)")
    print ("Boiling Point: 553.65 K (280.5°C or 536.9°F)")
    print ("Density: 1.82 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Non-metal")
    print ("Period Number: 3    Group Number: 15    Group Name: Pnictogen")

def d16():
    print ("")

def d17():
    print ("")

def d18():
    print ("")

def d19():
    print ("")

def d20():
    print ("")

def d21():
    print ("")

def d22():
    print ("")

def d23():
    print ("")

def d24():
    print ("")

def d25():
    print ("")

def d26():
    print ("")

def d27():
    print ("")

def d28():
    print ("")

def d29():
    print ("")

def d30():
    print ("")

def d31():
    print ("")

def d32():
    print ("")

def d33():
    print ("")

def d34():
    print ("")

def d35():
    print ("")

def d36():
    print ("")

def d37():
    print ("")

def d38():
    print ("")

def d39():
    print ("")

def d40():
    print ("")

def d41():
    print ("")

def d42():
    print ("")

def d43():
    print ("")

def d44():
    print ("")

def d45():
    print ("")

def d46():
    print ("")

def d47():
    print ("")

def d48():
    print ("")

def d49():
    print ("")

def d50():
    print ("")

def tracker() : #main nav
    number = input("Enter a number:")
    print ("                                                     ")
    if number == "1" :
        d1()
        tracker()
    elif number == "2" :
        d2()
        tracker()
    elif number == "3" :
        d3()
        tracker()
    elif number == "4":
        d4()
        tracker()
    elif number == "5":
        d5()
        tracker()
    elif number == "6":
        d6()
        tracker()
    elif number =="7":
        d7()
        tracker()
    elif number == "8":
        d8()
        tracker()
    elif number == "9":
        d9()
        tracker()
    elif number == "10":
        d10()
        tracker()
    elif number == "11":
        d11()
        tracker()
    elif number == "12":
        d12()
        tracker()
    elif number == "13":
        d13()
        tracker()
    elif number == "14":
        d14()
        tracker()
    elif number == "15":
        d15()
        tracker()
    elif number == "16":
        d16()
        tracker()
    elif number == "17":
        d17()
        tracker()
    elif number == "18":
        d18()
        tracker()
    elif number == "19":
        d19()
        tracker()
    elif number == "20":
        d20()
        tracker()
    elif number == "21":
        d21()
        tracker ()
    elif number == "22":
        d22()
        tracker()
    elif number == "23":
        d23()
        tracker()
    elif number == "24":
        d24()
        tracker()
    elif number == "25":
        d25()
        tracker()
    elif number == "26":
        d25()
        tracker()
    elif number == "27":
        d27()
        tracker()
    elif number == "28":
        d28()
        tracker()
    elif number == "29":
        d29()
        tracker()
    elif number == "30":
        d30()
        tracker()
    elif number == "31":
        d31()
        tracker()
    elif number == "32":
        d32()
        tracker()
    elif number == "33":
        d33()
        tracker()
    elif number == "34":
        d34()
        tracker()
    elif number == "35":
        d35()
        tracker()
    elif number == "36":
        d36()
        tracker()
    elif number == "37":
        d37()
        tracker()
    elif number == "38":
        d38()
        tracker()
    elif number == "39":
        d39()
        tracker()
    elif number == "40":
        d40()
        tracker()
    elif number == "41":
        d41()
        tracker()
    elif number == "42":
        d42()
        tracker()
    elif number == "43":
        d43()
        tracker()
    elif number == "44":
        d44()
        tracker()
    elif number == "45":
        d45()
        tracker()
    elif number == "46":
        d46()
        tracker()
    elif number == "47":
        d47()
        tracker()
    elif number == "48":
        d48()
        tracker()
    elif number == "49":
        d49()
        tracker()
    elif number == "50":
        d50()
        tracker()
    exit()


#game -lol under construction
tracker()