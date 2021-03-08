#Random-Lib-Exercise.py
import random as rand

Number = rand.randint(0,10932010)

letter = chr(rand.randint(65,90))

List_1 = ["1","2","3","4","5"]
Value = List_1[rand.randint(0,len(List_1)-1)]

List_2 = list("ABCDEFGHIJK")
rand.shuffle(List_2)

print(f"""\nNumber : {Number}
Letter : {letter}
Value : {Value}
List_2 : {List_2}""")