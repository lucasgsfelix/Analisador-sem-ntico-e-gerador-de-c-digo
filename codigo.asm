main:
	LOAD $S2,a
	STORE t1,$S2
	LOAD $S3,i
	STORE t2,$S3
Loop: 
	LOAD $Sa,i
	STORE t4 $Sa
	LOAD $S6,0
	STORE t5,$S6
	EQUAL $S7,$S8,$S9
	STORE t6,$S7
	BEQ t0,0, Label0
	JUMP Label0
	j loop