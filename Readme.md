# Deploying your ML Model in the Cloud

### Setting up your ML Model as a Web Service in Heroku

**Code setup steps**
1. setup your development environment in a virtual environment on your local machine
2. Implement your model as a Flask web service
3. Setup the solution a wsgi web service - you require gunicorn python package
4. Create a file called Procfile in your application root folder place the single line below in it. See sample Procfile in uploaded gitfolder
   > web: gunicorn wsgi:app
5. create a runtime.txt folder and specify the python version you would be using it e.g. python-3.9.1 (required to the Heroku what python version service you want)
6. you need a requirements.txt file containing the list of python packages. you can do this by running pip freeze > requirements
7. Create the wsgi.py awith the content as shown in the sample wsgi.py



**Setting up on web service on  Heroku App**
1. log into Heroku 
2. Create your App 
3. Select the deployment method Heroku Git or GitHub and follow the instructions Heroku provides.

Refer to the reference materials for more details

References:
-  https://www.freecodecamp.org/news/deploy-your-machine-learning-models-for-free/
-  Hosting your Web API  in Heroku :https://www.freecodecamp.org/news/end-to-end-machine-learning-project-turorial/
-  Specifying the Python runtime version - https://devcenter.heroku.com/articles/python-runtimes
