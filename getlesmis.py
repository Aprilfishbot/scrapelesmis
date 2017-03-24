import gutenberg
import markovify


# Get raw text as string.
with open("C:/Users/Florence/135-0.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text, state_size=3)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())
 