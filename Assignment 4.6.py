def computepay(h,r):
    if h < 0 or r < 0:
        return 0
    elif h > 40:
        return (40*r+(h-40)*1.5*r)
    else:
        return (h*r)
    
try:
    hrs = raw_input("Enter Hours:")
    hour = float(hrs)
    r = raw_input("please input your rate:")
    rate = float(r)
    p = computepay(hour,rate)
    print ("Pay", p)
except:
    print ("Please,input your numberic")