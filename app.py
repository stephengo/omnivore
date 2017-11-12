import os
from flask import Flask,render_template, request,json, redirect, url_for,session
import pandas as pd
from sqlalchemy import create_engine
import re
from werkzeug import secure_filename
import requests
import codecs

def send_welcome_message(rec_email):

    page =  codecs.open('./output.html').read()
    page = page.replace('\n','')
    print(page)
    # try to read an HTML file and put the HTML stuff in the variable
    return requests.post(
        "https://api.mailgun.net/v3/sandbox13724108971f4d0d8fb22ef48761a6b4.mailgun.org/messages",
        auth=("api", "key-49261d59430638911cc8337471cc82a9"),
        data={"from": "Travoquest <postmaster@sandbox13724108971f4d0d8fb22ef48761a6b4.mailgun.org>",
              "to": rec_email,
              "subject": "Travoquest Daily Digest",
              "text": "Travoquest",
              "html": page})

app = Flask(__name__)

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


engine = create_engine('mysql+pymysql://administrator:REaiTomorrow2017@reaidev1.chs96ez82dwu.us-east-1.rds.amazonaws.com:3306/Property')
user_engine = create_engine('mysql+pymysql://administrator:REaiTomorrow2017@reaidev1.chs96ez82dwu.us-east-1.rds.amazonaws.com:3306/User')



def get_vals(temp):
    for index, row in temp.iterrows():
        print row['FullStreetAddress'], row['SalePrice']

@app.route('/')
def hello():
    return render_template('index_m.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot_demo.html')
@app.route('/newhome')
def hello1():
    return render_template('index_m.html')

@app.route('/howitworks')
def howitworks():
    return render_template('howitworks.html')




@app.route('/test')
def test():
    return render_template('test_index.html')

@app.route('/home_page')
def home_page():
    return render_template('signUp.html')

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/uploader',methods=['GET', 'POST'])
def uploader():
    # print(request.form['emailsubmit'])
    print(request.json['post'], request.json['selected_vals'])

    df = pd.read_csv('info.csv')
    df.loc[-1]= [request.json['post'], request.json['selected_vals']]
    df.to_csv('info.csv', index=False)
    
    print('finished going  through the uploader function')

    # send_complex_message()  
    send_welcome_message(request.json['post'])
    return 'suceess!!'

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080,debug=True)
