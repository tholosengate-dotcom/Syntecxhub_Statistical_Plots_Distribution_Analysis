# Statistical Plots & Distribution Analysis

## Project Overview

This project analyzes the distribution of students' math scores using statistical plots and descriptive statistics. The analysis uses a Student Performance dataset containing 1,000 student records.

The main goal is to inspect the distribution of math scores, compare the distribution across gender groups, identify potential outliers, and analyze the skewness and spread of the data.

## Dataset

The dataset used is `StudentsPerformance.csv`.

It contains 1,000 rows and 8 columns, including:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score

For this project, the main numerical variable analyzed is `math score`, while `gender` is used for group comparison.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

## Analysis Performed

The project includes:

- Descriptive statistics for math scores
- Histogram of math scores
- Kernel Density Estimation (KDE) plot
- Boxplot comparing math scores by gender
- Skewness analysis
- Comparison of descriptive statistics by gender
- Outlier detection using the Interquartile Range (IQR) method

## Key Findings

The dataset contains 1,000 student records. The mean math score is approximately 66.09 and the median is 66.

The skewness value is approximately -0.279, indicating a slightly negatively skewed distribution.

When comparing groups, male students in this dataset have a mean math score of approximately 68.73 and a median of 69, while female students have a mean of approximately 63.63 and a median of 65.

Using the IQR method, the lower outlier boundary was calculated as 27 and the upper boundary as 107. Eight potential outliers were detected, all below the lower boundary.

These findings describe the students represented in this dataset and should not be generalized beyond the dataset.

## Project Structure

    Syntecxhub_Statistical_Plots_Distribution_Analysis/
    │
    ├── analysis.py
    ├── StudentsPerformance.csv
    ├── summary.txt
    ├── README.md
    │
    └── plots/
        ├── math_score_histogram.png
        ├── math_score_kde.png
        └── math_score_boxplot_by_gender.png

## How to Run

Install the required Python libraries:

    pip install pandas matplotlib seaborn

Run the analysis:

    python analysis.py

The program will display the statistical results in the terminal and generate the statistical plots.

## Output

The generated plots are saved inside the `plots` folder:

- `math_score_histogram.png`
- `math_score_kde.png`
- `math_score_boxplot_by_gender.png`