class UTM(object):
	"""docstring for UTM"""

	def __init__(self, table, tape, accept, blankSymbol ):
		self.currentState = "q0"
		self.tape = {}
		self.blankSymbol = blankSymbol
		self.index = 0
		self.accept = accept
		self.inputTape(tape)
		self.transitionTable = table
		self.numSteps = 0
		self.min = 0
		self.max = 0
		super(UTM, self).__init__()
	
	def inputTape(self, tape):
		if type(tape) is str :
			# print(len(tape))
			if len(tape) != 0:
				for i in range(len(tape)):
					self.tape[i] = tape[i]
					# print str(i) + " : " + self.tape.get(i)
			else:
				self.tape[0] = self.blankSymbol

		elif type(tape) is dict:
			self.tape = tape
		else:
			raise Exception("Invalid Tape input.")

	def move(self):
		#get the current index, current state
		# self.index
		# self.currentState
		# test = self.transitionTable.get(self.currentState).get(self.tape.get(self.index))
		#get the move and rewrite the part of the string
		# for x in test:
		# 	for y in test[x]:
		# 		print (y,':',test[x][y])
		# print(":::" + self.transitionTable.get(self.currentState).get(self.tape.get(self.index)) )
		# self.printID()

		if(self.min > self.index):
			self.min = self.index
			print("updating min")
		elif(self.max < self.index):
			self.max = self.index
			print("updating max")

		if(min(self.tape) > self.index or self.index > max(self.tape)):
			# print(self.index)
			self.addNull()

		# print(self.transitionTable.get("q1"))
		transition = self.transitionTable.get(self.currentState).get(self.tape.get(self.index)) 
		self.tape[self.index] = transition.get("rewrite")
		# print(move.get("rewrite"))
		self.currentState = transition.get("state")
		
		self.index += transition.get("move")

		self.numSteps += 1
		

	def printID(self):
		printME = ''
		# print(range(min(self.tape),max(self.tape)))
		# print(min(self.tape))
		
			# print(range(min(self.tape),max(self.tape)))
		for x in range(min(self.tape), max(self.tape)+1 ):
			 
			printME += ("(" + self.currentState + ")>" if (x == self.index) else '' )
			printME += self.blankSymbol if self.tape[x] == None else self.tape[x] + ""

		return printME

	def addNull(self):
		# print("adding null")
		self.tape[self.index] = self.blankSymbol
		
		# return self.transitionTable.get(self.currentState).get(None)
	def printIndex(self):
		print(self.index)

	def printState(self):
		print(self.currentState)

	def printNumSteps(self):
		print(self.numSteps)

	def simulate(self):
		import time
		self.printID()
		while(self.currentState != self.accept):
			self.move()
			# self.printID()
			# time.sleep(5)
			self.printNumSteps()
		# open("number.txt",'w').write/()
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
				blank : {"state" : "q1", "rewrite":"1", "move": -1},
				"1" : {"state" : "q3", "rewrite":"1", "move":-1 }},
		"q4" : {
				blank : {"state" : "q5", "rewrite":"1", "move":1 },
				"1" : {"state" : "q0", "rewrite":blank, "move":-1 }}
		
		}
		
# 
utm  = UTM(hw, "000100", "q6", blank)

utm.simulate()
utm.printNumSteps()
print(utm.printID())

