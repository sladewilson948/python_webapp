from pywebio.input import *
from pywebio.output import *
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
toast(f'It is a {k}')