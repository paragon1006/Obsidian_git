---
tags: []
---
#cs
# Index
| sr  | Topic                                                   | present |
| --- | ------------------------------------------------------- | ------- |
| 1   | [Datatypes and Structures](#Datatypes%20&%20Structures) | N       |
| 2   | Records                                                 | N       |
| 3   | [arrays (1d)](#Arrays)                                  | Y       |
| 4   | arrays (2d)                                             | N       |
| 5   | [Linear search](#Linear%20Search%20)                                           | N       |
| 6   | Bubble sort                                             | N       |
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
