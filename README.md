# Installation Notes:
1. Check out a project in Pycharm - [see here for help](Open%20lms%20folder%20using%20Pycharm)
URL of the remote repository: **https://gitlab.com/nsdevil/lms.git**
4.  [Create Virtual Environment](https://www.jetbrains.com/help/pycharm-edu/creating-virtual-environment.html)
5. Restart Pycharm
6. On the Pycharm's terminal run the following code to Install Requirements : **pip install -r requirements.txt**


**For Windows user:**
If you get problem in installing **Twisted** library:
Download Suitable Version of pre compilled library from: [https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted) and install from  venv activated Pycharm terminal using :
**pip install *filename*.whl** 
and again Install Requirements 

5.  Migrate Database: **python manage.py makemigrations WebApp**
6. Migrate Database: **python manage.py migrate**
7. After that, run the app using Django manage.py: **python manage.py runserver**
8. Access the homepage on     http://localhost:8000

# Live Deployment:
Check  http://lms-nsd.sushant.info.np


# Project Management Links
### Gitlab Board > [https://gitlab.com/nsdevil/lms/boards](https://gitlab.com/nsdevil/lms/boards)
### Bitrix Tasks > [https://nsdevil.bitrix24.com/extranet/workgroups/group/109/tasks/](https://nsdevil.bitrix24.com/extranet/workgroups/group/109/tasks/)

