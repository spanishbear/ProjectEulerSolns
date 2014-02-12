#
#
#   QUESTION 4
#   LARGEST PALINDROME PRODUCT
#       A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#       Find the largest palindrome made from the product of two 3-digit numbers.


largestNo = 0
for num in range(100, 1000):
    for num2 in range(100, 1000):
        product = num * num2
        stringint = str(product)
        if stringint == stringint[::-1]:
            largestNo = max(largestNo, product)
print "The largest palindrome made from the product of two 3-digit numbers is: %d." % (largestNo)
        
        
        
    
