L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

min = L[0]
max = L[0]

for num in L:
  if num < min:
    min = num
  elif num > max:
    max = num

print(f"valeur minimum: {min}")
print(f"Maximum value: {max}")