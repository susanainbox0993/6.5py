text = "X-DSPAM-Confidence: 0.8475"
t1= text.find('0.8475')
t2= float(text[t1:])
print(t2)
