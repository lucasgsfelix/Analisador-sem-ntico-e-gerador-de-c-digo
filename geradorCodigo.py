#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-
from semantico import *
s_usado = []
tokens_store = []
label_store = []
temps_store = []
arq_saida = open('codigo.asm', 'w')
def gerar_codigo(funcao, token, expressao):
	x = 0
	x = len(s_usado)
	x = x+1
	z = len(label_store)
	t = len(temps_store)
	if((funcao=='H')or(funcao=='identificadores')): #quer dizer que eu tenho minhas variaveis
		if any(token == i for i in tokens_store):
			i=0
			while(i<len(tokens_store)):
				if(tokens_store[i]==token):
					break
				i=i+1
			print '\tLOAD $S'+tokens_store[i-1]+','+token
			arq_saida.write('\tLOAD $S'+tokens_store[i-1]+','+token+'\n')
			print '\tSTORE t'+str(t)+' $S'+tokens_store[i-1]
			arq_saida.write('\tSTORE t'+str(t)+' $S'+tokens_store[i-1]+'\n')
		else:
			arq_saida.write('\tLOAD $S'+str(x)+','+token+'\n')
			print '\tLOAD $S'+str(x)+','+token
			arq_saida.write('\tSTORE t'+str(t)+',$S'+str(x)+'\n')
			print '\tSTORE t'+str(t)+',$S'+str(x)
	elif(funcao=='if'):
		if((expressao==0)):
			print '\tBEQ t'+str(tokens_store[len(tokens_store)-2])+',0, Label'+str(z)
			arq_saida.write('\tBEQ t'+str(tokens_store[len(tokens_store)-2])+',0, Label'+str(z)+'\n')
			label_store.append(z)
		#print 'JUMP Label1' #label o nome da função
		#print 'Label2'
		#print 'JUMP Label1'
		#print 'Label1'
	elif(funcao=='while'):# la --- load adress
		print 'Loop: '
		arq_saida.write('Loop: '+'\n')
	elif(funcao=='jump'):
		print '\tJUMP Label'+str(label_store[len(label_store)-1])
		arq_saida.write('\tJUMP Label'+str(label_store[len(label_store)-1])+'\n')
	elif(funcao=='fim loop'):
		print '\tj loop'
		arq_saida.write('\tj loop')
	elif(funcao=='Alinha'): # do alinha eu teria que passar as "duas variaveis que fazem a soma
		print '\tOR $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2)
		print '\tSTORE t'+str(t)+',$S'+str(x)
		arq_saida.write('\tOR $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2)+'\n')
		arq_saida.write('\tSTORE t'+str(t)+',$S'+str(x)+'\n')
		temps_store.append(t)
	elif(funcao=='Blinha'):
		print '\tAND $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2)
		print '\tSTORE t'+str(t)+',$S'+str(x)
		arq_saida.write('\tAND $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2)+'\n')
		arq_saida.write('\tSTORE t'+str(t)+',$S'+str(x)+'\n')
	elif(funcao=='else'):
		print '\tLabel'+str(label_store[len(label_store)-1])
	elif(funcao=='Dlinha'):
		if(token=='>'):
			print '\tSBT $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2) #bigger than 
			print '\tSTORE t'+str(t)+',$S'+str(x)
			arq_saida.write('\tSBT $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2)+'\n')
			arq_saida.write('\tSTORE t'+str(t)+',$S'+str(x)+'\n')
		else: # que no caso vai ser menor
			print '\tSLT $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2) #set smaller than
			print '\tSTORE t'+str(t)+',$S'+str(x)
			arq_saida.write('\tSLT $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2)+'\n')
			arq_saida.write('\tSTORE t'+str(t)+',$S'+str(x)+'\n')
	elif(funcao=='Elinha'):
		if(token=='=='):
			print '\tEQUAL $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2)
			print '\tSTORE t'+str(t)+',$S'+str(x)
			arq_saida.write('\tEQUAL $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2)+'\n')
			arq_saida.write('\tSTORE t'+str(t)+',$S'+str(x)+'\n')
		else:
			print '\tDIF $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2)
			print '\tSTORE t'+str(t)+',$S'+str(x)
			arq_saida.write('\tDIF $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2)+'\n')
			arq_saida.write('\tSTORE t'+str(t)+',$S'+str(x)+'\n')
	elif(funcao=='Flinha'):
		if(token=='+'):
			print '\tADD $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2)
			print '\tSTORE t'+str(t)+',$S'+str(x)
			arq_saida.write('\tADD $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2)+'\n')
			arq_saida.write('\tSTORE t'+str(t)+',$S'+str(x)+'\n')
		else:
			print '\tSUB $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2)
			print '\tSTORE t'+str(t)+',$S'+str(x)
			arq_saida.write('\tSUB $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2)+'\n')
			arq_saida.write('\tSTORE t'+str(t)+',$S'+str(x)+'\n')
	elif(funcao=='main'):
		print 'main:'
		arq_saida.write('main:'+'\n')
	elif(funcao=='Glinha'):
		if(token=='*'):
			print '\tMULT $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2)
			print '\tSTORE t'+str(t)+',$S'+str(x)
			arq_saida.write('\tMULT $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2)+'\n')
			arq_saida.write('\tSTORE t'+str(t)+',$S'+str(x)+'\n')
		else:
			print '\tDIV $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2)
			print '\tSTORE t'+str(t)+',$S'+str(x)
			arq_saida.write('\tDIV $S'+str(x)+',$S'+str(x+1)+',$S'+str(x+2)+'\n')
			arq_saida.write('\tSTORE t'+str(t)+',$S'+str(x)+'\n')

	s_usado.append(x)
	s_usado.sort()
	tokens_store.append(token)
	temps_store.append(t)

def retorna_regist(expressao):
	j=0
	tokens_expressao = []
	while(j<len(expressao)):
		if any(expressao[j] == i for i in tokens_store):
			i=0
			while(i<len(tokens_store)):
				if(tokens_store[i]==token):
					tokens_expressao.append(tokens_store[i-1])
				i=i+1
	return tokens_expressao

