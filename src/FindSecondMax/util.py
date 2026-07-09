def sec_largest(num):
    largest=float('-inf')
    sec_large=float('-inf')
    for i in range(len(num)):
        if num[i]>largest:
            sec_large=largest
            largest=num[i]
        elif num[i]>sec_large and num[i]!=largest:
            sec_large=num[i]
    return sec_large