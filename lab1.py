#ma209A lab 1
#author Ömer Kolsuz
#2023-11-16

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.optimize import minimize
from scipy import integrate

#1. Använd Python för att beräkna
#(a) 35 ·25 (b) √5 + 1/4 (c) e10 (d) tan(π/6)

#uppgift 1a)
print("uppgift 1a-)")
result_a = 35 * 25
print(result_a)

#uppgift 1b)
print("uppgift 1b-)")
result_b = math.sqrt(5) + 1/4
print(result_b)

#uppgift 1c)
print("uppgift 1c-)")
result_c = math.exp(10)
print(result_c)

#uppgift 1d)
print("uppgift 1d-)")
result_d = math.tan(math.pi/6)
print(result_d)

#2. Du har följande utskrift från Python (a) 1.3533e+16 (b) 2.1191e-11.
#Skriv båda talen i vanlig form med tiopotenser.
print("\n Uppgift 2:")

#uppgift 2a)
print("uppgift 2a-)")
a = 1.3533e+16
print("{:.4f}e+{}".format(a / 10**16, 16))

#uppgift 2b)
print("uppgift 2b-)")
b = 2.1191e-11
print("{:.4f}e-{}".format(b * 10**11, 11))



#uppgift3.
#3.Plotta funktionerna y = sin(x) och y = sin(x) cos(x) i intervallet [0, 10].
#Bägge funktionerna skall plottas i samma figur
print("\nUppgift 3:")

import numpy as np
import matplotlib.pyplot as plt
#Skapa ett jämnt fördelat intervall från 0 till 10
x = np.linspace(0, 10)

#Beräkna y-värden för varje funktion
y1 = np.sin(x)
y2 = np.sin(x) * np.cos(x)

#Plotta funktionerna
plt.plot(x, y1, label='y = sin(x)') # x är listan över x-värden
plt.plot(x, y2, label='y = sin(x) * cos(x)')

#Lägg till etiketter på axlarna
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#uppgift4.
#4.Använd kommando av typen np.arange(a,b,h) för att generera en vektor med värdena
#(a) 10 12 14 16 18 20 22 24 26 28 30 32
#(b) -2 -5 -8 -11 -14 -17 -20 -23 -26 -29 -32 -35
#Glöm inte att importera numpy och matplotlib.pyplot
print("\nUppgift 4:")


import numpy as np
import matplotlib.pyplot


x = np.arange(10,34,2) #jag använder 34 istället för 32, för att matcha mönstret
print(x)
x = np.arange(-2,-38,-3)
print(x)
plt.show()
#uppgift5.
#5. Inför funktionen f (x) = 1.2x + √x − 2.
#Plotta funktionen i intervallet [0, 2], sätt ut gridlinjer och skriv axeltext.
#Använd kommandot optimize.fsolve för att bestämma funktionens nollställe.
#Observera att du måste importera biblioteket scipy.optimize
#för att kommandot skall fungera, se Exempel 8.
#När du matar in ett startvärde använd decimalpunkt!
print("\nUppgift 5:")

import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt

# Definierar en lambda-funktion (anonym funktion) f(x)
f = lambda x : 1.2 * x + np.sqrt(x) - 2

# Skapar en array 'x' med jämnt fördelade punkter från 0 till 2
x = np.linspace(0, 2)

# Evaluerar funktionen 'f' för varje punkt i 'x' och lagra resultaten i 'y'
y = f(x)

# Plottar funktionen
plt.plot(x, y)

# Lägger till rutnät i bakgrunden av plottet
plt.grid()

# Sätter etiketter för x- och y-axlarna
plt.xlabel('x')
plt.ylabel('y')

# Använder optimize.fsolve för att hitta en nollpunkt för 'f' med en startpunkt på 0.5
x0 = optimize.fsolve(f, 0.5)

# Skriver ut den hittade nollpunkten
print(x0)

# Visar plottet
plt.show()


#uppgift6.
#6. nför funktionen f (x) = e−xsin(x). Plotta funktionen i intervallet [0, 6],
#sätt ut gridlinjer och skriv axeltext. Använd kommandot optimize.minimize för att
#bestämma funktionens minpunkt nära x= 4.
#Observera att du måste importera biblioteket scipy.optimize
#för att kommandot skall fungera, se Exempel 8.
print("\nUppgift 6:")

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# Definierar en lambda-funktion (anonym funktion) f(x)
f = lambda x : np.exp(-x) * np.sin(x)

# Skapar en array 'x' med jämnt fördelade punkter från 0 till 6
x = np.linspace(0, 6)

# Evaluerar funktionen 'f' för varje punkt i 'x' och lagra resultaten i 'y'
y = f(x)

# Plottar funktionen
plt.plot(x, y)

# Lägger till rutnät i bakgrunden av plottet
plt.grid()

# Sätter etiketter för x- och y-axlarna
plt.xlabel('x')
plt.ylabel('y')

# Använder optimize.minimize för att hitta det lokala minimumet för 'f' med en startpunkt på 4
xmin = optimize.minimize(f, 4)

# Skriver ut x-värdet för det lokala minimumet
print(xmin.x)

# Visar plottet
plt.show()

#uppgift7.
#7. Beräkna integralen
# (x3 + 2x2 − x + 1)dx
#med hjälp av kommandot quad.integrate.
#Kontrollera värde genom att beräkna integralen för hand
#(obs denna räkning skall också redovisas under labben).
#Observera att du måste importera biblioteket scipy.integrate,
#se Exempel 9.
print("\nUppgift 7:")

f = lambda x: x**3 + 2*x**2 - x + 1
I=integrate.quad(f, 0, 5)
print(I)
