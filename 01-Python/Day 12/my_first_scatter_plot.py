import matplotlib.pyplot as plt

hours = [1,2,3,4,5,6,7,8]
marks = [35,45,50,62,70,78,82,90]

plt.scatter(
    hours,
    marks,
    color="blue",
    s=100
)

plt.title("Study Hours vs Marks")

plt.xlabel("Study Hours")

plt.ylabel("Marks")

plt.show()