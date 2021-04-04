import dictionary_read
import time

class Game:
	def main(self):
		self.game_dict = dictionary_read.dictionary()
		self.game_loop()

		print("Bye! :\\")
		input()
		# mean = game_dict.mean_of(word)

		# if (mean == "NULL"):
		# 	print("Word does not exist!")
		# else:
		# 	print("It exists! \n It means: \n", mean)

	def game_loop(self):

		print("Enter a word to start (Enter 0 to exit):")
		word = ""
		prev_word = ""

		while word!= '0':
			word = input()

			if self.game_dict.is_word(word):
				if (self.is_accept(prev_word, word) or prev_word == ""):
					prev_word = self.game_dict.get_word(word)

					if (prev_word == None):
						prev_word = ""
						time.sleep(1)
						print("Can't find a word, I lost! :( \n Let's start again!")
						continue

					print(prev_word)
				else:
					print("Doesn't follow the rules, try again!")
			else:
				if (word != "0"):
					print("Not a word, try again :|")
		
	def is_accept(self, prev, word):
		for i in range(len(prev)-1):
			if word.startswith(prev[i:]): return True

		return False

if __name__ == '__main__':
	Game().main()