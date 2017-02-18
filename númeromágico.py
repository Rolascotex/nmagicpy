import random

def play(v):
	while v > 0 :
		print("Bienvenido a número mágico, tienes", v ,"vidas" )
		print("suerte")
		nummagic= random.randrange(1,11)
		intento = int(input("tu número es: "))

		if intento == nummagic:
			print("Ganaste!!")
			v += 1

		else:
			print("error, tú numero era: ", nummagic)
			v -= 1 
			print("vidas restantes: ", v)
			print("_______________________________________________________")
			print("_______________________________________________________")
	print("Game Over")

vidas = 7
play(vidas)