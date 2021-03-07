
import math
print(" press 0 to find overview \n press 1 to find prcentage \n press 2 to find market price  \n to exit press 0 in price")

i = int(input())
value = 1
multi = 1.7

if i==0 :
	while value != 0 :
		print(" Enter buy price")
		value = int(input())
		if value<=0:
			break
		print(" Enter sell price on buff ")
		bp = int(input())
		prec = (bp*10)/value*100
		print("buff price is ", "{:.2f}". format(prec) ," %  of market \n")
		pro = bp*multi*0.97*0.86*10
		overl = pro/value
		print("overall back price is ", "{:.2f}". format(pro) , ". Profit", "{:.2f}". format(overl) ,"\n")
		print("according to this ratio profit %  in a month (if go in 10 days)", "{:.2f}". format(overl*overl*overl), "\n")
		days = int(30/math.log(1.35,overl))
		print("It must sell in ", days-7 ,"days on buff and in" , days ,"days on overall \n")
		print("Steam lowest price is ", "{:.2f}". format( bp*10*multi*0.97)," after tax we get ", "{:.2f}". format( pro) ,"\n")
elif i==1 :
	while value != 0:
		print(" Enter price")
		value = int(input())
		if value<=0:
			break	
		print(" you want % ?  press y/n")
		if(input() == 'y'):
			prec = int(input())	
			print(" ",prec,"%   - ",value*prec/100)
			continue
		print("0.76  -  ", value*0.76)
		print("0.8  -  " , value*0.8)
		print("0.85  -  " , value*0.85)
		print("0.9  -  " , value*0.9)
elif i==2 :
	while value != 0 :
		if value<=0:
			break
		print(" Enter price")
		value = int(input())
		print("list steam market at  ", value*multi*0.97)