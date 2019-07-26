rm -r WebApp\migrations
rm -r  quiz\migrations
rm -r  forum\migrations

fuser -k -n tcp 9002
rm db.sqlite3
python manage.py makemigrations forum WebApp quiz
python manage.py migrate
python manage.py createsuperuserwithpassword    --username nsdevil --password nsdevil --email admin@example.org    --preserve
python manage.py runserver 0.0.0.0:9002