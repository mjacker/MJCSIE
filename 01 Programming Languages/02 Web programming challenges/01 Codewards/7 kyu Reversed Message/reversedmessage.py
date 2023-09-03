def reverseMessage(str):
    return "".join([w[0].upper() + w[1:] + " " for w in str[::-1].lower().split(" ")]).rstrip()

print(reverseMessage("This is an example of a Reversed Message!"))



