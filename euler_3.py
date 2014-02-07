# 
#   Project Euler Problem 3 - Solution 
#
#      Largest Prime Factor Problem:
#      The prime factors of 13195 are 5, 7, 13 and 29.
#      What is the largest prime factor of the number 600851475143 ?    
# 
primes = []
for num in range(1, 9999999):
    if 600851475143 % num == 0:
       primes.append(num) 
print "The largest prime number of 600851475143 is: %d" % max(primes)
