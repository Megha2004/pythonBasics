oddDays={"Mon","Wed","Fri"}
allDays={"Sun","Mon","Tue","Wed","Thu","Fri","Sat"}
union=oddDays | allDays
print("Union of sets= ",union)
intersection=oddDays&allDays
print("Intersection of sets= ",intersection)
difference=allDays-oddDays
print("Difference of sets= ",difference)
subset=oddDays<=allDays
print("Subset result= ",subset)
superset=allDays>=oddDays
print("Superset result= ",superset)
