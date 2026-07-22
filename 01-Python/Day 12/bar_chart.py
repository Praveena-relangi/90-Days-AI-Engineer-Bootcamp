import matplotlib.pyplot as plt

departments = ["IT", "HR", "Sales", "Finance"]
employees = [120, 45, 80, 30]

colors = ["blue", "green", "orange", "red"]

bars = plt.bar(departments, employees, color=colors, width=0.4)
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        str(int(bar.get_height())),
        ha="center",
        va="bottom"
    )
plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.show()