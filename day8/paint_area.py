
import math
def paint_calc(height , width ,coverage):
    area = height*width
    no_of_cans = math.ceil(area/coverage)
    print(f"you will need {no_of_cans} to paint the wall")

    


height = int(input("enter the height of wall in feets"))
width = int(input("enter the  width of wall in feets"))
coverage = 5
paint_calc(height , width ,coverage)
