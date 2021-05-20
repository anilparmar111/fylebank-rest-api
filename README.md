
## Live API Demo [Link](https://fylebank-rest-rapi.herokuapp.com/)

1. Autocomplete API to return possible matches based on the branch name **ordered by IFSC code** (ascending order) with limit and offset.
    1. **Endpoint: /api/branches/autocomplete?q=<>**
    2. Example: /api/branches/autocomplete?q=**RTGS**&limit=3&offset=0
    3. Sample response:

    ```json
    {
       "branches":[
          {
             "ifsc":"ABHY0065001",
             "bank_id":60,
             "branch":"RTGS-HO",
             "address":"ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024",
             "city":"MUMBAI",
             "district":"GREATER MUMBAI",
             "state":"MAHARASHTRA"
          },
          {
             "ifsc":"ABNA0000001",
             "bank_id":110,
             "branch":"RTGS-HO",
             "address": "414 EMPIRE COMPLEX, SENAPATI BAPAT MARG LOWER PAREL WEST MUMBAI 400013",
             "city":"MUMBAI",
             "district":"GREATER BOMBAY",
             "state":"MAHARASHTRA"
          },
          {
             "ifsc":"ADCB0000001",
             "bank_id":143,
             "branch":"RTGS-HO",
             "address":"75, REHMAT MANZIL, V. N. ROAD, CURCHGATE, MUMBAI - 400020",
             "city":"MUMBAI",
             "district":"MUMBAI CITY",
             "state":"MAHARASHTRA"
          },
          {
             "ifsc":"ADCC0000001",
             "bank_id":61,
             "branch":"RTGS-HO",
             "address": "THE AKOLA DISTRICT CENTRAL COOP. BANK LTD., P.B.NO. 8, CIVIL LINES, S.A. COLLEGE ROAD, AKOLA. 444001",
             "city":"AKOLA",
             "district":"AKOLA",
             "state":"MAHARASHTRA"
          }
       ]
    }
    ```
- **Endpoint: /api/branches/autocomplete?q=<>**

- **Example: /api/branches/autocomplete?q=**RTGS**&limit=3&offset=0**

```json
{
   "branches":[
      {
         "ifsc":"ABHY0065001",
         "bank_id":60,
         "branch":"RTGS-HO",
         "address":"ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024",
         "city":"MUMBAI",
         "district":"GREATER MUMBAI",
         "state":"MAHARASHTRA"
      },
      {
         "ifsc":"ABNA0000001",
         "bank_id":110,
         "branch":"RTGS-HO",
         "address": "414 EMPIRE COMPLEX, SENAPATI BAPAT MARG LOWER PAREL WEST MUMBAI 400013",
         "city":"MUMBAI",
         "district":"GREATER BOMBAY",
         "state":"MAHARASHTRA"
      },
      {
         "ifsc":"ADCB0000001",
         "bank_id":143,
         "branch":"RTGS-HO",
         "address":"75, REHMAT MANZIL, V. N. ROAD, CURCHGATE, MUMBAI - 400020",
         "city":"MUMBAI",
         "district":"MUMBAI CITY",
         "state":"MAHARASHTRA"
      },
      {
         "ifsc":"ADCC0000001",
         "bank_id":61,
         "branch":"RTGS-HO",
         "address": "THE AKOLA DISTRICT CENTRAL COOP. BANK LTD., P.B.NO. 8, CIVIL LINES, S.A. COLLEGE ROAD, AKOLA. 444001",
         "city":"AKOLA",
         "district":"AKOLA",
         "state":"MAHARASHTRA"
      }
   ]
}
```
## API Development And Deployment Django + Postgres + Heroku Deployment

REST API Is Develop Using Rest_Framwork Of Django
For DataBase I Have Used Postgres
## Step 01: requirements
```
pip install whitenoise
pip install gunicorn
pip install dj-database-url
pip install django-cors-headers
pip install psycopg2
```
Create two files in the project root.
```
Procfile
runtime.txt
```
Here is my current directory structure
```
.
├── Procfile
├── apps
├── manage.py
├── myproject
├── requirements.txt
└── runtime.txt
```
Let's freeze the requirements.txt file
```
pip freeze -> requirements.txt
```
We Can see something like this:
```
asgiref==3.3.4
dj-database-url==0.5.0
dj-static==0.0.6
Django==3.2.3
django-cors-headers==3.7.0
django-heroku==0.3.1
django-toolbelt==0.0.1
djangorestframework==3.12.4
gunicorn==20.1.0
psycopg2==2.8.6
pytz==2021.1
setproctitle==1.2.2
sqlparse==0.4.1
static3==0.7.0
whitenoise==5.2.0
```



## Step 02: Enable Middlware 
Edit  ```settings.py``` file and add CorsMiddleware to the ```MIDDLEWARE``` list. Order Of MIDDLEWARE Must Be Followed Other Wise When We Use That API In Our Then We Gate Error Of CORS Header.
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
Add ```CORS_ORIGIN_ALLOW_ALL``` before the ```ROOT_URLCONF```
```python
CORS_ORIGIN_ALLOW_ALL = True
ROOT_URLCONF = 'myproject.urls'
```

## Step 03: edit Heroku required files
Edit the ```Procfile``` file in the project root with the following content
```
web: gunicorn <project_name>.wsgi --log-file -
```
Web: gunicorn is necessary For Deployment. But For Windows User When We Deploye It Localy Then We Have To Add
'''
web: python manage.py runserver <project_name>.wsgi localhost:post
'''
Edit the ```runtime.txt``` file in the project root with the following content, For example, I'll be using Python 3.8.10
```
python-3.8.10
```


## Step 04: database configuration
We use the ```dj-database-url``` library to extract database configurations from the environment.
For Django applications, a Heroku Postgres hobby-dev database is automatically provisioned. This populates the ```DATABASE_URL``` environment variable.

To set up the database, we will add the following code in ```settings.py```:
```python
import os
import dj_database_url
```
After the databases setting add the following 
```python
DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
}

```

## Step 05: Deployment Settings
Alright, enough configuration. Let’s get the deployment started. First, let's initialize our gitrepo in the In your project root
```
git init
```
Take a look at what files we have to be committed to ```git```
```
git status
```
Some of these files we don’t want to track in git. some of them can be created each time When We run the program, so it is a waste of space and distracting to check them into git. To handle this, we create a file called .gitignore in the base directory of our project. Then, we write the file or folder names or paths that we want to exclude from git.
```
git add .
git commit -m "Initial commit"
code .gitignore

```
add the following to the ```.gitignore``` file
```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Django stuff:
*.log
local_settings.py




# mypy
.mypy_cache/

# vscode
.vscode/
```



## Step 06: sign up on Heroku and install the Heroku
Heroku actually uses a cli to control their deployments. So let’s install it.
Download And Install Heroku
Now, we need to “log in” to the local cli. This command will ask for your credentials.

```
heroku login
heroku create <app_name>
```

Now let's setup the databases. The following commands create postgresql database on heroku for you app and fetch its url.
```
heroku addons:create heroku-postgresql:hobby-dev
heroku config -s | grep DATABASE_URL
```
After That From The Heroku DashBoard We Can Get Name,User,password,host Of Database.
We Have To Add That Data In To Our settings.py File


## Step 07: building the app locally
Run the following command to test Heroku deployment locally. Make sure you're the root of the project.
```
heroku local web
```
Remember If You Are Windows User Then For Building App Locally(Only For Building App Localy For Deploying We Have To Use web : Gunicorn) We Have To Use This In Procfile
```
web : Python manage.py runserver <app_name>.wsgi localhost:post
```
This will run the Procfile and consequently you can debug any errors if any on your local machine. You should see an output similar to this.

Now visit http://localhost:5000 and see if you can see the Django application.

## Step 08: db migration, commit and collect static
Let's run the db migrations
```
heroku run python manage.py migrate
heroku run python manage.py makemigrations
```
```
heroku run python manage.py createsuperuser
```
```
heroku run python manage.py migrate
```


## Step 09:
Finally, we are now ready to deploy our application. Follow these steps to successfully deploy to Heroku.
Commit all changes to git.
```
git add .
git commit -m "deployment ready"
git push heroku main
heroku open
```
## Step 10(Not Necessary) :
If We Connect Heroku With Github Repo Then We Get Benifit Of Auto Deployment Wen There Is New Coomit.


