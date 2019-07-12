birth_date = raw_input("Enter birth date in format dd-mm-YYYY: ")
birth_date = birth_date.split("-")
byear = birth_date[2]
byear = [byear[i:i+2] for i in range(0, len(byear), 2)]
bdate = birth_date[:2] + byear
#print bdate

a, b, c, d = int(bdate[0]), int(bdate[1]), int(bdate[2]), int(bdate[3])

rmsquare = [[a,b,c,d,],[d+1,c-1,b-3,a+3],[b-2,a+2,d+2,c-2],[c+1,d-1,a+1,b-1]]
for row in rmsquare:
    print row
