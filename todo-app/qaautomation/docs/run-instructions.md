## Key requirements
Python 3.12 or newer
npm 8.11.0

## Clone repository

Open local hard drive and open CMD. Execute command:

'Git clone '

## Install NPM package

Go to root directory and open CMD. Execute command:

'npm install'


## Setup and activate venv

After successfully cloning repository to your local machine, go into the root/qaautomation directory. Then open CMD and
execute this command:

'pip install virtualenv'

Then in root/qaautomation directory, perform command:

'python -m venv venv'

After that:

'venv/Scripts/Activate.ps1'

After successfully activating venv, perform next command:

'pip install -r requirements.txt'


## You're all set

Go to root directory and execute:

'npm start'

Then, go to root/qaautomation/tests directory and execute command:

'pytest test_scenario.py'


## Enjoy!!