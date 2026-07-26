import matplotlib.pyplot as plt

marks = [35,40,42,50,55,60,62,65,70,72,75,78,80,82,85,90,95]

plt.hist(
    marks,
    bins=6,
    color="skyblue",
    edgecolor="black"
)

plt.title("Student Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Students")

plt.show()