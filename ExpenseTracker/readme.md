## Step by Step guide for django project.
- First create folder using command mkdir or create manually
- Setup a virtual env by Python venv <env_name>
- Now activate that `<env_name>\scripts\activate`
- Now to create a project use cmd django-admin createproject <project_name>(use . at the end if you want to make the curr dir as the project)
- Now create an app inside this Project using python manage.py startapp <app_name>
- Now configure the app in settings.py under the INSTALLED_APPS by adding the app_name at the end
- Create urls.py in the app folder to add your api end points
urlpatterns = ['',path(),name = ""]
- Include the above urls to the project by using the following command in project.urls.py
from django.urls import path,include
    url_patterns = ['',include("<app_name>.urls")]
- For each endpoint create a view to handle what that end point must do
- Create Models to interact with DB
- Configure your DB Settings in Settings.py by DATABASES variable
- To apply templates ,Create Templates folder in app
- Create the html files you want to render in the frontend using the endpoints
If thats form use the sample below

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Transaction Form</title>
</head>
<body>
    <form method="POST" action="home/">
        {% csrf_token %}
        Debit: <input name="Type" type="radio" value="Debit"> 
        <br>
        Credit: <input name="Type" type="radio" value="Credit"> 
        <br>
        Enter amount to Debit or Credit:
        <input type="number" name="Amount" required>
        <br>
        <button type="submit">Add Transaction</button>
    </form>
</body>
</html>

Cross-Site Request Forgery is a type of security vulnerability where a malicious website tricks a user's browser into performing unwanted actions on a different website where the user is authenticated.

Real-World Analogy:
Imagine you're logged into your bank account in one browser tab. In another tab, you're tricked into visiting a malicious site that secretly makes a request to your bank to transfer money—using your credentials—without your knowledge. That's CSRF.

- Inorder to make these templates accesible, change the settings.py TEMPLATES variable with the path to these templates folder 
'DIRS': [os.path.join(BASE_DIR, 'templates')]
sample is above

- To add the model and register it to our project, we need to make migrations
python manage.py makemigrations ---> shows the changes to be registered to the project 
python manage.py migrate

- Now, use cmd python manage.py runserver to see the changes

### In views,if you want to make specific view to work for a form, you need to add that in action = "" attribute in form