# Elements of a recursive function:

## 1. What is your base case (think logically about what this would be*)
e.g. factorial.
```java
if (n == 1){
    return 1;
}
```

* A lot of the time, it will be
```java 
if (n == 0){
    return 0;
}
```

* A lot of the time for String questions this will be:
```java 
if (str.length() == 0){
    return str;
}
```
* Or if it is a string question but return type is int:
```java 
if (str.length() == 0){
    return 0;
}
```
but you must consider if this works logically. For factorial, if this was our base case,
every answer would be 0 (as we are multiplying) so the 0 base case will not work.

____

## 2. What is your reducer element?
If we are not progressing toward the base case, we will run into StackOverflowException (sort of like an infinite loop until we run out of memory on the 'stack'). For the factorial example:
```java
return n * factorial(n-1); 
```
our reducer in this case is n-1

To reduce by one digit at a time, like in the sumDigits coding bat question:
```java
return someFunction(n/10); 
```

* Often for String questions our reducer will be:
str.substring(1); // this function returns the string from the passed index to the end, e.g. 
```java
String h = "hello";
h.substring(1); // returns "ello"
```

substring() can also take 2 arguments, a start and stop (non inclusive) index.
____

## 3. What do you want to keep track of?
Usually we are returning *something* + (or * or whatever it may be) our function call. E.g. in factorial, we want to multiply each function call by the answer of the previous call. Our 'keeping track of' element is the is n * in our return statement:
```return n * factorial(n-1)```

* Often for numerical questions, this will involve a count, 
e.g. 
```java 
return 1 + functionName(n-1);
```
or 
```java
return n + functionName(n-1);
```

* Often for String questions, this will involve the charAt() function 
(charAt(0) returns the char at the index passed - in this case index 0)
e.g. 
```java
return str.charAt(0) + functionName(str.substring(1));
```
charAt(index) cannot be used to assign a new value to the given index of the string, i.e. we cannot say:
``` str.charAt(4) = 'h'```. See the below example for how this type of question should be approached:

```java
public String changeXY(String str) {
  if (str.length() == 0)
    return str;
  
  if (str.charAt(0) == 'x') 
    return 'y' + changeXY(str.substring(1));
    
  return str.charAt(0) + changeXY(str.substring(1));
}
```
___
#### Lastly: Don't forget to recall the function!

## Visualising the method call stack during recursion:

This image does a good job at visualising the stack going towards the base case before working back up to the result.
[source](https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/tutorial/).

![](https://he-s3.s3.amazonaws.com/media/uploads/0e2df2e.png)
