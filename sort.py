class Sort:
    #selection sort
    def selectionSort(num =[1, 2, 3, 65, 34, 2,3]):
        all_perm = []
        for i in range(len(num)-1):
            for j in range(i, len(num)):
                if num[j] < num [i]:
                    num[i], num[j] = num[j], num[i]
                    temp = num.copy()
                    all_perm.append(temp)
        return all_perm




    #selection sort but O(n) ->idk how tho
    def idkwhatsort(num=[44, 35, 12, 43, 12, 2, 1, 4, 23, 4]):
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
        temp = []
        for i in range (len(num)):
            for j in range(len(num)):
                if num[i] < num[j]:
                    num[i], num[j] = Sort.swap(num[i], num[j])
                temp.append(num.copy())
        return temp

    def bubbleSort(num):
        temp = []
        for i in range(len(num)-1):
            isSwapped = False
            for j in range(len(num)-1):
                if num[j]>num[j+1]:
                    num[j], num[j+1] = num[j+1], num[j]
                    chor = num.copy()
                    temp.append(chor)
                    isSwapped = True
            if isSwapped == False:
                break
        return temp
