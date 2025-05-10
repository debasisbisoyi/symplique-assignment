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

cd remind_me_later

python manage.py migrate

python manage.py runserver


json format for create post request in postmen or from frontend to "http://127.0.0.1:{port of backend}/api/reminders/" (optional fetch to get the data by get request)
{
  "date": "2025-08-10",
  "time": "18:20:00",
  "message": "Birthday of my friend",
  "reminder_type": ["sms", "email"]
}


