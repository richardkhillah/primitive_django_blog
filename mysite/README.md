# primitive_django_blog

A very primitive blog site for learning purposes.

An authenticated user can add, update, and delete posts and comments. A post is considered a draft until it is published.

## Getting started
This project is not published on the wonderful world wide web, so one must run a local server to execute the program.


1. Download or cloan this repo. If you haven't already, open a command prompt and change into the directory containing this file.
2. Create a virtual environment. Run the line

`$ python -m venv venv`

This command will create a directory called "venv". It is good practice to use a virtual environment to ensure any change you make to run this application do not affect the rest of your operating system. 

3. Run the virtual environment using the following command

`$ source venv/bin/active`

Once you run this commeand, your command prompt should reload with a `(venv)` prefixed to each input line. For example, after running this command, my terminal shows:

`(venv) richardkhillah@Richards-MacBook-Air mysite %`

Note: unless you have changed your .bash, .profile, etc... file, or altered terminal settings in some meaningful way, this virtual environment should be limited to the scope of the window you ran the "source" command. 

You can similarly deactivate the virtual environment simply with:

`(venv) $ deactivate`

You can also just close the terminal window.

4. Install the packages required to run this program.

`(venv) $ pip install -r requirements.txt`

Note: This assumes that pip is installed. If pip, for whatever reason, is not installed in the virtual environment, you will need to install it. It is also quite possible also that python/pip will spit out upgrade warnings. Heed them or ignore them, the choice is yours.

5. Change into the "mysite" directory. The current state of the application only works with superusers on the account. (Not the best design, I know, the next project will be much better.)
6. Create database migrations and create a superuser:
```
(venv) mysite $ python manage.py makemigrations
...
(venv) mysite $ python manage.py migrate
...
(venv) mysite $ python manage.py createsuperuser
Username (leave blank to use 'richardkhillah'): testuser
Email address: test@gmail.com
Password:
Password (again):
Superuser created successfully.
```

7. Start a localhost development server

```
(venv) mysite $ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 15, 2022 - 01:56:41
Django version 4.1.4, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

The output will tell you "where" the application is running, here it is `http://127.0.0.1:8000/`.

8. Use an internet browser to navigate to the development server url.

<img width="1215" alt="landing" src="https://user-images.githubusercontent.com/25072000/207754841-1e7851fb-608d-4cce-88ff-dce82254c675.png">

**Notes:** 

1. When setting the password while creating a superuser, you will *not* be able to see characters as you type them. This is correct.
2. In the real world, the creation of a superuser should be done judiciously. The correct way of making a user for this program would be to create a user for the post.

## Playing around
Once you login, you can create, edit, and remove posts, add and remove comments, etc. Post and Comment body text can be formatted

<img width="1215" alt="format_popup" src="https://user-images.githubusercontent.com/25072000/207756059-187c54c2-7b4d-4942-abcc-721852287a52.png">

