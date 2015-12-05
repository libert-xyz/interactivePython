def an(w,w2):


	if len(w) == len(w2):

		for i in w:
			
			if i not in w2:

				return False
				break

		return True

	else:
		return "Bad lenght" 
