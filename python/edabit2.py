def hamming_distance(txt1, txt2):
	return sum(x!=y for (x,y) in zip(txt1,txt2))

iq = input("String 1!")
i2= 'abdccred'
print(hamming_distance(iq, i2))