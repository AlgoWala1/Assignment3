grade = int(input("Enter Grade"))
gradeCorrespondance = {10:"Your grade is A+ and Outstanding performance",9:"Your grade is A and Excellent performance",8:"Your grade us B+ and Very good",
                       7:"Your grade is B and good performance",
                       6:"Your grade is C+ and average performance",
                       5:"Your grade is C and below average performance",
                       4:"Your grade is D and Poor performance"
                       }

if grade>=4 and grade<=10:
    print(gradeCorrespondance.get(grade))
else:
    print("Input not supported")
