def inputmark():
    # Taking user name
    print('Enter Your Full Name: ')
    fullname = input()

    # Taking user exam score
    print('Enter Exam Score: ')
    exam = int(input())

    # Taking user class score
    print('Enter all class text Score: ')
    mark1 = int(input())
    mark2 = int(input())
    mark3 = int(input())
    mark4 = int(input())
    mark5 = int(input())
    mark6 = int(input())
    mark7 = int(input())

    # summing user class score all together
    sum = (mark1 + mark2 + mark3 + mark4 + mark5 + mark6 + mark7)

    # calculating average of user class score
    avegerage = sum/7

    # Printing all fields needed to be displayed

    print(fullname)
    print('Your exam score is: '+ str(exam))
    print('Test Average is : '+ str(avegerage))
    print('Final mark is: ', compute_mark(avegerage, exam))
    print('Letter Grade is: ', getgrade(compute_mark(avegerage, exam)))
    print(print_Remark(getgrade(compute_mark(avegerage, exam))))
    return avegerage


# Calculating student final mark
def compute_mark(average, exam):
    final_mark = 0.4*average + 0.6*exam
    return final_mark

    # Function to print grade of student
def getgrade(final_mark):
    if 90 <= final_mark <=100:
        grade = 'A'
    elif 80 <= final_mark <=90:
        grade = 'B'
    if 70 <= final_mark <=80:
        grade = 'C'
    if 60 <= final_mark <=70:
        grade = 'D'
    if 50 <= final_mark <=60:
        grade = 'E'
    if 0 <= final_mark <=50:
        grade = 'F'
    return grade

    # Function to print remark of student
def print_Remark(grade):
    if grade == 'A':
        print('Remark: Excellent')
    elif grade == 'B':
        print('Remark: gOODD')
    elif grade == 'C':
        print('Remark: Nice')

# Calling the function to run the entire code
inputmark()