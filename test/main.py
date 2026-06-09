from mypytool import *
print(perfect_square_plus_gs(1,2)) #输出：1^2+2^2+2^1+2*1*2
print(perfect_square_plus_z(1,2)) #输出：9
print(perfect_square_sub_gs(2,1)) #输出：2^2+1^2-2*2*1
print(perfect_square_sub_z(2,1)) #输出：1
print(glm(4)) #输出：[1,1,0]
print(glm2bin([1,1,0])) #输出：[1,0,0]
print(glm2dex([1,1,0])) #输出：4
print(fast_pow(2,128)) #输出：340282366920938463463374607431768211456
print(base_conversion(4,3)) #输出：[1,1]
print(base_conversion_dex("100")) #输出：4
print(swap(1,2)) #输出：[2,1]
print(swap1(1,2)) #输出：[2,1]
print(swap2(1,2)) #输出：[2,1]
print(factorial_recursion(5)) #输出：120
print(fibonacci_recursion(3)) #输出：2
print(pow(2,2)) #输出：4
print(pow_transform(2,128)) #输出：4^46