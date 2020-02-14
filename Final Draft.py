# This program takes input in the form of two sets. The first set contains the element maximum number of pizzas required
# and element which informs about the total types of pizzas. The second set contains the number of slices in each
# successive type of pizza, in a non decreasing order. The output generated is to be of two lines. First tells
# the no. types of pizza feasible and the next, the frequency of each type of pizza - with the goal to make a number
# nearest to max no. of slices provided but not exceeding. Save food. Apparently. ~ Google Hash Code

# By Haad Mehboob - 7 Feb, 2020
#
#
#
#

import random  # importing necessary library

# two variables for continuous looping through the given file
skip = int(0)
total = int(0)

xh = open("input.txt")  # open given input file

# total lines in the given file being saved in total
for g in xh:

    total += 1

while total != skip:  # skip is essentially the no. of lines already read

    max_slices = int(0)  # max no. of slices defined (line odd)
    types = int(0)  # total different types of pizza  (line odd)
    different = []  # stores values for different types of pizzas (line even)
    possible_sums = []  # stores all possible sums for the combinations. I like brute force.
    frequency = []  # no. of times values in different repeated to make the best chosen possible sum
    father = []  # stores all the exact combinations of the pizza types used to make corresponding possible_sums value
    child = []  # stores the lists needed to be stored within the father list
    large = int(0)  # largest value from possible_sums, lesser than max_slices

    # initializing all necessary variables for the program
    element_string = ""
    sums = int(0)
    index = int(0)
    sum2 = int(0)
    index2 = int(0)
    cnt = int(0)

    fh = open("input.txt")

    for s in range(skip):  # skipping the lines already read by the program

        next(fh)

    for line in fh:

        cnt += 1  # iterates when a line is read
        words = line.split()  # split the line read into individual components

        if cnt == 1:  # essentially an odd numbered line in the file (contains one set of data)

            max_slices = int(words[0])  # first word of each line being max slices required
            types = int(words[1])  # second word of each line in the no. of types
            continue

        if cnt == 2:  # essentially an even numbered line in the file (contains another set of data)

            different = words  # saving values independently in the list different for different types of pizzas

        break

    skip = skip + cnt  # skipping lines for next iteration
    cnt = 0  # reset count to zero so extra lines are not skipped in the next iteration
    different.sort()  # sort different for ease of my mind :p

    for x in different:

        possible_sums.append(int(x))  # individual values with the pizza sizes are included in possible_sums
        father.append(int(x))  # a lone value also makes for a possible combination

    child = []  # Just felt like doing this.
    x = int(0)  # x in loop starts with 0

    # This loop here works through the cycle in the manner described below
    # 1 2 3 4 5
    # 1 2 3 4 / 1 2 4 5 / 1 3 4 5 etc
    # 3 4 5 / 1 3 5 / 2 3 4.
    # This system repeats in different arrangements until I get all possible sums

    while x < types:

        # (types - x) to change the number of values combined
        for count in range(types - x):

            r = count  # for the loop in charge of sums of sorted list
            z = count  # for the loop in charge of sums of reverse sorted list
            y = count  # for the loop in charge of shuffled list

            # loop for sorted list
            while r >= 0:

                sums = sums + int(different[r])  # summation
                child.append(int(different[r]))  # creating sublist for the combination used to generate the sum
                r = r - 1  # work through the loop

            # look for the value of sums in possible_sums, so possible_sums are not repeated
            if not (sums in possible_sums):

                possible_sums.append(int(sums))  # append sums into possible_sums
                father.append(child)  # and correspondingly place the combination for the given sum

            child = []  # empty child list
            sums = 0  # empty value for sums
            different.sort(reverse=True)  # arrange in reverse / descending order

            # loop for reverse sorted list
            while z >= 0:

                sums = sums + int(different[z])  # summation
                child.append(int(different[z]))  # creating sublist for the combination used to generate the sum
                z = z - 1  # work through the loop

            # look for the value of sums in possible_sums, so possible_sums are not repeated
            if not (sums in possible_sums):

                possible_sums.append(int(sums))  # append sums into possible_sums
                father.append(child)  # and correspondingly place the combination for the given sum

            child = []  # empty child list
            sums = 0  # empty value for sums

            #  Main program to generate all possible sums. Unless the random function is unluckier than
            #  an apple falling back to earth after being thrown up (given falling to earth is unlucky), this will work.
            a = 0
            while a < types ** 3:  # types^3 combinations

                random.shuffle(different)  # shuffle the list for different arrangement of elements

                # loop for shuffled list
                while y >= 0:

                    sums = sums + int(different[y])  # summation
                    child.append(int(different[y]))  # creating sublist for the combination used to generate the sum
                    y = y - 1  # work through the loop

                y = count  # Y will be trapped in the loop for a while, for reset value. We do not want Y = 0

                # look for the value of sums in possible_sums, so possible_sums are not repeated
                if not (sums in possible_sums):

                    possible_sums.append(int(sums))  # append sums into possible_sums
                    father.append(child)  # and correspondingly place the combination for the given sum

                child = []  # empty the list
                sums = 0  # empty value for sums

                a = a + 1  # work through parent loop for sums of shuffled list

            x = x + 1  # work through types

    # the extra printing is purely for debugging purposes
    # the main output is generated in the file "output.txt" later

    print(possible_sums)

    for counter in range(len(possible_sums)):

        # finding value that fits the provided criteria
        if large < possible_sums[counter] <= max_slices:

            large = possible_sums[counter]  # store in var large
            index = counter  # store index from which the value is taken in possible_sums

    possible_sums.sort()  # sorted for the upcoming code

    print("Max pizza slices u can get: \n" + str(large))  # print max slices possible
    print("Father is: ")  # the combination from types used

    if type(father[index]) != int:
        father[index].sort() # print sorted corresponding father as possible_sums has also been sorted

    different.sort()  # sorted for the upcoming code

    # loop to store the frequency of each types in order
    for w in range(len(different)):  # work through indices

        if w < len(different) - 1:  # error trap for the following conditional statement

            # two successive same values will both be appended, twice frequency, therefore wrong
            if different[w] == different[w + 1]:  # ^^^ We do not want that

                w += 1  # skip the repeated value
                frequency.append(0)  # append 0 in its place, so frequency only appended once

                continue  # to skip the following command, the crux of this loop

        # append the frequency of occurrence of different[i] in the chosen father list
        if type(father[index]) != int:
            frequency.append(father[index].count(int(different[w])))  # a.count(x) returns int total repeated x present in a

    # debug printing
    print(father[index])
    if type(father[index]) != int:
        print(len(father[index]))
    else:
        print(1)
    print(*frequency)

    print("full father is:")
    print(father)

    print("index: " + str(index))

    # open output file with append mode
    wh = open("output.txt", "a")

    if type(father[index]) != int:
        wh.write(str(len(father[index])) + "\n")  # line 1, the total types of pizza you can have
    else:
        wh.write("1" + "\n")  # line 1, the total types of pizza you can have
        frequency = []
        print(different)
        for single in different:
            print(single)
            if int(single) == int(large):
                frequency.append(1)
            else:
                frequency.append(0)

    # producing a single string because wh.write won't take multiple arguments / lists

    for element in frequency:

        element_string = element_string + str(element) + " "

    wh.write(element_string + "\n")  # line 2, frequency of each type in order
