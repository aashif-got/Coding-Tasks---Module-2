def karatsuba(n1,n2):
    if n1<10 or n2<10:
        return n1*n2
    temp = n1
    digit_n1 = 0
    while temp != 0:
        temp = temp // 10
        digit_n1 +=1
    temp = n2
    digit_n2 = 0
    while temp != 0:
        temp = temp // 10
        digit_n2+=1
    n = max(digit_n1,digit_n2)
    half = n//2

    a = n1 // 10**half
    b = n1 % 10**half
    c = n2 // 10**half
    d = n2 % 10**half

    a_c = karatsuba(a,c) 
    b_d = karatsuba(b,d)
    ad_bc = karatsuba(a+b,c+d) - a_c - b_d

    return a_c * (10**(2*half)) + ad_bc * (10**half) + b_d

if __name__ == "__main__":
    print(karatsuba(23852,47573))