items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = {}
for item in items:
    if item in counter:
        counter[item] += 1
    else:
        counter[item] = 1   
for key, value in counter.items():
    print(f"{key}: {value}")