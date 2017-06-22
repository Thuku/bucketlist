from flask import render_template, request, redirect
from app.user_module import Accounts
from app.bucketlist_module import BucketLists
from app.items_module import BucketListItems

from app import app

account = Accounts()
bucketlist = BucketLists()
activity = BucketListItems()


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Renders the index page
    """
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        msg = account.login(email, password)
        if msg == "Welcome to your dashboard":
            return redirect('/dashboard')
        else:
            return redirect('/')
    else:
        return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Renders the sign up page
    """
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        account.create_user(email, password, confirm_password)
        return redirect('/')
    else:
        return render_template('signup.html')


@app.route('/dashboard')
def dashboard():
    """
    Renders the dashboard page
    """
    bucketlists = BucketLists.bucketlists
    return render_template("dashboard.html", data=bucketlists)


@app.route('/create', methods=['GET', 'POST'])
def create_bucketlist():
    """
    Renders the create bucket list page
    """
    if request.method == "POST":
        bucketlist_name = request.form['bucketlist_name']
        activity = []
        name = bucketlist.create_bucket_list(bucketlist_name, activity)
        return redirect('/add_activity/' + name)
    return render_template('create.html')


@app.route('/inprogress')
def inprogress():
    """
    Renders the inprogress page containing  bucketlists that are not yet fully done
    """
    return render_template('inprogress.html')


@app.route('/newbucketlists')
def newbucketlists():
    """
    Renders the page containing recently created bucketlists
    """
    return render_template('newbucketlists.html')


@app.route('/completed')
def completed():
    """
    This returns a rendered page of all completed bucketlists
    """
    return render_template('completed.html')


@app.route('/add_activity', methods=['GET', 'POST'])
def add_activity():
    if request.method == "GET":
        return render_template('add_activity.html')
    if request.method == "POST":
        item = request.form['activity']
        name = request.form['title']
        activity.add_activity(name, item)
        return redirect('/add_activity/' + name)


@app.route('/add_activity/<title>')
def get_bucketname(title):
    return render_template("add_activity.html", title=title)
