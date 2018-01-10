#py4e assignment 5.2

text = "X-DSPAM-Confidence:    0.8475";
fnum = text.find('0')
lnum = text.find('5')
num = text [fnum:lnum+1]
float(num)
print(num)
