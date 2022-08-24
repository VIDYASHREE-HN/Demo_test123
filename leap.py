class leap(object):
    def year(self,a):

        if (a % 400 == 0) and (a % 100 == 0):
            # print(f"{a} ia a leap year")
            return a
        elif (a % 4 == 0) and (a % 100 != 0):
            print(f"{a} is a leap year")
            return a  
        
#f=leap()
#print(f.year(2020))
