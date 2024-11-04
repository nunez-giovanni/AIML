import tiktoken

# Read file
with open("the_verdict.txt", "r") as f:
	raw_text = f.read()
	
# create a tokenizer 
tokenizer = tiktoken.get_encoding("gpt2")

# text to token_ids 
encoded_text_to_token_ids = tokenizer.encode(raw_text)

# print(encoded_text_to_token_ids)
print("count of token ids ", len(encoded_text_to_token_ids))


# ===  create X as input tokens and Y as the target tokens  ==

context_size = 4 # context size determines how many tokens are included in input


x = encoded_text_to_token_ids[0: context_size] # input is from first token_id up to `4`

y = encoded_text_to_token_ids[0: context_size +1] # input is from first token_id up to `5`

print("input x: ", x, "\n input y:", y)


for i in range(1, context_size +1):
	context = encoded_text_to_token_ids[0: i] # print all items up to but excluding current
	desired = encoded_text_to_token_ids[i] # print current which is the next desired token_id
	
	print("\n the context", context, "\n the desired", desired, "\n")
	print(tokenizer.decode(context), "---->", tokenizer.decode([desired]))
	