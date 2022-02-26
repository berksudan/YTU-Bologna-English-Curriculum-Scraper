#!/bin/bash

# Change current directory to project directory. 
CURRENT_PATH="$( cd "$(dirname "$0")" || exit ; pwd -P )"
cd "$CURRENT_PATH" || exit

# Install python3-venv package if not installed.
sudo apt install python3-venv

# Create virtual environment directory
python3 -m venv venv/

# Activate virtual environment
source venv/bin/activate

# Upgrade Python 
python -m pip install --upgrade pip

# Check version of pip
# Version must be below 18.XX and compatible with Python 3.5+
pip --version

# Install requirements
pip install requirements
