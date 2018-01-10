#py4e assignment 4.6

def computepay(h,r):
    if h <= 40.0:
        pay = h * r
    else:
        ot = h - 40.0
        pay = (40.0 * r) + (ot * (r * 1.5))
        return pay

hrs = input("Enter Hours Worked: ")
rate = input("Enter Hourly Rate: ")

h = float(hrs)
r = float(rate)

p = computepay(h,r)

print(p)
