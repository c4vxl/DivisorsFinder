def findPrimaryFactors(num: int):
    divider = 2 # divider
    result = [] # create empty array

    while (num > 1): # run untill num is smaller or equal to 1
        if (num % divider == 0): # check if num can be divided by current divider
            num //= divider # divide num by current divider
            result.append(divider) # add divider to array
            divider = 2 # reset divider
        else: divider+=1 # increase divider by one
    
    return result # return array

def findDividers(num: int):
    primaryFactors = findPrimaryFactors(num) # Find the primary factors of the given number

    result = [1] # Initialize the result list with 1 as a divisor (every number is divisible by 1)

    for i in range(1, 2**len(primaryFactors)): # Generate all possible combinations of primary factors to find divisors
        divisor = 1 # start with divisor 1
        for j in range(len(primaryFactors)): # loop throught primary factors
            if (i >> j) & 1: # Check if the j-th bit is set in the binary representation of 'i'
                divisor *= primaryFactors[j] # Multiply the divisor by the corresponding primary factor
        result.append(divisor) # Add the computed divisor to the result list

    # Remove duplicates by converting the list to a set and then back to a list
    result = list(set(result))
    # Sort the list of divisors in ascending order
    result.sort()

    # Return the list of divisors
    return result


print("Please enter a number!")
num = int(input(">> "))
for x in findDividers(num):
    print(x, ": ", num % x == 0)