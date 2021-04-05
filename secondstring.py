#A program that asks user to input a string and outputs every second letter in reverse order.
#Author: Mantvydas Jokubaitis

sentence = input("Please input a sentence: ")
example = "The quick brown fox jumps over the lazy dog."
print("Example sentence: ", example, "Every second letter in reverse order: ", example[::-2])
print("Your sentence: ", sentence[::-2])