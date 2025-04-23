import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def notify_anomalies(df, sender, recipient, password, dry_run=False):
    subject = "📊 Daily Stock Movement Summary"
    body_lines = ["Here is today's summary for monitored tickers:\n"]

    for _, row in df.iterrows():
        change = f"{row['% Change']:.2%}"
        open_price = f"{row['Open']:.2f}"
        high_price = f"{row['High']:.2f}"
        low_price = f"{row['Low']:.2f}"
        close_price = f"{row['Close']:.2f}"
        anomaly_flag = " 🚨" if row.get("Anomaly", False) else ""

        body_lines.append(
            f"- {row['Ticker']}: {change} → "
            f"O:{open_price} H:{high_price} L:{low_price} C:{close_price}{anomaly_flag}"
        )

    body = "\n".join(body_lines)

    if dry_run:
        print("[DRY RUN] Would send email with body:")
        print(body)
        return True

    try:
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)

        print("[INFO] Email sent.")
        return True
    except Exception as e:
        print(f"[ERROR] Email failed: {e}")
        return False
