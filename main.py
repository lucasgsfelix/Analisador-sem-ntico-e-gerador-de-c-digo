#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-
import unicodedata
import re
from arruma_entrada import *
from gramatica import *
from semantico import *
from geradorCodigo import *


arq_entrada = open('saida.txt', 'r')
saida_lexico = arq_entrada.read()
[tokens, ultima_linha] = trata_entrada(saida_lexico) # responsável pelo retorno da saída do léxico tratada e pelo primeiro caractere, onde o código começa 
i=0
j=0
linha = []
k=0
flag=0
while(1):
	if(flag==0):
		gerar_codigo('main', 0, 0)
		flag=1
	aux = tokens[i].split('\t') # isso é só pra descobrir qual é meu first
	if((aux[2]=='int')or(aux[2]=='float')or(aux[2]=='char')):
		i = declaracao(tokens, i)
	elif((aux[2]=='for')or(aux[2]=='while')): #tenho que retornar a posicao que termina a linha do for ou do while, a linha do } 
		i = repeticao(tokens, i)
	elif(aux[2]=='if'): # tenho que retornar a posicao que termina a linha do if, ou seja a linha que possui }
		i = condicao(tokens, i)
	elif(aux[3]=='1'):
		i = atribuicao(tokens, i)
	elif((aux[2]=='scanf')or(aux[2]=='printf')):
		i = comandos(tokens, i)
	else:
		erro(tokens, i, '')
	aux = tokens[i].split('\t')
	if(int(aux[0])==int(ultima_linha)):
		break
	i=i+1
	j=j+1
	k=k+1 # faz andar a linha
#verifica_tipos()




