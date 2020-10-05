the_file = open('test.txt')
test = {}
for line in the_file:
    line = line.rstrip()
    words = line.split(" ")
     
    for word in words:
        word = word.capitalize() 
        test[word] = test.get(word,0) + 1


print(test)

for test, number in test.items():
    print(f'{test}: {number}')
