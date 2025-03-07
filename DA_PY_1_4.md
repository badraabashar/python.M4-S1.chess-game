## Project description

> Please read the AI responsibilities below before starting.

### Using AI Responsibly for Project Reviews

For guidelines on the responsible and tactical use of AI tools, particularly regarding project reviews, please refer to the information provided in this [link](https://turingcollege.atlassian.net/wiki/spaces/DLG/pages/872480773/AI+tools+e.g.+ChatGPT+in+learning).


___


The first practical graded task will require you to implement a Python program which will answer a simple question – given a board state that the user enters, with 1 white figure and up to 16 black figures, which black figures can the white figure take?

The exact criteria you are given to implement are as follows:
- The program should first ask the user to input a chess piece and where it is on the board. This will be the white piece. The user should be informed that they can choose between two pieces of your choice (e.g. pawn and rook). The choice should be made by writing the piece and the coordinates in a predefined format <piece location> in the console, e.g.: knight a5
- Once the user successfully adds the white piece, the user is asked to enter the black pieces, one by one, in the same format as the white piece. They need to add at least 1 black piece or 16 at most. Once at least one black piece has been added, the user can write “done” instead of the coordinates to add no more pieces.
- You can assume that the user will input either “done” or the correct format for adding a piece (“piece coordinates”). You can also assume that coordinates will always be entered as <letter><digit> where letters are a-h and digits are 1-8, e.g. a1, d4, h8. You should not assume anything else about the inputs, however (*hint*: there are still at least a couple of ways for the user to make invalid input, e.g. trying to write “done” too early)
- After adding each piece, there should be either a confirmation that it was added successfully, or an error message explaining what the issue is.
- After the white and the black pieces are added, the program should print out the black pieces, if any, that the white piece can take.

Important note on project requirements:
In real life work, the majority of projects will be described in such a way that there might be some parts that are not defined explicitly. This can be due to lack of time, lack of experience or simply because it is extremely hard to think about everything before you are actually able to see the working program. The missing requirements can be some functionalities or edge/corner cases (e.g. strange inputs by the user) that were not originally thought of. In these cases, it is then up to the developer to either:
Ask follow-up questions to ensure that what they’re building is truly according to the demands and specifications
Make educated guesses/assumptions about how the program should work.

In this project, whenever you are unclear about a requirement or how the program should work, make an educated guess. Write all of these down as a list of comments at the end of the Python file that you submit.

> Also, Remember the [20-minute rule](https://turingcollege.atlassian.net/wiki/spaces/DLG/pages/537395978/How+to+learn+at+Turing+College#Asking-for-help): If you get stuck for 20+ minutes on a single exercise, take a break and join an **Open Session** designated to Python or check with your peers. It is okay if you cannot solve these challenges yet on your own.

Finally, if you don’t know chess, keep in mind that to solve problems at work as a data analyst, you will always need to learn more about the industry in which you are working. E.g. if you start working as a data analyst for a logistics company, you will benefit greatly from gaining a good understanding of how logistics work.

### Sample questions for a reviewer to ask (a reviewer is encouraged and expected to think of more, however!)

- How do you define a function in Python? How can you easily test whether something is a function in Python? How do you define parameters of a function?
- What is the difference between a list and a dictionary?
- What is pseudocode?
- Can you show how you debug the program that you have written? Could you make a small change in the code and explain what it will do?

### Project evaluation criteria
- The program correctly adds the white piece. Weight: 1
- The program correctly adds the black pieces. Weight: 1
- The program correctly says which black pieces the white piece can take. Weight: 1
- Code quality (at this point, you are expected to write code that is relatively tidy and easy to follow. You can refer to the hands-on suggested solution for the level that may be expected from you). Weight: 1
- General understanding of the sprint topics (the reviewer may ask you about topics covered in the sprint and the code that you have written). Weight: 2

### Submission

Submit your project's .py file, created with your preferred IDE, to the GitHub Repository.


**Estimate average time to complete: 20 hours**
