prefix = 0
count = {0: 1}
ans = 0

nums = [1,4,3,7,12]
prefix_array = [0]
k = 2

for num in nums:
    prefix += num
    prefix_array.append(prefix)
    if prefix - k in count:
        ans += count[prefix - k]
    count[prefix] = count.get(prefix, 0) + 1

print(f"Prefix: {prefix}")
print(f"Prefix array: {prefix_array}")
print(f"Count: {count}")