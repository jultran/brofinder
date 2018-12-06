from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, send, emit

# TODO: Logic for handling how events get broadcast/happen may need to change
# TODO: add logic for handling gps coords etc

app = Flask(__name__)
socketio = SocketIO(app)

# in process/memory, not good practice but it'll be good enough
groups = dict()

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


# Route to create new group
# Front end should transition to appropriate page
@app.route('/api/v1/create_group', methods=["POST"])
def create_group():
    username = flask.request.form['username']
    groupname = flask.request.form['groupname']
    group_password = flask.request.form['password']

    if groupname in groups:
        message = 'Specified group already exists'
        response = {'message': message, 'url': flask.request.path}
        return jsonify(**response), 403

    # create the group, add the password set things up for later
    groups[groupname] = dict()
    groups[groupname]['users'] = list()
    groups[groupname]['password'] = group_password

    # set up response
    response = dict()
    response['url'] = flask.request.path
    response['data'] = dict()
    response['data']['username'] = username
    response['data']['groupname'] = groupname
    response['data']['password'] = password
    response['data']['joined'] = True

    join_room(groupname)
    groups[groupname]['users'].append(username)

    return flask.jsonify(**response), 201


@app.route('/api/v1/join_group', methods=["POST"])
def join_group():
    username = flask.request.form['username']
    groupname = flask.request.form['groupname']
    group_password = flask.request.form['password']

    # TODO: fix these returns to be more useful
    if groupname not in groups:
        return 404

    # yes this protocol is incredibly insecure...
    if groups[groupname]['password'] != group_password:
        return 403

    # TODO: deal with duplicate usernames, probably need some kind of internal userid
    if username in groups[groupname]['users']:
        return 403

    groups['groupname']['users'].append(username)

    join_room(groupname)

    send(username + ' has joined the room', room=groupname)

    response = dict()
    response['url'] = flask.request.path
    response['data'] = dict()
    response['data']['username'] = username
    response['data']['groupname'] = groupname
    response['data']['password'] = password

    return flask.jsonify(**response), 201


@socketio.on('ping')
def ping(data):
    response = dict()
    response['data']['sent_by'] = data['username']
    response['data']['target'] = data['target_name']
    # can construct the alert message on the front end pretty easily
    emit('ping received', response, room=data['groupname'])

if __name__ == "__main__":
    socketio.run(app)