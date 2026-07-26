import matplotlib.pyplot as plt

expense = ['Rent', 'Food', 'Travel', 'Others']
amount = [40, 25, 20, 15]
explode = [0.2, 0, 0, 0]

plt.pie(
    amount,
    labels=expense,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True,
    explode=explode
)

plt.title("Monthly Expenses")
plt.show()