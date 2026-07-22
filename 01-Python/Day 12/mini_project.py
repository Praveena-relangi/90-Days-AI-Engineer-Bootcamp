import matplotlib.pyplot as plt

product_categories = ["Laptop", "Mobile", "Tablet", "Monitor"]
sales = [250, 400, 180, 150]

plt.bar(product_categories, sales, color="green")
plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()