# Javascript - Warm up

## Project takeaways
   - Why Javascript programming is amazing (don’t forget to tweet today, with the hashtag #javascriptisamazing :))
   - How to run a Javascript script
   - How to create variables and constants
   - What are differences between var, const and let
   - What are all the data types available in Javascript
   - How to use the if, if ... else statements
   - How to use comments
   - How to affect values to variables
   - How to use while and for loops
   - How to use break and continue statements
   - What is a function and how do you use functions
   - What does return a function that does not use any return statement
   - Scope of variables
   - What are the arithmetic operators and how to use them
   - How to manipulate dictionary
   - How to import a file

## Tasks

- First constant, first print
  - Write a script that prints “Javascript is amazing”:
    - You must create a constant variable called myVar with the value “Javascript is amazing”
    - You must use console.log(...) to print all output
    - You are not allowed to use var

- 3 languages
  - Write a script that prints 3 lines:
    - The first line: “C is fun”
    - The second line: “Python is cool”
    - The third line: “Javascript is amazing”
    - You must use console.log(...) to print all output
    - You are not allowed to use var

- Arguments
  - Write a script that prints a message depending of the number of arguments passed:
    - If no arguments are passed to the script, print “No argument”
    - If only one argument is passed to the script, print “Argument found”
    - Otherwise, print “Arguments found”
    - You must use console.log(...) to print all output
    - You are not allowed to use var

- Value of my argument
  - Write a script that prints the first argument passed to it:
    - If no arguments are passed to the script, print “No argument”
    - You must use console.log(...) to print all output
    - You are not allowed to use var
    - You are not allowed to use length

- Create a sentence
  - Write a script that prints two arguments passed to it, in the following format: “ is ”
    - You must use console.log(...) to print all output
    - You are not allowed to use var

- An Integer
  - Write a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
    - If the argument can’t be converted to an integer, print “Not a number”
    - You must use console.log(...) to print all output
    - You are not allowed to use var
    - You are not allowed to use try/catch

- Loop to languages
  - Write a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
    - The first line: “C is fun”
    - The second line: “Python is cool”
    - The third line: “Javascript is amazing”
    - You must use console.log(...) to print all output
    - You are not allowed to use var
    - You are not allowed to use any if/else statement
    - You can use only one console.log
    - You must use a loop (while, for, etc.)

- I love C
  - Write a script that prints x times “C is fun”
    - Where x is the first argument of the script
    - If the first argument can’t be converted to an integer, print “Missing number of occurrences”
    - You must use console.log(...) to print all output
    - You are not allowed to use var
    - You can use only two console.log
    - You must use a loop (while, for, etc.)

- Square
  - Write a script that prints a square
    - The first argument is the size of the square
    - If the first argument can’t be converted to an integer, print “Missing size”
    - You must use the character X to print the square
    - You must use console.log(...) to print all output
    - You are not allowed to use var
    - You must use a loop (while, for, etc.)

-  Add
   - Write a script that prints the addition of 2 integers
     - The first argument is the first integer
     - The second argument is the second integer
     - You have to define a function with this prototype: function add(a, b)
     - You must use console.log(...) to print all output
     - You are not allowed to use var

- Factorial
  - Write a script that computes and prints a factorial
    - The first argument is integer (argument can be cast as integer) used for computing the factorial
    - Factorial of NaN is 1
    - You must do it recursively
    - You must use a function
    - You must use console.log(...) to print all output
    - You are not allowed to use var

- Second biggest!
  - Write a script that searches the second biggest integer in the list of arguments.
    - You can assume all arguments can be converted to integer
    - If no argument passed, print 0
    - If the number of arguments is 1, print 0
    - You must use console.log(...) to print all output
    - You are not allowed to use var

- Object
  - Update this script to replace the value 12 with 89:
  - You are not allowed to use var

- Add file
  - Write a function that returns the addition of 2 integers.
    - The function must be visible from outside
    - The name of the function must be add
    - You are not allowed to use var

- Const or not const
  - Write a file that modifies the value of myVar to 333
  - #!/usr/bin/node
    myVar = 89;
    require('./100-let_me_const')
    console.log(myVar);

- Call me Moby
  - Write a function that executes x times a function.
    - The function must be visible from outside
    - Prototype: function (x, theFunction)
    - You are not allowed to use var

- Add me maybe
  - Write a function that increments and calls a function.
    - The function must be visible from outside
    - Prototype: function (number, theFunction)
    - You are not allowed to use var

-  Increment object
   - Update this script by adding a new function incr that increments the integer value.
     - You are not allowed to use var
