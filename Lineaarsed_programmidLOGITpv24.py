from random import * #3 importeerime kõik funkstioonid, mis on radnom moodulis
from math import *
#1
nimi=input("Whats your name ")
print(f"Hello, {nimi}!")
vanus=int(input("How old are you "))
print(f"You are {nimi} \n you are {vanus} old!")



#2
vanus = 18

eesnimi = "Jaak"

pikkus = 16.5

kas_käib_koolis = True

print(f"{vanus}is {type(vanus)} type")

print(f"{eesnimi} is {type(eesnimi)} type")

print (F"{pikkus} is {type(pikkus)} type")

print (F"{kas_käib_koolis} is {type(kas_käib_koolis)}")

#3


kommidearv=randint(2,100)
print (f"there s {kommidearv} on the table")
kommidvõtnud=int(input("how many candies you wanna take "))
kommidjäänud=kommidearv-kommidvõtnud
print (f"{kommidjäänud} are left on the table")

#4

ümbermõõdu= float(input("siseta puu läbimõõdu "))
läbimõõdu= float(ümbermõõdu/pi)
print (f"läbimõõdu on {läbimõõdu}")

#5

N = float(input("sisesta üks pool "))
M = float(input("sisesta teine pool "))
D2 = float((N**2)+(M**2))
D= float(sqrt(D2))
print(f"{D}")
