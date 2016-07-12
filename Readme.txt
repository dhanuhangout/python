This repo contains code snippets written in python.
Tools needed:
1. git
2. pytest


How to install tools:
---------------------
1. Git:
TODO: Need to update this ;-).

2. Pytest:
pip install -U pytest
sudo pip install -U pytest


How to run tools:
-----------------
1. pytest:
py.test test_factorial_v1.py


How to pull this repo:
----------------------
mkdir dhanraju
cd dh****ju
git init
git config user.name dh****ju
git config user.email dh***********ju@gmail.com
git remote add origin https://github.com/dhanuhangout/python.git
git pull origin master


How to push a change to repo:
-----------------------------
Edit and save a file: vim ****.py
Add file to staging: git add ****.py
Commit the change: git commit -m "Message that explains the reason of change in
file."
Push change to master: git push origin master


Some more notes:
----------------
- As we know, if a file get modified; then the status of it is "modified". If
want to revert this modified file, use command "git checkout <file name>
- If a file get added and not commited, then to revert that modified file, run
"git reset" and then "git checkout <file name> commands.
