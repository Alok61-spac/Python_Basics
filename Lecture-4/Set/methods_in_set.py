set = {8,39,9302,1793,18,13,0,13,379,37}
#add an element in set
set.add(66)
print(set)

#remove a paticular element
set.remove(13)
print(set)

#remove a random element
set.pop()
print(set)

#combine 2 sets
set2 = {24,44,15,94,52,53,37}
print(set.union(set2))

#combine common valuse of set and print
print(set.intersection(set2))