# AirBnB_clone
![0x00. AirBnB clone - The console](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240518%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240518T185948Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=56d7eba46528eec2f69eaf41df710c20b5e82cf3f2a350c0d260ae7a411a2b33)
## Background Context

Welcome to the AirBnB clone project!

Before starting, please read the AirBnB concept page.
First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- Put in place a parent class (called BaseModel) to take care of the initialization, serialization, and deserialization of your future instances.
- Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.
- Create the first abstracted storage engine of the project: File storage.
- Create all unittests to validate all our classes and storage engine.

## What’s a Command Interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (e.g., a new User or a new Place).
- Retrieve an object from a file, a database, etc.
- Do operations on objects (count, compute stats, etc.).
- Update attributes of an object.
- Destroy an object.

## Resources

Read or watch:

- [cmd module](https://docs.python.org/3/library/cmd.html)
- [cmd module in depth](https://pymotw.com/3/cmd/)
- [packages concept page](https://packaging.python.org/guides/)
- [uuid module](https://docs.python.org/3/library/uuid.html)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [unittest module](https://docs.python.org/3/library/unittest.html)
- [args/kwargs](https://realpython.com/python-kwargs-and-args/)
- [Python test cheatsheet](https://python-guide-pt-br.readthedocs.io/en/latest/writing/tests/)
- [cmd module wiki page](https://en.wikipedia.org/wiki/Cmd_(Python_module))
- [python unittest](https://docs.python.org/3/library/unittest.html)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- How to create a Python package.
- How to create a command interpreter in Python using the `cmd` module.
- What is unit testing and how to implement it in a large project.
- How to serialize and deserialize a Class.
- How to write and read a JSON file.
- How to manage `datetime`.
- What is a UUID.
- What is `*args` and how to use it.
- What is `**kwargs` and how to use it.
- How to handle named arguments in a function.

## Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`.
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the `pycodestyle` (version 2.8.*).
- All your files must be executable.
- The length of your files will be tested using `wc`.
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified).

### Python Unit Tests

- Allowed editors: `vi`, `vim`, `emacs`.
- All your files should end with a new line.
- All your test files should be inside a folder `tests`.
- You have to use the `unittest` module.
- All your test files should be Python files (extension: `.py`).
- All your test files and folders should start by `test_`.
- Your file organization in the `tests` folder should be the same as your project.
  - e.g., For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`.
  - e.g., For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`.
- All your tests should be executed by using this command: `python3 -m unittest discover tests`.
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`.
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
- We strongly encourage you to work together on test cases, so that you don’t miss any edge cases.## More Info

### Execution

Your shell should work like this in interactive mode:

```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
###0. README, AUTHORS:

 Write a README.md:
        description of the project
        description of the command interpreter:
            how to start it
            how to use it
            examples
    You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference Docker’s AUTHORS page
    You should use branches and pull requests on GitHub - it will help you as team to organize your work

Repo:

    GitHub repository: AirBnB_clone
    File: README.md, AUTHORS
