import matplotlib
import matplotlib.pyplot as plt

print(matplotlib.get_backend())

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 120, 150, 180, 220]

plt.title("Monthly Sales Report")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.plot(months, sales, color="blue", linestyle='--', marker="o")
plt.show()