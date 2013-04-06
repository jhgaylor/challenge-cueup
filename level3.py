#i know the directions said to do this in one sitting, but after the frustration of missing a comma for 2 hours i needed to take a shower and make some dinner to clear my head.
#when i sat down to start this level i submitted an answer of 'im back' to the the last password box.
numbers = [3, 4, 9, 14,15,19,28,37,47,50,54,56,59,61,70,73,78,81,92,95,97,99]
numbers.sort()
high_low = numbers[::-1]
#for each number find all subsets that sum to it
for number in high_low:
    print number
