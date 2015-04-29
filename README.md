# UTM
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