import mysql.connector as sqltor
mycon=sqltor.connect(host='localhost',user='hema',passwd='manager',database='bank')
cur=mycon.cursor()
while True:
    print("1.NEW EMPLOYEE")
    print("2.ADMIN")
    print("3.BANK CUSTOMER")
    h=int(input('WHO ARE YOU?:'))
    if h==1:
        print("1. CREATE NEW EMP_ID")
        q=int(input("enter your choice:"))
        if q==1:
            fna_me=input("ENTER FIRST NAME:")
            lna_me=input("ENTER LAST NAME:")
            phon_no=int(input("ENTER PHONE NO:"))
            ad=input("ENTER ADDRESS:")
            a_ge=int(input("ENTER AGE:"))
            query="insert into user values('{}','{}',{},'{}',{})".format(fna_me,lna_me,phon_no,ad,a_ge)
            cur.execute(query)
            mycon.commit()
            print("ID CREATED SUCCESSFULLY")
    if h==2:
        emp_id=int(input("ENTER EMP_ID:"))
        n_ame=input("ENTER NAME:")
        pass_wd=input("ENTER PASSWORD:")
        query="insert into admin_user values({},'{}','{}')".format(emp_id,n_ame,pass_wd)
        cur.execute(query)
        mycon.commit()
        print("login successful")
        print("1. ADD CUSTOMER")
        print("2. UPDATE CUSTOMER ACC")
        print("3. TRANSFER MONEY TO ANOTHER ACC")
        print("4. WITHDRAWL MONEY")
        print("5. DEPOSIT MONEY")
        s=int(input("ENTER YOUR CHOICE:"))
        if s==1:
            a_no=int(input('ENTER ACCOUNT NUMBER:'))
            name=input('ENTER ACCOUNT NAME:')
            ph_no=int(input('ENTER PHONE NO:'))
            add=input('ENTER ADDRESS:')
            ad_no=int(input('ENTER AADHAR NO:'))
            amount=int(input('ENTER CREDIT AMOUNT:'))
            query="INSERT INTO customer VALUES({},'{}',{},'{}',{},{})".format(a_no,name,ph_no,add,ad_no,amount)
            cur=mycon.cursor()
            cur.execute(query)
            mycon.commit()
            print("ACCOUNT CREATED SUCCESSFULLY")
        if s==2:
            print("1. CHANGE NAME")
            print("2. CHANGE PHONE NUMBER")
            print("3. CHANGE ADDRESS")
            d=int(input('ENTER YOUR CHOICE:'))
            if d==1:
                a_no=int(input('ENTER ACCOUNT NUMBER:'))
                cur.execute("select * from customer where acc_no={}".format(a_no))
                if cur.fetchone() is None:
                   print("INVALID ACCOUNT NUMBER")
                else:
                   a_no=int(input('ENTER ACCOUNT NUMBER:'))
                   name=input('ENTER NEW NAME:')
                   cur.execute("update customer set acc_name='{}' where acc_no={}".format(name,a_no))
                   mycon.commit()
                   print("changed successfully")
            if d==2:
                a_no=int(input('ENTER ACCOUNT NUMBER:'))
                cur.execute("select * from customer where acc_no={}".format(a_no))
                if cur.fetchone() is None:
                   print("INVALID ACCOUNT NUMBER")
                else:
                    a_no=int(input('ENTER ACCOUNT NUMBER:'))
                    ph_no=int(input('ENTER NEW PHONE NUMBER:'))
                    cur.execute("update customer set phone_no={} where acc_no={}".format(ph_no,a_no))
                    mycon.commit()
                    print("changed successfully")
            if d==3:
                a_no=int(input('ENTER ACCOUNT NUMBER:'))
                cur.execute("select * from customer where acc_no={}".format(a_no))
                if cur.fetchone() is None:
                   print("INVALID ACCOUNT NUMBER")
                else:
                   a_no=int(input('ENTER ACCOUNT NUMBER:'))
                   add=input('ENTER NEW ADDRESS:')
                   cur.execute("update customer set address='{}' where acc_no={}".format(add,a_no))
                   mycon.commit()
                   print("changed successfully")
        if s==3:
            a_no=int(input('ENTER ACCOUNT NUMBER:'))
            ca_sh=int(input('ENTER AMOUNT:'))
            cur.execute("update customer set op_bal=op_bal-{} where acc_no={}".format(ca_sh,a_no))
            a_no=int(input('ENTER SENDERS ACCOUNT NUMBER:'))
            ca_sh=int(input('ENTER AMOUNT:'))
            cur.execute("update customer set op_bal=op_bal+{} where acc_no={}".format(ca_sh,a_no))
            mycon.commit()
            print("TRANSFERRED SUCCESSFULLY")
        if s==4:
               a_no=int(input('ENTER ACCOUNT NUMBER:'))
               w_at=(input("ENTER WITHDRAWL/DEPOSIT AMOUNT="))
               d_at=int(input("ENTER AMOUNT=",))
               w="INSERT INTO transaction VALUES({},'{}',{})".format(a_no,w_at,d_at)
               cur.execute(w)
               cur.execute("update customer set op_bal=op_bal-{} where acc_no={}".format(d_at,a_no))
               mycon.commit
               print('AMOUNT WITHDRAWL SUCCESSFULLY')
        if s==5:
               a_no=int(input('ENTER ACCOUNT NUMBER:'))
               w_at=(input("ENTER WITHDRAWL/DEPOSIT AMOUNT="))
               d_at=int(input("ENTER AMOUNT=",))
               w="INSERT INTO transaction VALUES({},'{}',{})".format(a_no,w_at,d_at)
               cur.execute(w)
               cur.execute("update customer set op_bal=op_bal+{} where acc_no={}".format(d_at,a_no))
               mycon.commit
               print('AMOUNT DEPOSITED SUCCESSFULLY')
    if h==3:
           print('1.create bank acc')
           print('2.transaction')
           print('3.acc details')
           print('4.change detail')
           print('5.transaction details')
           print('6.delete acc')
           print('7.balance enquiry')
           print('8.exit')
           a=int(input('enter your choice:'))
           if a==1:
              a_no=int(input('ENTER YOUR ACCOUNT NUMBER:'))
              name=input('ENTER ACCOUNT NAME:')
              ph_no=int(input('ENTER PHONE NO:'))
              add=input('ENTER ADDRESS:')
              ad_no=int(input('ENTER AADHAR NUMBER:'))
              amount=int(input('ENTER CREDIT AMOUNT:'))
              query="INSERT INTO customer VALUES({},'{}',{},'{}',{},{})".format(a_no,name,ph_no,add,ad_no,amount)
              cur=mycon.cursor()
              cur.execute(query)
              mycon.commit()
              print("ACCOUNT CREATED SUCCESSFULLY")
           elif a==2:
                a_no=int(input('ENTER ACCOUNT NUMBER:'))
                cur.execute("select * from customer where acc_no={}".format(a_no))
                print("CHECKING AMOUNT")
                data=cur.fetchall()
                count=cur.rowcount
                mycon.commit()
                if count==0:
                    print('INVALID ACCOUT NUMBER TRY AGAIN LATER')
                else:
                    print('1.WITHDRAW AMOUNT')
                    print('2.DEPOSIT AMOUNT')
                    b=int(input("enter your choice:"))
                    if b==1:
                       a_no=int(input('ENTER ACCOUNT NUMBER:'))
                       w_at=(input("ENTER WITHDRAWL/DEPOSIT AMOUNT="))
                       d_at=int(input("ENTER AMOUNT=",))
                       w="INSERT INTO transaction VALUES({},'{}',{})".format(a_no,w_at,d_at)
                       cur.execute(w)
                       cur.execute("update customer set op_bal=op_bal-{} where acc_no={}".format(d_at,a_no))
                       mycon.commit
                       print('AMOUNT WITHDRAWL SUCCESSFULLY')
                    elif b==2:
                          a_no=int(input('ENTER ACCOUNT NUMBER:'))
                          w_at=input("ENTER WITHDRAWL/DEPOSIT AMOUNT=",)
                          d_at=int(input("ENTER AMOUNT="))
                          w="INSERT INTO transaction VALUES({},'{}',{})".format(a_no,w_at,d_at)
                          cur.execute(w)
                          cur.execute("update customer set op_bal=op_bal+{} where acc_no={}".format(d_at,a_no))
                          mycon.commit()
                          print('AMOUNT DEPOSITED SUCCESSFULLY')
                    else:
                        print("transaction failed")
           elif a==3:
                 a_no=int(input('ENTER ACCOUNT NUMBER:'))
                 cur.execute("select * from customer where acc_no={}".format(a_no))
                 if cur.fetchone() is None:
                    print("INVALID ACCOUNT NUMBER")
                 else:
                     cur.execute("select * from customer where acc_no={}".format(a_no))
                     data=cur.fetchall()
                     for row in data:
                         print('ACCOUNT NUMBER=',a_no)
                         print('ACCOUNT NAME=',row[1])
                         print('PHONE NUMBER=',row[2])
                         print('ADDRESS=',row[3])
                         print('AADHAR NUMBER=',row[4])
                         print('BALANCE=',row[5])
           elif a==4:
                 print("1. CHANGE NAME")
                 print("2. CHANGE PHONE NUMBER")
                 print("3. CHANGE ADDRESS")
                 d=int(input('ENTER YOUR CHOICE:'))
                 if d==1:
                     a_no=int(input('ENTER ACCOUNT NUMBER:'))
                     cur.execute("select * from customer where acc_no={}".format(a_no))
                     if cur.fetchone() is None:
                        print("INVALID ACCOUNT NUMBER")
                     else:
                         a_no=int(input('ENTER ACCOUNT NUMBER:'))
                         name=input('ENTER NEW NAME:')
                         cur.execute("update customer set acc_name='{}' where acc_no={}".format(name,a_no))
                         mycon.commit()
                         print("changed successfully")
                 if d==2:
                     a_no=int(input('ENTER ACCOUNT NUMBER:'))
                     cur.execute("select * from customer where acc_no={}".format(a_no))
                     if cur.fetchone() is None:
                        print("INVALID ACCOUNT NUMBER")
                     else:
                        a_no=int(input('ENTER ACCOUNT NUMBER:'))
                        ph_no=int(input('ENTER NEW PHONE NUMBER:'))
                        cur.execute("update customer set phone_no={} where acc_no={}".format(ph_no,a_no))
                        mycon.commit()
                        print("changed successfully")
                 if d==3:
                     a_no=int(input('ENTER ACCOUNT NUMBER:'))
                     cur.execute("select * from customer where acc_no={}".format(a_no))
                     if cur.fetchone() is None:
                        print("INVALID ACCOUNT NUMBER")
                     else:
                        a_no=int(input('ENTER ACCOUNT NUMBER:'))
                        add=input('ENTER NEW ADDRESS:')
                        cur.execute("update customer set address='{}' where acc_no={}".format(add,a_no))
                        mycon.commit()
                        print("changed successfully")
               
                 print("1. ENTER AGAIN")
                 print("2. EXIT")
                 f=int(input("enter your choice:"))
                 if f==1:
                     print(d)
                 if f==2:
                     exit()
                 else:
                     print("ERROR")
           elif a==5:
                a_no=int(input('ENTER ACCOUNT NUMBER:'))
                cur.execute("select * from transaction where acc_no={}".format(a_no))
                data=cur.fetchall()
                for row in data:
                     print('ACCOUNT NUMBER=',a_no)
                     print('w/d=',row[1])
                     print('balance=',row[2])
                if cur.fetchone() is None:
                    print("INVALID ACCOUNT NUMBER")
           elif a==6:
                a_no=int(input('ENTER ACCOUNT NUMBER:'))
                cur.execute("delete from customer where acc_no={}".format(a_no))
                mycon.commit()
                print("DELETED SUCCESSFULLY")
           elif a==7:
                a_no=int(input('ENTER ACCOUNT NUMBER:'))
                cur.execute("select op_bal from customer where acc_no={}".format(a_no))
                row=cur.fetchone()
                while row is not None:
                      print(row)
                      row=cur.fetchone()
                      print("TOTAL BALANCE")
           elif a==8:
                exit()
                break
