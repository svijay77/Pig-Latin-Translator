import sys
print(sys.executable)
print(sys.version)

def listToString(s):
	newStr = ""
	newStr = " ".join(s)
	return newStr

class Translator:
	def getInput(self):
		word = input("\nEnter your sentence: ")
		self.word = word
	def translate(self):
		sentence = self.word
		sentence = sentence.split()
		newSentence = []
		for word in sentence:
			if (word[0].lower() in ['a' ,'e' ,'i' ,'o' ,'u']) and (word[-1].lower() in ['a' ,'e' ,'i' ,'o' ,'u']):
				newSentence.append(word + "way")
				 #aioli is aioliway
			elif word[0].lower() in ['a' ,'e' ,'i' ,'o' ,'u']:
				newSentence.append(word + "ay")
				 #exit is exitay
			elif (word[0].lower() in ['b','c','d','f','g','h','l','m','n','p','r','s','t']) and (word[1].lower() in ['b','c','d','f','g','h','l','m','n','p','r','s','t']):
				newSentence.append(word[2:] + word[:2] + "ay")
				 #crash is ashcray
			else:
				newSentence.append(word[1:] + word[0] + "ay")
		newSentence = listToString(newSentence)
		print("In Pig Latin, your sentence,","'"+self.word+"'","translates to:","\n\n'"+newSentence+"'")


def main():
	w1 = Translator()
	s = False
	while not s:
		answer = input("Translate a sentence? [y/n]\n")
		answer = answer.lower()
		if answer == "no" or answer == "n":
			sys.exit()
		elif answer == "yes" or answer == "y":
			w1.getInput()
			w1.translate()
		else:
			print("\nOops, please type 'y' for yes, 'n' for no.")

main()
