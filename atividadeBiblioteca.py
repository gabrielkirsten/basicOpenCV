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
# 	sudo apt-get install python-imaging-tk
##############################################################################################
##############################################################################################

import cv2 									#importacao da biblioteca do OpenCV
from Tkinter import * 						#biblioteca para selecao do arquivo 
from tkFileDialog import * 					#biblioteca para selecao do arquivo 
import numpy as np
from PIL import Image
from PIL import ImageTk

# Classe para interface principal, que contem somente um botao para abrir um arquivo
# Metodos:
#	- abrir_imagem : abre um seletor de arquivos para selecionar uma imagem a ser aberta
class Gui:		
	#construtor da classe, inicia as principais interfaces
	def __init__(self, master=None):
		self.mainContainer = Frame(master, relief=RAISED, borderwidth=1, padx="10", pady="10")	#container principal
		self.mainContainer.pack(expand="no", fill="both")										#exibir container
		btn = Button(self.mainContainer , text="Abrir uma imagem", command=self.abrir_imagem)	#botao seletor de arquivos
		btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")				#exibir botao seletor de aquivos
	
	#metodo de selecao de aquivos
	def abrir_imagem(self):
		Tk().withdraw()													#abre o seletor de arquivos
		filename = askopenfilename(filetypes=[("Image Files", '*.jpg')])#somente arquivos .jpg poderao ser selecionadios
		img = cv2.imread(filename.encode('utf-8'), cv2.IMREAD_COLOR) 	#abrir imagem selecionada colorida		
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		ImageWindowNoPatch(root, img, self, 'original') 				#exibe a imagem sem tratamento
		img_greyScale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)			#alterar imagem para tons de cinza
		ImageWindowNoPatch(root, img_greyScale, self, 'tons de cinza') 	#exibe a imagem em tons de cinza
		img_invert = 255-img_greyScale 									#subtrai de 255 do valor de cada posicao do vetor em escala de cinza, para gerar o arquivo negativo
		ImageWindowNoPatch(root, img_invert, self, 'Imagem invertida') 	#exibe a imagem invertida

# Classe para interface de abertura de imagem, cada imagem aberta sera um novo objeto desta classe
# Metodos:
#	- zoomIn : aplica a operacao de zoom in na imagem objeto
#	- zoomOut :  aplica operacao de zoom out na imagem objeto
class ImageWindowNoPatch:
	#construtor da classe, inicia as interfaces, abre as imagens e inicias as variaveis
	def __init__(self, parent, img, janelaGui, nome):
		self.scaleZoom = 1.0																#a escala de todas as imagens, no  inicio correspode a 1 (nenhum zoom aplicado)
		self.imagem = Toplevel(parent)														#cria uma nova janela
		self.imagem.title("Imagem - "+nome)													#define o titulo da janela
		self.imgArray = Image.fromarray(img)												#conversao para imagem do tipo Image
		self.imgOrig = ImageTk.PhotoImage(self.imgArray)									#conversao para imagem do tipo PhotoImage
		self.frameImg = Frame(self.imagem)													#cria um novo Frame para exibir a imagem 
		self.frameImg.pack(side="top",  fill="both", expand = "yes")						#exibe o frameImg
		prop = 1																			#variavel para saber a proporcao da imagem em relacao a resolucao da tela
		if root.winfo_screenwidth() < self.imgOrig.width():									#se a resulucao da imagem for maior que a da tela, calcula essa proporcao somada de dois
			prop = (self.imgOrig.width())/root.winfo_screenwidth() + 2						#tanto na largura quanto na aultura
		if root.winfo_screenheight() < self.imgOrig.height():	
			propAux = (self.imgOrig.height())/root.winfo_screenheight() + 2
			if propAux > prop:
				prop = propAux		
		#cria um novo canvas para exibir a barra de rolagem, com a proporcao corrida pelo fator acima
		self.canvas = Canvas(self.frameImg, borderwidth=0, scrollregion=(0,0,self.imgOrig.width(),self.imgOrig.height()),  width=self.imgOrig.width()/(prop), height=self.imgOrig.height()/(prop))
		self.frame = Frame(self.canvas)														#cria um novo frame para conter uma barra de rolagem  				
		self.mainImg = Label(self.frame, image=self.imgOrig)								#cria uma label para conter a imagem 
		self.mainImg.image = self.imgOrig													#define a imagem a ser exibida
		self.mainImg.pack(side="top", fill="both", expand = "yes")							#exibe a imagem
		self.vsb = Scrollbar(self.frameImg, orient="vertical", command=self.canvas.yview)	#barra de rolagem vertical
		self.hsb = Scrollbar(self.frameImg, orient="horizontal", command=self.canvas.xview)	#barra de rolagem horizontal
		self.canvas.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)		#define a fucao da barra de rolagem 
		self.vsb.pack(side="right", fill="y")												#exibe a barra de rolagem vertical
		self.hsb.pack(side="bottom", fill="x")												#exibe a barra de rolagem horizontal
		self.canvas.pack(side="left", fill="both", expand="yes")							#exibe o canvas contendo a imagem e as barras
		self.canvas.create_window((0,0), window=self.frame, anchor="nw", tags="self.frame")	#cria uma janela no canvas
		self.containerBtn = Frame(self.imagem)												#cria um frame para os botoes de zoom
		self.containerBtn.pack(side="bottom")												#exibe o frame
		Label(self.containerBtn, text="Zoom")												#cria uma label com a palavra zoom
		self.zoominbtn = Button(self.containerBtn, text=" + ", command=self.zoomIn)			#cria o botao de zoom in
		self.zoomoutbtn = Button(self.containerBtn, text=" - ", command=self.zoomOut)		#cria o botao de zoom out
		self.zoominbtn.pack(side="left", fill="both", expand="yes", padx="10", pady="10")	#exibe o botao de zoom in
		self.zoomoutbtn.pack(side="right", fill="both", expand="yes", padx="10", pady="10")	#exibe o botao de zoom out
	
	#funcao que realiza o zoom in na imagem 
	def zoomIn(self):
		#a condicao abaixo e para realizar um zoom gradual, dependendo do nivel de zoom atual
		if self.scaleZoom > 1.5:
			self.scaleZoom += 0.05
		elif self.scaleZoom > 1.3:
			self.scaleZoom += 0.08
		else:
			self.scaleZoom += 0.1
		
		self.imgArrayAux = self.imgArray.resize((int(self.imgOrig.width()*self.scaleZoom), int(self.imgOrig.height()*self.scaleZoom)), Image.ANTIALIAS) #redimensiona a imagem 
		#o codigo abaixo e responsavel por exibir a nova imagem redimensionada
		self.img = ImageTk.PhotoImage(self.imgArrayAux)
		self.mainImg.configure(image=self.img)
		self.frame.configure(width=int(self.imgOrig.width()*self.scaleZoom),height=int(self.imgOrig.height()*self.scaleZoom))
		self.canvas.configure(scrollregion=(0,0,int(self.imgOrig.width()*self.scaleZoom), int(self.imgOrig.height()*self.scaleZoom)))
	
	#funcao que realiza o zoom out na imagem 	
	def zoomOut(self):
		#a condicao abaixo e para realizar um zoom gradual, dependendo do nivel de zoom atual
		if self.scaleZoom < 0.3:
			self.scaleZoom -= 0.08
		elif self.scaleZoom < 0.5:
			self.scaleZoom -= 0.05
		else:
			self.scaleZoom -= 0.1
			
		self.imgArrayAux = self.imgArray.resize((int(self.imgOrig.width()*self.scaleZoom), int(self.imgOrig.height()*self.scaleZoom)), Image.ANTIALIAS) #redimensiona a imagem 
		#o codigo abaixo e responsavel por exibir a nova imagem redimensionada
		self.img = ImageTk.PhotoImage(self.imgArrayAux)
		self.mainImg.configure(image=self.img)
		self.frame.configure(width=int(self.imgOrig.width()*self.scaleZoom),height=int(self.imgOrig.height()*self.scaleZoom))
		self.canvas.configure(scrollregion=(0,0,int(self.imgOrig.width()*self.scaleZoom), int(self.imgOrig.height()*self.scaleZoom)))

#codigo a ser executado no inicio do programa
root = Tk()																														#cria uma nova interface do TkInter
root.title("Visao Computacional - Biblioteca")																					#define um titulo
Label(root, text="Selecione um arquivo de imagem '*.jpg' para continuar").pack(expand="yes", padx="10", pady="10")				#exibe uma Label de orientacao
Gui(root)																														#cria um novo objeto da classe Gui
root.mainloop()																													#inicia o loop da interface
print 'Finalzando...'
	
