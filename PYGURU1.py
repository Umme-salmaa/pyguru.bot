import random

class PythonLearningChatbot:
    def __init__(self):
        
        self.levels = {
            "Beginner": {
                "topics": {
                    "WHAT IS PYTHON?": {
                        "description": """
Python is a high-level programming language created by Guido van Rossum in 1991. It's known for its simplicity and readability. You can use Python for web development, data science, artificial intelligence, and more!

It is a great language for beginners because you can learn it quickly and write simple, powerful programs in a short time.""",
                        "example": """# Simple example to print a message in Python
print('Hello, World!')""",
                        "practice": """
Try printing something yourself! Just type your message in quotes inside the print() function.
For example:
print('Your message here')""",
                        "learned": False
                    },
                    "variables": {
                        "description": """
Variables in Python are used to store data. Think of them like containers where you can keep your information (numbers, words, etc.) so you can use them later.

In Python, you create a variable by assigning a value to it with the '=' symbol.

For example:
x = 5  # Assigns the value 5 to the variable 'x'
y = 'Hello!'  # Assigns the string 'Hello!' to the variable 'y'""",
                        "example": """x = 5
y = 'Hello!'
print(x)
print(y)""",
                        "practice": """
Create your own variables and print them out!
For example:
a = 10
b = 'Python'
print(a)
print(b)""",
                        "learned": False
                    },
                    "data_types": {
                        "description": """
Python has several built-in data types that you will use all the time:

1. **int**: Integer numbers (e.g., 3, 100, -12)
2. **float**: Decimal numbers (e.g., 3.14, -0.5, 100.0)
3. **str**: Strings, or text (e.g., 'Hello', 'Python')
4. **list**: A collection of values in a sequence (e.g., [1, 2, 3], ['apple', 'banana'])

You can use these data types to store different kinds of information.""",
                        "example": """# Using different data types
x = 10  # int
y = 3.14  # float
z = 'Python'  # str
lst = [1, 2, 3, 4]  # list
print(x, y, z, lst)""",
                        "practice": """
Try creating your own variables using different data types!
For example:
integer = 20
float_num = 4.5
greeting = 'Hello, Python!'
my_list = [1, 2, 3, 4]

Now, print them out and check the results!""",
                        "learned": False
                    },
                    "operators": {
                        "description": """
Operators are symbols that perform operations on variables or values. In Python, you have arithmetic operators like:

- `+`: Addition
- `-`: Subtraction
- `*`: Multiplication
- `/`: Division

Let’s look at how they work!""",
                        "example": """a = 10
b = 5
print(a + b)  # Output: 15
print(a - b)  # Output: 5
print(a * b)  # Output: 50
print(a / b)  # Output: 2.0""",
                        "practice": """
Try out some arithmetic operations:
a = 15
b = 3
Now, try printing the result of adding, subtracting, multiplying, and dividing 'a' and 'b'!""",
                        "learned": False
                    },
                    "casting": {
                        "description": """
Casting is the process of converting one data type into another. For example, you can convert a string into an integer or a float into a string.

For example:
int(3.14) converts 3.14 into an integer (3)
str(10) converts 10 into a string ('10')""",
                        "example": """x = 3.14
y = int(x)  # Converts float to int
print(y)  # Output: 3

z = 10
w = str(z)  # Converts int to string
print(w)  # Output: '10'""",
                        "practice": """
Try casting between different types:
For example:
a = 2.8
b = int(a)  # Convert to integer
c = str(a)  # Convert to string

Print the results!""",
                        "learned": False
                    }
                },
                "quiz": {
                    "questions": [
                        {"question": "Who created Python and when?", "options": ["Dennis Ritchie, 1972", "Guido van Rossum, 1991", "James Gosling, 1995"], "answer": 2},
                        {"question": "What is a variable in Python?", "options": ["A way to store data.", "A loop structure.", "A condition statement."], "answer": 1},
                        {"question": "Name a data type in Python.", "options": ["int", "loop", "function"], "answer": 1},
                        {"question": "What is the result of 3 + 2 * 2?", "options": ["10", "7", "8"], "answer": 2}
                    ]
                }
            },
            "Intermediate": {
                "topics": {
                    "lists_and_methods": {
                        "description": """
Lists are ordered collections of items, and they are one of the most commonly used data structures in Python.

Here are some common methods you can use with lists:
- **append()**: Adds an item to the end of the list.
- **remove()**: Removes the first occurrence of a specified item.
- **sort()**: Sorts the list in ascending order.

Let is see how it works!""",
                        "example": """fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')  # Adds 'orange' to the list
fruits.remove('banana')  # Removes 'banana' from the list
fruits.sort()  # Sorts the list alphabetically
print(fruits)  # Output: ['apple', 'cherry', 'orange']""",
                        "practice": """
Create your own list and practice:
- Add items using append().
- Remove items using remove().
- Sort your list using sort().

For example:
fruits = ['apple', 'banana', 'grapes']
fruits.append('orange')
fruits.remove('banana')
fruits.sort()
print(fruits)""",
                        "learned": False
                    },
                    "dictionaries_and_methods": {
                        "description": """
Dictionaries are unordered collections of data stored in key-value pairs. Each key must be unique, and you can use the key to access its corresponding value.

Let’s take a look at how to work with dictionaries!""",
                        "example": """person = {'name': 'Alice', 'age': 25}
person['city'] = 'New York'  # Add a new key-value pair
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}""",
                        "practice": """
Create your own dictionary:
- Add key-value pairs.
- Access a value by its key.

For example:
my_dict = {'color': 'red', 'shape': 'circle'}
my_dict['size'] = 'large'
print(my_dict)""",
                        "learned": False
                    },
                    "tuples_and_methods": {
                        "description": """
Tuples are similar to lists, but they are **immutable**, which means they can’t be modified after they are created.

Use tuples when you want a collection of items that shouldn't change.

You can access items in a tuple just like you would with a list!""",
                        "example": """colors = ('red', 'green', 'blue')
print(colors[0])  # Output: red""",
                        "practice": """
Try creating a tuple and accessing an element from it!
For example:
my_tuple = ('apple', 'banana', 'cherry')
print(my_tuple[1])  # Output: banana""",
                        "learned": False
                    },
                    "strings_and_methods": {
                        "description": """
Strings in Python are sequences of characters. Python provides many helpful methods to manipulate strings, such as:

- **upper()**: Converts all characters to uppercase.
- **lower()**: Converts all characters to lowercase.
- **replace()**: Replaces a substring with another substring.

Let's take a closer look at these methods!""",
                        "example": """text = 'Hello, Python!'
print(text.upper())  # Output: 'HELLO, PYTHON!'
print(text.replace('Python', 'World'))  # Output: 'Hello, World!'""",
                        "practice": """
Practice with strings:
Try creating a string and then:
- Convert it to uppercase.
- Replace a part of the string.

For example:
greeting = 'hello'
greeting = greeting.upper()
print(greeting)""",
                        "learned": False
                    },
                    "if_else_conditions": {
                        "description": """
The `if-else` statement allows you to execute different blocks of code depending on a condition.

For example:
if a condition is true, one block of code will run; otherwise, a different block will run.

Here’s how it works:""",
                        "example": """age = 18
if age >= 18:
    print('You are an adult!')
else:
    print('You are a minor.')""",
                        "practice": """
Practice writing your own if-else statement:
Try checking if a number is positive, negative, or zero, and print the corresponding message.

For example:
number = 5
if number > 0:
    print('Positive')
elif number < 0:
    print('Negative')
else:
    print('Zero')""",
                        "learned": False
                    }
                },
                "quiz": {
                    "questions": [
                        {"question": "What method adds an item to a list?", "options": ["insert", "append", "extend"], "answer": 2},
                        {"question": "Are tuples mutable or immutable?", "options": ["mutable", "immutable", "both"], "answer": 2},
                        {"question": "What do dictionaries store data as?", "options": ["keys", "values", "key-value pairs"], "answer": 3},
                        {"question": "How do you convert a string to uppercase?", "options": ["upper", "toUpperCase", "to_upper"], "answer": 1}
                    ]
                }
            },
            "Pro": {
                "topics": {
                    "while_loop": {
                        "description": """
The `while` loop is used to execute a block of code as long as a condition is true.

For example:
The loop will run until the counter reaches a certain number.""",
                        "example": """i = 1
while i <= 5:
    print(i)
    i += 1  # Increment the counter""",
                        "practice": """
Write your own `while` loop:
Try counting from 1 to 10 using a while loop.

For example:
i = 1
while i <= 10:
    print(i)
    i += 1""",
                        "learned": False
                    },
                    "for_loop": {
                        "description": """
The `for` loop is used to iterate over a sequence (like a list, tuple, or string) and perform actions on each element.

Here’s how a simple `for` loop looks:""",
                        "example": """for fruit in ['apple', 'banana', 'cherry']:
    print(fruit)""",
                        "practice": """
Try writing your own `for` loop:
For example, iterate through a list of numbers and print them.

For example:
numbers = [1, 2, 3, 4]
for num in numbers:
    print(num)""",
                        "learned": False
                    },
                    "functions": {
                        "description": """
Functions are reusable blocks of code. You can define your own functions to perform specific tasks.

To define a function in Python, use the `def` keyword.""" ,
                        "example": """def greet(name):
    return f'Hello, {name}!'""",
                        "practice": """
Try writing your own function:
Define a function that takes a number and prints if it’s even or odd.

For example:
def check_even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
""",
                        "learned": False
                    }
                },
                "quiz": {
                    "questions": [
                        {"question": "What loop runs until a condition becomes false?", "options": ["while loop", "for loop", "do-while loop"], "answer": 1},
                        {"question": "What keyword is used to define a function?", "options": ["def", "func", "lambda"], "answer": 1},
                        {"question": "What does a for loop iterate over?", "options": ["a sequence", "a condition", "a range"], "answer": 1},
                        {"question": "Write the syntax to call a function named 'greet' with 'Alice'.", "options": ["greet()", "greet('Alice')", "call greet('Alice')"], "answer": 2}
                    ]
                }
            }
        }
        self.current_level = "Beginner"
        self.users = {}
        self.current_user = None
        self.points = {}

    def login(self):
        print("\n🔑 Login to Python Learning Chatbot")
        user_id = input("Enter your user ID: ").strip()
        password = input("Enter your password: ").strip()

        if user_id in self.users and self.users[user_id]['password'] == password:
            print(f"\n🎉 Welcome back, {user_id}!")
            self.current_user = user_id
            self.current_level = self.users[user_id]['level']
        else:
            print("\n❌ Invalid credentials. Let's create a new account!")
            self.register(user_id, password)

    def register(self, user_id, password):
        print("\n📋 Registering a new user.")
        self.users[user_id] = {
            "password": password,
            "level": "Beginner"
        }
        self.points[user_id] = 0
        print(f"\n🎉 Account created successfully! Welcome, {user_id}!")
        self.current_user = user_id

    def show_menu(self):
        print(f"\n🎉 Welcome to Python Learning Chatbot! 🎉")
        print(f"You are currently at the {self.current_level} level.")
        print(f"🏆 Points: {self.points[self.current_user]}")
        print("What would you like to learn today?")
        topics = self.levels[self.current_level]["topics"]
        for i, (topic, data) in enumerate(topics.items(), 1):
            status = "✅" if data["learned"] else "❌"
            print(f"{i}. {topic.replace('_', ' ').capitalize()} {status}")
        print("0. Exit")

    def teach_concept(self, concept):
        topics = self.levels[self.current_level]["topics"]
        data = topics.get(concept)
        if not data:
            print("Oops! I don't know that concept yet. Let's try something else!")
            return

        print(f"\n📘 Let's learn about {concept.replace('_', ' ').capitalize()}!")
        print(f"✨ Description: {data['description']}")
        print("💡 Example:")
        print(data['example'])
        print("\n🎯 Try writing your own code with this concept and see the magic happen!")
        print(f"\n📝 Practice:\n{data['practice']}")
        self.mark_as_learned(concept)

    def mark_as_learned(self, concept):
        self.levels[self.current_level]["topics"][concept]["learned"] = True
        self.points[self.current_user] += 10
        print(f"🎉 Great job! You've earned 10 points. Total points: {self.points[self.current_user]}.")

    def check_progress(self):
        topics = self.levels[self.current_level]["topics"]
        return all(data["learned"] for data in topics.values())

    def take_quiz(self):
        print("\n🎓 Quiz Time! Answer the following questions:")
        questions = self.levels[self.current_level]["quiz"]["questions"]
        correct_answers = 0

        for idx, question_data in enumerate(questions, 1):
            print(f"\n❓ {question_data['question']}")
            for opt_idx, option in enumerate(question_data['options'], 1):
                print(f"{opt_idx}. {option}")

            answer = int(input("Your answer: ").strip())
            if answer == question_data['answer']:
                print("✔️ Correct!")
                correct_answers += 1
            else:
                print("❌ Incorrect.")

        print(f"\n🎉 You got {correct_answers}/{len(questions)} correct!")

        if correct_answers == len(questions):
            self.promote_user()
        else:
            print("Keep practicing to improve your score!")

    def promote_user(self):
        if self.current_level == "Beginner":
            self.current_level = "Intermediate"
        elif self.current_level == "Intermediate":
            self.current_level = "Pro"
        else:
            print("🎉 Congratulations! You've mastered all levels!")
            return

        self.users[self.current_user]["level"] = self.current_level
        print(f"🎉 You've been promoted to {self.current_level} level! Keep up the great work!")

    def start(self):
        print("\nWelcome to Python Learning Chatbot! I AM PYGURU!🌟")
        self.login()

        while True:
            self.show_menu()
            choice = input("Enter the topic number you want to learn (or 0 to exit): ").strip()

            if choice == "0":
                print("Goodbye! Keep coding and learning! 🐍")
                break

            topics = list(self.levels[self.current_level]["topics"].keys())
            if choice.isdigit() and 1 <= int(choice) <= len(topics):
                self.teach_concept(topics[int(choice) - 1])

                if self.check_progress():
                    print("\n🎉 You've completed all topics at this level! Ready for the quiz?")
                    self.take_quiz()
            else:
                print("Invalid option. Please choose again.")

# Start the chatbot
chatbot = PythonLearningChatbot()
chatbot.start()
