### Answers

#### Section 1:
cdcac
babca
cbbca
aaadb

* After some considerations, b is also counted as correct now for 14

#### Section 2:
1. 
```
i = 1
while i < 5 :
    print(i)
    i += 1 # needs to be inside while loop
```

2. You can't add up a string and an integer
```
name = "Alice"
age = 25
print("Name:" + name + ", Age" + str(age))
```
```
name = "Alice"
age = "25"
print("Name:" + name + ", Age" + age)
```
```
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")
```

3. The function has a missing colon and the function shall return sum instead of printing the result.
```
def sum (x,y):
    sum = x + y
    return sum
```

#### Section 3:
```
for y in range(3):
    for x in range(3):
        print("A", end="_")
    print("A")
```
```
for y in range(3):
    for x in range(4):
        if x < 3:
            print("A", end="_")
        else:
            print("A", end="")
    print()
```
```
r = 3
c = 4
row = '_'.join('A'*c)
for _ in range(r):
    print(row)
```