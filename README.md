
# FVelGame

- Developer: Luis A. D'Afonseca
- Repository: https://github.com/luis-dafonseca/FVelGame
- License: GPL

## Introduction

This is a mini game engine to teach functions.

## Download

At the moment there is no package installation for any operational system.
The only way to execute the program is downloading the source code and
running via python interpreter.

To install python and run FVelGame follow the steps:

1. Python installation

    To install Python follow the instruction specific to for your operational system

    - [Windows](https://docs.python-guide.org/starting/install3/win/#pipenv-virtual-environments)
    - [MacOS](https://docs.python-guide.org/starting/install3/osx/)
    - [Linux](https://docs.python-guide.org/starting/install3/linux/#install3-linux)


2. Downloading the source code from GitHub

    One option is download a zip file of the code last version

    1. Got to the project repository [GitHub](https://github.com/luis-dafonseca/FVelGame)
    2. Click the button  `Code`
    3. Select option `Download ZIP`

    On linux it is possible to use the command line

    ```
    wget https://github.com/luis-dafonseca/FVelGame/archive/refs/heads/master.zip
    ```

    Another option, if you are a GitHub user, is to clone the repository, following this [instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

3. Unzip the file

## Executing the program

1. Create a virtual environment [Optional but recommended]

    For more information about Python Virtual Environment see the [documentation](https://docs.python.org/3/library/venv.html)

    Here are the prompt commands used to install, create and activate the environment:

    To install `virtualenv` execute

    ```
    pip install virtualenv
    ```

    To create a virtual environment, go to the directory with the `fvelgame.py` file and execute the following command

    ```
    python -m venv venv
    ```

    To activate the environment run

    ```
    .\venv\Scripts\activate
    ```
2. Dependencies

    To install the program dependencies execute

    ```
    pip install -r requirements.txt
    ```

3. Building internal dependencies and resources

    Go to directory `fvelgame-git/fvelgame/`

    Execute the script `make.py`

    ```
    python make.py
    ```

4. Executing

    To execute the graphical interface go to directory `fvelgame-git/fvelgame/` and run

    ```
    python fvelgame.py
    ```

    To execute the default game run

    ```
    python ./game/run_game.py
    ```

    To execute another game use

    ```
    python ./game/run_game.py ./resources/games/racing.game
    ```

## Technologies

This program is implemented in Python and uses the libraries

- [pygame](https://www.pygame.org)
- [PySide6](https://wiki.qt.io/Qt_for_Python)
- [Numpy](https://numpy.org)
- [NumExpr](https://pypi.org/project/numexpr/2.6.1)
- [PyQtGraph](https://pypi.org/project/pyqtgraph)
