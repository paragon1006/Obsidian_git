---
tags: []
---
#cs
# Index
| sr  | Topic                                                   | present |
| --- | ------------------------------------------------------- | ------- |
| 1   | [Datatypes and Structures](#Datatypes%20&%20Structures) | N       |
| 2   | [Records](#Records)                                                 | N       |
| 3   | [arrays (1d)](#Arrays)                                  | Y       |
| 4   | arrays (2d)                                             | N       |
| 5   | [Linear search](#Linear%20Search%20)                                           | N       |
| 6   | [Bubble sort](#Bubble%20Sort)                                             | N       |
| 7   | Files (read)                                            | N       |
| 8   | Files (write)                                           | N       |
| 9   | ADT (stack)                                             | N       |
| 10  | ADT (queue)                                             | N       |
| 11  | ADT (linkless)                                          | N       |

# Arrays 
Array:- User defined data type that allows the user to store multiple values.
``` PSEUDOCODE
DECLARE {Name}:ARRAY[{Start}:{End}] OF {Datatype}
```

>[!question]- WAP to store 10 marks in an array and print the total of all marks
>```PSEUDOCODDE
>DECLARE Marks:ARRAY[0:9] OF INTEGER
>Total <-- 0
>FOR Counter<-- 0 TO 9
>	INPUT Marks[Counter]
>	Total <-- Total + Counter
>Next Counter
>OUTPUT Marks
>OUTPUT Total
>```
>---
# Linear Search
###### Setting up array
``` PSEUDOCODE
Position <- -1
Found <- False
OUTPUT "Enter Marks"
FOR Count <- 0 TO 3
	INPUT Marks[Count]
NEXT Count
```
---
###### Linear search code
``` PSEUDOCODE
OUTPUT "Enter the search value"
INPUT Search
FOR Count <- 0 to 3
	IF Marks[Count]=Search
		FOUND <- TRUE
		Position <- Count
	ENDIF
NEXT Count
IF Found = TRUE THEN
	OUTPUT "Value is at position", position
ELSE 
	OUTPUT "Value not found"
ENDIF
```
---
# Bubble sort
#### Components
- Swapping of adjacent values
- FOR Loops (2)
- IF 
- Swapping
	```
	t = a
	a = b
	b = t
	```
#### Bubble sort code
```PSEUDOCODE
//Let's make an array to store the data//
FOR Count <-- 0 TO 3
	OUTPUT "Enter a value"
	INPUT Marks[Count]
NEXT Count

//Bubblesort//
FOR I <-- 0 TO 3
	FOR I <-- 0 TO 3
		IF Marks[i]>Marks[j] THEN
			Temp <-- Marks[i]
			Marks[i] <-- Marks[j]
			Marks[j] <-- Temp
		ENDIF
	NEXT j
NEXT i
OUTPUT Marks
```
#### Bubble sort python
>[!tip]- To write this in python...
>``` python
>marks = [18,12,14,11,17,16,15,13]
>
>print(marks)
>
>for i in range(0,7):
>	for j in range(0,7):
>		if marks[i]>marks[j]:
>			temp = marks[i]
>			marks[i] = marks[j]
>			marks[j] = temp 
>print("the list is",marks)
>
>```

# Records
1. It refers to a composite datatype made by the collection of multiple values of different datatypes.
2. A record will contain a fixed number of items.
3. A composite datatype must be defined before it can be used

***Syntax:***
	TYPE
	NAME
		{DECLARATIONS}
		{DECLARATIONS}
	ENDTYPE
	DECLARE NAME:RecordName

> [!question]- WAP a program to store the names details of books by using a record
> ``` PSEUDOCODE 
> TYPE 
> Book
> 	DECALRE title: STRING
> 	DECLARE cost: INTEGER
> ENDTYPE
> 
> DECLARE a:Book
> a.title <-- "Harry Potter"
> a.cost <-- 20
> 
> OUTPUT "title", a.title, "$", a.cost
> ```