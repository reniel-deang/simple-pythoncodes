def compute_average(name, mathGrade, englishGrade, scienceGrade):
    average = (mathGrade + englishGrade + scienceGrade) / 3
    print(f"{name}'s grade (Math={mathGrade}, Science={scienceGrade}, English={englishGrade}) and the average is {average:.2f}")


print("Enter grades for John:")
john_math = float(input("Math grade: "))
john_english = float(input("English grade: "))
john_science = float(input("Science grade: "))
compute_average("John", john_math, john_english, john_science)


print("\nEnter grades for Ana:")
ana_math = float(input("Math grade: "))
ana_english = float(input("English grade: "))
ana_science = float(input("Science grade: "))
compute_average("Ana", ana_math, ana_english, ana_science)

print("\nEnter grades for Frank:")
frank_math = float(input("Math grade: "))
frank_english = float(input("English grade: "))
frank_science = float(input("Science grade: "))
compute_average("Frank", frank_math, frank_english, frank_science)
