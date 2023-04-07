# Anonymous Confessions API

An very simple API i made to try out django rest framework.


# Installation
Clone the repo and run.
```cmd
git clone https://github.com/Jedddy/anonymous-confessions-api

cd anonymous-confessions-api

pip install -r requirements.txt

python manage.py runserver
```


## Routes
```
GET
    confessions/ - `Get a list of confessions`
    confessions/<id> - `Get a specific confession`
POST
    confessions/ - `Submit a confession`
```

## Admin
Create a super user by doing
```
python manage.py createsuperuser
```

After creating a super user, log in to `/admin` route.


## Submitting a Confession
```py
import requests

r = requests.post("http://127.0.0.1:8000/confessions/", json={"title": "Hello", "confession": "World"})
print(r.json())
```