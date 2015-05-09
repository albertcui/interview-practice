
def alternate_combine_equal(a, b):
    newList = []
    for i in range(0, len(a)):
        newList.append(a[i])
        newList.append(b[i])
    return newList
    
def alternate_combine_notequal(a, b):
    newList = []
    while len(a) and len(b):
        # this reverses, could do a.pop(0) if we wanted the front
        newList.append(a.pop())
        newList.append(b.pop())
    
    newList = newList + a + b
    return newList
    
def main():
    a = [1, 2, 3]
    b = ["a", "b", "c"]
    print alternate_combine_equal(a, b)
    
    a = [1, 2, 3, 5, 6, 7, 8]
    b = ["a", "b", "c"]
    print alternate_combine_notequal(a, b)

if __name__ == "__main__": main()    