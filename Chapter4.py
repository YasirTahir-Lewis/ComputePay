def computepay(h,r):

    if (h >= 41):

        h2 = h-40;
        overpay = (r*1.5) * h2;
        grosspay = overpay + (40*r);

	return grosspay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

hrs = float(hrs)
rate = float(rate)

p = computepay(hrs,rate)

print("Pay",p)

        
