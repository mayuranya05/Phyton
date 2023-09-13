print("Please select menu : \n 1.Display Heroes \n 2.Add Heroes, \n 3.Insert Heroes \n 4.Remove Heroes \n 5.Display Sorted Heroes(Ascending / Descanding)")
op_from = int(input("Select menu from 1, 2, 3, 4, 5 : "))

heroes = ['Ironman', 'Thor', 'Hulk', 'Superman', 'Spidman',]
h2 = ['Dr. Strange', 'Cat.America', 'Black Panther', 'Ant Man']

newheroes = heroes
newheroes[-1] = 'Woder Women'
print(newheroes)

heroes.remove('Woder Women')
print(heroes)

heroes.reverse()
print(heroes)

heroes.sort()
print(heroes)
