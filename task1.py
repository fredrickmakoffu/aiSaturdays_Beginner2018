
import random

underFive = [];
ourList = list()
count = 0 
while (count < 11):
    ourList.append(random.randint(1,10))
    count += 1
    
for listno in ourList:
	if(listno < 5):
		underFive.append(listno)

print(ourList)
print(underFive)