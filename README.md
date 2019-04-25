# CSforSAC

## How to get set up:

1. Clone the repo into your own directory.
	
	 	git clone https://github.com/ejprok/senior_project.git

2.  Go into the repo's directory. 

		cd senior_project

3.  Create a virtual environment for Python.  This is so that the project has its own version of python to install dependencies to.  This makes it so that you don't install dependencies systemwide.  We are using python3.

	 	virtualenv -p python3 venv

4.  After creating the virtual environment, you need to activate it.  This is something that you will need to do everytime you want to run the project or install dependencies.  

	 	. venv/bin/activate

5.  Now install the dependencies required for the project.  We have them listed in a file called "requirements.txt". Pip will use this text file to look for the dependencies that it needs and will install what it needs to.

		pip install -r requirements.txt

6.  Go into the Django project's directory.

		cd csforsac

7.  Run migrations to build your database.

		python manage.py migrate

8.  Run the actual project.  Replace "YOUR_PORT_NUM" with the port number assigned to you.  

		python manage.py runserver 0:YOUR_PORT_NUM

9.  Test to see if you can visit the website by visiting 50.116.12.68:YOUR_PORT_NUM in your browser.


## Update your Database

To stay updated with the current live demo's database, use this script to copy the database into your project.  It will overwrite your current database.  From the root directory of the project, use these commands.

1.  Go into the scripts directory

		cd scripts/

2.  Run the script

		./copy_db.sh 
		
		
## Fix Migration Issues

If you are having trouble with migrations after creating new models or pulling in recent changes, here are some steps to try to resolve the issues.

1.	You should first comment out any new model classes that you are trying to create.  

2.	You should also delete all of the migration files in the app that you are having issues with (ex Home, Blog, Events). Make sure that there is still an "__init__.py" file in the migrations directory, otherwise you wont be able to migrate.  If you understand why the migrations are causing an issue, you could edit the migration files instead.

		cd csforsac/<app_name>/migrations/
		
		rm *.py
		
		touch __init__.py
		
3.	Go back to the directory where manage.py is located, and makemigrations.

		./manage.py makemigrations
		
4.	Migrate the db, but with the fake option.

		./manage.py migrate --fake
		
5.	If you had any new models that you commented out, go ahead and uncomment them and makemigrations.

		./manage.py makemigrations
	
6.	You should finally be able to properly migrate your db.

		./manage.py migrate
	

