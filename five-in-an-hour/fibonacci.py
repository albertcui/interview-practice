def fibonacci_it(count):
    l = []
    
    if count > 0:
        l.append(0)
    else:
        return "Error!"
    
    if count > 1:
        l.append(1)
    
    for i in range(2, count):
        l.append(l[-1] + l[-2])
        
    return l

def fibonacci_rec(count, l):
    if count == 2:
        return l
    else:
        l.append(l[-1] + l[-2])
        return fibonacci_rec(count - 1, l)
        
def main():
    print fibonacci_it(100)
    print fibonacci_rec(100, [0, 1])

if __name__ == "__main__": main()