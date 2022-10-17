# tarot

- Oracul -
Oracle is a website that gives out a daily horoscope for each zodiac sign.

- Installation -

Version of Python: Python 3.10.6
Version of pgAdmin 4: PostgreSQL 13/14

Terminal requarements:

pip install flask

pip install psycopg2
for(macos) pip install psycopg2-binary

pip install sqlalchemy

pip install flask-sqlalchemy

pip install flask-restful

pip install requests


- pgAdmin 4 requarements -:
1. If you do not already have the software, download PostgreSQL and pgAdmin and install them.
2. Run pgAdmin.
3. Right-click on the item Databases, select Create -> Database. Name your Database in the Database input field. Set owner and click Save afterwards.
5. Now reach to a Database,right click on "tables" and click on "New Table". This will open a new window to create a New Table. Supply a name of your new table and then click Save.
6. Open the PostgreSQL 14 and CREATE NEW DATABASE and CALL IT "tarot"". Open the tarot database >>> Schemas >>> Tables >> right click and click Query Tool:


- Examples for use -:
Run app.py.
Click localhost in the terminal, and the program will open your browser.
You need to paste your zodiac sign and choose the date you want and click on the button submit. After clicking on the site, information about the sign that you entered earlier and a description with the date range will be displayed.

![2022-10-17 15 51 30](https://user-images.githubusercontent.com/97032059/196147391-7b56c10e-95d0-4729-bff3-9cc55cc7983c.jpg)


