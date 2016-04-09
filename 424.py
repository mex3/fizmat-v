#http://informatics.mccme.ru/mod/statements/view3.php?chapterid=424#1
d, l, k = map(int, input().split())


MonthNames = ('', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
DayOfTheWeek = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
MonthNums = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
DayNums = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
Months = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

fout = open("output.txt", "w")
# days = ((0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31), (0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))
day_start, l, k = map(int, fin.readline().split())
column = day_start
weeks_month = [1] * 13

fout.close()
