def main():
    infile = open('cities.txt', 'r')
    cities = infile.readlines()
    infile.close()

    Index = 0
    while Index < len(cities):
        cities[Index] = cities[Index].rstrip('\n')
        Index += 1
    print(cities)

main()