from flask  import render_template
from app import app



@app.route('/')
def index():
    """
    Renders the index page
    """
    return render_template("index.html")


@app.route('/signup')
def signup():
    """
    Renders the sign up page
    """
    return render_template('/signup.html')


@app.route('/dashboard')
def dashboard():
    """
    Renders the dashboard page
    """
    return render_template("dashboard.html")


@app.route('/create')
def create_bucketlist():
    """
    Renders the create bucketlist page
    """
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
