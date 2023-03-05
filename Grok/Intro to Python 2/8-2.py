letter_counts = {}
package_counts = {}

with open("mail.txt",'r') as f:
  for line in f:
    person, mail = line.rstrip().split(',')
    line = line.rstrip().split(',')

    if mail == "Letter":
      if person in letter_counts:
        print(person, "+= letter")
        letter_counts[person] += 1
      else:
        letter_counts[person] = 1
        print(person, "new letter")
    elif mail == "Package":
      if person in package_counts:
        package_counts[person] += 1
        print(person, "+= package")
      else:
        package_counts[person] = 1
        print(person, "new package")
  print(letter_counts)
  print(package_counts)

