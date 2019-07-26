rmdir /s /q WebApp\migrations
rmdir /s /q quiz\migrations
rmdir /s /q forum\migrations

del db.sqlite3
python manage.py makemigrations WebApp forum quiz
python manage.py makemigrations survey
python manage.py migrate
python manage.py createsuperuserwithpassword    --username nsdevil --password nsdevil --email admin@example.org    --preserve
python manage.py runserver