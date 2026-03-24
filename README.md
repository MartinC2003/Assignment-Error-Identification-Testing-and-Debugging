# Assignment: Concepts, Syntax and Lexical Analysis

- 📄 [Project Summary](#project-summary)  
- 👨‍🏫 [Trello](#Trello)
- 📝 [Documentation](#Documentation)
- 💻 [How to Run](#how-to-run)
- 👤 [Credits](#credits)  

## Project Summary 
Rebuilding and improving a broken Python program by fixing bugs, and restructuring the code for better through implementing unit and integration tests, documenting our process thorugh the useage of diagrams, code snippets and test output.

## Trello
Trello Link https://trello.com/b/Sgi6JnZi/my-trello-board 

## Documentation 

### Bug Report 1: Missing Colon in `add_item` Method
**Error Code Snippet:**
```python
def add_item(self, item_name, quantity, price)
    self.items.append((item_name, quantity, price))
```
**Assigned Team member**: Dhanpreet Kaur

**Expected Behavior**: add_item is defined successfully and items can be appended to the order

**Actual Behavior**: Python raises SyntaxError: expected ':' and the program refuses to run

**Steps to Reproduce**: run the file in VS Code, check the syntax error it gives while debugging. like in this case it said
```bash
“File "c:\Users\Dhanpreet\Downloads\Buggy Code.py", line 16
def add_item(self, item_name, quantity, price)
SyntaxError: expected ':'“
```
**Fixed Code:**
```python
 def add_item(self, item_name, quantity, price): #<-- colon added at the end of the add_item statement
        self.items.append((item_name, quantity, price))
```

## How to Run 
```bash 
```
## Credits
- [Martin](https://github.com/MartinC2003)
- [Thong](https://github.com/giathongnguyen)
- [Veer]()
- [Nida]()
- [Dhanpreet]()
- [Vaidik ]()







