# This is a basic example of Merge algorithm
# this code must have a refactoring, therea are more civilized ways
# to accomplish the same thing. But the idea here is to solve problems
# not to discuss code :)
class MergeList:

    def merge(self):
        listA = [5,2,7,11,3,6]
        listB = [1,8,20,9,4,12]
        result = []

        currentIndexA = 0
        currentIndexB = 0

        # In order to accomplish the merge, we have to sort the lists first.
        self.sort(listA) # Sorted:  [2,3,5,6,7, 11]
        self.sort(listB) # Sorted: [1,4,8,9,12,20]

        # OMG, a lot of IF ELSE... I know, but I don't care so far =)
        while currentIndexA < len(listA) or currentIndexB < len(listB):
            if currentIndexA < len(listA): valueA = listA[currentIndexA]
            if currentIndexB < len(listB): valueB = listB[currentIndexB]

            if valueA < valueB:
                if currentIndexA < len(listA):
                    currentIndexA = currentIndexA +1
                    result.append(valueA)
                else:
                    result.append(valueB)
                    currentIndexB = currentIndexB +1
            else:
                if currentIndexB < len(listB):
                    currentIndexB = currentIndexB +1
                    result.append(valueB)
                else:
                    result.appedn(valueA)
                    currentIndexA = currentIndexA +1

            print(result, currentIndexA, currentIndexB)

    # This sort is using binary search, this is the most easy way to sort a list
    def sort(self, to_sort):
        currentIndex = 1
        lastIndex = 0

        while currentIndex < len(to_sort):
            current = to_sort[currentIndex]
            left = to_sort[lastIndex]

            if current < left:
                to_sort[currentIndex] = left
                to_sort[lastIndex] = current
                if lastIndex != 0:
                    lastIndex = lastIndex -1
                    currentIndex = currentIndex -1
            else:
                lastIndex = currentIndex
                currentIndex = currentIndex +1

if __name__ == "__main__":
    m = MergeList()
    m.merge()

    #The result:
    # ([1], 0, 1)
    # ([1, 2], 1, 1)
    # ([1, 2, 3], 2, 1)
    # ([1, 2, 3, 4], 2, 2)
    # ([1, 2, 3, 4, 5], 3, 2)
    # ([1, 2, 3, 4, 5, 6], 4, 2)
    # ([1, 2, 3, 4, 5, 6, 7], 5, 2)
    # ([1, 2, 3, 4, 5, 6, 7, 8], 5, 3)
    # ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 4)
    # ([1, 2, 3, 4, 5, 6, 7, 8, 9, 11], 6, 4)
    # ([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12], 6, 5)
    # ([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 20], 6, 6)
