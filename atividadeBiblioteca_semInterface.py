##############################################################################################
##############################################################################################
#
#                 		VISAO COMPUTACIONAL - 29/07/2016
#
# Produzir um pequeno software que implemente as seguintes funcionalidades:
# - Abrir um arquivo de imagem colorida escolhida pelo usuario;
# - Mostrar a imagem aberta;
# - Permitir que o usuario reduza ou aumente o tamanho da imagem (zoom in e zoom out);
# - Converter a imagem para tons de cinza;
# - Produzir uma "versao negativa" da imagem e mostrar o resultado para o usuario, juntamente com a imagem original e a imagem em tons de cinza.
#
#   Academico: Gabriel Kirsten Menezes RA: 148298
#
# Comando para instalar outras bibliotecas:
# sudo apt-get install python-imaging-tk
##############################################################################################
##############################################################################################

import cv2 							#importacao da biblioteca do OpenCV
from Tkinter import Tk 						#biblioteca para selecao do arquivo 
from tkFileDialog import askopenfilename 			#biblioteca para selecao do arquivo 
import numpy as np




btn = Button(root, text="Abrir uma imagem", command=abrir_imagem)

btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")












#selecao do arquivo de imagem
Tk().withdraw()
filename = askopenfilename(filetypes=[("Image Files", '*.jpg')])

img = cv2.imread(filename.encode('utf-8'), cv2.IMREAD_COLOR) 	#abrir imagem selecionada colorida

cv2.namedWindow('Imagem', cv2.WINDOW_AUTOSIZE)			#carrega a visualizacao da imagem sem tratamento	
cv2.imshow('Imagem',img) 					#exibe a imagem sem tratamento

img_greyScale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)		#alterar imagem para tons de cinza
cv2.namedWindow('Imagem em tons de cinza', cv2.WINDOW_AUTOSIZE) #carrega a visualizacao da imagem em tons de cinza
cv2.imshow('Imagem em tons de cinza',img_greyScale) 		#exibe a imagem em tons de cinza

img_invert = 255-img_greyScale 					#subtrai de 255 do valor de cada posicao do vetor em escala de cinza, para gerar o arquivo negativo

cv2.namedWindow('Imagem invertida', cv2.WINDOW_AUTOSIZE)	#carrega a visualizacao da imagem invertida
cv2.imshow('Imagem invertida',img_invert) 			#exibe a imagem invertida

cont1 = cont2 = cont3 = 1.0					#as imagens abrem com escala de 1 para 1
scale = 0.05							#define a porcentagem de zoom
imagemSelecionada = 1						#inicialmente, a imagem 1 e selecionada

#comandos relacionados a teclas
# ESC - finaliza
# 1 - seleciona imagem original
# 2 - seleciona imagem em tons de cinza
# 3 - seleciona imagem invertida
# ctrl + '+' - zoom in
# ctrl + '-' - zoom out

while(1):
    k = cv2.waitKey(0)
    if k==1048603 or k==27:    							#esc para finalizar 
	print 'Finalzando...'
	cv2.destroyAllWindows()
        break

    #o trecho abaixo e responsavel por operacoes de zoom out
    elif k==1376299 or k==1376171 or k==1310781 or k==327595 or k==262205:	#ctrl + '+', ctrl + '=' zoom in
 	print 'zoom in'
 	if(imagemSelecionada == 1):
		cont1 = cont1 + scale
 		res = cv2.resize(img, (0,0), fx=cont1, fy=cont1) 
		cv2.imshow('Imagem',res)
	elif(imagemSelecionada == 2):
		cont2 = cont2 + scale
		res = cv2.resize(img_greyScale, (0,0), fx=cont2, fy=cont2) 
		cv2.imshow('Imagem em tons de cinza',res)
	elif(imagemSelecionada == 3):
		cont3 = cont3 + scale	
		res = cv2.resize(img_invert, (0,0), fx=cont3, fy=cont3) 
		cv2.imshow('Imagem invertida',res)
	continue

    #o trecho abaixo e responsavel por operacoes de zoom out
    elif k==1376173 or k==1310765 or k==1376351 or k==262189 or k==327597:	#ctrl + '-', ctrl + '_' zoom out
 	print 'zoom out'
	if(imagemSelecionada == 1):
		if cont1 <= scale:					#zoom minimo definido como valor de scale
			cont1 = scale
			print 'zoom minimo'
		else:
			cont1 = cont1 - scale
 		res = cv2.resize(img, (0,0), fx=cont1, fy=cont1) 
		cv2.imshow('Imagem',res)
	elif(imagemSelecionada == 2):
		if cont2 <= scale:					#zoom minimo definido como valor de scale
			cont2 = scale
			print 'zoom minimo'
		else:
			cont2 = cont2 - scale
		res = cv2.resize(img_greyScale, (0,0), fx=cont2, fy=cont2) 
		cv2.imshow('Imagem em tons de cinza',res)
	elif(imagemSelecionada == 3):
		if cont3 <= scale:					#zoom minimo definido como valor de scale
			cont3 = scale
			print 'zoom minimo'
		else:
			cont3 = cont3 - scale
		res = cv2.resize(img_invert, (0,0), fx=cont3, fy=cont3)
		cv2.imshow('Imagem invertida',res)
	continue

    #o trecho abaixo e responsavel pela selecao de telas
    elif k==1048625 or k==49 or k==1114033:
	imagemSelecionada = 1
	print 'Imagem original selecionada'
	continue
    elif k==1048626 or k==50 or k==1114034:
	imagemSelecionada = 2
	print 'Imagem em tons de cinza selecionada'
	continue
    elif k==1048627 or k==51 or k==1114035:
	imagemSelecionada = 3
	print 'Imagem invertida selecionada'
	continue
