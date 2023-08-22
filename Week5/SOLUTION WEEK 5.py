from csv import writer
with open('student.csv','w', newline='') as a:
    write=writer(a)
    header=['sid','sname','city','contact']
    write.writerow(header)

    row=[[1,'Dhruv','Vyara',1234567888],
              [2,'Harsh','Baroda',1234567890],
              [3,'Trupal','Bardoli',1122334455],
              [4,'Gopal','Amroli',2211334455],
              [5,'Abhishek','Anand',3322114455]]
    write.writerows(row)

    for i in range(5):
        sid=int(input("Enter ID of Student : "))
        sname=input("Enter Name of Student : ")
        city=input("Enter Name of Student's City : ")
        contact=int(input("Enter Contact Number of Student :"))
        row=[sid,sname,city,contact]
        write.writerow(row)

from csv import reader
with open('student.csv','r') as b:
    read=reader(b)
    for i in read:
        print(i)
    
