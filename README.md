# Basic OpenCV
A small software that opens an image, convert to grayscale and negative. The software uses openCV and tkinter.

	Ps. Description in PT-BR
------------------------------------------------------------------------
#Descrição
Desenvolvido em Python v2.7.12 utilizando como base a biblioteca OpenCV v3.0.0 
Sistema Operacional: Ubuntu 16.04 LTS 

Software desenvolvido para disciplina de Visão Computacional, foram dedicadas em um intervalo de uma semana, cerca de 10 horas de desenvolvimento.

A implementação, na parte dos itens referentes ao tratamento da imagem foi realizada facilmente, porém quando foi implementada a parte do zoom foram encontradas dificuldades, principalemente na decisão de como realizar esta tarefa de maneira mais intuitiva para o usuário. Foram implementadas tres versões do trabalho, duas com interface e botões e 
outra sem interface que realizava as operações por comandos enviadospelo teclado, no final, foi decidido manter a ultima versao pois apresenta uma interface melhor elaborada para o usuario.

Foram utilizados como material de apoio o site de documentação do OpenCVque foi sugerido pelo professor (http://docs.opencv.org/ e https://opencv-python-tutroals.readthedocs.io/) além de foruns diversos disponibilizados pela internet para tirar duvidas especificas de programação em Python

	**Etapas de desenvolvimento:

		- Estudo da estrutura básica do Python.
		- Implementação da abertura da imagem.
			(utilizando um arquivo fixo)
		- Implementação da seleção do arquivo.
		- Implementação dos tratamentos da imagem.
		- Implementação do zoom.
		- Nova implentacao com interface intuitiva.

------------------------------------------------------------------------	
#Utilização
	- Instale (se não estiver instalado) a biblioteca "ImageTk"com o comando: "sudo apt-get install python-imaging-tk";
	- Altere o diretorio no terminal linux com o comando 'cd' até a pastaonde se encontra o arquivo atividadeBiblioteca.py;
 	- Execute o código atividadeBiblioteca_semInterface.py com o comando "python atividadeBiblioteca.py";
	- Selecione a Imagem desejada, clicando no botao "Abrir uma Imagem"; (a imagem selecionada ser do tipo '*.jpg')
	- Utilize os comandos relacionados abaixo para navegação.
------------------------------------------------------------------------		
#ESTRUTURA DE DIRETORIOS
	.
	|-- atividadeBiblioteca
	|	|-- atividadeBiblioteca.py (codigo em python)
	|	|-- README.txt (arquivo contendo informações do software)
	|	|-- teste.jpeg (imagem utilizada para testes)

------------------------------------------------------------------------
#Comandos
	Comando			Descrição
	Botão "Abrir		Abre um seletor de aruivos para seleção da imagem;
	uma imagem" 
	
	Botao +			Realiza a operação de zoom in;
	
	Botao - 		Realiza a operação de zoom out.
-------------------------------------------------------------------------
