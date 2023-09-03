#cs #code 
# Index
| sr  | Topic                                                     | Fin |
| --- | --------------------------------------------------------- | --- |
| 1   | [Constants vs Variables](#Constants-vs-Variables)         | Y   |
| 2   | [Library Routines (Strings)](#Library-Routines(Strings))  | Y   |
| 3   | [Library Routines (Integer)](#Library-Routines(Integers)) | N   |
| 4   | [IF ELSE]()                                               | Y   |
| 5   | [Loops (For)]()                                           | Y   |
| 6   | [Loops (repeat)]                                          | Y   |
| 7   | Loops (while)                                             | Y   |
| 8   | [Procedures (default)](Procedures(Default))       | N   |
| 9   | Procedures (parameterized)                                | N   |
| 10  | Functions (default)                                       | N   |
| 11  | Functions (parameterized)                                 | N   |
| 12  | Functions (written)                                       | N   |
# Constants-vs-Variables
#### ***Variable***s 
- It refers to a name assigned to a memory location that can hold a value.
- Values stored in variable can change through the execution of the program
#### ***Constants***
It refers to a name assigned to a memory location that can hold a value.
- Values stored in constant remain same throughout execution of program
# Library-Routines(Strings)
##### ***LENGTH(STRING)***
It allows to find the length of the string
``` PSEUDOCODE
a <-- "HELLO"
OUTPUT LENGTH(s)
'''Out
	5
'''
```
##### RIGHT(String,{Number of char})
``` PSEUDOCODE
a <-- "Hello"
OUTPUT RIGHT(a,3)
OUTPUT RIGHT("bye",1)
''' OUT
	llo
	e
'''
```
##### LEFT(String,{Number of char})
``` PSEUDOCODE
a <-- "Hello"
OUTPUT LEFT(a,3)
OUTPUT LEFT("bye",1)
''' OUT
	Hel
	b
'''
```
##### MID(String,{Index},{Number of Characters})
``` PSEUDOCODE
a <-- "Hello"
OUTPUT MID(a,1,2)
OUTPUT MID("bye",2,1)
''' OUT
	He
	y
'''
```
# Library-Routines(Integers)
##### ***INT(Value)***
``` PSEUDOCODE
a <-- 5.2
OUTPUT INT(a)
''' OUT
	5
'''
```
##### ***MOD(Dividend, Divisor)***
``` PSEUDOCODE
OUTPUT MOD(13,2)
''' OUT
	1
'''
```
##### ***DIV(Dividend, Divisor)***
``` PSEUDOCODE
OUTPUT DIV(13,2)
''' OUT
	6
'''
```
# Procedures(Default)

