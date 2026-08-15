def calculate_power(Base,exponent):
    if exponent==0:
        return 1
    
    result=1
    for _ in range(abs(exponent)):
        result=result*Base

    if exponent<0:
        return 1/result
    
    return result

print(calculate_power(3,3))
print(calculate_power(3,-3))
