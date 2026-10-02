# Import the required libraries
# Pandas is used for loading and analyzing the dataset
# Matplotlib and Seaborn are used for creating visualizations
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the student performance dataset into a Pandas DataFrame
data = pd.read_csv("StudentsPerformance.csv")


# Display the first five rows of the dataset
print(data.head())


# Inspect the structure and data types of the dataset
print("\nDataset Information:")
data.info()


# Display all column names
print("\nColumn Names:")
print(data.columns)


# Display the number of rows and columns in the dataset
print("\nDataset Shape:")
print(data.shape)


# Generate descriptive statistics for math scores
print("\nMath Score Statistics:")
print(data["math score"].describe())


# --------------------------------------------------
# Histogram
# Shows the distribution of students' math scores
# --------------------------------------------------

plt.hist(data["math score"], bins=10, edgecolor="black")

plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Number of Students")

# Save the histogram as a PNG file
plt.savefig("plots/math_score_histogram.png", dpi=300, bbox_inches="tight")

# Display the histogram
plt.show()


# --------------------------------------------------
# KDE Plot
# Shows a smooth estimate of the math score distribution
# --------------------------------------------------

# Create a new figure so the KDE is separate from the histogram
plt.figure()

sns.kdeplot(data=data, x="math score", fill=True)

plt.title("KDE of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Density")

# Save the KDE plot as a PNG file
plt.savefig("plots/math_score_kde.png", dpi=300, bbox_inches="tight")

# Display the KDE plot
plt.show()


# --------------------------------------------------
# Boxplot
# Compares the distribution of math scores by gender
# and helps visualize potential outliers
# --------------------------------------------------

# Create a new figure for the boxplot
plt.figure()

sns.boxplot(data=data, x="gender", y="math score")

plt.title("Math Score Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Math Score")

# Save the boxplot as a PNG file
plt.savefig(
    "plots/math_score_boxplot_by_gender.png",
    dpi=300,
    bbox_inches="tight"
)

# Display the boxplot
plt.show()


# --------------------------------------------------
# Skewness Analysis
# Measures the asymmetry of the math score distribution
# --------------------------------------------------

print("\nMath Score Skewness:")
print(data["math score"].skew())


# --------------------------------------------------
# Group Comparison
# Compare descriptive statistics for male and female
# students' math scores
# --------------------------------------------------

print("\nMath Score Statistics by Gender:")
print(data.groupby("gender")["math score"].describe())


# --------------------------------------------------
# Outlier Detection Using the IQR Method
# --------------------------------------------------

# Calculate the first quartile (Q1) and third quartile (Q3)
Q1 = data["math score"].quantile(0.25)
Q3 = data["math score"].quantile(0.75)

# Calculate the Interquartile Range (IQR)
IQR = Q3 - Q1

# Calculate the lower and upper boundaries for potential outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find math scores below the lower bound or above the upper bound
outliers = data[
    (data["math score"] < lower_bound) |
    (data["math score"] > upper_bound)
]


# Display the outlier detection results
print("\nOutlier Detection:")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)


# Display the students whose math scores were identified
# as potential outliers
print("\nMath Score Outliers:")
print(outliers[["gender", "math score"]])


# Display the total number of potential outliers
print("\nNumber of Outliers:")
print(len(outliers))