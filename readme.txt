Jobcy Installation in Django Python
Python Version >> 3.8.10
Django Version >> 3.2.7
Bootstrap Version >> 5.1.1
>>>Installation Python
 ->https://www.python.org/downloads/
>>For Windows OS 
 -Download python  from windows store
 -Select the Python's version to download.
 -Click on the Install Now
 -Installation in Process
>>For Linux OS
 -sudo apt update
 -sudo apt install python3

>>>Note: Depending on your installation, you may need to use either pip3 or pip and for python you may need to use either python3 or python.

>>>Open terminal
 -python --version
 
>>>To check pip version  
  -py -m pip --version
  -upgread pip 
  -py -m pip install --upgrade pip
>>>Installing virtualenv   
  #linux & mac os
   ->python3 -m pip install --user virtualenv
  #Windows
  ->py -m pip install --user virtualenv
>>>Create Virtual Environment
  #linux & mac os
  ->python3 -m venv environment_name
  #Windows
  ->python -m venv environment_name
>>>Activate Environment
  #Linux & mac os
  ->source environment_name/bin/activate
  #Windows
  ->environment_name\Scripts\activate
 
>>>Install Django
 #linux & mac os
 ->pip3 install django
 #Windows
 ->pip install django
 
>>>First please check Django properly Installed or not
 #Linux/macOS
 python3 -m django --version
 #Windows
 python  -m django --version

>>>Open terminal 
 -Goto project directory using cd command

>>>Nodejs
->Make sure to have the Node.js installed & running in your computer

>>>Yarn
->Make sure to have the yarn installed & running in your computer

>>>gulp     
->Make sure to have the gulp installed & running in your computer

>>>Git
->Make sure to have the git installed globally & running in your computer

-->Now you can just run command `gulp`

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.#databaseservername#',
        'NAME': 'Your Database Name',
        'USER' : 'Database User Name',
        'PASSWORD' : 'Your Password',
        'HOST' : "Write down Host",
        'PORT' : 'Write down port',
                
    }
}

-Goto settings.py of Main Directory
-SMTP CONFIGURATION
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'YOUR EMAIL ADDRESS'
    EMAIL_HOST_PASSWORD = 'YOUR HOST Password'
    DEFAULT_FROM_EMAIL = 'YOUR EMAIL ADDRESS'
    SERVER_EMAIL = 'YOUR EMAIL ADDRESS'

>>>To load Static Files:-
>Go to Jobcy/setings.py
-Add following command:-
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]

>Run Command In Terminal
-python manage.py collectstatic
-Goto settings.py of Main Directory


#######To Set Default Color#########
 >Goto src/js/pages/switcher.init.js
<!--===========================================================================-->
                        <!--Color Mode -->
<!--===========================================================================-->
#Make changes according choice at Line No 29
1.Green 
color = "green"
2.Blue
color = "blue"
3.Purple 
color = "purple"
 
<!--===========================================================================-->
>> To set Default light/dark/RTL Mode
<!--===========================================================================-->
>>Go src/js/pages/switcher.init.js
-line number 47
<!--===========================================================================-->
>For Light theme
var mode = 'light'
>For Dark theme
var mode = 'dark'
<!--===========================================================================-->
<!--===========================================================================-->

###########To Set Default home page ############

 follow this steps:
>>Goto  jobcy/urls.py
:-At line number 24
--Use following line 
>for index 1
path('', views.Index.as_view(),name='index'),

>for index 2
path('', views.Index2.as_view(),name='index'),

>for index 3
path('', views.Index3.as_view(),name='index'),

-> Windows:-python manage.py migrate
-> Linux:-python3 manage.py migrate
>>>Run your project
-Windows:-python manage.py runserver
-Linux:-python3 manage.py runserver