# Web and Mobile Technology - Practice Paper 1

## Instructions
* **Time Allowed:** 1 Hour
* **Number of Questions:** 25 MCQs
* **Syllabus Coverage:** Lecture 1 to Lecture 5
* **Format:** Choose the single or multiple best options where specified.

---

### Question 1
Which of the following best describes the process of translating a human-readable domain name (like www.google.com) into an IP address?
A. DHCP assigning
B. IPv4 Routing
C. DNS Resolution
D. SSL Handshake

### Question 2
You are tasked with setting up a private network for your university staff that uses web technology but is securely accessible only by employees on-site. The most appropriate setup is a(n):
A. Internet
B. Intranet
C. Extranet
D. Wide Area Network

### Question 3
What is the correct protocol used for secure data communication between a web browser and a website?
A. FTP
B. HTTP
C. HTTPS
D. SMTP

### Question 4
A Uniform Resource Locator (URL) consists of multiple components. In the URL `https://developer.mozilla.org/en-US/learn`, what does `developer.mozilla.org` represent?
A. The Protocol
B. The Root Directory
C. The Domain Name
D. The Hyperlink

### Question 5
Which web concept refers to data being temporarily stored in a browser to speed up sequential visits to the same website?
A. Cookies
B. DOM Caching
C. Web Browser Caching
D. Sessions

---
### Question 6
Which is the correct HTML way of creating an image link that takes you to "contact.html" when clicked?
A. `<a src="contact.html"><img href="envelope.png"></a>`
B. `<a href="contact.html"><img src="envelope.png"></a>`
C. `<img href="contact.html" src="envelope.png">`
D. `<link href="contact.html"><img src="envelope.png"></link>`

### Question 7
Which of the following attributes is necessary for an input field if you want the form data to be identified by the server when submitted using POST?
A. `class`
B. `id`
C. `name`
D. `value`

### Question 8
What type of HTML list creates items marked with bullets by default?
A. `<ol>`
B. `<dl>`
C. `<ul>`
D. `<list>`

### Question 9
In HTML5, which tag is intended specifically to denote navigation links?
A. `<menu>`
B. `<nav>`
C. `<ul>`
D. `<header>`

### Question 10
If you want a cell in an HTML table to span across three columns, which attribute should you use?
A. `rowspan="3"`
B. `colspan="3"`
C. `span="3"`
D. `merge="3"`

---
### Question 11
What is the correct syntax to link an external CSS file named "main.css" inside an HTML document?
A. `<style src="main.css"></style>`
B. `<link rel="stylesheet" type="text/css" href="main.css">`
C. `<stylesheet>main.css</stylesheet>`
D. none of the mentioned

### Question 12
You have a CSS rule `.highlight { color: blue; }` and `#error { color: red; }`. 
For an element `<p class="highlight" id="error">Warning</p>`, what color will the text be?
A. Blue
B. Red
C. Purple
D. Black

### Question 13
```css
div { border: 1px solid black; padding: 10px; margin: 20px; }
```
Which property provides the space *between* the element's border and its content?
A. border
B. margin
C. padding
D. background

### Question 14
Which selector targets all `<p>` elements nested exactly one level deep inside a `<div>`?
A. `div p`
B. `div + p`
C. `div > p`
D. `div ~ p`

### Question 15
If an HTML page specifies red text via inline style, blue text via internal `<style>` block, and green text via external stylesheet. What color does the text become?
A. Red
B. Blue
C. Green
D. It depends on browser rendering.

---
### Question 16
What type of dialog box in JavaScript requires a user to click either "OK" or "Cancel", and returns a boolean value?
A. alert box
B. prompt box
C. confirm box
D. setup box

### Question 17
Select the incorrect statement associated with JavaScript.
A. Script execute without preliminary compilation.
B. It is a lightweight programming language.
C. Usually embedded directly into HTML pages.
D. Need computer processor for preliminary compilation.

### Question 18
```javascript
let count = 0;
while (count < 4) {
  if(count === 2) { count++; continue; }
  console.log(count);
  count++;
}
```
What is the output displayed in the console?
A. 0, 1, 2, 3
B. 0, 1, 3
C. 0, 1, 3, 4
D. Syntax Error

### Question 19
Which of the following array methods is used to add an element to the end of a JavaScript array?
A. `pop()`
B. `unshift()`
C. `push()`
D. `splice()`

### Question 20
```javascript
let fruits = ["Apple", "Mango", "Banana"];
fruits[1] = "Orange";
document.write(fruits.length);
```
What is printed to the browser screen?
A. 2
B. 3
C. 4
D. Apple, Orange, Banana

### Question 21
Consider the mouse moving onto an HTML element containing a link. Which event handler detects this action?
A. `onClick`
B. `onMouseOver`
C. `onMouseEnter`
D. Both B and C

### Question 22
```javascript
function calculate() {
   let x = "5";
   let y = 3;
   let z = x + y;
   console.log(z);
}
```
What does the calculation yield?
A. 8
B. "53"
C. NaN
D. Error

### Question 23
```html
<p id="demo">First</p>
<script>
  document.getElementById("demo").innerHTML = "Second";
</script>
```
What is visible on the web page?
A. First
B. Second
C. First and Second
D. Undefined

### Question 24
Which code correctly selects all elements with the class "btn"?
A. `document.querySelectorAll(".btn");`
B. `document.getElementsByClassName(".btn");`
C. `document.querySelector(".btn");`
D. `document.getElementById("btn");`

### Question 25
When attaching an event listener via `addEventListener`, what is best practice for attaching it to multiple elements retrieved via `querySelectorAll`?
A. Call `querySelectorAll(".btn").addEventListener("click", ...)` directly.
B. Iterate through the NodeList with a loop (like `.forEach()`) and apply `addEventListener` to each node.
C. `addEventListener` cannot be used with classes.
D. Query the document by ID instead.


<br><br><br><br>

---
## Answer Sheet
1. C
2. B
3. C
4. C
5. C
6. B
7. C
8. C
9. B
10. B
11. B
12. B (ID selector has higher specificity)
13. C
14. C
15. A (Inline styles typically have highest specificity)
16. C
17. D
18. B
19. C
20. B
21. D
22. B
23. B
24. A
25. B
