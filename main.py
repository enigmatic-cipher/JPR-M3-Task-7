"""
Given two arrays of equal length as input create the sum product, i.e. the elements at the same index of both the arrays are multiplied and then added.
Input-> [1,2,3],[5,10,20]
Output-> 85 (because 1*5+2*10+3*20)
"""

ls1 = [1,2,3]
ln1 = len(ls1)
ls2 = [5,10,20]
ln2 = len(ls2)
num = 0
total = 0
for i in range (0,ln1):
  e = ls1[i]
  for j in range (0,ln2):
    e2 = ls2[j]
    if (i==j):
      num = e * e2
      total += num
print(total)
