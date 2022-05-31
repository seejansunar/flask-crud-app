# flask-crud-app

```
git clone https://github.com/seejansunar/flask-crud-app.git
```

```
cd flask-crud-app
```

```
virtualenv env
```

```
source env/Scripts/activate
```

```
pip install -r requirements.txt
```

After the app is completed:
  - run ```pip freeze > requirements.txt```
  - create **Procfile**. Add ``` web: gunicorn app:app ``` to it.

Inorder to deploy the app to Heroku, run these commands one after another
```
heroku login

git init
git add .
git commit -m "initial commit"
git remote -v
git push origin main/master
```
