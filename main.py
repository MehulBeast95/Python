'''stk = []


def push():
    while True:
        x = input("Enter name: ")
        stk.append(x)
        display()
        ch = input("Enter more ? :  ")
        if ch == "no":
            break


def pop():
    if not stk:
        print("Underflow")
    else:
        z = stk.pop()
        print("deleted element: ", z)
        display()


def display():
    a = len(stk)
    for i in range(a - 1, -1, -1):
        print(stk[i])


while True:
    print("1.Add\n2.Delete \n3.Display \n4.Exit \n")
    c = int(input("Enter choice(1-4): "))
    if c == 1:
        push()
    elif c == 2:
        pop()
    elif c == 3:
        display()
    else:
        break'''
import mysql.connector as cn

db = cn.connect(host='localhost', user='root', password='1234')
cur = db.cursor()
#cur.execute("drop database project")
cur.execute("create database project")
cur.execute("use project")
cur.execute("create table payroll(e_id int primary key, e_name varchar(50),ctc bigint, basic bigint, lwp int\
, overtime int,allowance int, hra int, tax int, pf int, gross int, total bigint)")
idd_l = []
cur.execute("select e_id from payroll")
recs = cur.fetchall()
for i in recs:
    idd_l.append(i[0])
while True:
    print("WHAT WOULD YOU LIKE TO DO?")
    print("1. Add employee record")
    print("2. Update employee record")
    print("3. Delete employee record")
    print("4. Exit")
    x = int(input("choose:"))
    if x == 1:
        idd = int(input("enter employee id:"))
        idd_l.append(idd)
        nm = input("enter employee name:")
        ctc = int(input("enter cost to company:"))
        basic = 0.5 * ctc
        lwp = int(input("enter number of leaves without pay:"))
        ov = int(input("enter number of overtime hours:"))
        al = int(input("enter allowances(medical,travel,dearness):"))
        hra = 0.5 * basic
        tot_all = basic + al
        print(tot_all)
        if tot_all < 250000:
            tax = 0
        elif 250000 <= tot_all < 500000:
            tax = 5 / 100
        elif 500000 <= tot_all < 750000:
            tax = 10 / 100
        elif 750000 <= tot_all < 1000000:
            tax = 15 / 100
        elif 1000000 <= tot_all < 1250000:
            tax = 20 / 100
        elif 1250000 <= tot_all < 1500000:
            tax = 25 / 100
        elif tot_all >= 1500000:
            tax = 30 / 100
            print("tax", tax)
            pf = 12 / 100 * tot_all
            print("pf", pf)
            gross = tot_all
            sal_day = gross / 30
            overtime = (sal_day / 8) * ov * 2
            print("taxed amount", gross * tax)
            print(lwp * sal_day)
            total = (gross + overtime + hra) - (gross * tax) - (lwp * sal_day) - pf
            cur.execute("insert into payroll\
            values({},'{}',{},{},{},{},{},{},{},{},{},{})".format(idd, nm, ctc, basic, lwp, ov, al, hra, tax, pf, gross\
            , total))
            db.commit()

    elif x == 2:
        idd = int(input("enter employee id to update record:"))
        if idd in idd_l:
            nm = input("enter updated employee name:")
            ctc = int(input("enter updated cost to company:"))
            basic = 0.5 * ctc
            lwp = int(input("enter updated number of leaves without pay:"))
            ov = int(input("enter updated number of overtime hours:"))
            al = int(input("enter updated allowances(medical,travel,dearness):"))
            hra = 0.5 * basic
            totall = basic + al
            if tot_all < 250000:
                tax = 0
            if 250000 <= tot_all < 500000:
                tax = 5 / 100
            if 500000 <= tot_all < 750000:
                tax = 10 / 100
            if 750000 <= tot_all < 1000000:
                tax = 15 / 100
            if 1000000 <= tot_all < 1250000:
                tax = 20 / 100
            if 1250000 <= tot_all < 1500000:
                tax = 25 / 100
            if tot_all >= 1500000:
                tax = 30 / 100
            pf = 12 / 100 * tot_all
            gross = tot_all
            sal_day = gross / 30
            overtime = (sal_day / 8) * ov * 2
            tot_al = (gross + overtime + hra) - (gross * tax) - (lwp * sal_day) - pf
            cur.execute("update payroll set e_name='{}',ctc={},basic={},lwp={},overtime={},allowance={},hra={},tax={}\
            ,pf={},gross={},total={} where e_id={}".format(nm, ctc, basic, lwp, ov, al, hra, tax, pf, gross, total, idd))
            print("UPDATED SUCCESSFULLY")
            db.commit()
        else:
            print("such employee doesnt exist")
    elif x == 3:
        idd = int(input("enter employee id to delete record:"))
        if idd in idd_l:
            cur.execute("delete from payroll where e_id={}".format(idd))
            print("DELETED SUCCESSFULLY")
            db.commit()
        else:
            print("such employee doesnt exist")

    else:
        break