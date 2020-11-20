from . import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expense.Expenses()

expenses.read_expenses('data/spending_data.csv')
spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)
top5 = spending_counter.most_common(5)

# zip function combines 2 iterables, zip *dictionary_variable can also be used to
# separate the keys and values of a dictionary into separate lists
# We want to have 2 separate lists for the categories and their counts for the bar graph
# Call zip(*top5) and set the result equal to two variables - categories, count

categories, count = zip(*top5)


fig, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')

plt.show()
