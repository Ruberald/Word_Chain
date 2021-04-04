import json

class dictionary:

	def __init__(self):
		self.dict_json = ""
		with open('words_dictionary.json') as file:
			self.dict_json = json.load(file)

		self.dict_array = list(self.dict_json.keys())

	def is_word(self, word):

		word = word.lower()
		flag = False

		if word in self.dict_json:
			flag = True

		return flag

	# def get_word(self, word):

	# 	word = word.lower()
	# 	return_stuff = "NONE"

	# 	if(self.mean_of(word) == 'NULL'): return_stuff = 'NULL'
	# 	else:
	# 		i = 0
	# 		while i < len(word)-1:
	# 			subword = word[i:]
	# 			for a_word in self.dict_json:
	# 				if (a_word.startswith(subword)):
	# 					return_stuff = a_word
	# 			i+=1

	# 	return return_stuff

	def get_word(self, word):
		word = word.lower()

		for i in range(0 if len(word)==2 else 1, len(word)-1):
			sub_word = word[i:]
			# print(sub_word)
			l_lim = 0 
			u_lim = len(self.dict_array)-1
			mid = 0			

			while l_lim < u_lim:
				mid = l_lim + ((u_lim - l_lim)//2)
				midval = self.dict_array[mid]

				if sub_word < midval:
					if midval.startswith(sub_word):
						return midval
					else: 
						u_lim = mid-1

				elif sub_word > midval or sub_word == midval:
					l_lim = mid+1

				
# if __name__ == '__main__':
# 	dictionary().get_word(input("Enter:"))