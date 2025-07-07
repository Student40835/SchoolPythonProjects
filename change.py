#Author: Maxwell Benjamin
#GitHub Username: Student40835
#Date: 6/30/2025
#Description:tells you how to make the most efficient change off of a cent value
change = float(input("Please enter an amount in cents less than a dollar."))
q=int(change/25)
d=int((change-(q*25))/10)
n=int((change-((q*25)+(d*10)))/5)
p=int(change-((q*25)+(d*10)+(n*5)))
print ("Your change will be:")
print("Q: "+str(q))
print("D: "+str(d))
print("N: "+str(n))
print("P: "+str(p))