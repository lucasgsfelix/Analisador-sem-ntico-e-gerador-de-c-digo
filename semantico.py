#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-
import re
lista_tipo_id = [] #lista que írá receber a variavel e o identificador
linha_coluna_lista = [] #lista que irá receber linha e coluna dos identificadores e vars
lista_repetidos = [] #coloco só a posição 
lista_repetidos_posicao = []
express_tokens = [] # a pergunta que não quer calar, a= b+c (isso tudo é uma expressão) ou apenas b+c
def salva_var_tipo(tokens, i, local): # guarda o tipo da variavel e identificador dela, ex: int a 
	if(local==0): # quer dizer que a declaração é única
		aux = tokens[i].split('\t')
		lista_tipo_id.append(aux[2]) #adicionei o tipo da var
		linha_coluna(tokens, i)
		i=i+1
		aux = tokens[i].split('\t')
		lista_tipo_id.append(aux[2]) #adicionei o identificador que é definido
		linha_coluna(tokens, i)
	elif(local==1): #agora eu tenho a declaração multipla
		aux = tokens[i].split('\t')
		k = i # onde está o token original
		while(aux[2]!=';'):
			aux = tokens[k].split('\t')
			if(k==0):
				break;
			k=k-1 # procurando o tipo da variavel
		if(k>0):
			k=k+1
		aux = tokens[k].split('\t')
		lista_tipo_id.append(aux[2])
		linha_coluna(tokens, i)
		aux = tokens[i].split('\t')
		lista_tipo_id.append(aux[2])
		linha_coluna(tokens, i)
	
	verifica_elementos(tokens)


def linha_coluna(tokens, i):
	aux = tokens[i].split('\t')
	linha_coluna_lista.append(aux[0]) #adicionei a linha
	linha_coluna_lista.append(aux[1]) #adicionei a coluna

def verifica_elementos(tokens):
	k=1
	l=1
	aux_2 = 0
	if(len(lista_tipo_id)>2): # o que quer dizer temos mais de 1 elemento
		while(k<len(lista_tipo_id)):
			l=1
			while(l<len(lista_tipo_id)):
				if(l!=k): #para não comparar com ele mesmo
					if((len(lista_repetidos)==0)or all (lista_tipo_id[k] != i for i in lista_repetidos)):
						if(lista_tipo_id[l]==lista_tipo_id[k]):
							print 'Existe uma multipla declaração do token '+ lista_tipo_id[k] +'!'
							p = k*2
							print 'E o erro está na linha: ', linha_coluna_lista[p], ' coluna ', linha_coluna_lista[p+1]
							lista_repetidos.append(lista_tipo_id[k])
							#linha_coluna_repetidos(lista_tipo_id[k], tokens)
							# 0 a 3 é a posição de um id e de um identificador, ou seja 
							# 0 a 3 --> primeiro token
							# 4 a 7 --> segundo token ... assim por diante
				l=l+2
			k=k+2
def verifica_tipos(expressao, linha):

	operadores = ['+', '-', '>', '<', '=', '/', '*', '||', '&&', '<=', '>=', '(', ')', '==']
	nova_expressao = [] #ao fim essa função vai me retornar os tipos das variaveis que eu estou fazendo operação
	if(len(expressao)>0):
		if((re.match(r'^[0-9]+$', expressao[0]))and(expressao[1]==';')):
			i=0
		else:
			i=0
			while(i<len(expressao)):
				if any (expressao[i] == j for j in lista_tipo_id):
					j=0
					while(j<len(lista_tipo_id)):
						if(expressao[i]==lista_tipo_id[j]):
							aux = j
							break
						j=j+1
					nova_expressao.append(lista_tipo_id[aux-1])
				elif any (expressao[i] == j for j in operadores): #adiciona os operadores
					nova_expressao.append(expressao[i])
				else:
					if not (re.match(r'^[0-9]+$', expressao[i])):
						if any (expressao[i] != j for j in operadores):
							print 'Token '+expressao[i]+', na linha '+linha+' utilizado antes da declaração ! Declare-o !'
							exit()
						
				i=i+1
	verifica_expressao(nova_expressao, linha)
def verifica_expressao(nova_expressao, linha):
	i=0
	# +---char + char = char, int + int  =  int, float + float = float, int + float = float, resto inválido
	# *---char não tem multiplicação, int * int = int, float * float = float, int * float = float, resto inválido
	# /---char não possui divisão, int / int = float, float / float = float, float / int (vice versa) = float
	if(len(nova_expressao)!=0):
		if((nova_expressao[1]==';')or(re.match(r'^[0-9]+$', nova_expressao[0]))):
			i=0
		elif((nova_expressao[0]=='int')or(re.match(r'^[0-9]+$', nova_expressao[0]))):
			#pode ser int ou um numeral
			i=0
			while(i<len(nova_expressao)):
				if(nova_expressao[i]=='char'):
					print 'Erro: Você está tentando fazer uma operação entre um int e um char na linha '+linha+' e isso não é permitido, reformule a expressão !!'
					break
				elif(nova_expressao[i]=='float'):
					print 'Warning: Você está tentando somar um int e um float na linha '+linha+' ! O resultado retornado será um int !'
					break
				i=i+1
		elif(nova_expressao[0]=='float'):
			i=0
			while(i<len(nova_expressao)):
				if(nova_expressao[i]=='char'):
					print 'Erro: Você está tentando fazer uma operação entre um int e um char na linha '+linha+', e isso não é permitido, mude o tipo de sua variavel !!'
					break
				i=i+1
		elif(nova_expressao[0]=='char'):
			i=0
			while(i<len(nova_expressao)):
				if((nova_expressao[i]!='+')and(nova_expressao[i]!='int')and(nova_expressao[i]!='char')and(nova_expressao[i]!='(')and(nova_expressao[i]!=')')and(nova_expressao[i]!='=')):
					print 'Erro: A operação que você está tentando na linha '+linha+' é inválida, reformule a expressão !'
					break
				elif((nova_expressao[i]=='int')or(nova_expressao[i]=='float')):
					print 'Warning: Você está fazendo uma operação entre caracteres e números na linha'+linha+', isso vai resultador na concatenção dos mesmos!'
					break
				i=i+1

					

