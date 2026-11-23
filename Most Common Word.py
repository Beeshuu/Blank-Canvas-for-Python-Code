"""
Bishal Nath
bishal.nath66@login.cuny.edu		
"""

phrase = "MORE:  The more that you read, the more things you will know. The more that you learn, the more places you'll go. --Dr. Seuss" 
phrase = phrase.lower()
punctuation_list = ['.',',','!','?',':',';','\n','\t','-','  ']
for pun in punctuation_list:
	phrase = phrase.replace(pun,' ')
print('Phrase unpunctuated:', phrase)

def most_common(phrase):
	words = phrase.split()
	word_count = {}
	for word in words:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1
	most_common_word = max(word_count, key=word_count.get)
	return most_common_word
  
print('Most common word:', most_common(phrase))