from playsound import playsound
import turtle
import time
import random



wn = turtle.Screen()
tur = turtle.Turtle()

#make piano
tur.hideturtle()
wn.setup(512, 382)
wn.bgpic("C:\\Users\\Senya\\Pictures\\piano.png")
tur.penup()
tur.shape("circle")
tur.shapesize(1)
tur.speed(0)
#set up notes
def playC():
    playsound("C:\\Users\\Senya\\Downloads\\VS Code_Python\\Project 1.3.1\\mp3 Notes\\c4.mp3")
    random_number = random.randint(1118481,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    tur.color(hex_number)
    tur.goto( -230 ,-10)
    tur.stamp()

def playCs():
    playsound("C:\\Users\\Senya\\Downloads\\VS Code_Python\\Project 1.3.1\\mp3 Notes\\c-4.mp3")
    random_number = random.randint(1118481,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    tur.color(hex_number)
    tur.goto( -188.5 ,-10)
    tur.stamp()

def playD():
    playsound("C:\\Users\\Senya\\Downloads\\VS Code_Python\\Project 1.3.1\\mp3 Notes\\d4.mp3")
    random_number = random.randint(1118481,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    tur.color(hex_number)
    tur.goto( -147 ,-10)
    tur.stamp()

def playDs():
    playsound("C:\\Users\\Senya\\Downloads\\VS Code_Python\\Project 1.3.1\\mp3 Notes\\d-4.mp3")
    random_number = random.randint(1118481,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    tur.color(hex_number)
    tur.goto( -105.5 ,-10)
    tur.stamp()

def playE():
    playsound("C:\\Users\\Senya\\Downloads\\VS Code_Python\\Project 1.3.1\\mp3 Notes\\e4.mp3")
    random_number = random.randint(1118481,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    tur.color(hex_number)
    tur.goto( -64 ,-10)
    tur.stamp()

def playF():
    playsound("C:\\Users\\Senya\\Downloads\\VS Code_Python\\Project 1.3.1\\mp3 Notes\\f4.mp3")
    random_number = random.randint(1118481,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    tur.color(hex_number)
    tur.goto( -22.5 ,-10)
    tur.stamp()

def playFs():
    playsound("C:\\Users\\Senya\\Downloads\\VS Code_Python\\Project 1.3.1\\mp3 Notes\\f-4.mp3")
    random_number = random.randint(1118481,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    tur.color(hex_number)
    tur.goto( 19 ,-10)
    tur.stamp()

def playG():
    playsound("C:\\Users\\Senya\\Downloads\\VS Code_Python\\Project 1.3.1\\mp3 Notes\\g4.mp3")
    random_number = random.randint(1118481,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    tur.color(hex_number)
    tur.goto( 60.5 ,-10)
    tur.stamp()

def playGs():
    playsound("C:\\Users\\Senya\\Downloads\\VS Code_Python\\Project 1.3.1\\mp3 Notes\\g-4.mp3")
    random_number = random.randint(1118481,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    tur.color(hex_number)
    tur.goto( 102 ,-10)
    tur.stamp()

def playA():
    playsound("C:\\Users\\Senya\\Downloads\\VS Code_Python\\Project 1.3.1\\mp3 Notes\\a5.mp3")
    random_number = random.randint(1118481,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    tur.color(hex_number)
    tur.goto( 143.5 ,-10)
    tur.stamp()

def playAs():
    playsound("C:\\Users\\Senya\\Downloads\\VS Code_Python\\Project 1.3.1\\mp3 Notes\\a-5.mp3")
    random_number = random.randint(1118481,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    tur.color(hex_number)
    tur.goto( 185 ,-10)
    tur.stamp()

def playB():
    playsound("C:\\Users\\Senya\\Downloads\\VS Code_Python\\Project 1.3.1\\mp3 Notes\\b5.mp3")
    random_number = random.randint(1118481,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    tur.color(hex_number)
    tur.goto( 226.5 ,-10)
    tur.stamp()


#play sounds on key press
wn.listen()
wn.onkeypress(playC, "q")
wn.onkeypress(playCs, "2")
wn.onkeypress(playD, "w")
wn.onkeypress(playDs, "3")
wn.onkeypress(playE, "e")
wn.onkeypress(playF, "r")
wn.onkeypress(playFs, "5")
wn.onkeypress(playG, "t")
wn.onkeypress(playGs, "6")
wn.onkeypress(playA, "y")
wn.onkeypress(playAs, "7")
wn.onkeypress(playB, "u")


#show corresponding keys
x=-230
y=0
notes=['Q', '2', 'W', '3', 'E', 'R', '5', 'T', '6', 'Y', '7', 'U']
tur.color("grey")
for i in range(12):
    tur.goto(x, 0)
    tur.write(notes[y], font=('Comic Sans MS', 10, 'normal'))
    x+=41.5
    y+=1







wn.mainloop()