batch52 = ["zia", "zeesan", "uchchash", "amira"]

print("Using For Loop:")
for name in batch52:
    print(name)

print("\nUsing For Loop with Range:")
for i in range(len(batch52)):
    print(batch52[i])

print("\nUsing While Loop:")
i = 0
while i < len(batch52):
    print(batch52[i])
    i += 1

print("\nUsing List Comprehension:")
[print(name) for name in batch52]
