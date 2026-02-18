import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# UUID values
user_id = "7df7b091-6007-41a1-b08c-11826f8baca3"
campaign_id = "033f20a6-3f65-49c9-be6a-6866c18a3357"
lead_id = "aeb493cc-554d-4323-9a9d-2f30aabe441d"

tracking_url = f"https://email-tracking-0au6.onrender.com/track?u={user_id}&c={campaign_id}&l={lead_id}"

sender = "astelpauly2002@gmail.com"
receiver = "a.pauly@analytica-data.com"
password = "ewpfefvucsamzqvp"  # Gmail App Password

msg = MIMEMultipart("alternative")
msg["Subject"] = "Test Campaign Email"
msg["From"] = sender
msg["To"] = receiver

html_content = f"""
<html>
  <body>
    <p>Hello,</p>
    <p>This is campaign mail.</p>

    <!-- Hidden Tracking Pixel -->
    <img src="{tracking_url}" width="1" height="1" style="display:none;" />
  </body>
</html>
"""

msg.attach(MIMEText(html_content, "html"))

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())

print("Email Sent!")
