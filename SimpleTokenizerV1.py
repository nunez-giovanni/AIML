#!/usr/bin/env python3

import re

class SimpleTokenizerV1:
	def __init__(self, vocab):
		self.str_to_int = vocab
		self.int_to_str = { i:s for s, i in vocab.items() } # creates a map where we swap the KVP from original
		
		
		
	def encode(self, text):
		preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
		
		preprocessed = [
			item.strip() for item in preprocessed if item.strip()
		]
		
		# simply reads from map -> matches the unique string and grabs the unique integer for it 
		ids = [self.str_to_int[s] for s in preprocessed]
		
		return ids
	
	
	def decode(self, ids):
		# simply reads from the map -> matches the int and grabs the unique word its mapped to
		text = " ".join([self.int_to_str[i] for i in ids])
		
		text = re.sub(r'\s+([,.?!"()\'])', r'\1', text) 
		return text
	
	