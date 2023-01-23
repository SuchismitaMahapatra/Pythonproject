from flask import Flask,render_template,request,redirect
import pymysql

app=Flask('__name__')


@app.route('/')
def index():
    try:
        
        db=pymysql.connect(host='localhost',user='root',password='Joshi@1432',database='instiman')
        cu=db.cursor()
        q="select * from college"
        cu.execute(q)
        data=cu.fetchall()
        return render_template('index.html',d=data)
    
    except Exception as e:
        return("Error")  
    
@app.route('/create')
def create():
    return render_template('form.html')
    
    
@app.route('/store', methods=['POST'])
def store():
    t=request.form['t']
    d=request.form['det']
    dt=request.form['dt']
    dt1=request.form['dt1']
    det=request.form['dt2']
    try:
        db=pymysql.connect(host='localhost',user='root',password='Joshi@1432',database='instiman')
        cu=db.cursor()
        q="insert into college(SRNO,Name,Branch,Rollno,HorD) values('{}','{}','{}','{}','{}')".format(t,d,dt,dt1,det)
        cu.execute(q)
        db.commit()
        return redirect('/')
    
    except Exception as e:
        return("Error")
    
@app.route('/delete/<rid>')
def delete(rid):
    try:
        db=pymysql.connect(host="localhost",user="root",password="Joshi@1432",database="instiman")
        cu=db.cursor()
        q="delete from college where id='{}'".format(rid)
        cu.execute(q)
        db.commit()
        return redirect('/')
    
    except Exception as e:
        return ("Error")  

@app.route('/edit/<rid>')
def edit(rid):
    try:
        db=pymysql.connect(host='localhost',user='root',password='Joshi@1432',database='instiman')
        cu=db.cursor()
        q="select * from college where id='{}'".format(rid)
        cu.execute(q)
        data=cu.fetchone()
        return render_template("editstore.html",d=data)
    
    except Exception as e:
        return("Error")
    
@app.route('/update/<rid>',methods=['POST'])
def update(rid):
    ut=request.form['t']
    ud=request.form['det']
    udt=request.form['dt']
    udt1=request.form['dt1']
    udt2=request.form['dt2']
    try:
        db=pymysql.connect(host='localhost',user='root',password='Joshi@1432',database='instiman')
        cu=db.cursor()
        q="update college SET id='{}',Name='{}',Branch='{}',RollNo='{}',H/D='{}' where SRNO='{}'".format(ut,ud,udt,udt1,udt2,rid)
        cu.execute(q)
        db.commit()
        return redirect('/')
    
    except Exception as e:
        return("Error")
        
app.run(debug=True)