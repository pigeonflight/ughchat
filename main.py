"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, request
from flask import render_template
import urllib2
import json
import random
import uuid
from google.appengine.api import users
from google.appengine.api import channel
from utilities import funnames
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/')
def index():
    """Setup a chat"""
    gameid = "%s-%s" % (str(uuid.uuid4())[:4],random.choice(funnames).lower())
    template_values = {
                       "gameid":gameid
                                     }
    return render_template("index.html",values=template_values)

@app.route('/<gameid>/<name>')
def setupchat(gameid,name):
    """Return a simple page"""
    token = channel.create_channel(name + gameid) 
    template_values = {
                       "gameid":gameid,
                        "token": channel.create_channel(name + gameid)
                       }
    return render_template("setup.html",values=template_values)
    
@app.route('/g/<gameid>/<name>')
def chatgame(gameid,name):
    """Return a simple page""" 
    # unique token
    token = channel.create_channel(name + gameid)
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
    return 'Sorry, No Valid Chatroom There.', 404
