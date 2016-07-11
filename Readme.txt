This repo contains code snippets written in python.
Tools needed:
1. git
2. pytest
3. pylint


How to install tools:
---------------------
1. Git:
TODO: Need to update this ;-).

2. Pytest:
pip install -U pytest
sudo pip install -U pytest

3. Pylint:
sudo apt-get install pylint
python coding standards explained here: https://www.python.org/dev/peps/pep-0008/


How to run tools:
-----------------
1. git:
git init
git config user.name dh****ju
git config user.email dh*********ju@gmail.com
git remote add origin https://github.com/dhanuhangout/python.git
git pull origin master
git add <filename.py>
git commit -m "Message the reason for commit"
git push -u origin master

2. pytest:
py.test test_factorial_v1.py

3. pylint:
pylint programs/factorial.py


How to pull this repo:
----------------------
mkdir dhanraju
cd dh****ju
# Follow git section under "How to run tools".


How to push a change to repo:
-----------------------------
Edit and save a file: vim ****.py
Add file to staging: git add ****.py
Commit the change: git commit -m "Message that explains the reason of change in
file."
Push change to master: git push origin master

