from input_data.input_data import get_input_data
from subscribers.subscribers import get_subscriber_data
from news.news import get_news
from sendmail.sendmail import send_mail
import json

def start_process():
    #get input json/dict from API
    with open('config.json') as f: #context manager
        config = json.load(f)

    input_data = get_input_data(config["URL"]) #TODO: Add exception handling
    if isinstance(input_data, dict):
        if len(input_data) >0 :
            print("Got some data!, proceeding... ")
    else:
        print("aborting: Reason: API has no data")
        return
        
    #get subscriber data
    get_subscriber_data()

    #get news 
    get_news()

    #make reports
        #xls
    make_excel_report()
        #subs report
    make_user_specific_report()

    #send mail
    send_mail()


#-------
def make_excel_report():
    print("making xls report...")

def make_user_specific_report():
    print("making xls report...")
