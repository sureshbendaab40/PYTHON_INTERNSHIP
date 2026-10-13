import csv
import smtplib
import ssl
import certifi  

def run_notification_engine(data_source_csv, sender_account, account_token):
   
    smtp_distribution_server = "smtp.gmail.com"
    secure_port = 465      
    notification_template = """Subject: Urgent Academic Update: Lab Pending Requirements

Dear {candidate_name},

This is an automated notification tracking system message regarding your technical records. Our internal logs show an outstanding submission status for your recent course modules.

Please ensure that your files are uploaded before the upcoming university evaluation cycle.

Best Regards,
Academic Coordination Office
"""

    print("[INFO] Initiating network layer setup...")   
    encryption_context = ssl.create_default_context(cafile=certifi.where())
    try:        
        print(f"[INFO] Reading student contact records from: {data_source_csv}")
        with open(data_source_csv, mode='r', encoding='utf-8-sig') as registry_file:
            data_reader = csv.reader(registry_file)
            header = next(data_reader)             
            print(f"[INFO] Linking to mail distribution server: {smtp_distribution_server}")
            with smtplib.SMTP_SSL(smtp_distribution_server, secure_port, context=encryption_context) as network_pipe:                
                network_pipe.login(sender_account, account_token)
                print("[SUCCESS] Server verification passed. Commencing loop execution...")                
                for row in data_reader:
                    if not row or len(row) < 2:
                        continue 
                    recipient_name = row[0].strip()
                    recipient_email = row[1].strip()                    
                    personalized_message = notification_template.format(
                        candidate_name=recipient_name
                    )                    
                    network_pipe.sendmail(sender_account, recipient_email, personalized_message)
                    print(f"[LOG] Notification successfully pushed to: {recipient_name} ({recipient_email})")
        print("\n[SUCCESS] Notification pipeline completed all tasks without errors.")
    except FileNotFoundError:
        print("[ERROR] Could not read records. Target data sheet was not found.")
    except smtplib.SMTPAuthenticationError:
        print("[ERROR] Server login rejected. Check account credentials or access tokens.")
    except ssl.SSLCertVerificationError as ssl_err:
        print(f"[ERROR] SSL certificate verification failed: {ssl_err}")
        print("[HINT] Try running: pip install --upgrade certifi")
    except Exception as error_msg:
        print(f"[SYSTEM FAILURE] Transmission pipeline halted: {str(error_msg)}")
data_file = "student_directory.csv"          
admin_user = "freeusefree37yyyyyyy@gmail.com"       
admin_app_key ="dh d soashds asdfdhg"       
run_notification_engine(data_file, admin_user, admin_app_key)