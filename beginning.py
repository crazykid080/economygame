from secret import secret_key

econ_ref = None

class admin:
	def mint(self, amount):
		econ_ref = None
		econ_ref.stored_money += amount
		return None

class economy:
	work_payment = 0.007
	wage_tax = 0.35
	referral_tax = 0.1
	
	budget = 1000
	
	def work_tax(self, amount, refferer_ID):
		taxed = amount * wage_tax
		amount -= taxed
		amount = round(amount, 4) #Prevent floating point errors
		budget += round(taxed, 4)
		return amount
	
class player:
	able_to_work = True
	refferer_id = 0
	balance = 0.0000

	def work(self):
		if(not self.able_to_work):
			raise Exception
		self.able_to_work = False
		econ_ref.work_tax(econ_ref.work_payment)
		return None
	
	def pay(self, amount, player):
		if((self.balance > amount and amount > 0) == False):
			raise Exception
		balance -= amount
		return None
	
	def recieve(self, amount, sender):
		assert(amount > 0) #Prevent negative transfers
		return None
		
