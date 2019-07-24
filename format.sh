rm -r WebApp\migrations
rm -r  quiz\migrations
rm -r  forum\migrations
rm -r  survey\migrations
rm db.sqlite3
python manage.py makemigrations forum WebApp quiz survey
python manage.py migrate
python manage.py createsuperuserwithpassword    --username nsdevil --password nsdevil --email admin@example.org    --preserve
python manage.py runserver