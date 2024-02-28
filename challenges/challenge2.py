import sys
# <summary >
# During your time at mountain warheouse you will often have to go bug fix your own ( and other peoples!) code.
# The following method should return the smallest value in the given array. If the array is empty then it should return 0.
# However, the last dev has made some bugs.  It seems it only works when the number "1" is the smallest value in the array - for all other cases the method fails
# 4 bugs have been identified within the code.
# See if you can find them all!
# </summary >
# <param name = "numbers" > </param >
# <returns > </returns >

## ERRORS:
# def ReturnSmallestValueInArray(numbers):
#     min = -sys.maxsize-1 #1) This number will already be extreamly small that there will be no number in the array that would be smaller than it, so the code will never work
#     for i in range(len(numbers)):
#         if min < numbers[i]: # 2) swap inequality sign - currently finding the largest number in the array 
#             min = numbers[i]
#     # 3) we need to return the min num that we find which is not being done (return min)
#     return 1 # 4) code always returns one regardless of what min we find - which is why it works for 1


def ReturnSmallestValueInArray(numbers):
    if(len(numbers)):
        numbers.sort()
        return numbers[0]
    else:
        return 0