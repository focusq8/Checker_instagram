import requests
from uuid import uuid4

def check_username():
    file_username = input("[+] Enter Your File Name: ")
    open_file_username = open(file_username,"r").read().splitlines()
    for list_username in open_file_username:
        url = 'https://i.instagram.com/api/v1/users/check_username/'
        header = {
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTv10=',
            'X-IG-App-ID': '567067343352427',
            'User-Agent': 'Instagram 243.0.0.16.111 Android (25/7.1.2; 240dpi; 720x1280; samsung; SM-G977N; beyond1q; qcom; en_US; 382290502)',
            'Accept-Language': 'en-GB, en-US',
            'X-MID': 'YtCuogABAAHGb5ORU-D-La7ZpjiQ',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate'
            }

        data = {
            "is_group_creation":"false",
            "username":list_username,
            "_uid":uuid4(),
            "_uuid":uuid4()
            }

        req = requests.post(url=url,headers=header,data=data)
        if "username_is_taken" in req.text:
            print(f"UnAvailable: {list_username}")

        elif '"available":true' in req.text:
            print(f"Available: {list_username}")
        else:
            print(req.text)

def check_email():
    file_email = input("[+] Enter Your File Name: ")
    open_file_email = open(file_email,"r").read().splitlines()
    for list_email in open_file_email:
        url = 'https://i.instagram.com/api/v1/users/check_email/'
        header = {
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTv10=',
            'X-IG-App-ID': '567067343352427',
            'User-Agent': 'Instagram 243.0.0.16.111 Android (25/7.1.2; 240dpi; 720x1280; samsung; SM-G977N; beyond1q; qcom; en_US; 382290502)',
            'Accept-Language': 'en-GB, en-US',
            'X-MID': 'YtCuogABAAHGb5ORU-D-La7ZpjiQ',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate'
            }

        data = {
            "android_device_id":uuid4(),
            "login_nonce_map":"{}",
            "login_nonces":"[]",
            "email":list_email,
            "qe_id":uuid4(),
            "waterfall_id":uuid4()
            }
            
        req = requests.post(url=url,headers=header,data=data)

        if "email_is_taken" in req.text:
            print(f"UnAvailable: {list_email}")

        elif '"available":true' in req.text:
            print(f"Available: {list_email}")
        else:
            print(req.text)

if __name__ == "__main__":
    choose = input("""
1. Checker emails

2. Checker usernames


choose please the number: """)

    if choose == "1":
        check_email()   

    elif choose == "2":
        check_username()