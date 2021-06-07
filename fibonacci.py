def fib(number):
    try:
        if number>0:
            if type(number)==int:
                fibo=[1,1]
                index = 0
                a = fibo[index]
                b = fibo[index + 1]
                if number==1:
                    print(fibo[0])
                elif number==2:
                    print(fibo[1])
                else:
                    for i in range(1,number+1):
                        c=a+b
                        fibo.append(c)
                        a=b
                        b=c
                    print(fibo)
            else:
                print("please enter just integer numbers!!!")
        else:
            print("please enter a number that more than 1!!!")

    except TypeError:
        print("please enter just number")
fib(10)
fib(0)
fib(7.4)
fib("my")
fib(1)


