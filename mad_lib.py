# A Mad Libs style game where user enters nouns,
#verbs, and variables. A story is then produced
# using these words as a story as an output.

# User word variables
relative = input("Enter a type of relative:")

food = input("Enter a type of food:")

adjective = input("Enter a type of adjective:")

period = input("Enter a time period:")

# Tell the story
print("My", relative, "Says eating", food)
print("will make me more", adjective)
print("so now I eat them every", period)
