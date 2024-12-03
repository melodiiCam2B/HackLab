def XO(text):
  return text.lower().count('x')==text.lower().count('o')


iq = input("List of Xx/Oo?")
print(XO(iq))