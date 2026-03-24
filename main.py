import numpy as np

# Step 1: Input student scores
scores = np.array([78, 85, 62, 90, 55, 88, 73, 95, 67, 80])

# Step 2: Calculate statistics
mean_score = np.mean(scores)
median_score = np.median(scores)
std_dev = np.std(scores)
max_score = np.max(scores)
min_score = np.min(scores)

# Step 3: Assign grades
def assign_grade(score):
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'

grades = np.array([assign_grade(score) for score in scores])

# Step 4: Display results
print("📊 Student Scores:", scores)
print("\n📈 Statistics:")
print("Mean:", mean_score)
print("Median:", median_score)
print("Standard Deviation:", std_dev)
print("Highest Score:", max_score)
print("Lowest Score:", min_score)

print("\n🎓 Grades:")
for i in range(len(scores)):
    print(f"Student {i+1}: Score = {scores[i]}, Grade = {grades[i]}")