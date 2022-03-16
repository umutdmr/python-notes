def telephone(num):
    page_num = (num // 100) + 1
    num %= 100
    line_num = (num // 5) + 1
    colum_num = num % 5
    print(page_num, line_num, colum_num, sep = "  ")
    
nummmm = int(input())
telephone(nummmm)