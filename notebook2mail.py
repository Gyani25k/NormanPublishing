from dependency import *

email_sender = 'kgyanender4@gmail.com'
email_password = 'scah yckh byjy xnxa'

def send_email(html_file, email_receiver):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    view_report_button = '''
        <p style="text-align: center; margin-top: 20px;">
            <a href="https://codedmails.com/template-preview?template=newsletter-email-canaotes"
               style="text-decoration: none; color: #ffffff; padding: 10px 15px; font-size: 16px; border-radius: 30px; background-color: #007bff;">
                View Report
            </a>
        </p>
    '''

    html_content += view_report_button

    email_signature = '<p style="margin-top: 20px; text-align: left;">Best regards,<br>Gyanender Kumar Jha</p>'
    html_content += email_signature

    subject = "Here Your Report"

    html_body = MIMEText(html_content, 'html')

    em = MIMEMultipart()
    em.attach(html_body)

    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        
        temp = {"Message": "Email sent successfully!", "Response_Code": 200}
        return json.dumps(temp)
        
    except Exception as e:
        temp = {"Message": f"An error occurred: {e}", "Response_Code": 404}
        return json.dumps(temp)

result = send_email('blog-20200426-shapley.html', 'kgyanender4@outlook.com')
print(result)
