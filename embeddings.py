#!/usr/bin/env python3

import re
from SimpleTokenizerV1 import SimpleTokenizerV1



def get_raw_text():
	""" 1. Read Raw file """
	
	raw_text = None
	
	with open("the_verdict.txt", "r", encoding="utf-8") as f:
		raw_text = f.read()
		
	return raw_text

	
	
	
def tokenize_raw_text():
	""" 2. Take raw text and create tokenized words """
	
	split_text = re.split(r'([,.:;?_!"()\']|--|\s)', get_raw_text())
	preprocessed_words = [item.strip() for item in split_text if item.strip()]

	unique_words_sroted = sorted(set(preprocessed_words))
	
	return unique_words_sroted;
	
	
	
	
def create_vocab(sorted_tokens):
	""" Create vocab which is a mapping of the word token to a unique integer ID """
	
	# create a map of the sorted_tokens. The index works as our token_id in integer since the tokens are unique.
	vocab = {token: integer for integer, token in enumerate(sorted_tokens)}
	
	for i, item in enumerate(vocab.items()):
		print(item)
		
		
	print("====== END VOCAB ======\n")
	return vocab




vocab = create_vocab(tokenize_raw_text())

# Import our tokenizer 
tokenizer = SimpleTokenizerV1(vocab)

# tokenize new text
test_text = """"It's the last he painted, you know," 
		Mrs. Gisburn said with pardonable pride."""

ids = tokenizer.encode(test_text)
print(ids)



#detokenize 
print(tokenizer.decode(ids))