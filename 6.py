ticket = input()
sum_forward = 0
sum_backward = 0

for x in range(0, 3):
    sum_forward += int(ticket[x])
    sum_backward += int(ticket[-1-x])

if(sum_forward == sum_backward):
    print("yes")
else:
    print("no")
