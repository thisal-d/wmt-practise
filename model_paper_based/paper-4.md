# Web and Mobile Technology - Practice Paper 4 (Advanced Tracing & Logic)

## Instructions
* **Time Allowed:** 1 Hour
* **Number of Questions:** 25 MCQs
* **Syllabus Coverage:** Lecture 1 to Lecture 5
* **Format:** Choose the single or multiple best options where specified. This paper focuses heavily on interpreting code blocks.

---

### Question 1
```html
<style>
  div p.text { color: red; }
  #box p { color: blue; }
  p { color: green !important; }
</style>
<div id="box">
  <p class="text" style="color: yellow;">Exam Test</p>
</div>
```
Based on CSS specificity and rules, what color will the text "Exam Test" appear as?
A. Red
B. Blue
C. Green
D. Yellow

### Question 2
```css
.card { 
  width: 200px; 
  padding: 10px; 
  border: 5px solid black; 
  margin: 10px; 
}
```
Assuming the default browser behavior (`box-sizing: content-box`), what is the total horizontal pixel width this element occupies on the screen (including its margins)?
A. 200px
B. 220px
C. 230px
D. 250px

### Question 3
```javascript
let x = "5" + 2 + 3;
let y = 5 + 2 + "3";
console.log(x, y);
```
What will be traced in the console?
A. "55", "73"
B. "523", "73"
C. "10", "10"
D. 10, 10

### Question 4
```javascript
let counter = 0;
for(let i = 0; i < 5; i++) {
   if(i === 2) continue;
   if(i === 4) break;
   counter += i;
}
console.log(counter);
```
Select the correct output value for `counter`.
A. 1
B. 3
C. 4
D. 6

### Question 5
```javascript
let items = document.getElementsByClassName("item");
for(let i = 0; i < items.length; i++) {
  items[i].innerHTML = "Value: " + i;
}
```
If your HTML contains exactly 3 elements with the class `item`, what will be the innerHTML of the second element after this script runs?
A. Value: 0
B. Value: 1
C. Value: 2
D. Value: 3

---

### Question 6
```javascript
let arr = [10, 20, 30, 40];
arr.push(50);
arr.shift();
console.log(arr[1]);
```
What value is printed?
A. 10
B. 20
C. 30
D. 40

### Question 7
```css
div + p { 
  background-color: red; 
}
```
Which HTML element(s) does this selector target?
A. All `<p>` elements located anywhere inside a `<div>`.
B. Only the first `<p>` element directly following a `<div>`.
C. All `<p>` elements that are immediate siblings positioned immediately after any `<div>`.
D. Both `<div>` and `<p>` elements simultaneously.

### Question 8
```javascript
var a = 1;
function test() {
   if(true) {
      var a = 2;
      let b = 3;
   }
   console.log(a);
}
test();
```
What is the correct console output?
A. 1
B. 2
C. undefined
D. A reference error occurs

### Question 9
```javascript
let val1 = (0 == "0");
let val2 = (0 === "0");
console.log(val1, val2);
```
What will be output to the console?
A. true true
B. false false
C. false true
D. true false

### Question 10
```html
<p class="para">Item 1</p>
<p class="para">Item 2</p>
<script>
  let paras = document.querySelectorAll(".para");
  paras[0].classList.add("hidden");
  console.log(paras.length);
</script>
```
What will the console output?
A. 1
B. 2
C. 0
D. Error: .classList is undefined

---

### Question 11
What represents the proper method for placing an image on an HTML page so that it acts as a clickable hyperlink?
A. `<a href="page.html"><img src="logo.jpg"></a>`
B. `<img href="page.html" src="logo.jpg">`
C. `<a link="page.html"><img file="logo.jpg"></a>`
D. `<link href="page.html" image="logo.jpg">`

### Question 12
```javascript
let x = 0;
while (x < 3) {
   x++;
}
console.log(x);
```
What is printed?
A. 1
B. 2
C. 3
D. 4

### Question 13
```html
<a href="link.html" style="text-decoration:none;">
  <span style="color:red; text-decoration:underline;">Click Here</span>
</a>
```
Visually, how will "Click Here" appear?
A. Red and without an underline.
B. Default link blue, but with an underline.
C. Red and with an underline.
D. Purple with an underline.

### Question 14
```javascript
let nums = [2, 4, 6];
let result = 0;
for(let i = 0; i < nums.length; i++) {
  result += nums[i] % 3;
}
console.log(result);
```
What value does `result` hold?
A. 0
B. 2
C. 3
D. 12

### Question 15
```javascript
let str = "Hello";
switch(str) {
   case "hello": console.log("One");
   case "Hello": console.log("Two");
   case "HELLO": console.log("Three"); break;
   default: console.log("Four");
}
```
What is the console output? (Careful with syntax and casing)
A. Two
B. Two, next line Three
C. One, Two, Three
D. Four

---

### Question 16
If you want to create an internal CSS style specifically strictly for an HTML element with the id `"header"`, which character precedes the identifier in the `<style>` block?
A. `.`
B. `#`
C. `*`
D. `@`

### Question 17
```javascript
function greet(name) {
   return "Welcome " + name;
}
console.log(greet());
```
What happens when this executes?
A. "Welcome undefined" is printed.
B. "Welcome null" is printed.
C. "Welcome " is printed.
D. A SyntaxError is thrown because the argument is missing.

### Question 18
Which JavaScript operator is used to assign a value to a variable, and which checks for strict equality?
A. `=` assigns, `==` checks strict equality.
B. `==` assigns, `===` checks strict equality.
C. `=` assigns, `===` checks strict equality.
D. `===` assigns, `==` checks strict equality.

### Question 19
If you intend to use JavaScript to alter the visible text content of a `<h2>` tag, but do NOT want any HTML tags within your string to be parsed as code, which property is the safest to manipulate?
A. `innerHTML`
B. `textContent`
C. `value`
D. `outerHTML`

### Question 20
```html
<span style="width: 200px; height: 100px;">Block</span>
```
By default, what are the actual dimensions occupied by this `<span>`?
A. 200px length by 100px height.
B. It scales to exactly 100% of the display.
C. Its dimensions only wrap its interior text size ("Block") ignoring the fixed width/height.
D. It disappears.

---

### Question 21
```javascript
let nodes = document.getElementsByTagName("p");
nodes[1].style.color = "blue";
```
What happens if there is only *one* `<p>` element on the webpage?
A. The single element turns blue.
B. The script throws an error such as `Cannot read property 'style' of undefined`.
C. The script fails silently but the page loads.
D. Multiple `<p>` elements are generated automatically.

### Question 22
```html
<button id="submitBtn">Send</button>
<script>
  let count = 0;
  let btn = document.getElementById("submitBtn");
  btn.onclick = function() { count++; };
  btn.onclick = function() { count += 2; };
</script>
```
If the user clicks the button once, what is the value of `count`?
A. 1
B. 2
C. 3
D. Error due to duplicate event assignment.

### Question 23
A user is submitting a contact form. Which HTTP method hides the form data from the URL, generally making it more appropriate for sensitive information?
A. SEND
B. GET
C. POST
D. PUSH

### Question 24
```javascript
let message = "JavaScript";
console.log(message.length);
```
What is printed?
A. 9
B. 10
C. 11
D. undefined

### Question 25
```javascript
let heading = document.querySelector("#main-title");
heading.style.backgroundColor = "yellow";
```
What must exist in the HTML for this code to work without throwing errors?
A. `<h1 class="main-title"></h1>`
B. `<title name="main-title"></title>`
C. `<div id="main-title"></div>`
D. `<header>#main-title</header>`


<br><br><br><br>

---
## Answer Sheet
1. C (`!important` overrides inline styles)
2. D (Width 200 + left/right padding 20 + left/right border 10 + left/right margin 20 = 250px)
3. B (String concatenation left-to-right vs numeric addition then concatenation)
4. C (When i=0, +0. i=1, +1. i=2, continue. i=3, +3. i=4, break. Total = 4)
5. B
6. C (Array becomes [20, 30, 40, 50]. Index 1 is 30)
7. C
8. B (var in JS is function-scoped. Inside the test() function, var a is hoisted, then overridden to 2. Let is block-scoped but irrelevant here)
9. D (0 equals "0" loosely, but types are different so strict equality fails)
10. B
11. A
12. C
13. C (Inner span styling overrides parent purely inherited styles)
14. C (2%3=2, 4%3=1, 6%3=0. 2+1+0=3)
15. B (JavaScript switch statements without a break fall through to the next case)
16. B
17. A
18. C
19. B
20. C (Span is an `inline` element, so it ignores explicit width and height properties)
21. B (`nodes[1]` tries to access the second element, which does not exist, evaluating to undefined)
22. B (`onclick` assignment overwrites previous `onclick` properties, unlike `addEventListener`)
23. C
24. B
25. C (`#` looks for an element with that specific ID. TagName does not matter as long as the ID matches)
