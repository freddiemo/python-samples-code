d = {
    'Key1': [1, 2, 3],
    'Key2': True}
print d['Key2']

d2 = {
    'Key1': [1, 2, 3],
    4: True,
}

print d2[4]

d2[4] = "Hello"

print d2[4]
