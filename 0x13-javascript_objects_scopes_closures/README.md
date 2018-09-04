# Javascript - Objects, Scopes and Closures

## Project takeaways

- Why Javascript programming is amazing (don’t forget to tweet today, with the hashtag #javascriptisamazing :))
- How to create an object in Javascript
- What this means
- What undefined means
- Why the variable type and scope is important
- What is a closure
- What is a prototype
- How to inherit an object from another

## Tasks

- Write an empty class Rectangle that defines a rectangle:
  - You must use the class notation for defining your class

- Write a class Rectangle that defines a rectangle:
  - You must use the class notation for defining your class
  - The constructor must take 2 arguments w and h
  - Initialize the instance attribute width with the value of w
  - Initialize the instance attribute height with the value of h

- Write a class Rectangle that defines a rectangle:
  - You must use the class notation for defining your class
  - The constructor must take 2 arguments w and h
  - Initialize the instance attribute width with the value of w
  - Initialize the instance attribute height with the value of h
  - If w or h is equal to 0 or not a positive integer, create an empty object

- Write a class Rectangle that defines a rectangle:
  - You must use the class notation for defining your class
  - The constructor must take 2 arguments: w and h
  - Initialize the instance attribute width with the value of w
  - Initialize the instance attribute height with the value of h
  - If w or h is equal to 0 or not a positive integer, create an empty object
  - Create an instance method called print() that prints the rectangle using the character X

- Write a class Rectangle that defines a rectangle:
  - You must use the class notation for defining your class
  - The constructor must take 2 arguments: w and h
  - Initialize the instance attribute width with the value of w
  - Initialize the instance attribute height with the value of h
  - If w or h is equal to 0 or not a positive integer, create an empty object
  - Create an instance method called print() that prints the rectangle using the character X
  - Create an instance method called rotate() that exchanges the width and the height of the rectangle
  - Create an instance method called double() that multiples the width and the height of the rectangle by 2

- Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:
  - You must use the class notation for defining your class and extends
  - The constructor must take 1 argument: size
  - The constructor of Rectangle must be called (by using super())

- Write a class Square that defines a square and inherits from Square of 5-square.js:
  - You must use the class notation for defining your class and extends
  - Create an instance method called charPrint(c) that prints the rectangle using the character c
  - If c is undefined, use the character X

- Write a function that returns the number of occurrences in a list:
  - Prototype: exports.nbOccurences = function (list, searchElement)

- Write a function that returns the reversed version of a list:
  - Prototype: exports.esrever = function (list)
  - You are not allow to use the build-in method reverse

- Write a function that prints the number of argument already printed and the new argument value. (see example below)
  - Prototype: exports.logMe = function (item)
  - Output format: <number arguments already printed>: <current argument value>

- Write a function that converts a number from base 10 to another base passed as argument:
  - Prototype: exports.converter = function (base)
  - You are not allowed to import any file
  - You are not allowed to declare any new variable (var, let, etc..)

- Write a script that imports an array and computes a new array.
  - Your script must import list from the file 100-data.js
  - You must use a map. Tips
  - A new list must be created with each value equal to the value of the initial list, multipled by the index in the list

- Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
  - Your script must import dict from the file 101-data.js
  - In the new dictionary:
  - A key is a number of occurrences
  - A value is the list of user ids
  - Print the new dictionary at the end