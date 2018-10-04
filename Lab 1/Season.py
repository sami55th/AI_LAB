month = int(input("Input the month (1-12): "))

if month in (1 , 2, 3):
	season = 'winter'
elif month in  (4, 5, 6):
	season = 'spring'
elif month in (7, 8, 9):
	season = 'summer'
else:
	season = 'autumn'

print("Season is",season)