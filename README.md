# api-tutorial

A python flask api tutorial.

# Requirements
- Python 3.12
# Installation

## Installing Python
### MAC
I recommend installing [Homebrew](https://brew.sh/), a package manager for MAC. 
From the terminal app run the following:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
With [Homebrew](https://brew.sh/) installed, you can now run:
```bash
brew install python@3.12
```
### Linux
You'll have to add a repository to apt before installing:
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12 -y
```

## Installing virtualenv
#### MAC
Use Homebrew to install:
```bash
brew install virtualenv
```
#### Linux
```bash
sudo apt install python3-virtualenv -y
```
### Finding the Python Interpreter
To ensure we are using the correct python version for our virtualenv, run:
```bash
which python3.12
```
This should provide you the path to the python3.12 interpreter:
```bash
/usr/bin/python3.12
```
### Creating a Virtual Environment
Now use the path the interpreter to create your virtualenv
```bash
virtualenv -p <path_to_python_interpreter> venv
```
e.g. 
```bash
virtualenv -p /usr/bin/python3.12 venv
```
Now source the `activate` file to update your environment variables
```bash
source venv/bin/activate
```
To confirm things worked, run:
```bash
python --version
```
You should see a response indicating the version is `Python 3.12`

## Installing Dependencies
```bash
pip install -r requirementes.txt
```

# Using the App
## Run the Server
```bash
make serve
```
## Run Tests
```bash
make test
```

