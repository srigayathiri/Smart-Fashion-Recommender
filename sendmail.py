import configparser
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


config = configparser.ConfigParser()
config.read("config.ini")

def sendMailUsingSendGrid(API,from_email,to_emails,subject,html_content):
    if API!=None and from_email!= None and len(to_emails)>0:
        message = Mail(from_email,to_emails,subject,html_content)
        try:
            sg = SendGridAPIClient(API)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)

try:
    settings = config["SETTINGS"]
except:
    settings = {}
    
API = settings.get("APIKEY",None)
from_email = settings.get("FROM",None)


subject = "TEAM ID PNT2022TMID23050"

html_content = "Welcome To Unik Family, You Have Successfully Registered :) "

