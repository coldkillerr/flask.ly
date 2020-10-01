from flask import Blueprint
from flask import render_template,url_for,flash,redirect
from  werkzeug.security import generate_password_hash , check_password_hash
from forms import RegistrationForm
from models import db ,User

router = Blueprint("router", __name__)

key_url_mapping={}
# a dictionary stores data in the form of key:value
# Here, the key will store the shortened URL and
# the value corresponding to it will store the actual URL

@router.route('/api/status')
def status():
    return "Up and Running ! :)"

@router.route('/api/shorten/quick')
def quickShorten():
    # Create a dictionary which has the shortened URL as the key
    # And the actual URL as the value
    # For easy implementation, just keep auto incrementing the key 
    return 1;

@router.route('/api/shorten/url')
def shorten():
    # Take the input URL from a user
    # Check if it's already in the database
    # If it already exists: return the shortened URL
    # Else: Shorten it using any encoding or algorithm 
    # You can use Base 62 too, (https://helloacm.com/base62/)
    # Store the input URL and the shortened URL
    # mapped together in the url database
    # Return the shortened URL back
    return 1;

@router.route('/api/register')
def register():
    # Register a User by taking their credentials basically
    # email id and password and storing them in the user database
    # After registration, redirect them to the /shorten/custom
    form=RegistrationForm()
    if form.validate_on_submit():
    	hashed_password = generate_password_hash(form.password.data , method='sha256')
    	existing_users = User.query.all()
     
    	if existing_users:
    		for user in existing_users :
                if form.email.data == user.email_id :
                    flash('Email already taken . Please try again .','danger')
                    return redirect(url_for('register'))
        
        
 		new_user = Lawyer( email_id = form.email.data  , password = hashed_password)
		db.session.add(new_user)
		db.session.commit()
        flash('Registration Successfull','success')
        return redirect(url_for('customShorten'))
	# return render_template('Registrationform.html',form=form) 
    # Uncomment this when you add a registration page template
    return 1;

@router.route('/api/login')
def login():
    # Validate a user by taking their email id and password
    # Check if they match in the user database
    # If they match: redirect them to the /shorten/custom
    # Else send them appropriate message accordingly
    return 1;

@router.route('/api/logout')
def logout():
    # Check if a User is logged in
    # If user is logged in, log them out
    return 1;

@router.route('/api/shorten/custom')
def customShorten():
    # Check whether the user is logged in or not
    # If the user is not logged in, redirect them to the /login page
    # else take the input URL to be shortened & the shortened URL they want
    # Check if the shortened URL is already present in the database
    # If its not, store the user's input and return their custom URL
    # Else ask the user to enter any other custom URL and repeat the process
    return 1;

@router.route('/')
def redirectToActualURL():
    # Get the entered URL as (localhost:5000/shortenedURL)
    # Now, this route finds the actual URL corresponding to the given one
    # and redirects the user to that actual URL
    return 1;
