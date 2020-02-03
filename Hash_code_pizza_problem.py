import random
max_slices=int(input("Max Slices: \n"))
types=int(input("No. of Types of pizza: \n"))
index=int(0)
different=[]
possible_sums=[]
sums=int(0)
large=int(0)
for i in range(types):
    different.append(int(input("Enter num of slices in S"+ str(i) + ":\n")))
different.sort()
for x in different:
    possible_sums.append(x)
x=int(0)
while(x<types):
    for count in range(types-x):
        r=count
        z=count
        y=count
        while(r>=0):
            sums=sums+different[r]
            r=r-1
        if(not(sums in possible_sums)):
            possible_sums.append(sums)
        sums=0
        different.sort(reverse=True)
        while(z>=0):
            sums=sums+different[z]
            z=z-1
        if(not(sums in possible_sums)):
            possible_sums.append(sums)
        sums=0
        a=0
        while(a<types**3):
            random.shuffle(different)
            while(y>=0):
                sums=sums+different[y]
                y=y-1
            y=count
            if(not(sums in possible_sums)):
                possible_sums.append(sums)
            sums=0
            a=a+1
        x=x+1
possible_sums.sort()
print(possible_sums)
length=len(possible_sums)
for counter in range(length):
    if (possible_sums[counter]>large and possible_sums[counter]<=max_slices):
        large=possible_sums[counter]
        index=counter
possible_sums.sort()
print("Max pizza slices u can get: \n" +str(large))
