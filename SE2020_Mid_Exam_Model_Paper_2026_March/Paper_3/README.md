# Web and Mobile Technology - Practice Paper 3

## Instructions
* **Time Allowed:** 1 Hour
* **Number of Questions:** 25 MCQs
* **Syllabus Coverage:** Lecture 1 to Lecture 5
* **Format:** Choose the single or multiple best options where specified.

---

### Question 1
Which statement accurately describes a Virtual Private Network (VPN)?
A. A connection that simulates a private network over a public network.
B. A server dedicated solely to converting domain names into IP addresses.
C. A network entirely confined within a single physical office building.
D. A set of protocols that defines email transmission.

### Question 2
What does FTP stand for in web terminology?
A. File Transfer Protocol
B. Folder Text Protocol
C. Forward Transfer Process
D. File Transmission Process

### Question 3
An HTTP response code of '404' generally indicates:
A. Success
B. Server Error
C. Not Found
D. Method Not Allowed

### Question 4
```html
<a href="example.html">
  <img border="0" src="myfile.gif" width="50" height="100">
</a>
```
The above code snippet will display:
A. A standard text link that says "myfile.gif".
B. An image that acts as a hyperlink.
C. An image positioned correctly with an invisible border but without link capability.
D. A broken image.

### Question 5
Which HTML tag is employed to create a dropdown list?
A. `<list>`
B. `<input type="dropdown">`
C. `<select>`
D. `<dropdown>`

---
### Question 6
What does the `<br>` tag denote in an HTML layout?
A. A bold text line
B. A line break
C. The breaking point for responsive CSS
D. A horizontal rule

### Question 7
```css
p {
  color: green !important;
}
#myText {
  color: red;
}
```
If an HTML paragraph has `id="myText"`, what color is the paragraph?
A. Red
B. Green
C. Black
D. Error due to conflict

### Question 8
Which of the following is NOT a valid CSS selector?
A. `.navigation > li`
B. `body:hover`
C. `div~span`
D. `style="css"`

### Question 9
In CSS positioning, an element whose `position` property is set to `absolute`:
A. is positioned relative to its normal position.
B. is positioned relative to the browser window.
C. is positioned relative to its closest positioned ancestor.
D. stays in the same place in the normal document flow.

### Question 10
If `box-sizing: border-box;` is applied to an element, the `width` property determines:
A. Only the content width.
B. The content width plus padding and border.
C. The full width including margin.
D. Only the margin width.

---
### Question 11
Which of the following describes the behavior of `document.querySelectorAll()`?
A. Returns the first matching element.
B. Returns a live HTMLCollection.
C. Returns a static NodeList of all matching elements.
D. Modifies all matching elements.

### Question 12
You have a `<button onclick="testFunction()">Click Me</button>`. 
Which of the following JavaScript correctly defines `testFunction` to show an alert?
A. `function testFunction() { window.alert("Clicked!"); }`
B. `const testFunction = window.alert("Clicked!");`
C. `def testFunction(): print("Clicked!")`
D. Both A and B

### Question 13
```javascript
let i = 2;
let text = "";
while (i <= 6) {
  if (i == 4) {
    i++;
    continue;
  }
  text += i + " ";
  i++;
}
console.log(text);
```
What is the exact output of the code?
A. "2 3 5 6 "
B. "2 3 6 "
C. "2 3 4 5 6 "
D. "2 3 5 "

### Question 14
In JavaScript, arrays can hold:
A. Only Numbers
B. Only Strings
C. Only Objects
D. Any mix of data types

### Question 15
```javascript
let divset = document.getElementsByTagName("div");
for(let i=0 ;i<divset.length;i++){
    if(i%2==0) divset[i].style.color="pink";
    else divset[i].style.color="blue";
}
```
Select the correct outcome:
A. The very first `<div>` (index 0) becomes blue.
B. Even indexed `<div>` elements become pink and odd indexed `<div>` elements become blue.
C. Odd indexed `<div>` elements become pink and even indexed `<div>` elements become blue.
D. An error occurs because style cannot be set this way.

---
### Question 16
What will `typeof []` evaluate to in JavaScript?
A. "array"
B. "object"
C. "list"
D. "undefined"

### Question 17
```javascript
let buttons = document.querySelectorAll(".btn");
buttons.addEventListener("click", function(){
    console.log("Clicked");
});
```
What is true about the above code snippet?
A. The event listener correctly applies to all `.btn` elements.
B. `addEventListener` cannot be applied directly to a NodeList returned by `querySelectorAll`.
C. It will only apply the click event to the first item.
D. `.btn` selector is fundamentally illegal in JS.

### Question 18
Which JavaScript operator performs a strict comparison (checking value AND data type)?
A. `=`
B. `==`
C. `===`
D. `!==`

### Question 19
Which of the HTML `<input>` types automatically validates if the value contains an "@" symbol?
A. `type="text"`
B. `type="password"`
C. `type="email"`
D. `type="url"`

### Question 20
To wrap text beautifully around an image in CSS, which property do you use?
A. `clear`
B. `position`
C. `float`
D. `display`

---
### Question 21
```html
<style>
 .highlight { color: blue; }
 div { color: red; }
</style>
<div class="highlight">Item 1</div>
```
Which is the resulting color of Item 1?
A. Red because it is the last declared rule affecting divs.
B. Blue because the class selector outweighs the elemental selector.
C. Black as a fallback.
D. Purple because colors blend.

### Question 22
A JavaScript `prompt()` function returns:
A. `Boolean` only.
B. `Number` if a number is typed, otherwise `String`.
C. `String` (or `null` if cancelled).
D. `Undefined`.

### Question 23
```javascript
let y = "7";
let z = 2;
console.log(y - z);
```
What is the outcome of this subtraction in JavaScript?
A. "72"
B. 5
C. NaN
D. TypeError

### Question 24
In the DOM hierarchy, the topmost object that represents the browser window is:
A. `document`
B. `navigator`
C. `window`
D. `body`

### Question 25
When considering web architectures, the role of a DNS protocol is essentially to:
A. Encrypt data sent over connections.
B. Function as a phonebook for the internet.
C. Send web pages from server to client.
D. Establish state via session cookies.


<br><br><br><br>

---
## Answer Sheet
1. A
2. A
3. C
4. B
5. C
6. B
7. B (`!important` overrides everything)
8. D (This is an inline attribute, not a selector format inside a stylesheet)
9. C
10. B
11. C
12. A
13. A
14. D
15. B
16. B
17. B
18. C
19. C
20. C
21. B
22. C
23. B
24. C
25. B
