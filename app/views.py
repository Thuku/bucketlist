from flask import Flask, session,json, render_template, request, redirect, g, url_for, flash
import os
from app import app
from app.bucketlist_module import BucketLists
from app.items_module import BucketListItems
from app.user_module import User
user = User()
bucketlist=BucketLists()
bucket_item=BucketListItems()

app.secret_key = os.urandom(24)


@app.route('/', methods=['GET', 'POST'])
def home():
    if g.user:
        return render_template('dashboard.html')
    if request.method == 'POST':
        session.pop('user', None)
        email = request.form['email']
        password = request.form['password']
        bool = user.login(email,password)
        if bool == True:
            session['user'] = request.form['email']
            return redirect(url_for('dashboard'))
        # if request.form['password'] == 'password':
        #     session['user'] = request.form['email']
        #     return redirect(url_for('dashboard'))
       
    flash('Hello world!', 'success')
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Renders the sign up page
    """
    if g.user:
        return render_template('dashboard.html')
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        msg = user.create_user(email, password, confirm_password)
        if msg != None:
            flash('Wrong registration details')
            return home()
        elif msg == 'You have successfully signed Up':

            return redirect(url_for('home'), flash(msg + "Sign in to create your bucket list"))
    else:
        return render_template('signup.html')

@app.route('/create', methods=['GET', 'POST'])
def create_bucketlist():
    """
    Renders the create bucket list page
    """
    if g.user:
    
        if request.method == "POST":
            bucketlist_name = request.form['bucketlist_name']
            activity = []
            status = 'incomplete'
            bucketlist.create_bucket_list(bucketlist_name, activity, status)
            return redirect('/dashboard')
            
        return render_template('create.html')

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.route('/dashboard')
def dashboard():
    if g.user:
        buckets = BucketLists.bucketlists
        return render_template('dashboard.html',data=buckets)
    else:
        return redirect(url_for('home'))

@app.route('/inprogress', methods=['GET'])
def inprogress():
    """
    Renders the inprogress page containing  bucketlists that are not yet fully done
    """
    if g.user:
        buckets=BucketLists.bucketlists
        return render_template('inprogress.html', data=buckets)

@app.route('/add_activity', methods=['GET', 'POST'])
def add_activity():
    if g.user:
        if request.method == "POST":
            item = request.form['activity']
            name = request.form['title']
            bucket_item.add_activity(name, item)
            bucket_items = bucket_item.get_items_of_bucket(name)
            bucket_items_dict=[]
            for i in range(len(bucket_items)):
                item={"key":i+1,"value":bucket_items[i]}
                bucket_items_dict.append(item)
            print(bucket_items_dict)
            return render_template('add_activity.html',data=bucket_items_dict)
        else:
            name = request.form['title']
            bucket_items = bucket_item.get_items_of_bucket(name)
            bucket_items_dict=[]
            for i in range(len(bucket_items)):
                item={"key":i+1,"value":bucket_items[i]}
                bucket_items_dict.append(item)
            print(bucket_items_dict)
            return render_template('add_activity.html',data=bucket_items_dict)
    
    return redirect(url_for('home'))


@app.route('/add_activity/<title>')
def get_bucketname(title):
    if g.user:
        return render_template("add_activity.html", title=title)
    else:
        return redirect(url_for('home'))


@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']
    return 'Not logged in'


@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return redirect('/')
