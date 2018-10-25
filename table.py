import os
import time
import filecmp
import winsound
import tkinter as tk

class Application(tk.Frame): #Exit popup
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.Return = tk.Button(self)
        self.Return["text"] = "Return"
        self.Return["command"] = self.no
        self.Return.pack(side="right")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="left")

    def no(self):
        root.destroy()
        tracker()

root = tk.Tk()
app = Application(master=root)

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
    clr()

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
    clr()

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
    clr()

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
    clr()

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
    clr()

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
    clr()

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
    clr()

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
    clr()

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
    clr()

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
    clr()

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
    clr()

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
    clr()

def d16():
    print ("This is Sulphur [S]")
    print ("Atomic Number: 16")
    print ("Atomic Weight: 32.066")
    print ("Melting Point: 388.36 K (115.21°C or 239.38°F)")
    print ("Boiling Point: 717.75 K (444.60°C or 832.28°F)")
    print ("Density: 2.067 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Non-metal")
    print ("Period Number: 3    Group Number: 16    Group Name: Chalcogen")
    clr()

def d17():
    print ("This is Chlorine [Cl]")
    print ("Atomic Number: 17")
    print ("Atomic Weight: 35.4527")
    print ("Melting Point: 171.65 K (-101.5°C or -150.7°F)")
    print ("Boiling Point: 239.11 K (-34.04°C or -29.27°F)")
    print ("Density: 0.003214 grams per cubic centimeter")
    print ("Phase at Room Temperature: Gas")
    print ("Element Classification: Non-metal")
    print ("Period Number: 3    Group Number: 17    Group Name: Halogen")
    clr()

def d18():
    print ("This is Argon [Ar]")
    print ("Atomic Number: 18")
    print ("Atomic Weight: 39.948")
    print ("Melting Point: 83.80 K (-189.35°C or -308.83°F)")
    print ("oiling Point: 87.30 K (-185.85°C or -302.53°F)")
    print ("Density: 0.0017837 grams per cubic centimeter")
    print ("Phase at Room Temperature: Gas")
    print ("Element Classification: Non-metal")
    print ("Period Number: 3    Group Number: 18    Group Name: Noble Gas")
    clr()

def d19():
    print ("This is Potassium [K]")
    print ("Atomic Number: 19")
    print ("Atomic Weight: 39.0983")
    print ("Melting Point: 336.53 K (63.38°C or 146.08°F)")
    print ("Boiling Point: 1032 K (759°C or 1398°F)")
    print ("Density: 0.89 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 4    Group Number: 1    Group Name: Alkali Metal")
    clr()

def d20():
    print ("This is Calcium [Ca]")
    print ("Atomic Number: 20")
    print ("Atomic Weight: 40.078")
    print ("Melting Point: 1115 K (842°C or 1548°F)")
    print ("Boiling Point: 1757 K (1484°C or 2703°F)")
    print ("Density: 1.54 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 4    Group Number: 2    Group Name: Alkaline Earth Metal")
    clr()

def d21():
    print ("This is Scandium [Sc]")
    print ("Atomic Number: 21")
    print ("Atomic Weight: 44.955908")
    print ("Melting Point: 1814 K (1541°C or 2806°F)")
    print ("Boiling Point: 3109 K (2836°C or 5137°F)")
    print ("Density: 2.99 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 4    Group Number: 3")
    clr()

def d22():
    print ("This is Titanium [Ti]")
    print ("Atomic Number: 22")
    print ("Atomic Weight: 47.867")
    print ("Melting Point: 1941 K (1668°C or 3034°F)")
    print ("Boiling Point: 3560 K (3287°C or 5949°F)")
    print ("Density: 4.5 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 4    Group Number: 4")
    clr()

def d23():
    print ("This is Vanadium [V]")
    print ("Atomic Number: 23")
    print ("Atomic Weight: 50.9415")
    print ("Melting Point: 2183 K (1910°C or 3470°F)")
    print ("Boiling Point: 3680 K (3407°C or 6165°F)")
    print ("Density: 6.0 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 4    Group Number: 5 ")
    clr()

def d24():
    print ("This is Chromium [Cr]")
    print ("Atomic Number: 24")
    print ("Atomic Weight: 51.9961")
    print ("Melting Point: 2180 K (1907°C or 3465°F)")
    print ("Boiling Point: 2944 K (2671°C or 4840°F)")
    print ("Density: 7.15 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 4    Group Number: 6")
    clr()

def d25():
    print ("This is Manganese [Mn]")
    print ("Atomic Number: 25")
    print ("Atomic Weight: 54.938044")
    print ("Melting Point: 1519 K (1246°C or 2275°F)")
    print ("Boiling Point: 2334 K (2061°C or 3742°F)")
    print ("Density: 7.3 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 4    Group Number: 7")
    clr()

def d26():
    print ("This is Iron [Fe]")
    print ("Atomic Number: 26")
    print ("Atomic Weight: 55.845")
    print ("Melting Point: 1811 K (1538°C or 2800°F)")
    print ("Boiling Point: 3134 K (2861°C or 5182°F)")
    print ("Density: 7.874 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 4    Group Number: 8 ")
    clr()

def d27():
    print ("This is Cobalt [Co]")
    print ("Atomic Number: 27")
    print ("Atomic Weight: 58.933194")
    print ("Melting Point: 1768 K (1495°C or 2723°F)")
    print ("Boiling Point: 3200 K (2927°C or 5301°F)")
    print ("Density: 8.86 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 4    Group Number: 9 ")
    clr()

def d28():
    print ("This is Nickel [Ni]")
    print ("Atomic Number: 28")
    print ("Atomic Weight: 58.6934")
    print ("Melting Point: 1728 K (1455°C or 2651°F)")
    print ("Boiling Point: 3186 K (2913°C or 5275°F)")
    print ("Density: 8.912 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 4    Group Number: 10 ")
    clr()

def d29():
    print ("This is Copper [Cu]")
    print ("Atomic Number: 29")
    print ("Atomic Weight: 63.546")
    print ("Melting Point: 1357.77 K (1084.62°C or 1984.32°F)")
    print ("Boiling Point: 2835 K (2562°C or 4644°F)")
    print ("Density: 8.933 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 4    Group Number: 11")
    clr()

def d30():
    print ("This is Zinc [Zn]")
    print ("Atomic Number: 30")
    print ("Atomic Weight: 65.38")
    print ("Melting Point: 692.68 K (419.53°C or 787.15°F)")
    print ("Boiling Point: 1180 K (907°C or 1665°F)")
    print ("Density: 7.134 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 4    Group Number: 12")
    clr()

def d31():
    print ("This is Gallilum [Ga]")
    print ("Atomic Number: 31")
    print ("Atomic Weight: 69.723")
    print ("Melting Point: 302.91 K (29.76°C or 85.57°F)")
    print ("Boiling Point: 2477 K (2204°C or 3999°F)")
    print ("Density: 5.91 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 4    Group Number: 13")
    clr()

def d32():
    print ("This is Germanium [Ge]")
    print ("Atomic Number: 32")
    print ("Atomic Weight: 72.630")
    print ("Melting Point: 1211.40 K (938.25°C or 1720.85°F)")
    print ("Boiling Point: 3106 K (2833°C or 5131°F)")
    print ("Density: 5.323 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Semi-metal")
    print ("Period Number: 4    Group Number: 14 ")
    clr()

def d33():
    print ("This is Arsenic [As]")
    print ("Atomic Number: 33")
    print ("Atomic Weight: 74.921595")
    print ("Melting Point: 1090 K (817°C or 1503°F)")
    print ("Boiling Point: 887 K (614°C or 1137°F)")
    print ("Density: 5.776 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Semi-metal")
    print ("Period Number: 4    Group Number: 15    Group Name: Pnictogen")
    clr()

def d34():
    print ("This is Selenium [Se]")
    print ("Atomic Number: 34")
    print ("Atomic Weight: 78.971")
    print ("Melting Point: 493.65 K (220.5°C or 428.9°F)")
    print ("Boiling Point: 958 K (685°C or 1265°F)")
    print ("Density: 4.809 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Non-metal")
    print ("Period Number: 4    Group Number: 16    Group Name: Chalcogen")
    clr()

def d35():
    print ("This is Bromine [Br]")
    print ("Atomic Number: 35")
    print ("Atomic Weight: 79.904")
    print ("Melting Point: 265.95 K (-7.2°C or 19.0°F)")
    print ("Boiling Point: 331.95 K (58.8°C or 137.8°F)")
    print ("Density: 3.11 grams per cubic centimeter")
    print ("Phase at Room Temperature: Liquid")
    print ("Element Classification: Non-metal")
    print ("Period Number: 4    Group Number: 17    Group Name: Halogen")
    clr()

def d36():
    print ("This is Krypton [Kr]")
    print ("Atomic Number: 36")
    print ("Atomic Weight: 83.798")
    print ("Melting Point: 115.79 K (-157.36°C or -251.25°F)")
    print ("Boiling Point: 119.93 K (-153.22°C or -243.80°F)")
    print ("Density: 0.003733 grams per cubic centimeter")
    print ("Phase at Room Temperature: Gas")
    print ("Element Classification: Non-metal")
    print ("Period Number: 4    Group Number: 18    Group Name: Noble Gas")
    clr()

def d37():
    print ("This is Rubidium [Rb]")
    print ("Atomic Number: 37")
    print ("Atomic Weight: 85.4678")
    print ("Melting Point: 312.46 K (39.31°C or 102.76°F)")
    print ("Boiling Point: 961 K (688°C or 1270°F)")
    print ("Density: 1.53 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 5    Group Number: 1    Group Name: Alkali Metal")
    clr()

def d38():
    print ("This is Strontium [Sr]")
    print ("Atomic Number: 38")
    print ("Atomic Weight: 87.62")
    print ("Melting Point: 1050 K (777°C or 1431°F)")
    print ("Boiling Point: 1655 K (1382°C or 2520°F)")
    print ("Density: 2.64 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 5    Group Number: 2    Group Name: Alkaline Earth Meta")
    clr()

def d39():
    print ("This is Yttrium [Y]")
    print ("Atomic Number: 39")
    print ("Atomic Weight: 88.90584")
    print ("Melting Point: 1795 K (1522°C or 2772°F)")
    print ("Boiling Point: 3618 K (3345°C or 6053°F)")
    print ("Density: 4.47 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 5    Group Number: 3")
    clr ()

def d40():
    print ("This is Zirconium [Zr]")
    print ("Atomic Number: 40")
    print ("Atomic Weight: 91.224")
    print ("Melting Point: 2128 K (1855°C or 3371°F)")
    print ("Boiling Point: 4682 K (4409°C or 7968°F)")
    print ("Density: 6.52 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 5    Group Number: 4")
    clr()

def d41():
    print ("This is Niobium [Nb]")
    print ("Atomic Number: 41")
    print ("Atomic Weight: 92.90637")
    print ("Melting Point: 2750 K (2477°C or 4491°F)")
    print ("Boiling Point: 5017 K (4744°C or 8571°F)")
    print ("Density: 8.57 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 5    Group Number: 5")
    clr()

def d42():
    print ("This is Molybdenum [Mo]")
    print ("Atomic Number: 42")
    print ("Atomic Weight: 95.95")
    print ("Melting Point: 2896 K (2623°C or 4753°F)")
    print ("Boiling Point: 4912 K (4639°C or 8382°F)")
    print ("Density: 10.2 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 5    Group Number: 6")
    clr()

def d43():
    print ("This is Technetium [Tc]")
    print ("Atomic Number: 43")
    print ("Atomic Weight: 98")
    print ("Melting Point: 2430 K (2157°C or 3915°F)")
    print ("Boiling Point: 4538 K (4265°C or 7709°F)")
    print ("Density: 11 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 5    Group Number: 7")
    print ("Radioactive and Artificially Produced")
    clr()

def d44():
    print ("This is Ruthenium [Ru]")
    print ("Atomic Number: 44")
    print ("Atomic Weight: 101.07")
    print ("Melting Point: 2607 K (2334°C or 4233°F)")
    print ("Boiling Point: 4423 K (4150°C or 7502°F)")
    print ("Density: 12.1 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 5    Group Number: 8")
    clr()

def d45():
    print ("This is Rhodium [Rh]")
    print ("Atomic Number: 45")
    print ("Atomic Weight: 102.90550")
    print ("Melting Point: 2237 K (1964°C or 3567°F)")
    print ("Boiling Point: 3968 K (3695°C or 6683°F)")
    print ("Density: 12.4 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 5    Group Number: 9")
    clr()

def d46():
    print ("This is Palladium [Pd]")
    print ("Atomic Number: 46")
    print ("Atomic Weight: 106.42")
    print ("Melting Point: 1828.05 K (1554.9°C or 2830.8°F)")
    print ("Boiling Point: 3236 K (2963°C or 5365°F)")
    print ("Density: 12.0 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 5    Group Number: 10")
    clr()

def d47():
    print ("This is Silver [Ag]")
    print ("Atomic Number: 47")
    print ("Atomic Weight: 107.8682")
    print ("Melting Point: 1234.93 K (961.78°C or 1763.20°F)")
    print ("Boiling Point: 2435 K (2162°C or 3924°F)")
    print ("Density: 10.501 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 5    Group Number: 11")
    clr()

def d48():
    print ("This is Cadnium [Cd]")
    print ("Atomic Number: 48")
    print ("Atomic Weight: 112.414")
    print ("Melting Point: 594.22 K (321.07°C or 609.93°F)")
    print ("Boiling Point: 1040 K (767°C or 1413°F)")
    print ("Density: 8.69 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 5    Group Number: 12")
    clr()

def d49():
    print ("This is Indium [In]")
    print ("Atomic Number: 49")
    print ("Atomic Weight: 114.818")
    print ("Melting Point: 429.75 K (156.60°C or 313.88°F)")
    print ("Boiling Point: 2345 K (2072°C or 3762°F)")
    print ("Density: 7.31 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 5    Group Number: 13 ")
    clr()

def d50():
    print ("This is Tin [Sn]")
    print ("Atomic Number: 50")
    print ("Atomic Weight: 118.710")
    print ("Melting Point: 505.08 K (231.93°C or 449.47°F)")
    print ("Boiling Point: 2875 K (2602°C or 4715°F)")
    print ("Density: 7.287 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 5    Group Number: 14")
    clr()

def d51():
    print ("This is Antimony [Sb]")
    print ("Atomic Number: 51")
    print ("tomic Weight: 121.760")
    print ("Melting Point: 903.78 K (630.63°C or 1167.13°F)")
    print ("Boiling Point: 1860 K (1587°C or 2889°F)")
    print ("Density: 6.685 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Semi-metal")
    print ("Period Number: 5    Group Number: 15    Group Name: Pnictogen")
    clr()

def d52():
    print ("This is Tellurium [Te]")
    print ("Atomic Number: 52")
    print ("Atomic Weight: 127.60")
    print ("Melting Point: 722.66 K (449.51°C or 841.12°F)")
    print ("Boiling Point: 1261 K (988°C or 1810°F)")
    print ("Density: 6.232 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Semi-metal")
    print ("Period Number: 5    Group Number: 16    Group Name: Chalcogen")
    clr()

def d53():
    print ("This is Iodine [I]")
    print ("Atomic Number: 53")
    print ("Atomic Weight: 126.90447")
    print ("Melting Point: 386.85 K (113.7°C or 236.7°F)")
    print ("Boiling Point: 457.55 K (184.4°C or 364.0°F)")
    print ("Density: 4.93 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Non-metal")
    print ("Period Number: 5    Group Number: 17    Group Name: Halogen")
    clr()

def d54():
    print ("This is Xenon [Xe]")
    print ("Atomic Number: 54")
    print ("Atomic Weight: 131.293")
    print ("Melting Point: 161.36 K (-111.79°C or -169.22°F)")
    print ("Boiling Point: 165.03 K (-108.12°C or -162.62°F)")
    print ("Density: 0.005887 grams per cubic centimeter")
    print ("Phase at Room Temperature: Gas")
    print ("Element Classification: Non-metal")
    print ("Period Number: 5    Group Number: 18    Group Name: Noble Gas")
    clr()

def d55():
    print ("This is Cesium [Cs]")
    print ("Atomic Number: 55")
    print ("Atomic Weight: 132.90545196")
    print ("Melting Point: 301.59 K (28.44°C or 83.19°F)")
    print ("Boiling Point: 944 K (671°C or 1240°F)")
    print ("Density: 1.93 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: 1    Group Name: Alkali Metal")
    clr()

def d56():
    print ("This is Barium [Ba]")
    print ("Atomic Number: 56")
    print ("Atomic Weight: 137.327")
    print ("Melting Point: 1000 K (727°C or 1341°F)")
    print ("Boiling Point: 2170 K (1897°C or 3447°F)")
    print ("Density: 3.62 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: 2    Group Name: Alkaline Earth Metal")
    clr()

def d57():
    print ("This is Lanthanum [La]")
    print ("Atomic Number: 57")
    print ("Atomic Weight: 138.90547")
    print ("Melting Point: 1191 K (918°C or 1684°F)")
    print ("Boiling Point: 3737 K (3464°C or 6267°F)")
    print ("Density: 6.15 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: none    Group Name: Lanthanide")
    clr()

def d58():
    print ("This is Cerium [Ce]")
    print ("Atomic Number: 58")
    print ("Atomic Weight: 140.116")
    print ("Melting Point: 1071 K (798°C or 1468°F)")
    print ("Boiling Point: 3697 K (3424°C or 6195°F)")
    print ("Density: 6.770 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: none    Group Name: Lanthanide")
    clr()

def d59():
    print ("This is Praseodymium [Pr]")
    print ("Atomic Number: 59")
    print ("Atomic Weight: 140.90766")
    print ("Melting Point: 1204 K (931°C or 1708°F)")
    print ("Boiling Point: 3793 K (3520°C or 6368°F)")
    print ("Density: 6.77 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: none    Group Name: Lanthanide")
    clr()

def d60():
    print ("This is Neodymium [Nd]")
    print ("Atomic Number: 60")
    print ("Atomic Weight: 144.242")
    print ("Melting Point: 1294 K (1021°C or 1870°F)")
    print ("Boiling Point: 3347 K (3074°C or 5565°F)")
    print ("Density: 7.01 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: none    Group Name: Lanthanide")
    clr()

def d61():
    print ("This is Promethium [Pm]")
    print ("Atomic Number: 61")
    print ("Atomic Weight: 145")
    print ("Melting Point: 1315 K (1042°C or 1908°F)")
    print ("Boiling Point: 3273 K (3000°C or 5432°F)")
    print ("Density: 7.26 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: none    Group Name: Lanthanide")
    print ("Radioactive and Artificially Produced")
    clr()

def d62():
    print ("This is Samarium [Sm]")
    print ("Atomic Number: 62")
    print ("Atomic Weight: 150.36")
    print ("Melting Point: 1347 K (1074°C or 1965°F)")
    print ("Boiling Point: 2067 K (1794°C or 3261°F)")
    print ("Density: 7.52 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: none    Group Name: Lanthanide")
    clr()

def d63():
    print ("This is Europium [Eu]")
    print ("Atomic Number: 63")
    print ("Atomic Weight: 151.964")
    print ("Melting Point: 1095 K (822°C or 1512°F)")
    print ("Boiling Point: 1802 K (1529°C or 2784°F)")
    print ("Density: 5.24 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: none    Group Name: Lanthanide")
    clr()

def d64():
    print ("This is Gadolinium [Gd]")
    print ("Atomic Number: 64")
    print ("Atomic Weight: 157.25")
    print ("Melting Point: 1586 K (1313°C or 2395°F)")
    print ("Boiling Point: 3546 K (3273°C or 5923°F)")
    print ("Density: 7.90 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: none    Group Name: Lanthanide")
    clr()

def d65():
    print ("This is Terbium [Tb]")
    print ("Atomic Number: 65")
    print ("Atomic Weight: 158.92535")
    print ("Melting Point: 1629 K (1356°C or 2473°F)")
    print ("Boiling Point: 3503 K (3230°C or 5846°F)")
    print ("Density: 8.23 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: none    Group Name: Lanthanide")
    clr()

def d66():
    print ("This is Dysprosium [Dy]")
    print ("Atomic Number: 66")
    print ("Atomic Weight: 162.500")
    print ("Melting Point: 1685 K (1412°C or 2574°F)")
    print ("Boiling Point: 2840 K (2567°C or 4653°F)")
    print ("Density: 8.55 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: none    Group Name: Lanthanide")
    clr()

def d67():
    print ("This is Holmium [Ho]")
    print ("Atomic Number: 67")
    print ("Atomic Weight: 164.93033")
    print ("Melting Point: 1747 K (1474°C or 2685°F)")
    print ("Boiling Point: 2973 K (2700°C or 4892°F)")
    print ("Density: 8.80 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: none    Group Name: Lanthanide")
    clr()

def d68():
    print ("This is Erbium [Er]")
    print ("Atomic Number: 68")
    print ("Atomic Weight: 167.259")
    print ("Melting Point: 1802 K (1529°C or 2784°F)")
    print ("Boiling Point: 3141 K (2868°C or 5194°F)")
    print ("Density: 9.07 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: none    Group Name: Lanthanide")
    clr()

def d69():
    print ("This is Thulium [Tm]")
    print ("Atomic Number: 69")
    print ("Atomic Weight: 168.93422")
    print ("Melting Point: 1818 K (1545°C or 2813°F)")
    print ("Boiling Point: 2223 K (1950°C or 3542°F)")
    print ("Density: 9.32 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: none    Group Name: Lanthanide")
    clr()

def d70():
    print ("This is Ytterbium [Yb]")
    print ("Atomic Number: 70")
    print ("Atomic Weight: 173.045")
    print ("Melting Point: 1092 K (819°C or 1506°F)")
    print ("Boiling Point: 1469 K (1196°C or 2185°F)")
    print ("Density: 6.90 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: none    Group Name: Lanthanide")
    clr()

def d71():
    print ("This is Lutetium [Lu]")
    print ("Atomic Number: 71")
    print ("Atomic Weight: 174.9668")
    print ("Melting Point: 1936 K (1663°C or 3025°F)")
    print ("Boiling Point: 3675 K (3402°C or 6156°F)")
    print ("Density: 9.84 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: 3    Group Name: Lanthanide")
    clr()

def d72():
    print ("This is Hafnium [Hf]")
    print ("Atomic Number: 72")
    print ("Atomic Weight: 178.49")
    print ("Melting Point: 2506 K (2233°C or 4051°F)")
    print ("Boiling Point: 4876 K (4603°C or 8317°F)")
    print ("Density: 13.3 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: 4")
    clr()

def d73():
    print ("This is Tantalum [Ta]")
    print ("Atomic Number: 73")
    print ("Atomic Weight: 180.94788")
    print ("Melting Point: 3290 K (3017°C or 5463°F)")
    print ("Boiling Point: 5731 K (5458°C or 9856°F)")
    print ("Density: 16.4 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: 5")
    clr()

def d74():
    print ("This is Tungsten [W]")
    print ("Atomic Number: 74")
    print ("Atomic Weight: 183.84")
    print ("Melting Point: 3695 K (3422°C or 6192°F)")
    print ("Boiling Point: 5828 K (5555°C or 10031°F)")
    print ("Density: 19.3 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: 6")
    clr()

def d75():
    print ("This is Rhenium [Re]")
    print ("Atomic Number: 75")
    print ("Atomic Weight: 186.207")
    print ("Melting Point: 3459 K (3186°C or 5767°F)")
    print ("Boiling Point: 5869 K (5596°C or 10105°F)")
    print ("Density: 20.8 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: 7")
    clr()

def d76():
    print ("This is Osmium [Os]")
    print ("Atomic Number: 76")
    print ("Atomic Weight: 190.23")
    print ("Melting Point: 3306 K (3033°C or 5491°F)")
    print ("Boiling Point: 5285 K (5012°C or 9054°F)")
    print ("Density: 22.57 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: 8")
    clr()

def d77():
    print ("This is Iridium [Ir]")
    print ("Atomic Number: 77")
    print ("Atomic Weight: 192.217")
    print ("Melting Point: 2719 K (2446°C or 4435°F)")
    print ("Boiling Point: 4701 K (4428°C or 8002°F)")
    print ("Density: 22.42 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: 9 ")
    clr()

def d78():
    print ("This is Platinum [Pt]")
    print ("Atomic Number: 78")
    print ("Atomic Weight: 195.084")
    print ("Melting Point: 2041.55 K (1768.4°C or 3215.1°F)")
    print ("Boiling Point: 4098 K (3825°C or 6917°F)")
    print ("Density: 21.46 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: 10")
    clr()

def d79():
    print ("This is Gold [Au]")
    print ("Atomic Number: 79")
    print ("Atomic Weight: 196.966569")
    print ("Melting Point: 1337.33 K (1064.18°C or 1947.52°F)")
    print ("Boiling Point: 3129 K (2856°C or 5173°F)")
    print ("Density: 19.282 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: 11")
    clr()

def d80():
    print ("This is Mercury [Hg]")
    print ("Atomic Number: 80")
    print ("Atomic Weight: 200.592")
    print ("Melting Point: 234.32 K (-38.83°C or -37.89°F)")
    print ("Boiling Point: 629.88 K (356.73°C or 674.11°F)")
    print ("Density: 13.5336 grams per cubic centimeter")
    print ("Phase at Room Temperature: Liquid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: 12")
    clr()

def d81():
    print ("This is Thallium [Tl]")
    print ("Atomic Number: 81")
    print ("Atomic Weight: 204.3833")
    print ("Melting Point: 577 K (304°C or 579°F)")
    print ("Boiling Point: 1746 K (1473°C or 2683°F)")
    print ("Density: 11.8 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: 13")
    clr()

def d82():
    print ("This is Lead [Pb]")
    print ("Atomic Number: 82")
    print ("Atomic Weight: 207.2")
    print ("Melting Point: 600.61 K (327.46°C or 621.43°F)")
    print ("Boiling Point: 2022 K (1749°C or 3180°F)")
    print ("Density: 11.342 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: 14")
    clr()

def d83():
    print ("This is Bismuth [Bi]")
    print ("Atomic Number: 83")
    print ("Atomic Weight: 208.98040")
    print ("Melting Point: 544.55 K (271.40°C or 520.52°F)")
    print ("Boiling Point: 1837 K (1564°C or 2847°F)")
    print ("Density: 9.807 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: 15    Group Name: Pnictogen")
    print ("Radioactive")
    clr()

def d84():
    print ("This is Polonium [Po]")
    print ("Atomic Number: 84")
    print ("Atomic Weight: 209")
    print ("Melting Point: 527 K (254°C or 489°F)")
    print ("Boiling Point: 1235 K (962°C or 1764°F)")
    print ("Density: 9.32 grams per cubic centimeter")
    print ("   Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 6    Group Number: 16    Group Name: Chalcogen")
    print ("Radioactive")
    clr()

def d85():
    print ("This is Astatine [At]")
    print ("Atomic Number: 85")
    print ("Atomic Weight: 210")
    print ("Melting Point: 575 K (302°C or 576°F)")
    print ("Boiling Point: Unknown")
    print ("Density: about 7 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Semi-metal")
    print ("Period Number: 6    Group Number: 17    Group Name: Halogen")
    print ("Radioactive")
    clr()

def d86():
    print ("This is Radon [Rn]")
    print ("Atomic Number: 86")
    print ("Atomic Weight: 222")
    print ("Melting Point: 202 K (-71°C or -96°F)")
    print ("Boiling Point: 211.45 K (-61.7°C or -79.1°F)")
    print ("Density: 0.00973 grams per cubic centimeter")
    print ("Phase at Room Temperature: Gas")
    print ("Element Classification: Non-metal")
    print ("Period Number: 6    Group Number: 18    Group Name: Noble Gas")
    print ("Radioactive")
    clr()

def d87():
    print ("This is Francium [Fr]")
    print ("Atomic Number: 87")
    print ("Atomic Weight: 223")
    print ("Melting Point: 300 K (27°C or 81°F)")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: 1    Group Name: Alkali Metal")
    print ("Radioactive")
    clr()

def d88():
    print ("This is Radium [Ra]")
    print ("Atomic Number: 88")
    print ("Atomic Weight: 226")
    print ("Melting Point: 973 K (700°C or 1292°F)")
    print ("Boiling Point: 1413 K (1140°C or 2084°F)")
    print ("Density: 5 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: 2    Group Name: Alkaline Earth Metal")
    print ("Radioactive")
    clr()
 
def d89():
    print ("This is Actinium [Ac]")
    print ("Atomic Number: 89")
    print ("Atomic Weight: 227")
    print ("Melting Point: 1324 K (1051°C or 1924°F)")
    print ("Boiling Point: 3471 K (3198°C or 5788°F)")
    print ("Density: 10.07 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: none    Group Name: Actinide")
    print ("Radioactive")
    clr()

def d90():
    print ("This is Thorium [Th]")
    print ("Atomic Number: 90")
    print ("Atomic Weight: 232.0377")
    print ("Melting Point: 2023 K (1750°C or 3182°F)")
    print ("Boiling Point: 5061 K (4788°C or 8650°F)")
    print ("Density: 11.72 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: none    Group Name: Actinide")
    print ("Radioactive")
    clr()

def d91():
    print ("This is Protactinium [Pa]")
    print ("Atomic Number: 91")
    print ("Atomic Weight: 231.03588")
    print ("Melting Point: 1845 K (1572°C or 2862°F)")
    print ("Boiling Point: Unknown")
    print ("Density: 15.37 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: none    Group Name: Actinide")
    print ("Radioactive")
    clr()

def d92():
    print ("This is Uranium [U]")
    print ("Atomic Number: 92")
    print ("Atomic Weight: 238.02891")
    print ("Melting Point: 1408 K (1135°C or 2075°F)")
    print ("Boiling Point: 4404 K (4131°C or 7468°F)")
    print ("Density: 18.95 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: none    Group Name: Actinide")
    print ("Radioactive")
    clr()

def d93():
    print ("This is Neptunium [Np]")
    print ("Atomic Number: 93")
    print ("Atomic Weight: 237")
    print ("Melting Point: 917 K (644°C or 1191°F)")
    print ("Boiling Point: 4175 K (3902°C or 7056°F)")
    print ("Density: 20.25 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: none    Group Name: Actinide")
    print ("Radioactive and Artificially Produced")
    clr()

def d94():
    print ("This is Plutonium [Pu]")
    print ("Atomic Number: 94")
    print ("Atomic Weight: 244")
    print ("Melting Point: 913 K (640°C or 1184°F)")
    print ("Boiling Point: 3501 K (3228°C or 5842°F)")
    print ("Density: 19.84 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: none    Group Name: Actinide")
    print ("Radioactive and Artificially Produced")
    clr()

def d95():
    print ("This is Americium [Am]")
    print ("Atomic Number: 95")
    print ("Atomic Weight: 243")
    print ("Melting Point: 1449 K (1176°C or 2149°F)")
    print ("Boiling Point: 2284 K (2011°C or 3652°F)")
    print ("Density: 13.69 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: none    Group Name: Actinide")
    print ("Radioactive and Artificially Produced")
    clr()

def d96():
    print ("This is Curium [Cm]")
    print ("Atomic Number: 96")
    print ("Atomic Weight: 247")
    print ("Melting Point: 1618 K (1345°C or 2453°F)")
    print ("Boiling Point: ~3400 K (~3100°C or ~5600°F)")
    print ("Density: 13.51 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: none    Group Name: Actinide")
    print ("Radioactive and Artificially Produced")
    clr()

def d97():
    print ("This is Berkelium [Bk]")
    print ("Atomic Number: 97")
    print ("Atomic Weight: 247")
    print ("Melting Point: 1323 K (1050°C or 1922°F)")
    print ("Boiling Point: Unknown")
    print ("Density: 14 grams per cubic centimeter")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: none    Group Name: Actinide")
    print ("Radioactive and Artificially Produced")
    clr()

def d98():
    print ("This is Californium [Cf]")
    print ("Atomic Number: 98")
    print ("Atomic Weight: 251")
    print ("Melting Point: 1173 K (900°C or 1652°F")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: none    Group Name: Actinide")
    print ("Radioactive and Artificially Produced")
    clr()

def d99():
    print ("This is Einsteinium [Es]")
    print ("Atomic Number: 99")
    print ("Atomic Weight: 252")
    print ("Melting Point: 1133 K (860°C or 1580°F)")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: none    Group Name: Actinide")
    print ("Radioactive and Artificially Produced")
    clr()

def d100():
    print ("This is Fermium [Fm]")
    print ("Atomic Number: 100")
    print ("Atomic Weight: 257")
    print ("Melting Point: 1800 K (1527°C or 2781°F)")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: none    Group Name: Actinide")
    print ("Radioactive and Artificially Produced")
    clr()

def d101():
    print ("This is Mendelevium [Md]")
    print ("Atomic Number: 101")
    print ("Atomic Weight: 258")
    print ("Melting Point: 1100 K (827°C or 1521°F)")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: none    Group Name: Actinide")
    print ("Radioactive and Artificially Produced")
    clr()

def d102():
    print ("This is Nobelium [No]")
    print ("Atomic Number: 102")
    print ("Atomic Weight: 259")
    print ("Melting Point: 1100 K (827°C or 1520°F)")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: none    Group Name: Actinide")
    print ("Radioactive and Artificially Produced")
    clr()

def d103():
    print ("This is Lawrencium [Lr]")
    print ("Atomic Number: 103")
    print ("Atomic Weight: 262")
    print ("Melting Point: 1900 K (1627°C or 2961°F)")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: 3    Group Name: Actinide")
    print ("Radioactive and Artificially Produced")
    clr()

def d104():
    print ("This is Rutherfordium [Rf]")
    print ("Atomic Number: 104")
    print ("Atomic Weight: 263")
    print ("Melting Point: Unknown")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: 4    Group Name: none")
    print ("Radioactive and Artificially Produced")
    clr()

def d105():
    print ("This is Dubnium [Db]")
    print ("Atomic Number: 105")
    print ("Atomic Weight: 268")
    print ("Melting Point: Unknown")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: 5    Group Name: none")
    print ("Radioactive and Artificially Produced")
    clr()

def d106():
    print ("This is Seaborgium [Sg]")
    print ("Atomic Number: 106")
    print ("Atomic Weight: 271")
    print ("Melting Point: Unknown")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: 6    Group Name: none")
    print ("Radioactive and Artificially Produced")
    clr()

def d107():
    print ("This is Bohrium [Bh]")
    print ("Atomic Number: 107")
    print ("Atomic Weight: 270")
    print ("Melting Point: Unknown")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: 7    Group Name: none")
    print ("Radioactive and Artificially Produced")
    clr()

def d108():
    print ("This is Hassium [Hs]")
    print ("Atomic Number: 108")
    print ("Atomic Weight: 270")
    print ("Melting Point: Unknown")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: 8    Group Name: none")
    print ("Radioactive and Artificially Produced")
    clr()

def d109():
    print ("This is Meitnerium [Mt]")
    print ("Atomic Number: 109")
    print ("Atomic Weight: 278")
    print ("Melting Point: Unknown")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: 9    Group Name: none")
    print ("Radioactive and Artificially Produced")
    clr()

def d110():
    print ("This is Darmstadtium [Ds]")
    print ("Atomic Number: 110")
    print ("Atomic Weight: 281")
    print ("Melting Point: Unknown")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Expected to be a Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: 10    Group Name: none")
    print ("Radioactive and Artificially Produced")
    clr()

def d111():
    print ("This is Roentgenium [Rg]")
    print ("Atomic Number: 111")
    print ("Atomic Weight: 281")
    print ("Melting Point: Unknown")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Expected to be a Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: 11    Group Name: none")
    print ("Radioactive and Artificially Produced")
    clr()

def d112():
    print ("This is Copernicium [Cn]")
    print ("Atomic Number: 112")
    print ("Atomic Weight: 285")
    print ("Melting Point: Unknown")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Expected to be a Solid")
    print ("Element Classification: Metal")
    print ("eriod Number: 7    Group Number: 12    Group Name: none")
    print ("Radioactive and Artificially Produced")
    clr()

def d113():
    print ("This is Nihonium [Nh]")
    print ("Atomic Number: 113")
    print ("Atomic Weight: 286")
    print ("Melting Point: Unknown")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Expected to be a Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: 13    Group Name: none")
    print ("Radioactive and Artificially Produced")
    clr()

def d114():
    print ("This is Flerovium [Fl]")
    print ("Atomic Number: 114")
    print ("Atomic Weight: 289")
    print ("Melting Point: Unknown")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Expected to be a Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: 14    Group Name: none")
    print ("Radioactive and Artificially Produced")
    clr()

def d115():
    print ("This is Moscovium [Mc]")
    print ("Atomic Number: 115")
    print ("Atomic Weight: 289")
    print ("Melting Point: Unknown")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Expected to be a Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: 15    Group Name: Pnictogen")
    print ("Radioactive and Artificially Produced")
    clr()

def d116():
    print ("This is Livermorium [Lv]")
    print ("Atomic Number: 116")
    print ("Atomic Weight: 293")
    print ("Melting Point: Unknown")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Expected to be a Solid")
    print ("Element Classification: Metal")
    print ("Period Number: 7    Group Number: 16    Group Name: Chalcogen")
    print ("Radioactive and Artificially Produced")
    clr()

def d117():
    print ("This is Tennessine [Ts]")
    print ("Atomic Number: 117")
    print ("Atomic Weight: 294")
    print ("Melting Point: Unknown")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Expected to be a Solid")
    print ("Element Classification: Unknown")
    print ("Period Number: 7    Group Number: 17    Group Name: Halogen")
    print ("Radioactive and Artificially Produced")
    clr()

def d118():
    print ("This is Oganesson [Og]")
    print ("Atomic Number: 118")
    print ("Atomic Weight: 294")
    print ("Melting Point: Unknown")
    print ("Boiling Point: Unknown")
    print ("Density: Unknown")
    print ("Phase at Room Temperature: Expected to be a Gas")
    print ("Element Classification: Non-metal")
    print ("Period Number: 7    Group Number: 18    Group Name: Noble Gas")
    print ("Radioactive and Artificially Produced")
    clr()

def Games(): #Game selection
    print ("Game1-           Game2-          ")
    select = input("Please Select game:")
    if select == "Game1":
        G1()
        clr()
    elif select == "Game2":
        G2()
        clr()

def G1(): #game1
    pass

def G2(): #game 2
    pass

def credits(): #credits
    print ("Written by Zen")
    clr()

def tracker() : #main nav
    number = input("Enter a task:")
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
    elif number == "51":
        d51()
        tracker()
    elif number == "52":
        d52()
        tracker ()
    elif number == "53":
        d53()
        tracker()
    elif number == "54":
        d54()
        tracker()
    elif number == "55":
        d55()
        tracker()
    elif number == "56":
        d56()
        tracker()
    elif number == "57":
        d57()
        tracker()
    elif number == "58":
        d58()
        tracker()
    elif number == "59":
        d59()
        tracker()
    elif number == "60":
        d60()
        tracker()
    elif number =="61":
        d61()
        tracker()
    elif number =="62":
        d62()
        tracker()
    elif number =="63":
        d63()
        tracker()
    elif number =="64":
        d4()
        tracker()
    elif number =="65":
        d65()
        tracker()
    elif number =="66":
        d66()
        tracker()
    elif number =="67":
        d67()
        tracker()
    elif number =="68":
        d68()
        tracker()
    elif number =="69":
        d69()
        tracker()
    elif number =="70":
        d70()
        tracker()
    elif number =="71":
        d71()
        tracker()
    elif number =="72":
        d72()
        tracker()
    elif number =="73":
        d73()
        tracker()
    elif number =="74":
        d74()
        tracker()
    elif number =="75":
        d75()
        tracker()
    elif number =="76":
        d76()
        tracker()
    elif number =="77":
        d77()
        tracker()
    elif number =="78":
        d78()
        tracker()
    elif number =="79":
        d79()
        tracker()
    elif number =="80":
        d80()
        tracker()
    elif number =="81":
        d81()
        tracker()
    elif number =="82":
        d82()
        tracker()
    elif number =="83":
        d83()
        tracker()
    elif number =="84":
        d84()
        tracker()
    elif number =="85":
        d85()
        tracker()
    elif number =="86":
        d86()
        tracker()
    elif number =="87":
        d87()
        tracker()
    elif number =="88":
        d88()
        tracker()
    elif number =="89":
        d89()
        tracker()
    elif number =="90":
        d90()
        tracker()
    elif number =="91":
        d91()
        tracker()
    elif number =="92":
        d92()
        tracker()
    elif number =="93":
        d93()
        tracker()
    elif number =="94":
        d94()
        tracker()
    elif number =="95":
        d95()
        tracker()
    elif number =="96":
        d96()
        tracker()
    elif number =="97":
        d97()
        tracker()
    elif number =="98":
        d98()
        tracker()
    elif number =="99":
        d99()
        tracker()
    elif number =="100":
        d100()
        tracker()
    elif number =="101":
        d101()
        tracker()
    elif number =="102":
        d102()
        tracker()
    elif number =="103":
        d103()
        tracker()
    elif number =="104":
        d104()
        tracker()
    elif number =="105":
        d105()
        tracker()
    elif number =="106":
        d106()
        tracker()
    elif number =="107":
        d107()
        tracker()
    elif number =="108":
        d108()
        tracker()
    elif number =="109":
        d109()
        tracker()
    elif number =="110":
        d110()
        tracker()
    elif number =="111":
        d111()
        tracker()
    elif number =="112":
        d112()
        tracker()
    elif number =="113":
        d113()
        tracker()
    elif number =="114":
        d114()
        tracker()
    elif number =="115":
        d115()
        tracker()
    elif number =="116":
        d116()
        tracker()
    elif number =="117":
        d117()
        tracker()
    elif number =="118":
        d118()
        tracker()
    elif number == "Games":
        Games()
        tracker()
    elif number == "Credits":
        credits()
        tracker()
    os.system("cls")
    app.mainloop()

print ("Enter a number to search elements(1-118).Type Games for games and Credits for Credits.Press enter to exit.")
tracker()