phonebook = {'Anirach': '777-1111', 'Micky': '777-2222',
             'Donald': '777-3333', 'Pluto': '777-4444'}

heroesdit = {}
heroesdit['Hulk'] = '888-1111'
heroesdit['Iron Man'] = '888-2222'
print(heroesdit.get('Hulk', 'Key not found'))
print(heroesdit.get('Iron Man', 'Key not found'))

for key, value in phonebook.items():
    print(key, value)

print(phonebook.keys())
print(phonebook.values())

print(phonebook.pop('Mic', 'Element not found'))
print(phonebook.pop('Micky', 'Element not found'))
print(phonebook)
print(phonebook.popitem())
print(phonebook)
phonebook.clear()
print('After clear')
print(phonebook)