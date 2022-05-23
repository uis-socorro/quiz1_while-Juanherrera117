"""Capitales Juan y Pedro"""
("---------------------------------")
("------------Capital--------------")
("---------------------------------")

# input
C1 = int(input("Introduzca el valor del capital C1: "))
C2 = int(input("Introduzca el valor del capital C2: "))
C3 = int(input("Introduzca el valor del capital C3: "))

# processing 
M = 0 
Suma = C1 + C2

while Suma < C3:
    C1 = C1 + C1*0.03
    C2 = C2 + C2*0.04
    Suma = C1 + C2
    M = M + 1

# output
print("Para alcanzar un capital de: " + str(Suma) + " se necesitan  " + str(M) + " Meses")