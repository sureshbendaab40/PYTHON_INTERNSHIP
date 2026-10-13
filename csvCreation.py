import csv
f = open("new.csv","w",newline = "")
wobj = csv.writer(f)
wobj.writerow(["Name ", "Marks"," DEPARTMENT"])
wobj.writerow(["Suresh ", 89,"CSE DEPARTMENT"])
f.close
print("run success")