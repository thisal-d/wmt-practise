# Web and Mobile Technology - Practice Paper 2

## Instructions
* **Time Allowed:** 1 Hour
* **Number of Questions:** 25 MCQs
* **Syllabus Coverage:** Lecture 1 to Lecture 5
* **Format:** Choose the single or multiple best options where specified.

---

### Question 1
Which of the following components uniquely identifies a machine on the Internet?
A. MAC Address
B. IP Address
C. Browser Name
D. Subnet Mask

### Question 2
DNS translates:
A. MAC addresses to IP addresses.
B. Domain names to Host names.
C. Domain names to IP addresses.
D. IP addresses to Domain names.

### Question 3
An organization uses a subset of its internal network and provides restricted access to external suppliers. This is known as:
A. Internet
B. Intranet
C. Extranet
D. Wide Area Network

### Question 4
In the HTML structure, which of the following tags is used to place metadata, CSS links, and page title?
A. `<body>`
B. `<footer>`
C. `<head>`
D. `<section>`

### Question 5
Which tag is correctly enclosed to create a table row in HTML?
A. `<td>`
B. `<table>`
C. `<th>`
D. `<tr>`

---
### Question 6
You have the following HTML structure:
```html
<form method="get" action="/submit">
  <input type="text" name="username">
  <button type="submit">Submit</button>
</form>
```
How is the form data transmitted?
A. In the HTTP POST request body.
B. Attached to the URL as query parameters.
C. Hidden in cookies.
D. Securely without exposure.

### Question 7
To make a hyperlink open in a new browser tab or window, what attribute and value pair should be used?
A. `href="_blank"`
B. `target="_new"`
C. `target="_blank"`
D. `open="new"`

### Question 8
```css
#container p { color: #333; }
p.text-muted { color: #999; }
```
In the above CSS, which selector has the highest specificity?
A. `#container p`
B. `p.text-muted`
C. Both have equal specificity
D. Neither

### Question 9
What does the "C" in CSS stand for?
A. Cascading
B. Creative
C. Computer
D. Colorful

### Question 10
If you want to remove the underline from an HTML hyperlink using CSS, which rule should you apply?
A. `text-decoration: no-underline;`
B. `text-decoration: none;`
C. `font-style: un-italic;`
D. `font-weight: normal;`

---
### Question 11
Consider the following HTML & CSS:
```html
<style>
 .box { width: 100px; padding: 10px; border: 5px solid black; margin: 5px; }
</style>
<div class="box"></div>
```
Assuming standard `box-sizing: content-box`, what is the total horizontal width taken up by the browser for this element?
A. 100px
B. 120px
C. 130px
D. 140px

### Question 12
You are using JavaScript inside your HTML page. A correct way to link an external JS file is:
A. `<script src="script.js"></script>`
B. `<script href="script.js"></script>`
C. `<link rel="javascript" src="script.js">`
D. `<js src="script.js" />`

### Question 13
```javascript
let num = 10;
if(num == "10") {
   console.log("Equal");
} else {
   console.log("Not Equal");
}
```
The console will display:
A. Equal
B. Not Equal
C. Error
D. Nothing

### Question 14
Which popup box method is used to allow a user to type in a value?
A. `window.alert()`
B. `window.prompt()`
C. `window.confirm()`
D. `window.input()`

### Question 15
```html
<!DOCTYPE html>
<html>
<body>
<script>
function checkCars() {
  var cars = ["Honda", "Toyota", "Ford"];
  var result = "";
  for (var i = 0; i < cars.length; i++) {
    if (cars[i] == "Toyota") {
      continue;
    }
    result += cars[i] + " ";
  }
  document.write(result);
}
checkCars();
</script>
</body>
</html>
```
What is the output?
A. Honda Toyota Ford
B. Honda Ford
C. Toyota Ford
D. Honda

---
### Question 16
What happens when you declare a variable inside a JavaScript function using `var`?
A. It becomes a global variable.
B. It becomes a block-scoped variable.
C. It becomes a function-scoped variable scoped only to that function.
D. It is inaccessible.

### Question 17
Select the correct event handler when an input field loses focus.
A. `onchange`
B. `onfocus`
C. `onblur`
D. `onfocusexit`

### Question 18
```javascript
let elements = document.getElementsByTagName("p");
for(let i=0; i< elements.length; i++) {
   elements[i].style.backgroundColor = "yellow";
}
```
What does this JavaScript code snippet accomplish?
A. Selects exactly one `<p>` element and changes its background to yellow.
B. Selects all `<p>` elements and causes an error because NodeList cannot be modified.
C. Changes the background color of every `<p>` element on the page to yellow.
D. Creates new `<p>` elements painted yellow.

### Question 19
Which function is used to convert a string `"15.5"` to a floating-point number in JavaScript?
A. `Number.parseFloat()`
B. `parseInt()`
C. `toString()`
D. `typeof`

### Question 20
To modify the text content strictly (ignoring HTML tags embedded within) of an element with `id="heading"`, the best property to use is:
A. `innerHTML`
B. `outerHTML`
C. `textContent`
D. `value`

---
### Question 21
```javascript
let x = [10, 20, 30];
x.push(40);
x.pop();
console.log(x.length);
```
What is printed?
A. 3
B. 4
C. 5
D. 2

### Question 22
A very large Web site may be spread over a number of ___ in different geographic locations.
A. Workstations
B. Servers
C. Hard drives
D. Routers

### Question 23
When you try to use `document.getElementById('missing')` where no element has the id "missing", what is the returned value?
A. `0`
B. `false`
C. `null`
D. `undefined`

### Question 24
In JavaScript, single-line comments begin with:
A. `/*`
B. `<--`
C. `//`
D. `#`

### Question 25
```html
<div class="test">Item 1</div>
<div class="test">Item 2</div>
<script>
  document.querySelector(".test").style.color = "red";
</script>
```
What occurs?
A. Both Items 1 and 2 become red.
B. Only Item 1 becomes red.
C. Only Item 2 becomes red.
D. An error is thrown.


<br><br><br><br>

---
## Answer Sheet
1. B
2. C
3. C
4. C
5. D
6. B
7. C
8. A (ID carries a weight of 100, class is 10)
9. A
10. B
11. D (100 width + 10L+10R padding + 5L+5R border = 130px visible. With margins it's 140px total horizontal space)
12. A
13. A
14. B
15. B
16. C
17. C
18. C
19. A
20. C
21. A
22. B
23. C
24. C
25. B (`querySelector` returns only the first matched element)
