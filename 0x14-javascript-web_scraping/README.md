# Javascript - Web scraping

## Project takeaways
- How to manipulate JSON data
- How to use request and fetch API
- How to read and write a file using fs module

## Tasks

- Write a script that reads and prints the content of a file.
  - The first argument is the file path
  - The content of the file must be read in utf-8
  - If an error occurred during the reading, print the error object

- Write a script that writes a string to a file.
  - The first argument is the file path
  - The second argument is the string to write
  - The content of the file must be written in utf-8
  - If an error occurred during while writing, print the error object

- Write a script that display the status code of a GET request.
  - The first argument is the URL to request (GET)
  - The status code must be printed like this: code: <status code>
  - You must use the module request

- Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
  - The first argument is the episode number
  - You must use the Star wars API with the endpoint http://swapi.co/api/films/:id
  - You must use the module request

- Write a script that prints the number of movies where the character “Wedge Antilles” is present.
  - The first argument is the API URL of the Star wars API: http://swapi.co/api/films/
  - Wedge Antilles is character ID 18
  - You must use the module request

- Write a script that gets the contents of a webpage and stores it in a file.
  - The first argument is the URL to request
  - The second argument the file path to store the body response
  - The file must be UTF-8 encoded
  - You must use the module request

- Write a script that computes the number of tasks completed by user id.
  - The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
  - You must use the module request

