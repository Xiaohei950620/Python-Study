#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
import problem1


def Fibonacci(num):
    fib_list=[]
    if num < 1:
        print 'Error: enter number should be bigger than 1'
        return

    if num == 1:
        fib_list.append(1)
        return fib_list
    elif num == 2:
        fib_list.append(1)
        fib_list.append(2)
        return fib_list
    fib_list=[1,2]
    for i in range(0,num-2):
        New_num = fib_list[i]+fib_list[i+1]
        fib_list.append(New_num)
#        print fib_list
    return fib_list

if __name__ == '__main__':
    num = 3
    value = 0
    while value < 20:
        FB_list = Fibonacci(num)
        value = FB_list[-1]
        num = num + 1
    
    print FB_list
    del FB_list[-1]
    print FB_list
    porblem2Object = problem1.Multiples()
    porblem2Object.Sum_list(FB_list)
    

    