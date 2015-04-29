class TM(object):
	"""docstring for TM"""
	def __init__(self, table, halt, blank):
		super(TM, self).__init__()

		self.table = table
		self.halt = halt
		self.blank = blank

	def returnMachine(self):
		return self.table, self.halt, self.blank
		

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
		5. All transition tables are assume to start on q0.

	Additonal notes:

		Data Structures:

			I opted to use a dictionary as my tape, making the keys integer values. To move on the tape, 
			the 'machine' gets the current value at self.index and then determines what to do next. Using
			dictionaries makes the tape size theoretically infinite (but in all practicality, you would 
			need lots of memory)
			
			Transition tables are also dictionaries, but thrice nested. Please take care to use the structure 
			laid out in the 5 tables I've provided.

		Run Times:

			Both the bb3 and bb4 seem to speed quickly. When running, it's almost immediate output. But, the bb5
			takes notably longer, just based on the number of transitions needed. bb5 took about 1:24(1 minute, 24 seconds)
			to run. 

	"""

	def __init__(self, TM, tape):
		self.currentState = "q0"

		table, accept, blankSymbol = TM.returnMachine()

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
			if len(tape) != 0:
				self.min = 0
				for i in range(len(tape)):
					self.tape[i] = tape[i]
					self.max = i
			else:
				self.tape[0] = self.blankSymbol

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
		print("Number of steps: " , format(self.numSteps,",d"))

	def printAccepts(self):
		for x in self.accept:
			print(x)

	def printStats(self):
		num0 = 0
		num1 = 0
		numblank = 0
		for x in range(self.min , self.max+1 ):
			 if(self.tape[x] == self.blankSymbol):
			 	numblank += 1
			 elif(self.tape[x] == "1"):
			 	num1 += 1
			 elif(self.tape[x] == "0"):
			 	num0 += 1

		print("blank : ", numblank, "\n1 : ", num1, "\n0 : ", num0)

	def simulate(self):

		while(not(self.currentState in self.accept)):
			self.move()
			print(self.printID())   ## I would suggest commenting this out for the bb5, considering it's 47 million steps. But, be my guest to leave it in.
			

blank = "_"

hw = {	 "q0" : {"0": {"state":"q1", "rewrite": blank, "move":1}, "1":{"state":"q5", "rewrite":blank, "move":1}}
			,"q1" : {"0": {"state":"q1", "rewrite": "0", "move":1}, "1":{"state":"q2", "rewrite":"1", "move":1}}
			,"q2" : {"0": {"state":"q3", "rewrite": "1", "move":-1} , "1" : {"state":"q2", "rewrite": "1", "move":1} , blank: {"state":"q4", "rewrite": blank, "move":-1}}
			,"q3" : {"0": {"state":"q3", "rewrite": "0", "move":-1} , "1" : {"state":"q3", "rewrite": "1", "move":-1} , blank: {"state":"q0", "rewrite": blank, "move":1}}
			,"q4" : {"0": {"state":"q4", "rewrite": "0", "move":-1} , "1" : {"state":"q4", "rewrite": blank, "move":-1} , blank: {"state":"q6", "rewrite": "0", "move":1}}
			,"q5" : {"0": {"state":"q5", "rewrite": blank, "move":1} , "1" : {"state":"q5", "rewrite": blank, "move":1} , blank: {"state":"q6", "rewrite": blank, "move":1}}
					} #HALT State is q6


nonTerminating = { "q0": { #this transition table has no halt state. 
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

bb3 = {	"q0" : { #HALT State is q3
			blank : {"state" : "q1", "rewrite":"1", "move":1 },
			"1" : {"state" : "q3", "rewrite":"1", "move":1 }},
		"q1" : {
			blank : {"state" : "q2", "rewrite":blank, "move":1 },
			"1" : {"state" : "q1", "rewrite":"1", "move":1 }},
		"q2" : {
			blank : {"state" : "q2", "rewrite":"1", "move":-1 },
			"1" : {"state" : "q0", "rewrite":"1", "move":-1 }}
		}

bb4 = {	"q0" : { #HALT State is q4
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


bb5 = {	"q0" : { #HALT State is q5
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
		
homework = TM(hw,"q6",blank)
nonTerm = TM(nonTerminating,"none",blank)
busyBeaver3 = TM(bb3,"q3",blank)
busyBeaver4 = TM(bb4,"q4",blank)
busyBeaver5 = TM(bb5,"q5",blank)

utm_homework  = UTM(homework, "000100")
utm_nonTerm  = UTM(nonTerm, "000100")
utm_bb3  = UTM(busyBeaver3, "")
utm_bb4  = UTM(busyBeaver4, "")
utm_bb5  = UTM(busyBeaver5, "")
try:
	choice = int(input("Choose which TM you wish to simulate: \n1)The Homework Problem\n2)Self Defined NonTerminating\n3)Busy Beaver 3\n4)Busy Beaver 4\n5)Busy Beaver 5\n\nPlease type an integer: "))
	if choice == 1:
		utm_homework.simulate()
		# utm_bb5.printStats()
	elif choice == 2:
		utm_nonTerm.simulate()
		utm_bb5.printStats()
	elif choice == 3:
		utm_bb3.simulate()
		utm_bb5.printStats()
	elif choice == 4:
		utm_bb4.simulate()
		utm_bb5.printStats()
	elif choice == 5:
		print("Please note the comment to comment out the printID function in the move function. This will allow you to run this busy beaver in a quicker time.")
		utm_bb5.simulate()
		utm_bb5.printStats()
except KeyboardInterrupt:
	print("Exiting...")
except:
	print("Invalid Choice.")

