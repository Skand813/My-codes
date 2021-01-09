
#Reading docx files from python script
import docx

def getText(filename) :
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return ('\n').join(fullText)






#Mail from python
import smtplib
conn =smtplib.SMTP("smtp.gmail.com",587)
conn.ehlo()
conn.starttls()
conn.login('EMAIL address','EMAIL password')
conn.sendmail('Sender Email','Reciever Email','Subject : Text......\n\n Hi Skand,\n This is test mail from python script')
conn.quit()
