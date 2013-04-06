import itertools

#i know the directions said to do this in one sitting, but after the frustration of missing a comma for 2 hours i needed to take a shower and make some dinner to clear my head. when i sat down to start this level i submitted an answer of 'im back' to the the last password box.

#Before I started coding I thought through the problem and knew right away the brute force way of solving this.
#The code I wrote takes advantage of the fact that the input is a set and ordered.
#If the data didn't have these properties I would have had to use itertools.permutions which would have been an order of magnitude slower.

#Python has a standard library class that makes this pretty easy.  
#I discovered itertools.combinations when googleing for how to create all permutions of a set
numbers = [3, 4, 9, 14,15,19,28,37,47,50,54,56,59,61,70,73,78,81,92,95,97,99]

successes = 0
for i in range(2, len(numbers)):
    combinations = itertools.combinations(numbers, i)
    for combo in combinations:
        local_max = max(combo)
        local_sum = sum(combo)
        if local_max == local_sum-local_max:
            successes += 1
            print local_max, local_sum, combo

print successes



##My Initial approach was to create a hash table of the sums of subsets

#speed is a hashtable that associates a tuple with its sum  
# speed = {}

# def speedup(key):
#     if key not in speed:
#         speed[key] = sum(key)

# for index, number in enumerate(numbers):
#     current = tuple(numbers[index:index+1])
#     before = tuple(numbers[:index])
#     after = tuple(numbers[index:])

#     for chomp_before in range(1,index-2):
#         print "adding: ", before[chomp_before:index-1]
#     print index,"\t",number, "\t", current, "\t", before
#     speedup(current) #current number
#     speedup(before) #numbers before
#     speedup(after) #numbers after

# print speed[(3,4)]