#py4e assignment 5.1 - worked with video, not my work
number = 0
total = 0.0
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input...')
        continue
    number = number + 1
    total = total + fval

print(total, number, total/number)
