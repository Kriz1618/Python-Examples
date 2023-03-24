def avg(marks: list) -> float:
    print('2', 'marks', marks)
    assert len(marks) != 0, 'List is empty'
    return sum(marks)/len(marks)

print(avg([3,4,5,2,1]))
print(avg([]))