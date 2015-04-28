class UTM(object):
	"""

	In order to run this UTM, please follow the instructions below:

		1. I have supplied the necessary transition tables. Please replace them at your
			will to demonstrate the functionality.
		2. To pass in the tape, please only use strings. So, if you want a tape of 
			5 zeros, enter '00000'. Entering '' is interpreted to be a tape of blank symbols.
		3. When constructing the transition tables, I've omitted the accept states as seperate lines.
			Please take notice that you can supply the accept states as their values seperated by commas.
		4. The blank symbol is considered to be an underscore. You may change this at your own risk. 
		5. 


	"""

	def __init__(self, table, tape, accept, blankSymbol ):
		self.currentState = "q0"
		self.tape = {}
		self.blankSymbol = blankSymbol
		self.min = 0
		self.max = 0
		self.index = 0
		self.accept = accept.split(',')
		self.inputTape(tape)
		self.transitionTable = table
		self.numSteps = 0
		super(UTM, self).__init__()
	
	def inputTape(self, tape):
		if type(tape) is str :
			# print(len(tape))
			if len(tape) != 0:
				self.min = 0
				for i in range(len(tape)):
					self.tape[i] = tape[i]
					self.max = i
			else:
				self.tape[0] = self.blankSymbol

		elif type(tape) is dict:
			self.tape = tape
		else:
			raise Exception("Invalid Tape input.")

	def move(self):

		transition = self.transitionTable.get(self.currentState).get(self.tape.get(self.index)) 
		self.tape[self.index] = transition.get("rewrite")
		self.currentState = transition.get("state")
		self.index += transition.get("move")
		self.numSteps += 1

		if(self.min > self.index or self.index > self.max):
			self.addNull()

		if(self.min > self.index):
			self.min = self.index
			
		elif(self.max < self.index):
			self.max = self.index
		

	def printID(self):
		printME = ''
		
		for x in range(self.min , self.max+1 ):
			 
			printME += ("(" + self.currentState + ")>" if (x == self.index) else '' )
			printME += self.blankSymbol if self.tape[x] == None else self.tape[x] + ""

		return printME

	def addNull(self):
		
		self.tape[self.index] = self.blankSymbol
		
	def printIndex(self):
		print(self.index)

	def printState(self):
		print(self.currentState)

	def printNumSteps(self):
		print(format(self.numSteps,",d"))

	def printAccepts(self):
		for x in self.accept:
			print(x)

	def printStats(self):
		num0 = 0
		num1 = 0
		numblank = 0
		# print(self.min, ":", self.max)
		for x in range(self.min , self.max+1 ):
			 if(self.tape[x] == self.blankSymbol):
			 	numblank += 1
			 elif(self.tape[x] == "1"):
			 	num1 += 1
			 elif(self.tape[x] == "0"):
			 	num0 += 1

		print("blank : ", numblank, "\n1 : ", num1, "\n0 : ", num0)

	def simulate(self):
		import time
		# self.printID()
		while(not(self.currentState in self.accept)):
			self.move()
			print(self.printID())   
			

blank = "_"

# table = {"q0": { "0" : {"state": "q0", "rewrite": "1" , "move": 1 }, "1":{"state":"q0", "rewrite":"0", "move":-1}, None:{"state":"q1", "write":"0", "move":-1} } }
hw = {	 "q0" : {"0": {"state":"q1", "rewrite": blank, "move":1}, "1":{"state":"q5", "rewrite":blank, "move":1}}
			,"q1" : {"0": {"state":"q1", "rewrite": "0", "move":1}, "1":{"state":"q2", "rewrite":"1", "move":1}}
			,"q2" : {"0": {"state":"q3", "rewrite": "1", "move":-1} , "1" : {"state":"q2", "rewrite": "1", "move":1} , blank: {"state":"q4", "rewrite": blank, "move":-1}}
			,"q3" : {"0": {"state":"q3", "rewrite": "0", "move":-1} , "1" : {"state":"q3", "rewrite": "1", "move":-1} , blank: {"state":"q0", "rewrite": blank, "move":1}}
			,"q4" : {"0": {"state":"q4", "rewrite": "0", "move":-1} , "1" : {"state":"q4", "rewrite": blank, "move":-1} , blank: {"state":"q6", "rewrite": "0", "move":1}}
			,"q5" : {"0": {"state":"q5", "rewrite": blank, "move":1} , "1" : {"state":"q5", "rewrite": blank, "move":1} , blank: {"state":"q6", "rewrite": blank, "move":1}}
					}

# nonTerm = {	 "q0" : {"0": {"state":"q0", "rewrite": blank, "move":1}, "1":{"state":"q0", "rewrite":"0", "move":1}, blank : {"state":"q0", "rewrite":"1", "move": 1}}}

nonTerminating = { "q0": {
						"0": { "state" : "q0" , "rewrite":"1", "move": 1},
						blank : {"state" : "q1", "rewrite":blank, "move": -1},
						"1": {"state" : "q0", "rewrite" : "1", "move" : 1}
						},
					"q1":
						{
						"0": { "state" : "q1" , "rewrite":"0", "move": -1},
						blank : {"state" : "q0", "rewrite":blank, "move": 1},
						"1": {"state" : "q1", "rewrite" : "0", "move" : -1}
						}}

bb3 = {	"q0" : {
			blank : {"state" : "q1", "rewrite":"1", "move":1 },
			"1" : {"state" : "q3", "rewrite":"1", "move":1 }},
		"q1" : {
			blank : {"state" : "q2", "rewrite":blank, "move":1 },
			"1" : {"state" : "q1", "rewrite":"1", "move":1 }},
		"q2" : {
			blank : {"state" : "q2", "rewrite":"1", "move":-1 },
			"1" : {"state" : "q0", "rewrite":"1", "move":-1 }}
		}

bb4 = {	"q0" : {
			blank : {"state" : "q1" , "rewrite": "1", "move": 1},
			"1" : {"state" : "q1" , "rewrite": "1", "move": -1}},
		"q1" : {
				blank : {"state" : "q0", "rewrite":"1", "move": -1},
				"1" : {"state" : "q2", "rewrite": blank, "move": -1}},
		"q2" : {
				blank : {"state" : "q4", "rewrite":"1", "move":1 },
				"1" : {"state" : "q3" , "rewrite":"1", "move": -1 }},
		"q3" : {
				blank : {"state" : "q3", "rewrite": "1", "move": 1},
				"1" : {"state" : "q0", "rewrite":blank, "move": 1}},
		}


bb5 = {	"q0" : {
				blank : {"state" : "q1", "rewrite":"1", "move": 1},
				"1" : {"state" : "q2", "rewrite":"1", "move": -1}},
		"q1" : {
				blank : {"state" : "q2", "rewrite":"1", "move": 1},
				"1" : {"state" : "q1", "rewrite":"1", "move": 1}},
		"q2" : {
				blank : {"state" : "q3", "rewrite":"1", "move": 1},
				"1" : {"state" : "q4", "rewrite":blank, "move": -1}},
		"q3" : {
				blank : {"state" : "q0", "rewrite":"1", "move": -1},
				"1" : {"state" : "q3", "rewrite":"1", "move":-1 }},
		"q4" : {
				blank : {"state" : "q5", "rewrite":"1", "move":1 },
				"1" : {"state" : "q0", "rewrite":blank, "move":-1 }}
		
		}
		
# 
utm  = UTM(bb4, "", "q4", blank)
utm.printStats()
try:
	utm.simulate()
	# utm.printNumSteps()
	# utm.printAccepts()
	# utm.printStats()
	# print(utm.printID())
except KeyboardInterrupt:
	print()
	utm.printNumSteps()
# utm.printStats()
# utm.printIndex()