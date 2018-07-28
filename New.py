Total = 0
Budget = 0
SaveToMum = 0
IfRemain = 1
Month = 0
for i in range (1,13):
	Total += 300
	Budget = int(input())
	Total -= Budget
	if (Total < 0):
		IfRemain = 0
		Month = i
		FinalMonth = Month
	SaveToMum+=int(Total/100)
	Total = Total%100
if (IfRemain == 1):
	FinalTotal = int(120*SaveToMum + Total)
	print(FinalTotal)
else:
	print (-FinalMonth)