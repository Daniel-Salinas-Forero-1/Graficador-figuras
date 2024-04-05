
from math import tan,sqrt
import pygame
import math
import time
import numpy as np
from pyparsing import col


# colores necesarios 
WHITE = (255,255,255)
BLUE = (65, 115, 204)
RED = (255,0,0)
YELLOW = (255,255,0)
BLACK = (0, 0, 0)
PINK = (197, 11, 183)
BROWN = (132, 60, 12)
GRAY = (191, 191, 191)
ORANGE = (240, 123, 53)
DARKYELLOW = (189, 146, 5)
DARKGREEN = (83, 131, 45)
LIGHTBLUE = (0, 176, 244)
PURPLE = (116, 48, 157)
LIGHTGREEN = (146, 208, 81)

pygame.init()
# imagen de las formas y de los colores 
pantalla = pygame.display.set_mode ((800,600))
BarraFig = pygame.image.load("Figuras.jpg")
BarraCol = pygame.image.load("Colores.jpg")

# con la funcion SeleccionarColor escogemos que colores vamos a usar 
# la funcion recive 3 parametros una posicion X y Y una variable 
# en donde se guardara el color elegido y retorna la variable con el color
def SeleccionarColor (x,y,color):
	if x>= 0 and y >= 0 and x <=88  and y <= 30:
		color = WHITE
	elif x>= 89 and y >= 0 and x <= 177 and y <= 30:
		color = YELLOW
	elif x>= 177 and y >= 0 and x <= 264 and y <= 30:
		color = BLUE
	elif x>= 264 and y >= 0 and x <= 351 and y <= 30:
		color = RED
	elif x>= 351 and y >= 0 and x <= 439 and y <= 30:
		color = ORANGE
	elif x>= 439 and y >= 0 and x <= 527 and y <= 30:
		color = DARKGREEN
	elif x>= 527 and y >= 0 and x <= 615 and y <= 30:
		color = PURPLE
	elif x>= 0 and y >= 30 and x <=88  and y <= 60:
		color = BLACK
	elif x>= 89 and y >= 30 and x <= 177 and y <= 60:
		color = PINK
	elif x>= 177 and y >= 30 and x <= 264 and y <= 60:
		color = BROWN
	elif x>= 264 and y >= 30 and x <= 351 and y <= 60:
		color = GRAY
	elif x>= 351 and y >= 30 and x <= 439 and y <= 60:
		color = DARKYELLOW
	elif x>= 439 and y >= 30 and x <= 527 and y <= 60:
		color = LIGHTBLUE
	elif x>= 527 and y >= 30 and x <= 615 and y <= 60:
		color = LIGHTGREEN

	return color

# con la funcion SeleccionarFigura escogemos que figura vamos a dibujar en pantalla
# la funcion recive 3 parametros una posicion X y Y una variable 
# en donde se guardara un texto dependiendo la figura elegido y retorna la variable con el nombre de la figura

def SeleccionarFigure (x,y,figura):
	print(x,y)
	if x >= 0 and y >= 61 and x <= 88 and y <= 129:
		figura="Rectangle"
	if x >= 0 and y >= 130 and x <= 88 and y <= 198:
		figura="Circle"
	if x >= 0 and y >= 199 and x <= 88 and y <= 267:
		figura="Line"
	if x >= 0 and y >= 268 and x <= 88 and y <= 336:
		figura="Equilateral"
	if x >= 0 and y >= 337 and x <= 88 and y <= 405:
		figura="Isoceles"
	if x >= 0 and y >= 406 and x <= 88 and y <= 470:
		figura="Pen"

	return figura

#-----------------------------------------------------------------------------
# funcion principal 
def main():
	# se inicializan las variables de posicion 
	figura="Pen"
	color= WHITE
	cont=0
	x=0
	y=0
	x1 = 0
	y1 = 0
	x2 = 0
	y2 = 0
	while True:
		for eventos in pygame.event.get():
			if eventos.type == pygame.QUIT:
				exit()
			elif eventos.type == pygame.MOUSEBUTTONDOWN:
				x, y = eventos.pos
				# si el evento mousebuttondown se lleva a acabo en alguna de las siguientes pocision 
				# se llamaran  ha las funciones de seleccionar colores o figuras dependiendo el lugar en donde se hizo click 
				if x >=0 and y >=0 and x <= 616 and y <=59:
					color= SeleccionarColor(x,y,color)
				if x >=0 and y >= 60 and x <= 88 and y <=536:
					figura= SeleccionarFigure(x,y, figura)
				if x >=89 and y >= 61 and x <= 800 and y <=600:
					# segun el color y la figura se comenzara a dibujar 
					if figura == "Rectangle":
						cont += 1
						if cont == 1:
							x1 = x
							y1 = y
						if cont == 2:
							x2 = x
							y2 = y
							pygame.draw.rect(pantalla,color,(x1,y1,x2-x1,y2-y1),1)
							cont = 0
					if figura == "Circle":
						cont += 1
						if(cont == 1):
							x1 = x
							y1 = y
						if(cont == 2):
							x2 = x
							y2 = y
							pygame.draw.circle(pantalla,color,(x1,y1),sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)),width=4)
							cont = 0
					if figura == "Line":
						cont += 1
						if cont == 1:
							x1 = x
							y1 = y
						if cont == 2:
							x2 = x
							y2 = y
							pygame.draw.line(pantalla,color,(x1,y1),(x2,y2),1)
							cont = 0
					if figura == "Equilateral":
						cont += 1
						if cont == 1 :
							x1 = x
							y1 = y
						if cont == 2:
							x2 = x
							y2 = y1
							pygame.draw.polygon(pantalla,color, points=[(x1,y1), (x1+(x2-x1)/2,y1 - int(tan(45)*(x2-x1)/2)), (x2,y2)])
							cont = 0
					if figura == "Isoceles":
						cont += 1
						if cont == 1:
							x1 = x
							y1 = y
						if cont == 2:
							x2 = x
							y2 = y1
							pygame.draw.polygon(pantalla,color, points=[(x1,y1), (x1,y1 - int(tan(45)*(x2-x1)/2)), (x2,y2)])
							cont = 0

			elif eventos.type == pygame.MOUSEMOTION:
				if figura == "Pen":
					pixel_array = pygame.PixelArray(pantalla)
					if pygame.mouse.get_pressed()[0]:
						pixel_array[eventos.pos[0], eventos.pos[1]] = color
					pixel_array.close()

		pantalla.blit(BarraCol,(0,0))
		pantalla.blit(BarraFig,(0,60))

		pygame.display.update()

main()