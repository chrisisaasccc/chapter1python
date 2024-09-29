#Author:chris isaac
#date:29/09/24
#homework pg42 q1/14 tasks1/2
#task1
numbers = []
for i in range(5):
    num = int(input("Enter number (i+1): "))
incremented_numbers = [x + 1 for x in numbers]
print("List after incrementing each number by 1:", incremented_numbers)
#task2
hours = [12, 7, 9, 9, 6, 8, 2]
milk_consumption_per_hour = 0.5
total_milk = sum(hours) * milk_consumption_per_hour
cost_per_liter = 1.35
total_cost = total_milk * cost_per_liter
print("Total liters of milk consumed in 7 days: (total_milk:.2f) liters")
print("Total cost of milk: €(total_cost:.2f)")
