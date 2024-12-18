import tiktoken

"""
The purpose of this file is to show how we can use an already established tokenizer library
Instead of our SimpleTokenizerV1 used in Embeddings.
"""

# get the tokenizer 
tokenizer = tiktoken.get_encoding("gpt2")

# Raw text
text = (
	"Hello, do you like tea? <|endoftext|> In the sunlit terrace akwirw ier"
	"of someunknownplace"
)

# Encode text to token_id
# explicitly tell tokenizer what special tags to look out for
token_id = tokenizer.encode(text, allowed_special={"<|endoftext|>"})


print(token_id)


# convert tokens back into text

token_back_to_text = tokenizer.decode(token_id)
print(token_back_to_text)