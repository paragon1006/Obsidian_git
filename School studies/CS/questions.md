---
tags:
  - cs
  - code
---

``` python
age = int(input("what is your age"))
if age<13:
	print("price is $8")
elif (age>12 and age<18)==True:
	print("price is $10")
else:
	print("price is $12")
```
*** 
``` python
weight=float(input("enter your weight"))
print("Your weight in metric is",(weight*0.453592))
```
---
```python
monthsave = float(input("What is your monthly saving"))
interestrate = float(input("What is your interest rate"))
print("Your yearly savings are",(monthsave*12*(1+interestrate)))
```

``` PSEDUOCODE
FUNCTION MakeString(Count:INTEGER,Chr:CHAR) RETURN:STRING
	DECLARE Temp:STRING
	DECLARE J:INTEGER
	IF Count<1 THEN
		RETURN "ERROR 193I74"
	ELSE 
		FOR J <-- 0 TO Count
			Temp <-- Temp & Chr
		NEXT J
		RETURN Temp
ENDFUNCTION
```
---
``` PSEUDOCODE
FUNCTION Name(Ogstr:STRING,C_Rep:CHAR,C_New:CHAR) RETURN:STRING
	Len <-- LENGTH(Ogstr)
	N_Str
	FOR J <-- 0 TO Len
			IF Ogstr[J] = C_Rep THEN
				N_Str <-- N_Str & C_New
			ELSE
				N_Str <-- Ogstr[J]
	NEXT J 
	RETURN N_Str
```