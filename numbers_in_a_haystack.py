import re
hand = open('C:\\Users\\april\\Desktop\\python\\actual_data.txt')
numlist = []

for line in hand:
  line = line.rstrip()
  stuff = re.findall('[0-9]+', line)
  
  if len(stuff) < 1:
    continue
  
  for string in stuff:
    numlist.append(int(string))
print(sum(numlist))


# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
