# Some useful shell commands:
#
# req () {
# 	bin/pip install -r deploy/requirements.txt
# }
# 
# syn () {
# 	rm *.db
# 	python manage.py syncdb
# 	python manage.py syncdb --settings=settings_test
# 	python manage.py loaddata test
# }
# 
# ser () {
# 	python manage.py runserver 0.0.0.0:8000 --adminmedia=static/admin
# }
# 
# she () {
#     python manage.py shell
# }
# 
# har () {
#     python manage.py harvest --settings=settings_test -d $*
# }
# 
