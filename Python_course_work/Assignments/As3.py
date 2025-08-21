def get_questions():
    return [
        {
            "question": "What does the pass statement do?",
            "options": {"a": "Stops the loop", "b": "Skips the current iteration", "c": "Does nothing (placeholder)", "d": "Terminates the program"},
            "answer": "c",
        },
        {
            "question": "Which method is used to add an element to a list?",
            "options": {"a": "add()", "b": "append()", "c": "insert()", "d": "extend()"},
            "answer": "b",
        },
        {
            "question": "What will be the output of this code? \n print(bool([]))",
            "options": {"a": "True", "b": "False", "c": "Error", "d": "None"},
            "answer": "b",
        },
        {
            "question": "What is the output? \n print('Hello'.lower())",
            "options": {"a": "HELLO", "b": "hello", "c": "Hello", "d": "Error"},
            "answer": "b",
        },
        {
            "question": "How do you check if two variables a and b refer to the same object?",
            "options": {"a": "a == b", "b": "a is b", "c": "a equals b", "d": "a ==! b"},
            "answer": "b",
        },
        {
            "question": "Which of the following is true?",
            "options": {"a": "Lists are immutable", "b": "Tuples are mutable", "c": "Dictionaries use key-value pairs", "d": "Sets are ordered collections"},
            "answer": "c",
        },
        {
            "question": "What does 'break' do in a loop?",
            "options": {"a": "Skips next iteration", "b": "Exits the loop", "c": "Continues", "d": "Restarts the loop"},
            "answer": "b",
        },
        {
            "question": "Which of the following keywords is used to define a generator function?",
            "options": {"a": "def", "b": "yield", "c": "generator", "d": "return"},
            "answer": "b",
        },
        {
            "question": "How do you insert an item at index 2 in a list called 'mylist'?",
            "options": {"a": "mylist.add(2, item)", "b": "mylist.insert(2, item)", "c": "mylist[2] = item", "d": "mylist.put(2, item)"},
            "answer": "b",
        },
        {
            "question": "How do you import the math module?",
            "options": {"a": "import math", "b": "using math", "c": "#import math", "d": "include math"},
            "answer": "a",
        },
        {
            "question": "What data type is returned by input()?",
            "options": {"a": "int", "b": "str", "c": "float", "d": "bool"},
            "answer": "b",
        },
        {
            "question": "Which keyword defines a class in Python?",
            "options": {"a": "func", "b": "define", "c": "class", "d": "object"},
            "answer": "c",
        },
        {
            "question": "Which function converts a string to an integer?",
            "options": {"a": "str()", "b": "int()", "c": "float()", "d": "bool()"},
            "answer": "b",
        },
        {
            "question": "What is the index of 'b' in ['a','b','c']?",
            "options": {"a": "0", "b": "1", "c": "2", "d": "3"},
            "answer": "b",
        },
        {
            "question": "How do you start a while loop?",
            "options": {"a": "while x > 0:", "b": "loop x > 0", "c": "repeat x > 0", "d": "while (x > 0) {}"},
            "answer": "a",
        },
        {
            "question": "Which of the following closes a file?",
            "options": {"a": "file.save()", "b": "file.delete()", "c": "file.close()", "d": "file.exit()"},
            "answer": "c",
        },
        {
            "question": "Which function returns the largest item in an iterable?",
            "options": {"a": "min()", "b": "large()", "c": "big()", "d": "max()"},
            "answer": "d",
        },
        {
            "question": "What is the output of print('Hello' * 2)?",
            "options": {"a": "HelloHello", "b": "Hello2", "c": "Hello Hello", "d": "Error"},
            "answer": "a",
        },
        {
            "question": "Which operator is used for exponentiation?",
            "options": {"a": "^", "b": "**", "c": "//", "d": "%"},
            "answer": "b",
        },
        {
            "question": "What will print(type([1, 2, 3])) output?",
            "options": {"a": "<class 'tuple'>", "b": "<class 'list'>", "c": "<class 'set'>", "d": "<class 'dict'>"},
            "answer": "b",
        },
    ]


def ask_question(q, num):
    print(f"\nQuestion {num + 1}: {q['question']}")
    for key in sorted(q["options"]):
        print(f"    {key}) {q['options'][key]}")
    answer = input("Your answer (a/b/c/d): ").lower()
    return answer == q["answer"]


def run_quiz():
    questions = get_questions()
    score = 0
    print("\nWelcome to the Python Interview Prep Quiz!\n")
    for i, q in enumerate(questions):
        if ask_question(q, i):
            print("✔ Correct!\n")
            score += 1
        else:
            print(f"✗ Wrong! The correct answer was '{q['answer']}'.\n")
    print(f"Quiz Over! Your Score: {score}/{len(questions)}")
    print("Thank You")

run_quiz()
