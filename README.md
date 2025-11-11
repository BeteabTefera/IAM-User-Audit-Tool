# 🛠️ IAM User Audit Tool

## 📘 Overview
The **IAM User Audit Tool** is a lightweight Python script that uses the **AWS SDK for Python (boto3)** to audit IAM users in an AWS account.  
It lists all users, their last login date, and the number of active access keys to help identify inactive or risky accounts.

## 🚀 Features
- Lists all IAM users  
- Shows each user’s last password usage  
- Displays number of active access keys  
- Helps enforce IAM security best practices  

## 🧩 Requirements
- Python 3.x  
- AWS CLI configured with valid credentials  
- boto3 library  

Install boto3:
```bash
pip install boto3
```

## ▶️ Usage
1. Configure your AWS CLI:
   ```bash
   aws configure
   ```
2. Run the script:
   ```bash
   python iam_audit.py
   ```

## 🧠 Learning Objectives
- Practice using the AWS SDK (boto3)  
- Understand IAM users, keys, and password policies  
- Apply the principle of least privilege  

## ⚙️ Example Output
```
User                 Last Used                Active Keys
------------------------------------------------------------
admin                2025-11-08               1 active keys
dev-user             Never logged in          0 active keys
```

## 📚 License
This project is for educational purposes and AWS Cloud Practitioner learning.
