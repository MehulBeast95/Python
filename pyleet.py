"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example
1:

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because
nums[0] + nums[1] == 9, we
return [0, 1].
Example
2:

Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Example
3:

Input: nums = [3, 3], target = 6
Output: [0, 1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only
one
valid
answer
exists."""
"""l=[]
while True:
    a=int(input("Enter element for list: "))
    l.append(a)
    b=input("Want to add more ?(y/n): ")
    if b.lower()=="n":
        print(l)
        break
tar=int(input("Target: "))
while True:
    if l[0]+l[1]==tar:
        print()"""
#sawp first and last element in the list
"""l1=[2,3,4,5,6,7,8,9]
print(l1)
a=l1[0]
b=l1[-1]
l1[0]=b
l1[-1]=a
print(l1)"""
#wap to remove duplicates and sort them in ascending order
l1=[5,2,2,2,3,4,3,5,4,2,3,6,7,5,6,7]
a=[]
for i in l1:
    if i not in a:
        a.append(i)
        a.sort()
print(l1)
print(a)