from mongoengine import *

# Connect to MongoDB
connect(host='mongodb://mongo:27017/testdb')

class User(Document):
    name = StringField(required=True)

if __name__ == '__main__':
    # Create a new user
    new_user = User(name='John Doe')
    new_user.save()
    # Retrieve and print all users
    for user in User.objects:
        print(f'User: {user.name}')

