import matplotlib.pyplot as plt

brands = ["Apple", "Samsung", "Xiaomi", "Others"]
share = [40, 30, 20, 10]

explode = [0.1, 0, 0, 0]

plt.pie(
    share,
    labels=brands,
    autopct="%1.1f%%",
    startangle=90,
    explode=explode,
    shadow=True
)

plt.title("Smartphone Market Share")

plt.show()