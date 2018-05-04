import random

word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()

num = random.randint(3,5)

#print " ".join([WORDS[random.randrange(0, len(WORDS))] for i in range(8)])

term = ' ' .join([WORDS[random.randrange(0, len(WORDS))] for i in range(num)])

#print term
#print (WORDS)
