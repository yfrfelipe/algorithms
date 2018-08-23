# This is a simple example of a sort algorithm using
# binary search
class SortList:

    def sort(self):
        list = [3,4,2,5,1,6]
        sortedList = []
        currentIndex = 1
        lastIndex = 0

        print(list)
        while currentIndex < len(list):
            print(list, lastIndex, currentIndex)
            origin = list[currentIndex]
            left = list[lastIndex]

            if origin < left:
                list[lastIndex] = origin
                list[currentIndex] = left
                if lastIndex != 0:
                    lastIndex = lastIndex -1
                    currentIndex = currentIndex -1
            else:
                lastIndex = currentIndex
                currentIndex = currentIndex + 1

if __name__ == "__main__":
    s = SortList()
    s.sort()
