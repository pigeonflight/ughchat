"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, request
from flask import render_template
import urllib2
import json
from google.appengine.api import users
from google.appengine.api import channel

app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/current_player')
def current_player():
    """Return a current player name as json"""
    return "johnbrown"
    #user = users.get_current_user()
    #if user:
    #    return user.nickname()
    #else:
    #    return '<a href="%s">Sign in or register</a>.' % users.create_login_url('/')
    

@app.route('/mygame/<gameid>/<name>')
def hello(gameid,name):
    """Return a simple page"""
    token = channel.create_channel(name + gameid) #hardcoded key
    template_values = {
                       "gameid":gameid,
                       "name": name,
                       "token":token
                       }
    return render_template("chatroom.html",values=template_values)

@app.route('/sendmessage/<user>/<gameid>', methods=['GET', 'POST'])
def sendmessage(user,gameid):
    """sends a message that is useless"""
    message = request.form['message']
    channel.send_message(user+gameid,message)
    
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404
