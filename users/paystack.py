import requests
from django.conf import settings

class Paystack():
    def __init__(self,*args,**kwargs):

        self.base_url = 'https://api.paystack.co'
        self.SECRET_KEYS = settings.PAYSTACK_SECRET_KEYS    
        self.PUBLIC_KEYS = settings.PAYSTACK_PUBLICK_KEYS
    def verify_payment(self,ref,*args,**kwargs):
        path = f'/transaction/verify/{ref}'
        headers = {
            'Authorization':f"Bearer {self.SECRET_KEYS}",
            'Content-type':'application/json',
        }

        url = self.base_url + path
        response = requests.get(url,headers = headers)
        if response.status_code ==200:
            response_data = response.json()
            return response_data['status'],response_data['data']
        response_data = response.json()
        return response_data['status'],response_data['message']