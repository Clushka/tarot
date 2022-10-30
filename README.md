# tarot

- Oracul

Oracul is a website that gives out a daily horoscope for each zodiac sign.

- Installation

Version of Python: Python 3.10.6
Version of pgAdmin 4: PostgreSQL 13/14

- Terminal requarements:

pip install flask

pip install psycopg2
for(macos) pip install psycopg2-binary

pip install sqlalchemy

pip install flask-sqlalchemy

pip install flask-restful

pip install requests

pip install -U Flask-WTF

pip install flask-wtf

pip install wtforms-validators

pip install email_validator

pip install bcrypt


- pgAdmin 4 requarements:
1. If you do not already have the software, download PostgreSQL and pgAdmin and install them.
2. Run pgAdmin.
3. Right-click on the item Databases, select Create -> Database. Name your Database in the Database input field. Set owner and click Save afterwards.
5. Now reach to a Database,right click on "tables" and click on "New Table". This will open a new window to create a New Table. Supply a name of your new table and then click Save.
6. Open the PostgreSQL 14 and CREATE NEW DATABASE and CALL IT "tarot"". Open the tarot database >>> Schemas >>> Tables >> right click and click Query Tool:


- Examples for use:

Run app.py.
Click localhost in the terminal, and the program will open your browser.
You need to paste your zodiac sign and choose the date you want and click on the button submit. After clicking on the site, information about the sign that you entered earlier and a description with the date range will be displayed.

<img width="1440" alt="Снимок экрана 2022-10-31 в 02 03 31" src="https://user-images.githubusercontent.com/97032059/198899311-9e36a8c7-e831-42af-ae1b-d2c86d1bf1f5.png">

<img width="1440" alt="Снимок экрана 2022-10-31 в 02 06 49" src="https://user-images.githubusercontent.com/97032059/198899376-9d6974f1-9854-42e3-b16a-2afce6f8dd57.png">

<img width="1440" alt="Снимок экрана 2022-10-31 в 02 06 59" src="https://user-images.githubusercontent.com/97032059/198899387-3dcda393-5011-4c1d-92d5-d51e7047a42e.png">

<img width="1440" alt="Снимок экрана 2022-10-31 в 02 07 21" src="https://user-images.githubusercontent.com/97032059/198899397-39a40d34-31b9-4d42-858c-cfb4bc450da8.png">







