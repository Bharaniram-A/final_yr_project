# main.py
import os
import base64
import io

from flask import Flask, render_template, Response, redirect, request, session, abort, url_for
import mysql.connector
import hashlib
from datetime import datetime
from datetime import date
import datetime
import random
from random import seed
from random import randint
from urllib.request import urlopen
import webbrowser

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from werkzeug.utils import secure_filename
from PIL import Image
#import stepic
import urllib.request
import urllib.parse
#import pulp


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  charset="utf8",
  database="appointment_scheduling"

)
app = Flask(__name__)
##session key
app.secret_key = 'abcdef'
#######
UPLOAD_FOLDER = 'static/upload'
ALLOWED_EXTENSIONS = { 'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#####

    
@app.route('/', methods=['GET', 'POST'])
def index():
    msg=""
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()

    return render_template('index.html',msg=msg,title=title)

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg=""
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    
    if request.method=='POST':
        uname=request.form['uname']
        pwd=request.form['pass']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM ho_user WHERE uname = %s AND pass = %s', (uname, pwd))
        account = cursor.fetchone()
        if account:
            session['username'] = uname
            return redirect(url_for('userhome'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('login.html',msg=msg,title=title)

@app.route('/login_hos', methods=['GET', 'POST'])
def login_hos():
    msg=""
    act=request.args.get("act")
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    if request.method=='POST':
        uname=request.form['uname']
        pwd=request.form['pass']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM ho_staff WHERE uname = %s AND pass = %s', (uname, pwd))
        account = cursor.fetchone()
        if account:
            session['username'] = uname
            return redirect(url_for('staff_home'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('login_hos.html',msg=msg,act=act,title=title)

@app.route('/login_nur', methods=['GET', 'POST'])
def login_nur():
    msg=""
    act=request.args.get("act")
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    if request.method=='POST':
        uname=request.form['uname']
        pwd=request.form['pass']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM ho_nurse WHERE uname = %s AND pass = %s', (uname, pwd))
        account = cursor.fetchone()
        if account:
            session['username'] = uname
            return redirect(url_for('nur_home'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('login_nur.html',msg=msg,act=act,title=title)

@app.route('/login_admin', methods=['GET', 'POST'])
def login_admin():
    msg=""
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    
    if request.method=='POST':
        uname=request.form['uname']
        pwd=request.form['pass']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM ho_admin WHERE username = %s AND password = %s', (uname, pwd))
        account = cursor.fetchone()
        if account:
            session['username'] = uname
            return redirect(url_for('admin'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('login_admin.html',msg=msg,title=title)


@app.route('/login_doc', methods=['GET', 'POST'])
def login_doc():
    msg=""
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    
    if request.method=='POST':
        uname=request.form['uname']
        pwd=request.form['pass']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM ho_doctor WHERE uname = %s AND pass = %s', (uname, pwd))
        account = cursor.fetchone()
        if account:
            session['username'] = uname

            
            return redirect(url_for('doc_home'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('login_doc.html',msg=msg)



@app.route('/register', methods=['GET', 'POST'])
def register():
    msg=""
    mess=""
    email=""
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT max(id)+1 FROM ho_user")
    maxid = mycursor.fetchone()[0]
    if maxid is None:
        maxid=1
    patid="PT"+str(maxid) 
    now = datetime.datetime.now()
    rdate=now.strftime("%d-%m-%Y")
    
    
    if request.method=='POST':
        name=request.form['name']
        gender=request.form['gender']
        dob=request.form['dob']
        
        mobile=request.form['mobile']
        email=request.form['email']
        address=request.form['address']
        parent_mobile=request.form['parent_mobile']
        aadhar=request.form['aadhar']
        #blood_grp=request.form['blood_grp']
        
       
        pass1=request.form['pass']
       
        mycursor.execute('SELECT count(*) FROM ho_user WHERE aadhar=%s', (aadhar,))
        cnt = mycursor.fetchone()[0]
        if cnt==0:
            mycursor.execute("SELECT max(id)+1 FROM ho_user")
            maxid = mycursor.fetchone()[0]
            if maxid is None:
                maxid=1
    
            sql = "INSERT INTO ho_user(id,name,gender,dob,mobile,email,address,parent_mobile,aadhar,blood_grp,uname,pass,rdate,stype) VALUES (%s,%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)"
            val = (maxid,name,gender,dob,mobile,email,address,parent_mobile,aadhar,'',patid,pass1,rdate,'register')
            mycursor.execute(sql, val)
            mydb.commit()            
            
            msg="success"
 
        else:
            mycursor.execute('SELECT * FROM ho_user WHERE aadhar=%s', (aadhar,))
            dd = mycursor.fetchone()
            patid=dd[10]
            mycursor.execute("update ho_user set name=%s,gender=%s,dob=%s,mobile=%s,email=%s,address=%s,parent_mobile=%s,pass=%s,stype='register' where aadhar=%s",(name,gender,dob,mobile,email,address,parent_mobile,pass1,aadhar))
            mydb.commit()
            msg='success'

        mess="Dear "+name+", Patient ID: "+patid+", Password: "+pass1
            
    return render_template('register.html',msg=msg,title=title,patid=patid,mess=mess,email=email)





@app.route('/admin', methods=['GET', 'POST'])
def admin():
    msg=""
    mess=""
    email=""
    act=request.args.get("act")
    if 'username' in session:
        uname = session['username']
    
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_hospital')
    data = mycursor.fetchall()

    mycursor.execute("SELECT max(id)+1 FROM ho_hospital")
    maxid = mycursor.fetchone()[0]
    if maxid is None:
        maxid=1
    if request.method=='POST':
        name=request.form['name']
        mobile=request.form['mobile']
        address=request.form['address']
        email=request.form['email']
        uname=request.form['uname']
        pass1=request.form['pass']
        
     

        mycursor.execute("SELECT count(*) FROM ho_hospital where uname=%s",(uname,))
        cnt = mycursor.fetchone()[0]
        
        if cnt==0:
            sql = "INSERT INTO ho_hospital(id,name,mobile,email,address,uname,pass,status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (maxid,name,mobile,email,address,uname,pass1,'1')
            mycursor.execute(sql, val)
            mydb.commit()            
            mess="GH: "+name+", Hospital ID:"+uname+", Password:"+pass1
            msg="success"
            
        else:
            msg='fail'

        
    return render_template('admin.html',msg=msg, data=data,act=act,mess=mess,email=email)


def pad_left(s, length):
    return s.zfill(length)

@app.route('/add_hospital', methods=['GET', 'POST'])
def add_hospital():
    msg=""
    mess=""
    email=""
    act=request.args.get("act")
    if 'username' in session:
        uname = session['username']

    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_hospital')
    hdata = mycursor.fetchall()

    now = datetime.datetime.now()
    rdate=now.strftime("%d-%m-%Y")

    mycursor.execute("SELECT max(id)+1 FROM ho_doctor")
    maxid = mycursor.fetchone()[0]
    if maxid is None:
        maxid=1
  
    input_str = str(maxid)
    padded_str = pad_left(input_str, 3)
    hosid="GH"+padded_str
    
    if request.method=='POST':
        
        hospital=request.form['hospital']
        address=request.form['address']
        city=request.form['city']
        speciality=request.form['speciality']
        
        mobile=request.form['mobile']
        
        email=request.form['email']
        uname=request.form['uname']
       

        mycursor.execute("SELECT count(*) FROM ho_hospital where uname=%s",(uname,))
        cnt = mycursor.fetchone()[0]
        
        if cnt==0:
            sql = "INSERT INTO ho_hospital(id,hospital,address,city,mobile,email,speciality,uname,status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)"
            val = (maxid,hospital,address,city,mobile,email,speciality,uname,'1')
            mycursor.execute(sql, val)
            mydb.commit()            
            
            msg="success"
            
        else:
            msg='fail'

        
    return render_template('add_hospital.html',msg=msg, hdata=hdata,act=act,mess=mess,email=email,hosid=hosid,title=title)


@app.route('/add_doctor', methods=['GET', 'POST'])
def add_doctor():
    msg=""
    mess=""
    email=""
    act=request.args.get("act")
    if 'username' in session:
        uname = session['username']

    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_hospital')
    hdata = mycursor.fetchall()

    now = datetime.datetime.now()
    rdate=now.strftime("%d-%m-%Y")

    mycursor.execute("SELECT max(id)+1 FROM ho_doctor")
    maxid = mycursor.fetchone()[0]
    if maxid is None:
        maxid=1
    docid="D"+str(maxid)
    if request.method=='POST':
        name=request.form['name']
        hospital=request.form['hospital']
        speciality=request.form['speciality']
        av_time=request.form['av_time']
        mobile=request.form['mobile']
        
        email=request.form['email']
        uname=request.form['uname']
        pass1=request.form['pass']
        
      

        mycursor.execute("SELECT count(*) FROM ho_doctor where uname=%s",(uname,))
        cnt = mycursor.fetchone()[0]
        
        if cnt==0:
            sql = "INSERT INTO ho_doctor(id,name,hospital,speciality,mobile,email,av_time,uname,pass,rdate,status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)"
            val = (maxid,name,hospital,speciality,mobile,email,av_time,uname,pass1,rdate,'1')
            mycursor.execute(sql, val)
            mydb.commit()            
            mess="Hospital ID: "+hospital+", Doctor:"+name+", Dotor ID:"+uname+", Password:"+pass1
            msg="success"
            
        else:
            msg='fail'

        
    return render_template('add_doctor.html',msg=msg, hdata=hdata,act=act,mess=mess,email=email,docid=docid,title=title)


@app.route('/add_staff', methods=['GET', 'POST'])
def add_staff():
    msg=""
    mess=""
    email=""
    act=request.args.get("act")
    if 'username' in session:
        uname = session['username']

    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_hospital')
    hdata = mycursor.fetchall()

    now = datetime.datetime.now()
    rdate=now.strftime("%d-%m-%Y")

    mycursor.execute("SELECT max(id)+1 FROM ho_staff")
    maxid = mycursor.fetchone()[0]
    if maxid is None:
        maxid=1
    staff_id="S"+str(maxid)
        
    if request.method=='POST':
        name=request.form['name']
        hospital=request.form['hospital']
        
        mobile=request.form['mobile']
        
        email=request.form['email']
        uname=request.form['uname']
        pass1=request.form['pass']
        
      

        mycursor.execute("SELECT count(*) FROM ho_staff where uname=%s",(uname,))
        cnt = mycursor.fetchone()[0]
        
        if cnt==0:
            sql = "INSERT INTO ho_staff(id,name,hospital,mobile,email,uname,pass) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (maxid,name,hospital,mobile,email,uname,pass1)
            mycursor.execute(sql, val)
            mydb.commit()            
            mess="GH: "+hospital+", Staff:"+name+", Staff ID:"+uname+", Password:"+pass1
            msg="success"
            
        else:
            msg='fail'

        
    return render_template('add_staff.html',msg=msg, hdata=hdata,act=act,mess=mess,email=email,staff_id=staff_id,title=title)

@app.route('/add_nurse', methods=['GET', 'POST'])
def add_nurse():
    msg=""
    mess=""
    email=""
    act=request.args.get("act")
    if 'username' in session:
        uname = session['username']

    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_hospital')
    hdata = mycursor.fetchall()

    now = datetime.datetime.now()
    rdate=now.strftime("%d-%m-%Y")

    mycursor.execute("SELECT max(id)+1 FROM ho_nurse")
    maxid = mycursor.fetchone()[0]
    if maxid is None:
        maxid=1
    nurse_id="N"+str(maxid)
        
    if request.method=='POST':
        name=request.form['name']
        hospital=request.form['hospital']
        
        mobile=request.form['mobile']
        
        email=request.form['email']
        uname=request.form['uname']
        pass1=request.form['pass']
        
      

        mycursor.execute("SELECT count(*) FROM ho_nurse where uname=%s",(uname,))
        cnt = mycursor.fetchone()[0]
        
        if cnt==0:
            sql = "INSERT INTO ho_nurse(id,name,hospital,mobile,email,uname,pass) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (maxid,name,hospital,mobile,email,uname,pass1)
            mycursor.execute(sql, val)
            mydb.commit()            
            mess="GH: "+hospital+", Name:"+name+", Nurse ID:"+uname+", Password:"+pass1
            msg="success"
            
        else:
            msg='fail'

        
    return render_template('add_nurse.html',msg=msg, hdata=hdata,act=act,mess=mess,email=email,nurse_id=nurse_id,title=title)

@app.route('/view_doc', methods=['GET', 'POST'])
def view_doc():
    msg=""
    act=request.args.get("act")
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    
    if 'username' in session:
        uname = session['username']
    st=""
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ho_doctor")
    data = cursor.fetchall()

    if request.method=='POST':
        st="1"

    if act=="del":
        did=request.args.get("did")
        cursor.execute("delete from ho_doctor where id=%s",(did,))
        mydb.commit()
        return redirect(url_for('view_doc'))
        
        
    return render_template('view_doc.html',msg=msg,act=act,data=data,st=st,title=title)

@app.route('/view_staff', methods=['GET', 'POST'])
def view_staff():
    msg=""
    act=request.args.get("act")
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    
    if 'username' in session:
        uname = session['username']
    st=""
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ho_staff")
    data = cursor.fetchall()

    if request.method=='POST':
        st="1"

    if act=="del":
        did=request.args.get("did")
        cursor.execute("delete from ho_staff where id=%s",(did,))
        mydb.commit()
        return redirect(url_for('view_staff'))
        
    return render_template('view_staff.html',msg=msg,act=act,data=data,st=st,title=title)

@app.route('/view_nurse', methods=['GET', 'POST'])
def view_nurse():
    msg=""
    act=request.args.get("act")
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    
    if 'username' in session:
        uname = session['username']
    st=""
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ho_nurse")
    data = cursor.fetchall()

    if request.method=='POST':
        st="1"

    if act=="del":
        did=request.args.get("did")
        cursor.execute("delete from ho_doctor where id=%s",(did,))
        mydb.commit()
        return redirect(url_for('view_nurse'))
        
    return render_template('view_nurse.html',msg=msg,act=act,data=data,st=st,title=title)

@app.route('/view_report', methods=['GET', 'POST'])
def view_report():
    msg=""
    adata=[]
    act=request.args.get("act")
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    
    if 'username' in session:
        uname = session['username']
    st=""
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ho_hospital")
    hdata = mycursor.fetchall()

    if request.method=='POST':
        hos=request.form['hos']
        rdate1=request.form['rdate']
        rd=rdate1.split("-")
        rdate=rd[2]+"-"+rd[1]+"-"+rd[0]
        st="1"
        
        mycursor.execute('SELECT * FROM ho_entry WHERE rdate=%s && hospital=%s', (rdate,hos))
        d1 = mycursor.fetchall()
        i=1
        for d11 in d1:
            dt=[]
            dt.append(d11[0])
            dt.append(d11[1])
            dt.append(d11[2])
            dt.append(d11[3])
            dt.append(d11[4])
            dt.append(d11[5])
            dt.append(d11[6])
            dt.append(d11[7])
            dt.append(d11[8])
            dt.append(d11[9])
            dt.append(d11[10])
            dt.append(d11[11])
            dt.append(d11[12])
            dt.append(d11[13])

            
            mycursor.execute('SELECT * FROM ho_user WHERE uname = %s', (d11[1], ))
            d2 = mycursor.fetchone()
            dt.append(d2[1])
            dt.append(d2[6])
            dt.append(d2[2])
            dt.append(d2[3])
            
            adata.append(dt)
            
            i+=1

  
        
    return render_template('view_report.html',msg=msg,act=act,st=st,title=title,adata=adata,hdata=hdata)


@app.route('/userhome', methods=['GET', 'POST'])
def userhome():
    msg=""
    st=""
    act=request.args.get("act")
    rid=request.args.get("rid")
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    bdata=[]
    sdata=[]
    mess=""
    name=""
    mobile=""
    if 'username' in session:
        uname = session['username']
    st=""
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_user WHERE uname = %s', (uname, ))
    data = mycursor.fetchone()

    import datetime
    now1 = datetime.datetime.now()
    rdate=now1.strftime("%d-%m-%Y")

    mycursor.execute('SELECT count(*) FROM ho_entry WHERE rdate=%s && patient_id = %s && status<3', (rdate,uname))
    cnt = mycursor.fetchone()[0]

    if cnt>0:
        st="1"
        mycursor.execute('SELECT * FROM ho_entry WHERE rdate=%s && patient_id = %s', (rdate,uname))
        bdata = mycursor.fetchone()

        mycursor.execute('SELECT * FROM ho_entry WHERE rdate=%s && status = 1', (rdate,))
        sdata = mycursor.fetchone()

        

    #if request.method=='POST':
    #    st="1"
        
    if act=="cancel":

        mycursor.execute('SELECT * FROM ho_entry  WHERE id=%s', (rid,))
        d6 = mycursor.fetchone()
        gid=d6[0]
        t=d6[5]
        
        mycursor.execute("update ho_entry set status=3 where patient_id=%s && rdate=%s",(uname,rdate))
        mydb.commit()
        
        
        mycursor.execute('SELECT * FROM ho_entry  WHERE id>%s && status=0 && rdate=%s order by id', (rid,rdate))
        d5 = mycursor.fetchall()
        dd=[]
        for d55 in d5:
            dd.append(d55[1])

        nn=len(dd)
        if nn>0:
            patid=dd[0]
            mycursor.execute('SELECT * FROM ho_user WHERE uname = %s', (patid, ))
            dat = mycursor.fetchone()
            name=dat[1]
            mobile=str(dat[4])
            mess="Token:"+str(t)+" cancelled, You are now next for doctor consultation"

            
    return render_template('userhome.html',msg=msg,act=act,data=data,st=st,title=title,bdata=bdata,sdata=sdata,mess=mess,name=name,mobile=mobile)

@app.route('/user_search', methods=['GET', 'POST'])
def user_search():
    msg=""
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    
    if 'username' in session:
        uname = session['username']
    st=""
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_user WHERE uname = %s', (uname, ))
    data = mycursor.fetchone()

    mycursor.execute('SELECT * FROM ho_hospital')
    hdata = mycursor.fetchall()

    if request.method=='POST':
        st="1"
        
    return render_template('user_search.html',msg=msg, data=data,st=st,hdata=hdata,title=title)


@app.route('/user_doc', methods=['GET', 'POST'])
def user_doc():
    msg=""
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    hid=request.args.get("hid")
    if 'username' in session:
        uname = session['username']
    st=""
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_user WHERE uname = %s', (uname, ))
    data = mycursor.fetchone()

    mycursor.execute('SELECT * FROM ho_hospital where id=%s',(hid,))
    hdata = mycursor.fetchone()
    hos=hdata[9]

    mycursor.execute('SELECT * FROM ho_doctor where hospital=%s',(hos,))
    ddata = mycursor.fetchall()

    if request.method=='POST':
        st="1"
        
    return render_template('user_doc.html',msg=msg, data=data,st=st,hdata=hdata,ddata=ddata,title=title,hid=hid)

@app.route('/appoint', methods=['GET', 'POST'])
def appoint():
    msg=""
    mess=""
    name=""
    mobile=""
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    hid=request.args.get("hid")
    did=request.args.get("did")
    if 'username' in session:
        uname = session['username']
    st=""
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_user WHERE uname = %s', (uname, ))
    data = mycursor.fetchone()
    name=data[1]
    mobile=str(data[4])

    mycursor.execute('SELECT * FROM ho_hospital where id=%s',(hid,))
    hdata = mycursor.fetchone()
    hos=hdata[9]

    mycursor.execute('SELECT * FROM ho_doctor where id=%s',(did,))
    ddata = mycursor.fetchone()
    doc=ddata[7]
    dname=ddata[1]

    import datetime
    now1 = datetime.datetime.now()
    edate=now1.strftime("%Y-%m-%d")
    rtime=now1.strftime("%H:%M")
    print(edate)


    if request.method=='POST':
        rdate1=request.form['ap_date']
        reason=request.form['reason']

        rd=rdate1.split("-")
        rdate=rd[2]+"-"+rd[1]+"-"+rd[0]
        month=rd[1]
        year=rd[0]

        mycursor.execute('SELECT count(*) FROM ho_entry WHERE hospital = %s && docid=%s && rdate=%s', (hos,doc,rdate))
        cnt = mycursor.fetchone()[0]
        token_no=cnt+1
    
        mycursor.execute("SELECT max(id)+1 FROM ho_entry")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        sql = "INSERT INTO ho_entry(id,patient_id,hospital,docid,doctor,token_no,reason,rdate,rtime,month,year,staff_id,entry_type) VALUES (%s,%s,%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s)"
        val = (maxid,uname,hos,doc,dname,token_no,reason,rdate,rtime,month,year,'','booked')
        mycursor.execute(sql, val)
        mydb.commit()

        mess="Patient ID: "+uname+", Name:"+name+", Token No."+str(token_no)
        msg="success"
        
    return render_template('appoint.html',msg=msg, data=data,st=st,hdata=hdata,title=title,ddata=ddata,mess=mess,name=name,mobile=mobile,edate=edate)

@app.route('/user_pres', methods=['GET', 'POST'])
def user_pres():
    msg=""
    mess=""
    name=""
    mobile=""
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    docid=request.args.get("docid")
    rdate=request.args.get("rdate")
    if 'username' in session:
        uname = session['username']
    st=""
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_user WHERE uname = %s', (uname, ))
    data = mycursor.fetchone()
    name=data[1]
    mobile=str(data[4])

    mycursor.execute('SELECT * FROM ho_medicine WHERE patient_id = %s && docid=%s && rdate=%s', (uname,docid,rdate ))
    mdata = mycursor.fetchall()


    return render_template('user_pres.html',msg=msg, data=data,st=st,title=title,mdata=mdata)

@app.route('/user_appoint', methods=['GET', 'POST'])
def user_appoint():
    msg=""
    mess=""
    name=""
    mobile=""
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    hid=request.args.get("hid")
    did=request.args.get("did")
    if 'username' in session:
        uname = session['username']
    st=""
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_user WHERE uname = %s', (uname, ))
    data = mycursor.fetchone()
    name=data[1]
    mobile=str(data[4])

    mycursor.execute('SELECT * FROM ho_entry WHERE patient_id = %s order by id desc', (uname, ))
    adata = mycursor.fetchall()


    return render_template('user_appoint.html',msg=msg, data=data,st=st,title=title,adata=adata)

@app.route('/staff_home', methods=['GET', 'POST'])
def staff_home():
    msg=""
    uname=""
    st=""
    aadhar=""
    if 'username' in session:
        uname = session['username']
    data=[]

    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
   
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_staff WHERE uname = %s', (uname, ))
    data2 = mycursor.fetchone()

    hospital=data2[2]

    if request.method=='POST':
        aadhar=request.form['aadhar']

        mycursor.execute('SELECT count(*) FROM ho_user WHERE aadhar = %s', (aadhar, ))
        cnt = mycursor.fetchone()[0]

        if cnt>0:
            st="1"
            mycursor.execute('SELECT * FROM ho_user WHERE aadhar = %s', (aadhar, ))
            data = mycursor.fetchone()
            patid=data[10]
        else:
            st="2"

    return render_template('staff_home.html',msg=msg, data=data,st=st,title=title,aadhar=aadhar)

@app.route('/staff_entry', methods=['GET', 'POST'])
def staff_entry():
    msg=""
    uname=""
    st=""
    mess=""
    mobile=""
    name=""
    
    pid=request.args.get("pid")
    if 'username' in session:
        uname = session['username']
    data=[]

    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
   
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_staff WHERE uname = %s', (uname, ))
    data2 = mycursor.fetchone()

    hospital=data2[2]

    import datetime
    now1 = datetime.datetime.now()
    rdate=now1.strftime("%d-%m-%Y")
    edate1=now1.strftime("%Y-%m-%d")
    rtime=now1.strftime("%H:%M")

    rd=rdate.split("-")
    month=rd[1]
    year=rd[2]
    mycursor.execute('SELECT * FROM ho_doctor WHERE hospital = %s', (hospital, ))
    cdata = mycursor.fetchall()

    mycursor.execute('SELECT * FROM ho_user WHERE uname = %s', (pid, ))
    pdata = mycursor.fetchone()
    name=pdata[1]
    mobile=str(pdata[4])
    

    if request.method=='POST':
        doctor=request.form['doctor']
        reason=request.form['reason']

        mycursor.execute('SELECT count(*) FROM ho_entry WHERE hospital = %s && docid=%s && rdate=%s', (hospital,doctor,rdate))
        cnt = mycursor.fetchone()[0]
        token_no=cnt+1

        mycursor.execute('SELECT * FROM ho_doctor WHERE uname = %s', (doctor, ))
        dc = mycursor.fetchone()
        dname=dc[1]
    
        mycursor.execute("SELECT max(id)+1 FROM ho_entry")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        sql = "INSERT INTO ho_entry(id,patient_id,hospital,docid,doctor,token_no,reason,rdate,rtime,month,year,staff_id,entry_type) VALUES (%s,%s,%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s)"
        val = (maxid,pid,hospital,doctor,dname,token_no,reason,rdate,rtime,month,year,uname,'entry')
        mycursor.execute(sql, val)
        mydb.commit()

        mess="Patient ID: "+pid+", Name:"+name+", Token No."+str(token_no)
        msg="success"

    return render_template('staff_entry.html',msg=msg, data=data,st=st,title=title,cdata=cdata,mess=mess,mobile=mobile,name=name)

@app.route('/staff_addpat', methods=['GET', 'POST'])
def staff_addpat():
    msg=""
    act=""
    mess=""
    email=""
    uname=""
    aadhar=request.args.get("aadhar")
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    
    data=[]
    if 'username' in session:
        uname = session['username']
    data2=[]

    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_staff WHERE uname = %s', (uname, ))
    data2 = mycursor.fetchone()

    hospital=data2[2]
    
    import datetime
    now1 = datetime.datetime.now()
    rdate=now1.strftime("%d-%m-%Y")
    rtime=now1.strftime("%H:%M")
    
    mycursor.execute("SELECT max(id)+1 FROM ho_user")
    maxid = mycursor.fetchone()[0]
    if maxid is None:
        maxid=1

    patid="PT"+str(maxid)
    
    
    if request.method=='POST':
        name=request.form['name']
        gender=request.form['gender']
        dob=request.form['dob']
        
        address=request.form['address']
        mobile=request.form['mobile']
        parent_mobile=request.form['parent_mobile']
        email=request.form['email']

        sql = "INSERT INTO ho_user(id,name,gender,dob,mobile,email,address,parent_mobile,aadhar,uname,rdate,stype) VALUES (%s,%s,%s,%s,%s,%s, %s, %s, %s, %s,%s,%s)"
        val = (maxid,name,gender,dob,mobile,email,address,parent_mobile,aadhar,patid,rdate,'entry')
        mycursor.execute(sql, val)
        mydb.commit()            

        msg="success"

    return render_template('staff_addpat.html',msg=msg,uname=uname,pid=patid,title=title)


@app.route('/staff_patview', methods=['GET', 'POST'])
def staff_patview():
    msg=""
    uname=""
    st=""
    aadhar=""
    adata=[]
    if 'username' in session:
        uname = session['username']
    data=[]

    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
   
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_staff WHERE uname = %s', (uname, ))
    data2 = mycursor.fetchone()

    hospital=data2[2]

    if request.method=='POST':
        rdate1=request.form['rdate']
        rd=rdate1.split("-")
        rdate=rd[2]+"-"+rd[1]+"-"+rd[0]
        st="1"
        
        mycursor.execute('SELECT * FROM ho_entry WHERE rdate=%s && hospital=%s', (rdate,hospital))
        d1 = mycursor.fetchall()
        i=1
        for d11 in d1:
            dt=[]
            dt.append(d11[0])
            dt.append(d11[1])
            dt.append(d11[2])
            dt.append(d11[3])
            dt.append(d11[4])
            dt.append(d11[5])
            dt.append(d11[6])
            dt.append(d11[7])
            dt.append(d11[8])
            dt.append(d11[9])
            dt.append(d11[10])
            dt.append(d11[11])
            dt.append(d11[12])
            dt.append(d11[13])

            
            mycursor.execute('SELECT * FROM ho_user WHERE uname = %s', (d11[1], ))
            d2 = mycursor.fetchone()
            dt.append(d2[1])
            dt.append(d2[6])
            dt.append(d2[2])
            dt.append(d2[3])
            
            adata.append(dt)
            
            i+=1


    return render_template('staff_patview.html',msg=msg, data=data,st=st,title=title,adata=adata)


#ILP-Based Priority Scheduling
def ILP_priority():
    # Parameters
    priority = {'P1': 3, 'P2': 5, 'P3': 1}  # Higher = more urgent

    # Doctor availability (1 if available at that time)
    availability = {
        ('D1', 0): 1, ('D1', 1): 1, ('D1', 2): 0,
        ('D2', 0): 1, ('D2', 1): 0, ('D2', 2): 1,
    }

    # Max 1 patient per doctor per time slot
    max_patients = 1

    # Problem definition
    model = pulp.LpProblem("Doctor_Appointment_Scheduling", pulp.LpMaximize)

    # Decision variables
    x = pulp.LpVariable.dicts("x", [(i, j, t) for i in patients for j in doctors for t in times],
                              cat='Binary')

    # Objective: Maximize weighted priorities (earlier time = better)
    model += pulp.lpSum(priority[i] * (len(times) - t) * x[(i, j, t)] 
                        for i in patients for j in doctors for t in times)

    # Constraint 1: Each patient gets at most one appointment
    for i in patients:
        model += pulp.lpSum(x[(i, j, t)] for j in doctors for t in times) <= 1

    # Constraint 2: Doctor can only see 1 patient per time
    for j in doctors:
        for t in times:
            model += pulp.lpSum(x[(i, j, t)] for i in patients) <= max_patients * availability.get((j, t), 0)

    # Constraint 3: Respect doctor availability
    for i in patients:
        for j in doctors:
            for t in times:
                model += x[(i, j, t)] <= availability.get((j, t), 0)

    # Solve the model
    model.solve()

    # Output the schedule
    print("Scheduled Appointments:")
    for i, j, t in x:
        if pulp.value(x[(i, j, t)]) == 1:
            print(f"Patient {i} -> Doctor {j} at Time Slot {t}")

@app.route('/doc_home', methods=['GET', 'POST'])
def doc_home():
    msg=""
    act=request.args.get("act")
    pid=request.args.get("pid")
    rid=request.args.get("rid")
    patid=""
    mess=""
    name=""
    mobile=""
    adata=[]

    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()

    ff=open("static/emr.txt","w")
    ff.write("0")
    ff.close()
    
    if 'username' in session:
        uname = session['username']
    data2=[]

    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_doctor WHERE uname = %s', (uname, ))
    data = mycursor.fetchone()

    import datetime
    now1 = datetime.datetime.now()
    rdate=now1.strftime("%d-%m-%Y")
    edate1=now1.strftime("%Y-%m-%d")
    rtime=now1.strftime("%H:%M")

    mycursor.execute('SELECT * FROM ho_entry WHERE docid = %s && rdate=%s && status<2 order by id', (uname, rdate))
    d1 = mycursor.fetchall()
    i=1
    for d11 in d1:
        dt=[]
        dt.append(d11[0])
        dt.append(d11[1])
        dt.append(d11[2])
        dt.append(d11[3])
        dt.append(d11[4])
        dt.append(d11[5])
        dt.append(d11[6])
        dt.append(d11[7])
        dt.append(d11[8])
        dt.append(d11[9])
        dt.append(d11[10])
        dt.append(d11[11])
        dt.append(d11[12])
        dt.append(d11[13])

        
        mycursor.execute('SELECT * FROM ho_user WHERE uname = %s', (d11[1], ))
        d2 = mycursor.fetchone()
        dt.append(d2[1])
        dt.append(d2[6])
        dt.append(d2[4])
        dt.append(d2[5])
        dt.append(d2[2])
        dt.append(d2[3])
        adata.append(dt)
        if i==1:
            mycursor.execute("update ho_entry set status=1 where status=0 && id=%s",(d11[0],))
            mydb.commit()
        i+=1
    
    ###
    if act=="cons":
        mycursor.execute('SELECT * FROM ho_entry  WHERE id>%s && status=0 && docid=%s && rdate=%s', (rid,uname,rdate))
        d4 = mycursor.fetchall()
        dd=[]
        for d44 in d4:
            dd.append(d44[1])

        n=len(dd)
        if n>0:
            patid=dd[0]
            mycursor.execute('SELECT * FROM ho_user WHERE uname = %s', (patid, ))
            dat = mycursor.fetchone()
            name=dat[1]
            mobile=str(dat[4])
            mess="You are now next for doctor consultation"
    
        msg="ready"

        
    return render_template('doc_home.html',msg=msg,data=data,adata=adata,title=title,pid=pid,mess=mess,name=name,mobile=mobile,patid=patid)

@app.route('/doc_consult', methods=['GET', 'POST'])
def doc_consult():
    msg=""
    st=""
    act=request.args.get("act")
    pid=request.args.get("pid")
    adata=[]
    mdata=[]
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    
    if 'username' in session:
        uname = session['username']
    data2=[]

    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_doctor WHERE uname = %s', (uname, ))
    data = mycursor.fetchone()

    import datetime
    now1 = datetime.datetime.now()
    rdate=now1.strftime("%d-%m-%Y")
    edate1=now1.strftime("%Y-%m-%d")
    rtime=now1.strftime("%H:%M")

    mycursor.execute('SELECT * FROM ho_entry WHERE docid = %s && rdate=%s && patient_id=%s', (uname, rdate,pid))
    d1 = mycursor.fetchall()
    i=1
    for d11 in d1:
        dt=[]
        dt.append(d11[0])
        dt.append(d11[1])
        dt.append(d11[2])
        dt.append(d11[3])
        dt.append(d11[4])
        dt.append(d11[5])
        dt.append(d11[6])
        dt.append(d11[7])
        dt.append(d11[8])
        dt.append(d11[9])
        dt.append(d11[10])
        dt.append(d11[11])
        dt.append(d11[12])
        dt.append(d11[13])

        
        mycursor.execute('SELECT * FROM ho_user WHERE uname = %s', (d11[1], ))
        d2 = mycursor.fetchone()
        dt.append(d2[1])
        dt.append(d2[6])
        dt.append(d2[4])
        dt.append(d2[5])

        dt.append(d11[14])
        dt.append(d11[15])
        dt.append(d11[16])
        dt.append(d11[17])
        dt.append(d11[18])
        adata.append(dt)
        
        i+=1

    if request.method=='POST':
        medicine=request.form['medicine']
        details=request.form['details']
        mycursor.execute("SELECT max(id)+1 FROM ho_medicine")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1

        sql = "INSERT INTO ho_medicine(id,docid,patient_id,medicine,details,rdate) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (maxid,uname,pid,medicine,details,rdate)
        mycursor.execute(sql, val)
        mydb.commit()   
        
        msg="ok"

    mycursor.execute('SELECT count(*) FROM ho_medicine WHERE patient_id = %s && rdate=%s', (pid,rdate ))
    mcnt = mycursor.fetchone()[0]
    if mcnt>0:
        st="1"
        mycursor.execute('SELECT * FROM ho_medicine WHERE patient_id = %s && rdate=%s', (pid,rdate ))
        mdata = mycursor.fetchall()

    if act=="complete":
        mycursor.execute("update ho_entry set status=2 where status=1 && patient_id = %s && rdate=%s", (pid,rdate ))
        mydb.commit()
        msg="done"
    
    return render_template('doc_consult.html',msg=msg,data=data,adata=adata,title=title,pid=pid,mdata=mdata,st=st)

@app.route('/doc_emr', methods=['GET', 'POST'])
def doc_emr():
    msg=""
    act=request.args.get("act")
    pid=request.args.get("pid")
    rid=request.args.get("rid")
    patid=""
    mess=""
    name=""
    mobile=""
    adata=[]

    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    
    if 'username' in session:
        uname = session['username']
    data2=[]

    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_doctor WHERE uname = %s', (uname, ))
    data = mycursor.fetchone()

    import datetime
    now1 = datetime.datetime.now()
    rdate=now1.strftime("%d-%m-%Y")
    edate1=now1.strftime("%Y-%m-%d")
    rtime=now1.strftime("%H:%M")

    ff=open("static/emr.txt","r")
    emr=ff.read()
    ff.close()

    n=int(emr)
    n1=n+5

    if n<60:

        if n>=20:
            msg="emr"
        if n==20:
            mycursor.execute('SELECT * FROM ho_entry  WHERE status=0 && docid=%s && rdate=%s order by id', (uname,rdate))
            d5 = mycursor.fetchall()
            dd=[]
            for d55 in d5:
                dd.append(d55[1])

            nn=len(dd)
            if nn>0:
                patid=dd[0]
                mycursor.execute('SELECT * FROM ho_user WHERE uname = %s', (patid, ))
                dat = mycursor.fetchone()
                name=dat[1]
                mobile=str(dat[4])
            mess="Emergency case is being handled, Please wait"

        ff=open("static/emr.txt","w")
        ff.write(str(n1))
        ff.close()

        
    

    return render_template('doc_emr.html',msg=msg,data=data,title=title,mess=mess,mobile=mobile,name=name)


@app.route('/doc_report', methods=['GET', 'POST'])
def doc_report():
    msg=""
    st=""
    act=request.args.get("act")
    pid=request.args.get("pid")
    adata=[]
    mdata=[]
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
    
    if 'username' in session:
        uname = session['username']
    data2=[]

    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_doctor WHERE uname = %s', (uname, ))
    data = mycursor.fetchone()

    if request.method=='POST':
        rdate1=request.form['rdate']
        rd=rdate1.split("-")
        rdate=rd[2]+"-"+rd[1]+"-"+rd[0]
        st="1"
        
        mycursor.execute('SELECT * FROM ho_entry WHERE docid = %s && rdate=%s && status<3', (uname, rdate))
        d1 = mycursor.fetchall()
        i=1
        for d11 in d1:
            dt=[]
            dt.append(d11[0])
            dt.append(d11[1])
            dt.append(d11[2])
            dt.append(d11[3])
            dt.append(d11[4])
            dt.append(d11[5])
            dt.append(d11[6])
            dt.append(d11[7])
            dt.append(d11[8])
            dt.append(d11[9])
            dt.append(d11[10])
            dt.append(d11[11])
            dt.append(d11[12])
            dt.append(d11[13])

            
            mycursor.execute('SELECT * FROM ho_user WHERE uname = %s', (d11[1], ))
            d2 = mycursor.fetchone()
            dt.append(d2[1])
            dt.append(d2[6])
            dt.append(d2[2])
            dt.append(d2[3])

            dt.append(d11[14])
            dt.append(d11[15])
            dt.append(d11[16])
            dt.append(d11[17])
            dt.append(d11[18])

            dtt=[]
            mycursor.execute('SELECT * FROM ho_medicine WHERE docid=%s && patient_id = %s && rdate=%s', (d11[3],d11[1],d11[7] ))
            d3 = mycursor.fetchall()
            for d33 in d3:
                dt1=[]
                dt1.append(d33[3])
                dt1.append(d33[4])
                dtt.append(dt1)
            dt.append(dtt)
            
            adata.append(dt)
            
            i+=1

    
    return render_template('doc_report.html',msg=msg,data=data,adata=adata,title=title,st=st)


@app.route('/nur_home', methods=['GET', 'POST'])
def nur_home():
    msg=""
    uname=""
    st=""
    aadhar=""
    if 'username' in session:
        uname = session['username']
    data=[]
    adata=[]
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
   
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_nurse WHERE uname = %s', (uname, ))
    data = mycursor.fetchone()

    hospital=data[2]

    import datetime
    now1 = datetime.datetime.now()
    rdate=now1.strftime("%d-%m-%Y")
    edate1=now1.strftime("%Y-%m-%d")
    rtime=now1.strftime("%H:%M")

    mycursor.execute('SELECT * FROM ho_entry WHERE rdate=%s && hospital=%s', (rdate,hospital))
    d1 = mycursor.fetchall()
    i=1
    for d11 in d1:
        dt=[]
        dt.append(d11[0])
        dt.append(d11[1])
        dt.append(d11[2])
        dt.append(d11[3])
        dt.append(d11[4])
        dt.append(d11[5])
        dt.append(d11[6])
        dt.append(d11[7])
        dt.append(d11[8])
        dt.append(d11[9])
        dt.append(d11[10])
        dt.append(d11[11])
        dt.append(d11[12])
        dt.append(d11[13])

        
        mycursor.execute('SELECT * FROM ho_user WHERE uname = %s', (d11[1], ))
        d2 = mycursor.fetchone()
        dt.append(d2[1])
        dt.append(d2[6])
        dt.append(d2[4])
        dt.append(d2[5])

        dt.append(d11[14])
        dt.append(d11[15])
        dt.append(d11[16])
        dt.append(d11[17])
        dt.append(d11[18])
        
        adata.append(dt)
        
        i+=1


    return render_template('nur_home.html',msg=msg, data=data,st=st,title=title,adata=adata)

@app.route('/nur_edit', methods=['GET', 'POST'])
def nur_edit():
    msg=""
    uname=""
    st=""
    aadhar=""
    pid=request.args.get("pid")
    rid=request.args.get("rid")
    if 'username' in session:
        uname = session['username']
    data=[]
    adata=[]
    ff=open("static/title.txt","r")
    title=ff.read()
    ff.close()
   
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM ho_nurse WHERE uname = %s', (uname, ))
    data = mycursor.fetchone()

    hospital=data[2]

    import datetime
    now1 = datetime.datetime.now()
    rdate=now1.strftime("%d-%m-%Y")
    edate1=now1.strftime("%Y-%m-%d")
    rtime=now1.strftime("%H:%M")

    if request.method=='POST':
        temp=request.form['temp']
        pulse=request.form['pulse']
        bp=request.form['bp']
        height=request.form['height']
        weight=request.form['weight']

        mycursor.execute("update ho_entry set temp=%s,pulse=%s,bp=%s,height=%s,weight=%s where patient_id=%s && id=%s",(temp,pulse,bp,height,weight,pid,rid))
        mydb.commit()
        msg="ok"


    return render_template('nur_edit.html',msg=msg, data=data,st=st,title=title,adata=adata)

@app.route('/doc_sugg', methods=['GET', 'POST'])
def doc_sugg():
    msg=""
    
    if 'username' in session:
        uname = session['username']
    
    if request.method=='GET':
        pid = request.args.get('pid')
    if request.method=='POST':
        pid=request.form['pid']
        sugg=request.form['suggestion']
        pres=request.form['prescription']
        cursor = mydb.cursor()

        now = datetime.datetime.now()
        rdate=now.strftime("%d-%m-%Y")
            
        mycursor = mydb.cursor()
        mycursor.execute("SELECT max(id)+1 FROM suggest")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        sql = "INSERT INTO suggest(id,pid,suggestion,prescription,rdate) VALUES (%s, %s, %s, %s, %s)"
        val = (maxid,pid,sugg,pres,rdate)
        cursor.execute(sql, val)
        mydb.commit()            
        print(cursor.rowcount, "Registered Success")
        msg="Register success"
        
    return render_template('doc_sugg.html',msg=msg, pid=pid)



@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


