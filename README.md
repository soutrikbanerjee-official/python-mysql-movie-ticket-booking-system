# 🎬 Movie Ticket Booking System

A command-line based movie ticket booking system developed using **Python and MySQL**, designed to simulate a real-world cinema booking platform.

This project provides a complete digital solution for browsing movies, selecting show timings, booking tickets, managing user profiles, and generating bills with tax calculations.

---

## 🚀 Features

- 🔐 **User Authentication System**
  - Login using mobile number with OTP verification (Sample)
  - New user registration with profile details (Name, Email, Gender, DOB)

- 🎥 **Movie Selection System**
  - Browse movies by genre (Action, Crime, Fantasy, etc.)
  - Select movie, day, and time slot

- 🎟 **Ticket Booking**
  - Book multiple tickets (1–10)
  - Base pricing with dynamic bill calculation

- 💺 **Seat Upgrade System**
  - Premium, Deluxe, and Recliner seat options
  - Automatic cost adjustment based on upgrades

- 💳 **Payment System**
  - Multiple payment modes (UPI, Card, Net Banking, Cash)
  - GST calculation (18%)
  - Booking confirmation with unique booking number

- 🧾 **Bill Generation**
  - Generates detailed booking bill
  - Saves bill as a `.txt` file for future reference

- 👤 **User Profile Management**
  - View and edit personal details
  - View booking history
  - Delete account functionality

- 💬 **Feedback System**
  - Users can submit feedback linked to their booking

---

## 🛠 Technologies Used

- **Python** – Core programming logic
- **MySQL** – Database management
- **MySQL Connector (Python)** – Database connectivity
- **File Handling** – Bill storage and retrieval

---

## 🧠 Project Structure

The program is modular and built using multiple functions:

- `Login()` – Handles authentication and user creation
- `Movies_Shows()` – Movie selection and booking flow
- `Addon_Seats()` – Seat upgrade management
- `Payment()` – Billing, GST calculation, and booking confirmation
- `Feedback()` – Stores user feedback
- `My_Profile()` – Profile viewing and editing
- `MainMenu()` – Navigation system
- `control()` – Main driver function

Refer to the data-flow chart for a better understanding of the program execution. 

---

## ⚙️ System Requirements

**Software:**
- Python 3
- MySQL Server (8.0 recommended)
- MySQL Connector

---

## ▶️ How to Run

1. Install Python and MySQL
2. Install MySQL connector
3. Create the database and tables using the provided SQL script
4. Update database credentials in the Python file
5. Run the program

---

## 🎯 Purpose

This project was developed to demonstrate how programming and database systems can be integrated to build a real-world application. It focuses on applying concepts such as:

- modular programming
- database management
- user interaction design
- logical decision-making

---

## 🔮 Future Improvements

The follwing features can be added to enhance the programs outlook:

- Graphical User Interface (GUI)
- Online payment gateway integration
- Real-time seat availability system
- Web-based deployment

---

## 📌 Note

This project was developed as part of a Class XII Computer Science project and represents a practical implementation of Python and MySQL concepts.

---

## 📜 License

This project is licensed under the MIT License.
