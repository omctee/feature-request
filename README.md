# Feature Request Application 

This app will allow you to create and view feature requests for your customers. 
#The Online version of this app is deployed here -> https://frequest.herokuapp.com/

Default login:

```bash
  Username: login
  Password: login
```
# Pre-requisite

```bash
The app uses the following  dependencies:
- Python 3.6+
- ES6
- KnockoutJS (for DOM manipulation)
- Bootstrap (for the front-end)
```
# To run the project on your local machine:
 - [Python 3.6](https://www.python.org/downloads/) or higher installed on your machine.

# Next, open up a command interface and clone the project:

  $ git clone https://github.com/omctee/feature-request.git


# Then change your current location to the project root folder:
```
  $ cd feature-request-master
```
# Create a virtual environment:
```bash
  $ python3 -m venv env
  #or
  $ python -m venv env
```
The command to use depends on which associates with your Python 3 installation.

Then, activate the virtual environment: (linux)

```
    $ source env/bin/activate
```
To use in Windows, activate the virtualenv with the below command:
```
  [path_to_Python_install_path]\Scripts\activate
```
#This is meant to be a full path to the activate script. Replace `[path_to_Python_install_path]` with  your Python installed path name.

# Install the required dependencies:
```
  $ pip install -r requirements.txt
```

# Next, run the migration and populate the database with some data:
```bash
  - python run.py db init 
  - python run.py db migrate 
  - python run.py db upgrade
  - python run.py populate
```
# Start up the server:
```
  $ python run.py runserver
```
A web server should be active and accessible from http://127.0.0.1:5000/  

The default login credential is:
The logic for the login credential is located in ``populate.py``.

```bash
Username: login
Password: login
```
