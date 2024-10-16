my_set = {1,2,3,4,55,4}
yourset = {4,5,6,22}
my_set.add(100)
print(my_set)
my_set.add(200)
my_set.remove(100)
print(my_set)
print(list(my_set))
print('The difference of sets is:', my_set.difference(yourset))
print('The union of two sets is: ', my_set.union(yourset))
print('The intersection of two sets is: ', my_set.intersection(yourset))
print('Ate the two set are disjoint: ', my_set.isdisjoint(yourset))


