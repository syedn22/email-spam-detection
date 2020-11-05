import imaplib
import email
from email.header import decode_header
import pickle
import pandas as pd


# username = input("Enter your mail id : ")  # villersabde360@gmail.com
# password = input("Password : ")
username = "villersabde360@gmail.com"
password = "/*-+7896"

imap = imaplib.IMAP4_SSL("imap.gmail.com")
result = imap.login(username, password)
imap.select('"[Gmail]/All Mail"', readonly=True)

response, messages = imap.search(None, 'ALL')
messages = messages[0].split()
latest = int(messages[-1])
oldest = int(messages[0])


def findWords(message):
    df = pd.read_csv("emails.csv")
    x = list(df.iloc[0:0, 1:3001])
    result = []
    for a in x:
        if a in message:
            result.append(message.count(a))
        else:
            result.append(0)            
    return [result]


def findSpamOrNot(msg):
    email_spam_model = 'email_spam_model.sav'
    loaded_model = pickle.load(open(email_spam_model, 'rb'))
    existing_words = findWords(msg)
    result = loaded_model.predict(existing_words)
    print(result)
    if result[0] == 1:
        print("Spam Mail")
    else:
        print("Not a spam")


for i in range(latest, latest-8, -1):
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            print("***************************")
            print("\n From ,{}".format(msg["From"]))
            print("\n Subject ,{}".format(msg["Subject"]))
            
    for part in msg.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            print('Body: {}'.format(str(body.decode())))
            if body is not None:
                findSpamOrNot(str(body))
            print("***************************")
