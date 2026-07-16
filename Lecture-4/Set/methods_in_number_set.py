number_set = {8,39,9302,1793,18,13,0,13,379,37}
#add an element in set
number_set.add(66)
print(number_set)

#remove a paticular element
number_set.remove(13)
print(number_set)

#remove a random element
number_set.pop()
print(number_set)

#combine 2 number_sets
number_set2 = {24,44,15,94,52,53,37}
print(number_set.union(number_set2))

#combine common valuse of numer_set and print
print(set.intersection(number_set2))