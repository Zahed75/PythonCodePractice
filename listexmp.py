def even(num):
    even_num = []
    for i in num:
        if i % 2 == 0:
            even_num.append(i)
    print(even_num)


a = [10, 20, 15, 18, 25, 14, 22]
even(a)