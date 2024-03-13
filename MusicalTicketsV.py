from guizero import *
from viperdb import *

def storeDB():
    db = ViperDB('./.db')
    db['seats'] = seats
    db.close()

def loadDB():
    global seats
    db = ViperDB('./.db')
    seats = db['seats']
    db.close()

def populatePurchased():
    x = 0
    y = 0
    for row in seats:
        for seat in row:
            if seat == "black":
                seatsWaffle.set_pixel(x,y, "black")
            x = x + 1
        y = y + 1
        x = 0

def wafflePressed(x,y):
    if seatsWaffle.get_pixel(x,y) == "white":
        seatsWaffle.set_pixel(x,y, "green")
    elif seatsWaffle.get_pixel(x,y) == "green":
        seatsWaffle.set_pixel(x,y, "white")
    elif seatsWaffle.get_pixel(x,y) == "black":
        print("already purchased")
    else:
        print("some other color")
        
def purchasePressed():
    global seats
    allSeats = seatsWaffle.get_all()
    x = 0
    y = 0
    for row in allSeats:
        for seat in row:
            if seat == "green":
                seatsWaffle.set_pixel(x,y, "black")
            x = x + 1
        y = y + 1
        x = 0
    seats = seatsWaffle.get_all()
    storeDB()   
            

row1 = ["white", "white", "white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white"]
row2 = ["white", "white", "white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white"]
row3 = ["white", "white", "white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white"]
row4 = ["white", "white", "white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white"]
row5 = ["white", "white", "white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white"]
row6 = ["white", "white", "white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white"]
row7 = ["white", "white", "white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white"]
row8 = ["white", "white", "white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white","white"]

seats = [row1, row2, row3, row4, row5, row6, row7, row8]

app = App(title="Musical Tickets", width=600, height=400)

instructionText = Text(app, text="Click On Available Seats")
seatsWaffle = Waffle(app, width=20, height=8, command=wafflePressed)
purchaseButton = PushButton(app, text="Purchase", command=purchasePressed)

loadDB()
if seats == None:
    seats = [row1, row2, row3, row4, row5, row6, row7, row8]
populatePurchased()
app.display()