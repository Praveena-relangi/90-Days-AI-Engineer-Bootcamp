import matplotlib.pyplot as plt

marks = [45,52,61,62,64,68,71,72,73,75,76,78,81,82,85,90,95]

plt.hist(
    marks,
    bins=5,
    color="skyblue",
    edgecolor="black"
)

plt.title("Distribution of Student Marks")

plt.xlabel("Marks")

plt.ylabel("Number of Students")

plt.show()