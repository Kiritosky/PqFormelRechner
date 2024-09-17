import math
print("Pq formel Rechner Bitte geben sie ihre zahlen ein")

q = int(input("Gebe den wert für q an "))
p = int(input("Gebe den Wert für p an "))

d = p * p / 4 - q

if (d < 0):
    print("keine lösung")
elif (d == 0):
    x1 = -p/2
    print(x1)
else:
    x1 = -p/2 - math.sqrt(d)
    x2 = p/2 + math.sqrt(d)
    print(x1, x2)

