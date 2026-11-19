subjects = {
     "Math": int(input("Enter your score in Math (0-100): ")),
     "English": int(input("Enter your score in English (0-100): ")),
     "Arabic": int(input("Enter your score in Arabic (0-100): ")),
}

valid_scores = True

for subject, score in subjects.items():
  if score < 0 or score > 100:
    print(
        f"{subject}: Invalid score! Please enter a number between 0 and 100."
    )
    valid_scores = False
  elif score >= 50:
    print(f"{subject}: Passed! Good work ({score})")
  else:
    print(f"{subject}: Failed / Needs improvement ({score})")

if valid_scores:
    total = sum(subjects.values())
    percentage = total / len(subjects)
    print(f"\nTotal:{total}/300")
    print(f"Average Percentage: {percentage:.2f}%")  