#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-
import unicodedata
import re
def trata_entrada(saida_lexico): # ordem é linha, coluna, token
	i=0
	saida_lexico = saida_lexico.split('\n')
	j=0
	identificadores = []
	op_log_ari = []
	palavras_reservadas = []
	comandos = []
	literais = []
	separadores = []
	atribuicao = []
	i=0
	while(i<len(saida_lexico)):
		if(saida_lexico[i]=='Identificadores: '): # id 1 
			i=i+1
			while(saida_lexico[i]!=''):
				identificadores.append(saida_lexico[i]+"\t1\t")
				i=i+1
		elif(saida_lexico[i]=='Operadores Lógicos e Aritméticos: '): # id 2
			i=i+1
			while(saida_lexico[i]!=''):
				op_log_ari.append(saida_lexico[i]+"\t2\t")
				i=i+1
		elif(saida_lexico[i]=='Palavras Reservadas: '): # id 0
			i=i+1 
			while(saida_lexico[i]!=''):
				palavras_reservadas.append(saida_lexico[i]+"\t0\t")
				i=i+1
		elif(saida_lexico[i]=='Comandos: '): # id 3 
			i=i+1
			while(saida_lexico[i]!=''):
				comandos.append(saida_lexico[i]+"\t3\t")
				i=i+1
		elif(saida_lexico[i]=='Literais: '): # id 4 
			i=i+1
			while(saida_lexico[i]!=''):
				literais.append(saida_lexico[i]+"\t4\t")
				i=i+1
		elif(saida_lexico[i]=='Separadores: '): # id 5
			i=i+1
			while(saida_lexico[i]!='Atribuição: '):
				separadores.append(saida_lexico[i]+"\t5\t")
				i=i+1
		if(saida_lexico[i]=='Atribuição: '): # id 6
			i=i+1
			while(saida_lexico[i]!=''):
				atribuicao.append(saida_lexico[i]+"\t6\t")
				i=i+1
		i=i+1
	separadores = retira_valores(separadores)
	[tokens, ultimo_valor] = junta_linhas(palavras_reservadas, identificadores, op_log_ari, comandos, literais, separadores, atribuicao)
	tokens = ordena_coluna(tokens, ultimo_valor)
	return tokens, ultimo_valor

def ordena_coluna(tokens1, ultimo_valor):
	i=0
	linha = []
	x = []
	j=0
	a = 0
	passo = 0
	soma = 0
	valor_antigo_i = 0
	while(soma<=int(ultimo_valor)):
		linha = []
		valor_antigo_i = i
		while(tokens1[i]!='\n'):
			aux = tokens1[i].split('\t')
			#aux[1] é minha coluna 
			linha.append(int(aux[1])) # que é a coluna
			i=i+1
		linha.sort() # ordenei os valores da linha 1
		k=0
		j = valor_antigo_i
		passo = j
		while(k<len(linha)):
			aux = tokens1[j].split('\t')
			if(aux[0]=='\n'):
				j=passo
			else:
				aux[1] = int(aux[1])
				if(aux[1]==linha[k]):
					x.append(tokens1[j])
					k=k+1
					j=j+1
				else:
					j=j+1
					if(j>i):
						j=passo
		#x.append('\n')
		j=j+1
		i=i+1
		soma = soma + 1
	return x

def junta_linhas(palavras_reservadas, identificadores, op_log_ari, comandos, literais, separadores, atribuicao):
	i=0
	j=0
	lista = []
	posicao = [0,0,0,0,0,0,0] #vetor que vai recebendo as ultima posicao de j
	flag = 0
	ultimo_valor = 0
	tokens = [palavras_reservadas, identificadores, op_log_ari, comandos, literais, separadores, atribuicao]
	while(i<len(tokens)):
		if(len(tokens[i])>0):	
			aux = tokens[i][len(tokens[i])-1]
			aux = aux.split('\t')
			if(aux[0]>ultimo_valor):
				ultimo_valor = aux[0]
			i=i+1
		else:
			i=i+1
	k=0 # representa a linha
	while(k<=int(ultimo_valor)):
		j = posicao[0]
		while(j<len(palavras_reservadas)):
			aux = palavras_reservadas[j].split('\t')
			aux[0] = int(aux[0])
			if(aux[0]==k):
				lista.append(palavras_reservadas[j])
				j=j+1
			else:
				posicao[0] = j
				break
		j = posicao[1]
		while(j<len(identificadores)):
			aux = identificadores[j].split('\t')
			aux[0] = int(aux[0])
			if(aux[0]==k):
				lista.append(identificadores[j])
				j=j+1
			else:
				posicao[1] = j
				break
		j = posicao[2]
		while(j<len(op_log_ari)):
			aux = op_log_ari[j].split('\t')
			aux[0] = int(aux[0])
			if(aux[0]==k):
				lista.append(op_log_ari[j])
				j=j+1
			else:
				posicao[2] = j
				break
		j = posicao[3]
		while(j<len(literais)):
			aux = literais[j].split('\t')
			aux[0] = int(aux[0])
			if(aux[0]==k):
				lista.append(literais[j])
				j=j+1
			else:
				posicao[3] = j
				break
		j = posicao[4]
		while(j<len(atribuicao)):
			aux = atribuicao[j].split('\t')
			aux[0] = int(aux[0])
			if(aux[0]==k):
				lista.append(atribuicao[j])
				j=j+1
			else:
				posicao[4] = j
				break
		j = posicao[5]
		while(j<len(comandos)):
			aux = comandos[j].split('\t')
			aux[0] = int(aux[0])
			if(aux[0]==k):
				lista.append(comandos[j])
				j=j+1
			else:
				posicao[5] = j
				break
		j = posicao[6]
		while(j<len(separadores)):
			aux = separadores[j].split('\t')
			aux[0] = int(aux[0])
			if(aux[0]==k):
				lista.append(separadores[j])
				j=j+1
			else:
				posicao[6] = j
				break
		lista.append('\n') #quer dizer que acabou a linha
		k=k+1
	i=0
	return lista, ultimo_valor


def retira_valores(separadores):
	i=0
	while(i<len(separadores)): #retira caractere ''
		if((separadores[i]=='')):
			separadores.pop(i)
		i=i+1
	i=0
	while(i<len(separadores)):
		if((separadores[i]=='\t5\t')):
			separadores.pop(i)
		i=i+1
	i=0
	while(i<len(separadores)): #retira valores que sejam iguais a -1
		j=0
		while(j<len(separadores[i])):
			if((separadores[i][j-1]=='-')and(separadores[i][j]=='1')):
				separadores.pop(i)
			j=j+1
		i=i+1
	return separadores


