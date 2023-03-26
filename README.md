#Adco 🏠

>Just download the rest_auth/
>Create a virtual environment
>activate environment on the cmd 
`pip install -r requirements.txt` 

>Start development server:
`python manage.py runserver`

>Go to your favorite browser and test the endpoints:

`http://127.0.0.1:8000/api/` 

>This django project connects to a postgreSQL database named "adco", setup the project and run: 
`python manage.py migrate`

>Or you can connect to any other SQL DBMS by modifying "settings.py" file on rest_auth/ subdirectory
