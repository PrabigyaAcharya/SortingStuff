class Sort:
    #selection sort
    def selectionSort(num):
        all_perm = [num.copy()]
        for i in range(len(num)-1):
            min_index = i
            for j in range(i+1, len(num)):
                if num[min_index] > num[j]:
                    min_index = j
            num[i], num[min_index] = num[min_index], num[i]
            all_perm.append(num.copy())
        return all_perm

    def test(num):
        listend = len(num)+1
        for i in range(0,len(num)-1):
            listend -= 1
            minnum = min(num[0:listend])
            num.append(minnum)
            num.remove(minnum)
            print(num)
    #This is to put the biggest number to the end of the list
        lastnum = num[0]
        num.append(lastnum)
        num.remove(lastnum)
        print(num)
        return num

    #swaps 2 numbers
    def swap(a, b):
        temp = a
        a = b 
        b = temp
        return a,b   
    
    def insertionSort(num):
        temp = [num.copy()]
        for i in range (1, len(num)):
            present = num[i]
            j = i-1
            while j>=0 and present<num[j]:
                num[j+1] = num[j]
                j -=1
            num[j+1] = present
            temp.append(num.copy())
        return temp

    def bubbleSort(num):
        temp = []
        for i in range(len(num)):
            for j in range(len(num)-i-1):
                if num[j]>num[j+1]:
                    num[j], num[j+1] = num[j+1], num[j]
                temp.append(num.copy())
        return temp
