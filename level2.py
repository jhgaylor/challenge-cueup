#I needed a generator for memory's sake. This one has been online forever and looks perfect, so I shamelessly copy it :D
#http://code.activestate.com/recipes/66316-fibonacci-sequence-using-generators/
def fib():
    "unbounded generator, creates Fibonacci sequence"
    x = 0
    y = 1
    while True:
        x, y = y, x + y
        yield x

#i was using xrange, but n was too large.
#this used to be a beautiful bit of code.  why oh why must i fall back on this c style of iteration!!!! 
def isPrime(n):
    #this is a hack for an odd bug i ran into with long ints and floats.
    #can't use range because it's not a generator, can't use xrange because of long int to float bug
    #can't set i to 1 because of long int to float bug
    if n in [1,2]:
        return True    
    i = 2

    while i < int(n**.5)+1: #int is actually not necessary here but i think it will prevent a bug if this is refactored to use xrange after fixing the previous bug
        if n%i == 0:
            return False
        i+=1
    return True

fib_gen = fib()
min_fib = 227000
prime = False
prime_number = 1
while not prime:
    cur = fib_gen.next()
    
    if(cur > min_fib): #no need to check if cur is prime if it isn't large enough
        this_prime = isPrime(cur)
        prime = this_prime
        prime_number = cur

# I'm SO silly.  I sat here for 2 hours debugging the stupidest of bugs.  I set min_fib = 227,000 not 227000.  That's what I get for copy pasting from the website.
x = prime_number

#this function wasntt  returning the correct factors initially so i called the number to verify x.  x was correct, but if I had called sooner I would have noticed the comma problem sooner and not have wasted so much time above
#the phone call was very cloak and dagger.  +1
def prime_devisors(num):
    primes = []
    for i in xrange(2,int((num**.5))+1): #int to convert from float. +1 for inclusive
        if isPrime(i):
            if num%i==0:
                primes.append(i)
    return primes

primes = prime_devisors(x+1)
print x
print primes
print sum(primes)
