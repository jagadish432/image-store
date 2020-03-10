# Python-Flask Image store application
This is a simple image store app with password protective and also maintains number of visits occurred for each image.

### To install the dependencies and run the application
For steps to run the application, please refer to [this file](steps.md)

### Initial DB creation
As this project is using a sqlite database, we need to create a file which can be used as storage for our database

**Note**: Please make sure you completed the above "dependencies" section to proceed further.

1 Create a file for database with the environment specific database name
```cmd
.\envs\dev
type nul>db\%DATABASE_NAME%
``` 

2 

a. Initialize the migrations folder for database related changes and information.

b. run the migrate command to generate the migration script contains DB schema(for First time) and changes in schema(from Second time onwards)

```cmd
python migrate.py db init
python migrate.py db migrate
```
c. Make any required changes in the generated migration script and run the following command
```cmd
python migrate.py db upgrade
```

### Run the application
```cmd
Python app.py
```
