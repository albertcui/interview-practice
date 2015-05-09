def recursive_add(sum, l):
    if len(l) == 0:
        return sum
    sum += l.pop()
    return recursive_add(sum, l)
    
def main():
    print recursive_add(0, [1,2,3,5,6,7,8,9])

if __name__ == "__main__": main()    