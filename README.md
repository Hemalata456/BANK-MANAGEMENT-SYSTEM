# 🏦 Bank Management System – Class 12 Python Project

This is a **Bank Management System** project developed as part of the CBSE Class 12 Computer Science curriculum. The application uses **Python** for frontend logic and **MySQL** for backend data storage.

It simulates basic banking operations such as creating accounts, deposits, withdrawals, balance inquiries, and transaction management.

---

## 📚 Features

### 👨‍💼 Admin / Employee
- Add customer accounts
- Update customer details (name, phone number, address)
- Transfer funds between accounts
- Deposit and withdraw money
- View customer balance
- Maintain transaction logs

### 🧑‍💻 Bank Customers
- Create a new bank account
- Perform transactions (deposit/withdraw)
- Check account details
- Update personal information
- View transaction history
- Delete account
- Check current balance

---

## 🛠️ Technologies Used

- **Python 3.x**
- **MySQL Database**
- `mysql-connector-python` for database connectivity

---

## 🏗️ Database Tables Used

- `user`: Stores employee information
- `admin_user`: Stores admin credentials
- `customer`: Stores customer account data
- `transaction`: Records customer transactions

> 💡 You must create these tables in MySQL before running the code. Let me know if you want a `.sql` file for this!

---

## 🚀 How to Run the Project

1. Install Python and MySQL on your system.
2. Install the MySQL connector:
   ```bash
   pip install mysql-connector-python
