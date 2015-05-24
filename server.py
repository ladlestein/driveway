from flask import Flask
from flask import request
from twilio.rest import TwilioRestClient

app = Flask(__name__)
app.config['DEBUG'] = True

account_sid = "AC888bdf652500c36645782e8e428d0d25"
auth_token = "2bf69fd06e031a9af5afced4897736d3"
twilio_number = "+1 415-951-3997"

#
# Q: Is it safe to keep the client in a global like this??
#
client = TwilioRestClient(account_sid, auth_token)

@app.route('/', methods=['POST'])
def hello():
    """Return a friendly HTTP greeting."""
    sender = request.form['From']
    target = request.form['Body']
    print "{} from {}".format(sender, target)
    print repr(request.form)

    # call some service, get back a tuple (blocked: boolean, number: phone-number)
    response = lookup(sender, target)
    if response[0]:
        sendThanks(sender)
    else:
        if target <> None:
            send(response[1], "Move your car")
            sendThanks(sender)
        else:
            send(sender, "We couldn't find that guy")
    
    return 'Hello World!'

def sendThanks(target):
    send(target, "Thanks for using Driveway")

def send(target, message):
    print "to = {}".format(target)
    client.messages.create(body = message, to = target, from_ = twilio_number )


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

def lookup(sender, target):
    return (False, "+14157139148")

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

# Uh, that's the canned text I copied. To get this server to run, I added the call to run() below.


if __name__ == '__main__':
    app.run(port=8080, host="0.0.0.0")
