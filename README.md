
# MathRunner

- Developer: Luis A. D'Afonseca
- Repository: https://github.com/LAD-MathQuest/MathRunner
- License: GPL

## Introduction

This is a mini game engine to teach functions.

## Download

At the moment there is no package installation for any operational system.
The only way to execute the program is downloading the source code and
running via python interpreter.

To install python and run MathRunner follow the steps:

1. Python installation

    To install Python follow the instruction specific to for your operational system

    - [Windows](https://docs.python-guide.org/starting/install3/win/#pipenv-virtual-environments)
    - [MacOS](https://docs.python-guide.org/starting/install3/osx/)
    - [Linux](https://docs.python-guide.org/starting/install3/linux/#install3-linux)


2. Downloading the source code from GitHub

    One option is download a zip file of the code last version

    1. Got to the project repository [GitHub](https://github.com/LAD-MathQuest/MathRunner)
    2. Click the button `Code`
    3. Select option `Download ZIP`

    On linux it is possible to use the command line

    ```
    wget https://github.com/LAD-MathQuest/MathRunner/archive/refs/heads/master.zip
    ```

    Another option, if you are a GitHub user, is to clone the repository, following this [instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

3. Unzip the file

4. Install `uv`, following this [instructions](https://docs.astral.sh/uv/getting-started/installation)

5. Go to the folder where you unzipped the code. On linux terminal execute
    ```
    cd path_to_code
    ```

6. Fist you must compile the game examples
    ```
    uv run src/examples/make.py
    ```

6. Now you can execute the program using the command
    ```
    uv run -m mathrunner
    ```

## Technologies

This program is implemented in Python and uses the libraries

- [pygame](https://www.pygame.org)
- [Numpy](https://numpy.org)
- [NumExpr](https://pypi.org/project/numexpr/2.6.1)
- [PySide6](https://wiki.qt.io/Qt_for_Python)
- [PyQtGraph](https://pypi.org/project/pyqtgraph)
