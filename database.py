from secret import secret_key
import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker

class database:
	connection = None
	session = None
	users = None #Bad way to do it? Probably.
	def __init__(self, name='main'):
		engine = db.create_engine('sqlite:///'+name+'.sqlite')
		self.connection = engine.connect()
		Session = sessionmaker(bind=engine)
		self.session = Session()
		metadata = MetaData()
		self.users = Table('users', metadata, 
		Column('id', Integer, primary_key=True),
		Column('username', String(25) ),
		Column('email', String(40) ),
		Column('password', String(70) ) )
	
	def get_user(self, username):
		query = self.session.query(self.users).filter_by(username=username).all()
		print(query)
		#user = self.connection.execute(query)
		return user
	
	def get_email(self, email):
		query = self.session.query(self.users).filter_by(email=email)
		user = self.connection.execute(query)
		return user
	
	def add_user(self, name, email, password):
		#verify user does not exist
		user_check = self.get_user(name)
		if(user_check != None):
			raise Exception
		#verify email does not exist
		user_check = self.get_email(email)
		if(user_check != None):
			raise Exception
		#sanitize. How? Regex maybe?
		#add user to database
		self.users.insert().values(username=name, email=email, password=password)
		return None
	
	def change_password(self, user, old_password, new_password):
		#verify user exists
		#get current password from db
		#compare current to old, return false if false
		if(old_password == new_password):
			raise Exception
		return None

if __name__ == '__main__':
	maindb = database()
	insertion = None