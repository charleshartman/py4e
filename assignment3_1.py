#py4e assignment 3.1
hrs = input("Enter Hours Worked: ")
rate = input("Enter Hourly Rate: ")
h = float(hrs)
r = float(rate)
if h <= 40.0:
    pay = h * r
else:
    ot = h - 40.0
    pay = (40.0 * r) + (ot * (r * 1.5))
print(pay)
