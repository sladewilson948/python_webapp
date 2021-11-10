
from pywebio.input import *
from pywebio.output import *

def main():
     def absolute_sum(i):
         value=str(i)
         while len(value)!=1:
             value=list(value)
             value=[int(i) for i in value]
             value=sum(value)
             value=str(value)
         return int(value)
     def validate_card(number):
         number=list(number)
         list1=number[-1::-2]
         list2=number[-2::-2]
         list1=[int(i) for i in list1]
         list2=[int(i) for i in list2]
         list2=[2*i for i in list2]
         list2=[absolute_sum(i) for i in list2]
         sum1=sum(list1)
         sum2=sum(list2)
         sum3=sum1+sum2
         if sum3%10==0:
             return 'Valid Card'
         else:
             return 'Invalid Card'
     def check_number(text):
         if len(text)<16:
             return 'The credit card number must have 16 digits'
         elif len(text)>16:
             return 'The credit card number must have 16 digits'
         else:
             pass
     card_number=input("Enter card number here : ",type=TEXT,validate=check_number)
     k=validate_card(card_number)
     put_table([[card_number,k]],headers=['Card Number','Validity'])

if __name__ == '__main__':
    import argparse
    from pywebio.platform.tornado_http import start_server as start_http_server
    from pywebio import start_server as start_ws_server

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    parser.add_argument("--http", action="store_true", default=False, help='Whether to enable http protocol for communicates')
    args = parser.parse_args()

    if args.http:
        start_http_server(main, port=args.port)
    else:
        # Since some cloud server may close idle connections (such as heroku),
        # use `websocket_ping_interval` to  keep the connection alive
        start_ws_server(main, port=args.port, websocket_ping_interval=30)

