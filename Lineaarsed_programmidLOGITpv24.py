from random import * #3 importeerime kõik funkstioonid, mis on radnom moodulis
from math import *
# #1
nimi=input("Whats your name ")
print(f"Hello, {nimi}!")
vanus=int(input("How old are you "))
print(f"You are {nimi} \n you are {vanus} old!")



# #2
vanus = 18

eesnimi = "Jaak"

pikkus = 16.5

kas_käib_koolis = True

print(f"{vanus}is {type(vanus)} type")

print(f"{eesnimi} is {type(eesnimi)} type")

print (F"{pikkus} is {type(pikkus)} type")

print (F"{kas_käib_koolis} is {type(kas_käib_koolis)}")

# #3


kommidearv=randint(2,100)
print (f"there s {kommidearv} on the table")
kommidvõtnud=int(input("how many candies you wanna take "))
kommidjäänud=kommidearv-kommidvõtnud
print (f"{kommidjäänud} are left on the table")

# #4

ümbermõõdu= float(input("siseta puu läbimõõdu "))
läbimõõdu= float(ümbermõõdu/pi)
print (f"läbimõõdu on {läbimõõdu}")

# #5

N = float(input("sisesta üks pool "))
M = float(input("sisesta teine pool "))
D2 = float((N**2)+(M**2))
D= float(sqrt(D2))
print(f"{D}")

# #6
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg
print("Sinu kiirus oli " + str(kiirus) + " km/h")

#7

random1=randint(1,5)
random2=randint(1,5)
random3=randint(1,5)
random4=randint(1,5)
random5=randint(1,5)
average1= (random1 + random2 + random3 + random4 + random5) / 5
print(f"Numbers are; {random1},{random2},{random3},{random4},{random5} and the average is {average1},")

#8
 #8.1
frog="""          @..@ 
          (----)
         ( \__/ )
         ^^ "" ^^ """
print(frog)
 #8.2
print("""      @..@ """)
print("""     (----) """)
print("""    ( \__/ )) """)

#9

a=randint(1,10)
b=randint(1,10)
c=randint(1,10)
perimeter= a + b + c
print(f"Perimeter is {perimeter}")

#10

pizza= 12.90
friends=randint(2,3)
tip= pizza*0.1+pizza
summ= tip / friends
print(f"you are {friends}, so the pizza and tip would cost you {summ}$")