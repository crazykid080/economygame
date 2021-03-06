import json
from exceptions import *

def convert_currency(amount):
	units = amount * 10000
	return units
	
def convert_units(units):
	currency = units / 10000
	return currency

class economy:
	work_payment = 0.007
	wage_tax = 0.35
	referral_tax = 0.1
	account = None
	user = None

	def __init__(self, database):
		try:
			account = database.get_account(1)
			if(account[0][1] == "SYSTEM"):
				self.account = account
		except NoAccountExists:
			database.add_account("SYSTEM", 1000000)
			account = database.get_account(1)
			self.account = account
		try:
			user = database.get_user(1)
			if(user == None):
				database.add_user("SYSTEM", "SYSTEM", None)
				user = database.get_user(1)
			if(user[0][1] == "SYSTEM"):
				self.user = user

	def work_tax(self, units, refferer_ID):
		taxed = units * self.wage_tax
		units -= taxed
		units = round(units, 4) #Prevent floating point errors
		return units
		
	def read_state(self, file):
		file_obj = open(file + '.json')
		json_data = json.load(file_obj)
		print(json_data["test"])
		pass
	
	def write_state(self, file):
		pass
