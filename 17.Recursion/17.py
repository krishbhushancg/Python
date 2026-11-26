def stop_at_zero(n):
    if n <0:
        return n
    
    print(n)
    stop_at_zero(n-1)


(stop_at_zero(5))