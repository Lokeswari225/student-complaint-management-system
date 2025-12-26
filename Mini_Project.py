from datetime import date
import mysql.connector

def getConnection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Lokeswari123",
        database="python_practice"
    )

#test connection is the connection is established or not 
try:
    conn=getConnection() #user-defined method
    print("connection is establihed successfully")
    
except mysql.connector.error as err:
    print("connection failed ")

#register the compliant
def register_complaint():
    mycursor=conn.cursor()
    print("Register a new Complaint")
    student_name=input("enter a student name: ")
    complaint_category=input("enter a complaint category: ")
    complaint_description=input("enter a compliant description: ")
    reg_date=date.today()

    sql="insert into complaints (student_name,complaint_category,complaint_description,Reg_date,status)" \
    "values (%s,%s,%s,%s,%s)"
    val=(student_name,complaint_category,complaint_description,reg_date,"pending")

    mycursor.execute(sql,val)
    conn.commit()

    print("compliant Registered successfully")


#now we can view  all complaints
def view_All_complaints():
    conn=getConnection()
    mycursor=conn.cursor()
    print("\nAll Compliants are")
    sql="select * from complaints"
    mycursor.execute(sql)
    result=mycursor.fetchall() #here result has some records 

    if len(result)==0:   #len() can count the how many records available in database
        print("No complaints raised\n")
    else:
        for col in result:
            print(f"id: {col[0]}")
            print(f"student name: {col[1]}")
            print(f"complaint_category: {col[2]}")
            print(f"complaint_description: {col[3]}")
            print(f"date: {col[4]}")
            print(f"status: {col[5]}")
            print("-"*40)


#we can update the complaint status
def update_complaint_status():
    conn=getConnection()
    mycursor=conn.cursor()
    print("\nUpdating the complaint status:")
    complaint_id=input("enter complaint id: ")
    new_status=input("complaint resolved/pending: ")
    #we need to check the complaint_id is there in database or not
    mycursor.execute("select * from complaints where id=%s",(complaint_id,)) #we have to give the complaint_id ike this because it prevents sql injection
    complaint=mycursor.fetchone()

    if complaint:
        sql="update complaints set status=%s where id=%s"
        mycursor.execute(sql,(new_status,complaint_id))
        conn.commit()
        print("\ncomplaint status updated successully")
    else:
        print("complaint id not found")


#we can also search complaints by category
def Search_Complaint_By_category():
    conn=getConnection()
    mycursor=conn.cursor()
    print("\nsearch the complaint by category")
    category=input("enter a complaint category: ")
    sql="select * from complaints where complaint_category=%s"
    mycursor.execute(sql,(category,))
    result=mycursor.fetchall()
    if result:
        print("complaints under category",category)
        for row in result:
            print(f"id: {row[0]}, Name:{row[1]}, complaint_category:{row[2]}, complaint_description:{row[3]}, status:{row[5]}")
    else:
        print("\nno complaints found under this category")

#creating final menu for the student complaint management system 
def main_menu():
    while True:
        print("\n====STUDENT COMPLAINT MANAGEMENT SYSTEM====")
        print("1.Register a New Complaint")
        print("2.View All Complaints")
        print("3.Update Complaint Status")
        print("4.Search Complaint by Category")
        print("5.Exit")
        print("------------------------------------------------")
        user=input("Are you Admin or Student:")
        if user=="Admin":
            adminChoice=input("enter choice: ")
            if adminChoice=='v':
                view_All_complaints()
            elif adminChoice=='u':
                update_complaint_status()
            elif adminChoice=='s':
                Search_Complaint_By_category()
            elif adminChoice=='exit':
                print("Exiting.....Thank you")
                break
        elif user=="Student":
            StudentChoice=input("enter choice: ")
            if StudentChoice=='r':
                register_complaint()
            elif StudentChoice=='v':
                view_All_complaints()
            elif StudentChoice=='exit':
                print("Exiting.....Thank you")
                break
        else:
            print("invalid choice.Please try again")
main_menu()



