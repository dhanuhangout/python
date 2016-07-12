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


Some Notes:
-----------
1. Since, dhanraju repo is ahead of dhanuhangout; Followed below procedure to
update dhanraju master branch:

- Create a folder with dhanuhangout user and ha*******10@gmail.com email.
mkdir dhanuhangout_python
cd dhanuhangout_python
git init
git config user.name dhanuhangout
git config user.email ha********10@gmail.com
- Pull master branch of dhanraju (Remember not dhanuhangout, though the user is
	dhanuhangout).
git remote add origin https://github.com/dhanraju/python.git
git pull origin master
- Edit file
git add Readme.txt
- login to github.com with user dhanraju and all dhanuhangout in
settings->collaborators and then sign out.
- login to github.com with user dhanuhangout and accept invitation from
dhanraju.
- Now commit the code.
git commit -m "Sync to dhanraju master branch with dhanuhangout user and
uploading all files to dhanuhangout master branch"
git push -u origin master
