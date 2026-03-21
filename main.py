import mysql.connector
import time
import random
import os

print("\n===== WELCOME TO SB THEATRES, BENGALURU =====")

sbdb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="sb_theatres")
sbcursor = sbdb.cursor()

genre = ["Action", "Crime", "Fantasy", "Horror", "Romance", "Fiction", "Thriller"]
day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_slot = ["Morning (10:00 am onwards)", "Afternoon (2:00 pm onwards)", "Evening (6:00 pm onwards)", "Night (10:00 pm onwards)"]
seat = ["Premium -> +₹50/-", "Delux -> +₹100/-", "Recliner -> +₹200/-"]
payment = ["UPI", "Credit/Debit Card", "Net Banking", "Cash"]
cr_user_details = []
#Current user details will be stored as follows: [Phone Number, Movie Genre, Movie Name, Day, Slot, No. of Tickets, Seats]
bill = 0

def Login():
    global cr_user_details
    user_exists = False
    while user_exists==False:
        while True:
            ph_no = input("Enter your 10 digit phone number to continue:\n")
            if ph_no.strip().isdigit() and len(ph_no)==10:
                ph_no = int(ph_no)
                break
            else:
                print("❌ Invalid mobile number! Try again!")
        print("Auto-verifying OTP in 3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("✅ OTP succesfully verified!")
        sbcursor.execute("SELECT Mobile_No FROM Users")
        t = sbcursor.fetchall()
        for x in t:
            if x[0]==ph_no:
                print("✅ Welcome back!")
                user_exists = True
                break
        if user_exists==False:
            name = input("Enter your full name:\n").strip().upper()
            while True:
                email = input("Enter your valid email ID (press * to skip): (Note: We are currently only accepting Gmail ID's)\n").strip().lower()
                if email=='*':
                    break
                elif email.endswith("@gmail.com") and email.count("@")==1 and len(email.split("@")[0]) > 0:
                    break
                else:
                    print("You have either entered an invalid/non-accepted email ID! Try again or skip this section!")
            while True:
                gender = input("Enter your gender (press * to skip): (M/F)\n").upper().strip()
                if gender=='M' or gender=='F' or gender=='*':
                    break
                else:
                    print("❌ Invalid input! Try again!")
            while True:
                dob = input("Enter your DOB in YYYY/MM/DD format (press * to skip):\n").strip()
                if len(dob)==10:
                    x = dob.split('/')
                    if len(x[0])==4 and len(x[1])==2 and len(x[2])==2 and (x[0]+x[1]+x[2]).isdigit() and int(x[1])<=12 and int(x[2])<=31:
                        break
                    else:
                        print("❌ Invalid input! Try again!")
                elif dob=='*':
                    break
                else:
                    print("❌ Invalid input! Try again!")
            email = None if email=='*' else email
            gender = None if gender=='*' else gender
            dob = None if dob=='*' else dob
            values = (name, ph_no, email, gender, dob)
            sbcursor.execute("INSERT INTO Users (Name, Mobile_No, Email, Gender, DOB) VALUES (%s, %s, %s, %s, %s)", values)
            sbdb.commit()
            print("🎉 Account created successfully!")
            user_exists = True
    print("✅ Login successful!")
    cr_user_details.append(ph_no)

def choice():
    while True:
        ch = input("Enter your choice:\n")
        if ch.isdigit():
            break
        else:
            print("❌ Invalid input! Try again!")
    return int(ch)

def Addon_Seats(n):
    global cr_user_details
    global bill
    print("SEATS")
    s = 0
    seats = ""
    upgrd_seat = seat.copy()
    print("The following are our seat upgrade options:")
    for x in range(len(seat)):
        print(f"{x+1}. {seat[x]}")
    while s<n:
        if len(upgrd_seat)==0:
            print("You have no more choices to upgrade!")
            break
        print("Choose the seat upgrade, hence enter the number of tickets for which you would like to upgrade the seat.")
        print(f"You can currently upgrade {n-s} seats;")
        print("By default, you have the standard seat; If you wish to skip this section or continue after selection, then press 0;")
        while True:
            ch = choice()
            if ch>=0 and ch<=3:
                break
            else:
                print("❌ Invalid choice! Choose again!")
        if ch!=0 and seat[ch-1] in upgrd_seat:
            print(f"You have selected {seat[ch-1]} upgrade, now enter the number of seats for this upgrade;")
            while True:
                nm = choice()
                if nm<=(n-s) and nm>=1:
                    s+=nm
                    break
                else:
                    print("❌ Out of range! Enter a valid number of seats!")
            if ch==1 and seat[0] in upgrd_seat:
                upgrd_seat.remove(seat[0])
                bill+=nm*50
                seats+=str(nm)+" Premium seat(s)"
            elif ch==2 and seat[1] in upgrd_seat:
                upgrd_seat.remove(seat[1])
                bill+=nm*100
                seats+=str(nm)+" Delux seat(s)"
            elif ch==3 and seat[2] in upgrd_seat:
                upgrd_seat.remove(seat[2])
                bill+=nm*200
                seats+=str(nm)+" Recliner seat(s)"
            if s<n:
                seats+=', '
        elif ch!=0 and seat[ch-1] not in upgrd_seat:
            print("You have already selected this upgrade! Please choose again!")
        else:
            break
    if s<n:
        seats+=str(n-s)+" Standard seat(s)"
    print(f"You have in total selected {seats}.")
    cr_user_details.append(seats)

def Payment():
    global cr_user_details
    global bill
    status = False
    print("\n===== BILL =====")
    fin_det = cr_user_details
    sbcursor.execute("SELECT * FROM Users WHERE Mobile_No = %s", (fin_det[0],))
    t = sbcursor.fetchone()
    print("Name:", t[0])
    print("Mobile Number:", t[1])
    print("Email:", t[2])
    print("Gender:", t[3])
    print("DOB:", t[4])
    print(f"Movie: {fin_det[2]} (Genre: {fin_det[1]})")
    print("Day:", fin_det[3])
    print("Slot:", fin_det[4])
    print("Number of tickets:", fin_det[5])
    print("Seats:", fin_det[6])
    print(f"Net amount: ₹{bill}/-")
    gst = 0.18*bill
    print(f"GST (@ 18%): ₹{gst:.2f}/-")
    print(f"Grand total: ₹{(bill+gst):.2f}/-")
    print("========================\n")
    print("To proceed to checkout press 1, to cancel/return to main menu press 0;")
    while True:
        ch = choice()
        if ch>=0 and ch<=1:
            break
        else:
            print("❌ Invalid choice! Choose again!")
    if ch==1:
        print("Choose a method to complete payment:")
        for x in range(len(payment)):
            print(f"{x+1}. {payment[x]}")
        while True:
            ch = choice()
            if ch>=1 and ch<=4:
                break
            else:
                print("❌ Invalid choice! Choose again!")
        print(f"You have selected {payment[ch-1]} as mode of payment!")
        print("Processing payment...")
        time.sleep(3)
        print("Payment Successful!")
        status = True
        while True:
            booking_number = random.randint(100000, 999999)
            filename = f"Booking_{booking_number}.txt"
            if not os.path.isfile(filename):
                break
            else:
                pass
        print("Your booking number is:", booking_number)
        filename = f"Booking_{booking_number}.txt"
        bill_text = f"""
===== BILL =====
Name: {t[0]}
Mobile Number: {t[1]}
Email: {t[2]}
Gender: {t[3]}
DOB: {t[4]}
Movie: {fin_det[2]} (Genre: {fin_det[1]})
Day: {fin_det[3]}
Slot: {fin_det[4]}
Number of tickets: {fin_det[5]}
Seats: {fin_det[6]}
Net amount: ₹{bill}/-
GST (@ 18%): ₹{gst:.2f}/-
Grand total: ₹{(bill+gst):.2f}/-
Booking number: {booking_number}
Booking status: Successful
========================
"""
        f = open(filename, 'w', encoding='utf-8')
        f.write(bill_text)
        f.close()
        sbcursor.execute("SELECT Booking_Nos FROM Users WHERE Mobile_No = %s", (fin_det[0],))
        result = sbcursor.fetchone()
        if result[0]:
            updated = result[0] + "," + str(booking_number)
        else:
            updated = str(booking_number)
        sbcursor.execute("UPDATE Users SET Booking_Nos = %s WHERE Mobile_No = %s", (updated, fin_det[0]))
        sbdb.commit()
    else:
        pass
    return status

def Movies_Shows():
    global cr_user_details
    global bill
    booking = False
    print("\n===== MOVIES & SHOWS =====")
    print("Select genre:")
    for x in range(len(genre)):
        print(f"{x+1}. {genre[x]}")
    while True:
        ch = choice()
        if ch>=1 and ch<=len(genre):
            break
        else:
            print("❌ Invalid choice! Choose again!")
    cr_user_details.append(genre[ch-1])
    sbcursor.execute(f"SELECT * from {genre[ch-1]}")
    t = sbcursor.fetchall()
    print("Select movie:")
    for x in range(len(t)):
        print(f"{t[x][0]}. {t[x][1]}")
    while True:
        ch = choice()
        if ch>=1 and ch<=len(t):
            break
        else:
            print("❌ Invalid choice! Choose again!")
    cr_user_details.append(t[ch-1][1])
    print("The base price for your movie is ₹250/-")
    print("Please enter the number of tickets you wish to purchase (min 1 to max 10):\n")
    while True:
        n = choice()
        if n>=1 and n<=10:
            break
        else:
            print("❌ Invalid choice! Choose again!")
    bill+=n*250
    print("We operate on all days of the week!")
    print("Select day:")
    for x in range(1,8):
        print(f"{x}. {day[x-1]}")
    while True:
        ch = choice()
        if ch>=1 and ch<=7:
            break
        else:
            print("❌ Invalid choice! Choose again!")
    cr_user_details.append(day[ch-1])
    print("Select time slot:")
    for x in range(1,5):
        print(f"{x}. {time_slot[x-1]}")
    while True:
        ch = choice()
        if ch>=1 and ch<=4:
            break
        else:
            print("❌ Invalid choice! Choose again!")
    cr_user_details.append(time_slot[ch-1])
    cr_user_details.append(n)
    print("To continue press 1, to cancel/return to main menu press 0;")
    while True:
        ch = choice()
        if ch>=0 and ch<=1:
            break
        else:
            print("❌ Invalid choice! Choose again!")
    if ch==1:
        print("\n===== ADD-ONS =====")
        Addon_Seats(n)
        status = Payment()
        booking = status
    else:
        pass
    return booking

def Feedback():
    print("\n===== FEEDBACK =====")
    bk_no = input("Enter your booking number:\n")
    filename = f"Booking_{bk_no}.txt"
    if not os.path.isfile(filename):
        print("❌ Booking number not found! Please check and try again.")
        print("Returning to main menu...")
        time.sleep(1)
        return
    comment = input("Let us know how you feel about our booking service (type NIL to skip): ")
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"\nUser comment: {comment}\n")
    print("Thank you! Your comment has been added to your booking file.")

def My_Profile():
    ph_no = cr_user_details[0]
    sbcursor.execute("SELECT * FROM Users WHERE Mobile_No = %s", (ph_no,))
    name, mobile, email, gender, dob, booking_nos = sbcursor.fetchone()
    while True:
        print("\n===== MY PROFILE =====")
        print(f"Name: {name}")
        print(f"Mobile Number: {mobile}")
        print(f"Email: {email if email is not None else 'NULL'}")
        print(f"Gender: {gender if gender is not None else 'NULL'}")
        print(f"DOB: {dob if dob is not None else 'NULL'}")
        print(f"Bookings: {booking_nos if booking_nos else 'No bookings yet.'}")
        print("======================\n")
        print("Choose a following operation to continue:")
        print("1. Edit Email")
        print("2. Edit Gender")
        print("3. Edit DOB")
        print("4. View Bill of past booking")
        print("5. Delete Account")
        print("6. Exit Profile")
        ch = choice()
        if ch==1:
            new_email = input("Enter new Email ID:\n")
            sbcursor.execute("UPDATE Users SET Email = %s WHERE Mobile_No = %s", (new_email, ph_no))
            sbdb.commit()
            print("✅ Email updated successfully!")
            email = new_email
        elif ch==2:
            new_gender = input("Enter Gender (M/F):\n")
            sbcursor.execute("UPDATE Users SET Gender = %s WHERE Mobile_No = %s", (new_gender, ph_no))
            sbdb.commit()
            print("✅ Gender updated successfully!")
            gender = new_gender
        elif ch==3:
            new_dob = input("Enter DOB (YYYY/MM/DD):\n")
            sbcursor.execute("UPDATE Users SET DOB = %s WHERE Mobile_No = %s", (new_dob, ph_no))
            sbdb.commit()
            print("✅ DOB updated successfully!")
            dob = new_dob
        elif ch==4:
            if not booking_nos:
                print("No bookings available!")
            else:
                print("\nYour Booking Numbers:", booking_nos.split(','))
                view_no = input("Enter the booking number whose bill you want to view:\n").strip()
                filename = f"Booking_{view_no}.txt"
                try:
                    with open(filename, 'r', encoding='utf-8') as f:
                        print("\n===== BILL DETAILS =====")
                        print(f.read())
                        print("========================\n")
                except FileNotFoundError:
                    print("❌ Booking number not found!")
        elif ch==5:
            confirm = input("⚠ Are you sure you want to delete your account? (Y/N):\n")
            if confirm.lower()=='y':
                sbcursor.execute("DELETE FROM Users WHERE Mobile_No = %s", (ph_no,))
                sbdb.commit()
                print("🗑 Account deleted successfully!")
                cr_user_details.clear()
                return False
            elif confirm.lower()=='n':
                print("Account deletion cancelled!")
            else:
                print("❌ Invalid input!")
        elif ch==6:
            print("Exiting profile...")
            time.sleep(1)
            break
        else:
            print("Invalid choice! Choose again!")

def MainMenu():
    global cr_user_details
    global bill
    print("\n===== MAIN MENU =====")
    print("Welcome to SB Theatres, the epitome of modern entertainment!")
    print("Explore our various menus to get the best experience for your movie.")
    print("Book your best show now!")
    print("Select one of the menus below to proceed:")
    print("1. Movies & Shows")
    print("2. Feedback")
    print("3. My Profile")
    print("Press 0 to exit;")
    while True:
        ch = choice()
        if ch>=0 and ch<=3:
            break
        else:
            print("Invalid choice! Choose again!")
    if ch==1:
        update = Movies_Shows()
        if update==True:
            print("✅ Booking successful!")
            print("Returning to Main Menu...")
            cr_user_details = [cr_user_details[0]]
            bill = 0
            time.sleep(1)
        else:
            print("❌ Booking failed!")
            print("Returning to Main Menu...")
            cr_user_details = [cr_user_details[0]]
            bill = 0
            time.sleep(1)
    elif ch==2:
        Feedback()
    elif ch==3:
        if My_Profile()==False:
            print("You will have to login/signup again to continue using SB Theatres!")
            print("🥲 We hope you come back soon!")
            return False
    else:
        return False
    return True

def control():
    print("\n===== LOGIN/SIGNUP =====")
    Login()
    a = True
    while a==True:
        a = MainMenu()
    print("Thank you for using SB Theatres!")
    print("We hope you had a great experience!")
    print("Goodbye!")
    print("Developed by Soutrik Banerjee | GitHub: github.com/EnderionX\n© 2025 All Rights Reserved")

control()
