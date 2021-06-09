lst = ['hello', 'my', 'purpose', 'is', 'to', 'be', 'a', 'test'] 
print(lst)
lst = [lst[i:i + 3] for i in range(0, len(lst), 3)]
print(lst)