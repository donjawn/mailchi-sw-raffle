import requests
from random import getrandbits
url = 'https://mailchi.mp/seftonfashion/air-max-day-raffle-release'

headers = {'User-Agent':
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


# CHANGE the fields as the comments say  
def main(limit):
    for i in range(1, limit+1):
        num = getrandbits(40)
        firstname = 'firstname{}'.format(num) # put your name here, don't remove the {}
        lastname = 'lastname{}'.format(num) # put your name here, don't remove the {}
        phone = 'cell' # your phone number here no dashes or spaces
        email = 'your_email+{}@gmail.com'.format(num) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        payload = {
            'u': '4c3c77a19f16808f6714b45b9',
            'id': '0092c2e1f0',
            'EMAIL': email,
            'FNAME': firstname,
            'LNAME': lastname,
            'PHONE': phone,
            'MMERGE5': '10', # change your size
            'b_4c3c77a19f16808f6714b45b9_697153': ,
            'c': 'dojo_request_script_callbacks.dojo_request_script2'
        }
        resp = requests.post(url, data=payload, headers=headers)
        print('{}/{} registered.'.format(i, limit))

if __name__ == "__main__":
    x = int(raw_input("How many entries do you want: "))
    main(x)

# ALL CREDIT GOES TO github user yousefissa
# THIS SCRIPT IS MODIFICATION TO HIS PREEXISTING SCRIPTS

