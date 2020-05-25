try:
    age = int(input('Age: '))
    income=20000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print('Age canot  be 0')
except ValueError:
    print('Invalid Error')
# Surya is don
