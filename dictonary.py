
iq = input("Dictonary?")
name = str(iq)
i2 = ''
dict_replace = {
    'land':'nederland',
    'dier':'hond',
    'steen':'stone',
    'Dier':'cat'
}

for l in name: 
  i2 += dict_replace[l] #it broke-