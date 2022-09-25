## Online Polls And Surveys for Kasetsart University
Kasetsart University's web application for polls and surveys. Django is a Python framework [Django Tutorial Project](https://docs.djangoproject.com/en/4.1/intro/tutorial01/).

This application is part of the [Individual Software Process](https://cpske.github.io/ISP) course at Kasetsart University.

## Install and Run
1. Clone this repository

``` 
git clone https://github.com/dzptahh/ku-polls.git
```
```
cd ku-polls
```

2. You need to install required package

```
pip install -r requirements.txt
```
3. Don't forget to change file name `sample.env` to `.env`
4. Before run the server, run migrations first
```
python manage.py migrate
```
5. Install data
```
python manage.py loaddata data/polls.json data/user.json
```

6. Then run the server. You can run by using
```
python manage.py runserver
```
The server : `http://127.0.0.1:8000/`

## Project Documents
All project documents are in the [Project Wiki](../../wiki/Home)
+ [Vision Statement](../../wiki/Vision%20Statement)
+ [Requirements](https://github.com/dzptahh/ku-polls/wiki/Requirements)
+ [Project Plan](https://github.com/dzptahh/ku-polls/wiki/Development-Plan)
+ [Iteration 1 Plan](../../wiki/Iteration-1-Plan)
+ [Iteration 2 Plan](../../wiki/Iteration-2-Plan)
+ [Iteration 3 Plan](../../wiki/Iteration-3-Plan)
+ [Iteration 4 Plan](https://github.com/dzptahh/ku-polls/wiki/Iteration-4-Plan)

| Username  | Password  |
|-----------|-----------|
|   test11  | fortest11|
|   test22   | fortest22 | # wait for update
