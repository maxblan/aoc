with open('2022\day1_calorie_counting\input.txt', 'r') as f:
    input = f.read().split('\n\n')
input = [sum([int(j) for j in i.split('\n')]) for i in input]
input.sort(reverse=True)
print(sum(input[0:3]))


