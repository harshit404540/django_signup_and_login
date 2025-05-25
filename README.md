# django_signup_and_login
Normal Signup and Login working webpages using Django

This web app has been developed using the popular Django framework . My motivation to build this project is so that I can learn about Django and tighten up my skills. This mini-app can be easily integrated into a bigger system projects.

### Basic Features of The App
    
* Register – Users can register.
* Login - Registered users can login using username and password
* Messages visibility - Error messages / Success messages will be shown.

### Quick Start
To get this project up and running locally on your computer follow the following steps.
1. Set up a python virtual environment
2. Run the following commands
```
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
Open your Browser and Type 127.0.0.1:8000(Default Port)

### For Mail
1. Go to google account manager
2. Make sure your 2-step verification is on
3. Search app password
4. Creat app (name it Mail)
5. Copy and Paste the 16 character password to EMAIL_HOST_PASSWORD = 'Your_app_password' in first/settings.py
