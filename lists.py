namelist = []
agelist = []
name = input('Enter your name, or enter \'stop\' to stop.')
while name != 'stop':
    age = int(input('Entere your age, Mr.' +name+'?'))
    namelist.append(name)
    agelist.append(age)
    name = input('Enter your name, or enter \'stop\' to stop.')
maxindex = 0
for i in range(1, len(agelist)):
    if agelist[i]>agelist[maxindex]:
        maxindex = i
print("the oldest person is ", namelist[maxindex])


