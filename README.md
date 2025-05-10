 Reminder Me Later create api end point (Django Backend)
 

 Tech Stack
 
- Python 3.x
- Django 5.2+
- Django REST Framework
- SQLite (default, but can be changed to any DB)
  

steps to run:

git clone https://github.com/debasisbisoyi/symplique-assignment.git
cd symplique-assignment

python -m venv venv
source venv/bin/activate  
On Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
