import firebase_admin
from firebase_admin import credentials, firestore

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)

db = firestore.client()

def get_users():
    """Returns all users in the db
    """
    return db.collection('users').get()


def get_user(user_id):
    """Returns a user by id
    """
    return db.collection('users').document(user_id).get()


def user_put(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password})


def get_todos(user_id):
    """Returns todos of an user
    """
    return db.collection('users').document(user_id).collection('todos').get()


def put_todo(user_id, description):
    todos_collection_ref = db.collection('users')\
        .document(user_id).collection('todos')

    todos_collection_ref.add({'description': description,
                              'done': False})


def delete_todo(user_id, todo_id):
    
    #! Las dos siguientes formas son equivalentes:
    todo_ref = db.document('users/{}/todos/{}'.format(user_id, todo_id))
    #? todo_ref = db.collection('users').document(user_id)\
    #?     .collection('todos').document(todo_id)

    todo_ref.delete()
