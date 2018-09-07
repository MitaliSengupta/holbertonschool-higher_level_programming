# Javascript - Web JQuery

## Project takeaways

- How to select HTML elements in Javascript
- How to select HTML elements with jQuery
- What are differences between ID, class and tag name selectors
- How to modify an HTML element style
- How to get and update an HTML element content
- How to modify the DOM
- How to make a GET request with jQuery Ajax
- How to make a POST request with jQuery Ajax
- How to listen/bind to DOM events
- How to listen/bind to user events

## Tasks

- Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000):
  - You must use document.querySelector to select the HTML tag
  - You can’t use the jQuery API

- Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000):
  - You can’t use document.querySelector to select the HTML tag
  - You must use the jQuery API

- Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header:
  - You can’t use document.querySelector to select the HTML tag
  - You must use the jQuery API

- Write a Javascript script that adds the class red to the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header:
  - You can’t use document.querySelector to select the HTML tag
  - You must use the jQuery API

- Write a Javascript script that toggles the class of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#toggle_header:
  - The HEADER tag must always have one class: red or green, never both in the same time, never empty.
  - If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse.
  - You can’t use document.querySelector to select the HTML tag
  - You must use the jQuery API

- Write a Javascript script that adds a LI element to a list when the user clicks on the tag DIV#add_item:
  - The new element must be: <li>Item</li>
  - The new element must be added to UL.my_list
  - You can’t use document.querySelector to select the HTML tag
  - You must use the jQuery API

- Write a Javascript script that updates the text of the HTML tag HEADER to “New Header!!!” when the user clicks on DIV#update_header
  - You can’t use document.querySelector to select the HTML tag
  - You must use the jQuery API

- Write a Javascript script that fetches and replaces the name of this URL: https://swapi.co/api/people/5/?format=json
  - The name must be displayed in the HTML tag DIV#character
  - You can’t use document.querySelector to select the HTML tag
  - You must use the jQuery API

- Write a Javascript script that fetches and lists all movies title by using this URL: https://swapi.co/api/films/?format=json
  - All movie titles must be list in the HTML tag UL#list_movies
  - You can’t use document.querySelector to select the HTML tag
  - You must use the jQuery API

- Write a Javascript script that fetches and prints the San Francisco wind speed by using this URL: https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22San%20Francisco%2C%20CA%22)&format=json
  - The wind speed must be display in the HTML tag DIV#sf_wind_speed
  - You can’t use document.querySelector to select the HTML tag
  - You must use the jQuery API You script must be work when it imported from the HEAD tag
