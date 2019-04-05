from datetime import datetime, timedelta
from requester import db
from werkzeug.security import generate_password_hash, check_password_hash
from requester.models import User, Client, ProductCategory
#from faker import Faker
#import utils

def populate_db():
    print('Populating database ...')
    try:
        populate_clients_data()
        populate_product_categories_data()
        populate_user_data()
        #populate_description_data()
    except Exception as e:
        print(f'Something went wrong: {e}')
        exit(1)
    
    print('Data successfully populated!')

def populate_clients_data():
    try:
        # Delete existing data
        db.session.query(Client).delete()
        db.session.commit()
        
        clients = [ 'Client A', 'Client B', 'Client C', 'Client D' ]
        
        for client in clients:
                db.session.add( Client(client) )

        db.session.commit()

    except Exception as e:
        print( f'Error: {e}' )
        db.session.rollback()
        exit(1)

def populate_description_data():
    try:
      fake = Faker()
      description = utils.Truncate(fake.text(), 999)
      print(description)

    except Exception as e:
      print( f'Error: {e}' )
      db.session.rollback()
      exit(1)

def populate_product_categories_data():
    try:
        # Delete existing data
        db.session.query(ProductCategory).delete()
        db.session.commit()
        
        categories = [ 'Policies', 'Billing', 'Claims', 'Reports' ]
        
        for category in categories:
                db.session.add( ProductCategory(category) )

        db.session.commit()

    except Exception as e:
        print( f'Error: {e}' )
        db.session.rollback()
        exit(1)

def populate_user_data():
    try:
        # Delete existing data
        db.session.query(User).delete()
        db.session.commit()
        
        logins = [ 
                ("login", "login")
        ]
        
        for login in logins:
                db.session.add(User(login[0], login[1]))

        db.session.commit()

    except Exception as e:
        print( f'Error: {e}' )
        db.session.rollback()
        exit(1)

if __name__ == '__main__':
    populate_db()