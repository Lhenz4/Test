mul_num = int(input("Enter th number for which you want the multipliv=cation table: "))
mul_limit = int(input("Enter the limit to which you want the multiplication table to be generate: "))
print(f"multiplication table of {mul_num}")

for i in range(1, mul_limit + 1):
    print (f"{mul_num} x {i} = {mul_num*i}")