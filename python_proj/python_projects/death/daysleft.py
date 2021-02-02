#from sys import argv
from datetime import datetime
from datetime import date
import sys
import random
import time
f=open("/mnt/d/Documents/python_projects/death/dayscount.txt", "r")
if f.mode == 'r':
    Productive_life = int(f.readline().rstrip("\n"))
    PhD_life = int(f.readline().rstrip("\n"))
f.close()
dt = (datetime.now())
#print(dt.date())
deadline = date(2034, 9 , 8)
deadline_phd = date(2023, 9, 8)
#print(deadline)
#print(dt)
#days_gone = input("Days gone: ")
val_date = deadline - dt.date()
val_date_phd = deadline_phd - dt.date()
val = val_date
#print(val)
try:
   #val = int(days_gone)
   #val
   print("Good..")
   time.sleep(2)
   print("Calculating...")
   time.sleep(random.randint(1,5))   
except ValueError:
   print("That's not an integer!")
   #print("No.. input string is not an Integer. It's a string")

print("Stand by...")
time.sleep(random.randint(1,5))



Productive_life=val_date
PhD_life=val_date_phd

print("\n")
print(Productive_life,": Days left for your productive young, healthy life")
print(PhD_life,": Days left for your PhD project and ideas")
print("\n")
print("Remember to put some wise quote here")
print("Deadlines are good for you")
print("Start your own project")
print("Do smth everyday")
print("Do not give up")
print("Notes from previous day")
