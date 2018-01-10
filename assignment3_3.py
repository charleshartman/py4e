#py4e assignment 3.3

score = input("Enter Score: ")
try :
    sc = float(score)
except :
    print("that is not a number, exiting...")
    quit()

if sc > 1.0 :
    print ("Not a valid score, exiting...")
elif sc < 0 :
    print ("Not a valid score, exiting...")
elif sc >= 0.9 :
    print ("A")
elif sc >= 0.8 :
    print ("B")
elif sc >= 0.7 :
    print ("C")
elif sc >= 0.6 :
    print ("D")
elif sc < 0.6 :
    print ("F")
else :
    print ("Not a valid score, exiting...")
