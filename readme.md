# Mega App Project Backend
This codebase is for the Mega App project backend. 
It is a Django codebase.

To run the app on your computer, follow the steps:
1. Clone the repository to your local machine.
2. Move to the repository's directory on your machine
3. Activate a virtual environment. You can use python's 
    inbuilt tool by running the command:
    `python venv -m {{ NAME OF VIRTUAL ENVIRONMENT }}`.
4. Install the requirements (specified in the 
    requirements.txt file) with pip using the command:
    `pip install -r requirements.txt`.
5. Next, you need to add some variables to your environment.
    The sensitive data used were saved in the environment 
    variables and read to the app on runtime. 
    You can find the keys in the
    **mega_backend/settings.py** file. You need to create
    these keys on your environment along with appropriate 
    values.
6. Finally, start the Django server with the command:
    `python manage.py runserver 0.0.0.0:9000`.

## Admin Console
There is a builtin admin console located at 
**0.0.0.0:9000/admin/**.
In order to access the admin console, you will need an admin user.
You can create an admin user by running the command 
`python manage.py createsuperuser` in the root directory 
of the codebase. 
Login to the admin console with the username and password used.
You can administer the app from here.
If there is no data in the app, run the population script 
using the command `python pop_script.py` 

## Developer Console
Developers can create features and manage their features by
visiting the URL: **0.0.0.0:9000/developer/**.
Login is required.
You can login as a super user.
If you do not have a super user account nor a regular account,
you can create a regular account through the Mega App.
After login, a web interface can be used to manage features.


## How to write feature code
On the form for creating features,
the feature code field refers to the configuration code used
to render the feature on the frontend.
It is advisable to write the code using a map-like data 
structure in a programming language and using a script to 
convert the map to JSON. A JS script is included in 
developers guide accompanying this project. 
The instructions to write feature code are 
also available there.

## API endpoints
The API endpoints can be found in the **documentation**.

## Documentation
Documentation homepage can be found in 
**docs/_build/html/index.html**

 
    