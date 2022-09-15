from solution import FileReader

reader = FileReader('not_exist_file.txt')
print(reader.read())
# ''

with open('some_file.txt', 'w') as file:
    file.write('some text')
reader = FileReader('some_file.txt')
print(reader.read())
# 'some text'

print(type(reader))
# <class 'solution.FileReader'>

reader = FileReader('Lorem_ipsum.txt')
print(reader.read())
# 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,
# sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
