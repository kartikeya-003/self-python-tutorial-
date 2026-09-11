a = 5
b = 10

temp = a   # temp mein a ki value store kar li (5)
a = b      # ab a mein b ki value daal di (10)
b = temp   # ab b mein temp (jo purani a thi) daal di (5)

print(a, b)   # 10 5


a = 5
b = 10
print("Before swap:", a, b)   # 5 10

temp = a
a = b
b = temp

print("After swap:", a, b)    # 10 5