def bacteria(initial_num, time_it_takes, total_timne):
    """total süre sonundaki bakteri sayısını gösterir."""
    
    total_bacteria = initial_num *  2 ** (total_timne/time_it_takes)
    total_bacteria = int(total_bacteria)
    print(total_bacteria)

a = int(input())
b = int(input())
c = int(input())

bacteria(a,b,c)