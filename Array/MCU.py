# Let's try something new. My favourite Super Hero's.
# Let's list down them first.
# 1. Iron Man
# 2. Captain America
# 3. Thor
# 4. Black Widow
# 5. Clint Barten
# Let's make an array by letting this guys in.
heros = ['Iron Man', 'Captain America', 'Thor', 'Black Widow', 'Clint Barten']
print(heros)
# Oops! I forgot about Hulk and Black Panther. Let's add him to the list.
heros.append('Hulk')
print(heros)
heros.append('Black Panther')
print(heros)
# Ohh! I realize that Doctor Strange is also there but he came before Black Panther
# for me. So let's add him to the list at specific position.
heros.insert(6, 'Doctor Strange')
print(heros)
# Let's sort them by their alphabetical order.
heros.sort()
print(heros)
