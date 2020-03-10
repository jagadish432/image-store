

## steps to run this application

1. cd <your_project_directory_root>

2. virtualenv venv

3. venv\Scripts\activate

4. pip install -r requirements.txt

6. .\envs\dev ("dev" for "development" environment, "prod" for "production" environment, etc..)

7. Clear the database dependencies by running the "Database migration commands" mentioned in the [README.md](README
.md) file

8. python main.py


## update requirements.txt
If you've installed any other packages apart from requirements.txt then update your requirements.txt file by running
 the below command.
```bash
"pip freeze > requirements.txt"
```


