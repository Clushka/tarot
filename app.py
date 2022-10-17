from xmlrpc.client import ResponseError
from flask import Flask, render_template, request, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import requests
import json
from sqlalchemy.sql import exists  

app = Flask(__name__)
# creating an API object
api=Api(app)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:admin@localhost/tarot'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db=SQLAlchemy(app)


class Data(db.Model):
        __tablename__="names" 
        id=db.Column(db.Integer, primary_key=True)
        sign=db.Column(db.String(120))
        date=db.Column(db.Date)
        description = db.Column(db.String(600))
        date_range = db.Column(db.String(600))

    
        def __init__(self, sign, date, description,date_range):
                self.sign=sign
                self.date=date
                self.description=description
                self.date_range=date_range


@app.route('/', methods=['GET', 'POST'])
def index():

        # exists = db.session.query(
        #     db.session.query(Data).filter_by(sign="Leo").exists()
        # ).scalar()

        if request.method=='POST':

            sign=request.form.get('sign')
            date=request.form.get('date_type')
            print(sign, date)
            

            url = "https://sameer-kumar-aztro-v1.p.rapidapi.com/"

            querystring = {"sign": sign,"day":"today"}

            headers = {
                "X-RapidAPI-Key": "0459c6f8a8mshc3aaf65a2576dc5p19c1b1jsndc488967f473",
                "X-RapidAPI-Host": "sameer-kumar-aztro-v1.p.rapidapi.com"
            }

            response = requests.request("POST", url, headers=headers, params=querystring)

            # {'date_range': 'Sep 23 - Oct 22', 'current_date': 'October 16, 2022',
            # 'description': "Still shopping? Still getting crazy with the charge cards? Well, it might be time to stop that nonsense 
            # -- just for a day or two. If you're not sure you can manage it, hire a bodyguard. A charge-guard, so to speak.", 
            #  'compatibility': 'Pisces', 'mood': 'Productive', 'color': 'Silver', 'lucky_number': '81', 'lucky_time': '6pm'}
            
            date_range = response.json()["date_range"]
            description = response.json()["description"]

        
            data=Data(sign, date, description, date_range)
            db.session.add(data)
            db.session.commit()

            print(data)

    
            return render_template("1card.html", sign=sign, date=date, description=description, date_range=date_range)


        
        return render_template('index.html')
        
with app.app_context():
    db.create_all()        

if __name__ == '__main__':
    db.create_all()
    app.debug=True
    app.run()