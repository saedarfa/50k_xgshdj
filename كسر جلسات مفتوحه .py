import os
import json
from colorama import Fore
import time
import threading
import requests
import time
import json
import os , sys
import random
import re
from threading import Thread
from colorama import init, Fore, Style
from colorama import Fore
import pyfiglet
import webbrowser
import pwinput  


init(autoreset=True)

G = Fore.GREEN
R = Fore.RED
Y = Fore.YELLOW
B = Fore.BLUE

s=("□■"*30)
m=("□■"*30)
g=("□■"*30)
SK = pyfiglet.figlet_format('                TEAM')
saa = pyfiglet.figlet_format('       ALKAPOS')
sk2=pyfiglet.figlet_format('        VODAFONE')
alkapos=pyfiglet.figlet_format('          50K_Flex ')
def sped(s):
        for c in s + '\n':
        	sys.stdout.write(c)
        	sys.stdout.flush()
        	time.sleep(0.001)
        	def alkapos():
        		print("")
sped(R+s)
sped(G+SK)
sped(G+saa)
sped(R+m)
sped(Y+sk2)
sped(R+g)
sped(G+alkapos)
sped(R+g)
webbrowser.open("https://t.me/TEAM_ALKAP0S")

SETTINGS_FOLDER = "TAEM_ALKAP00S"
SETTINGS_FILE = os.path.join(SETTINGS_FOLDER, "settings.json")
os.makedirs(SETTINGS_FOLDER, exist_ok=True)


users = {
    "xxxxx1xxx": "Mohamed Al-Ahly"
}


password = pwinput.pwinput(prompt=G+"🔑 Enter your password: ", mask="*")

if password in users:
    name = users[password]
    print(G+f"✅ Welcome {name}, script is now running...")
    
else:
    print(R+"❌ Incorrect password!")
    sys.exit()








def wait_timer(seconds):
    for remaining in range(seconds, 0, -1):
        print(Y+f"\r\033[K⏳ Waiting {remaining} seconds...", end="")
        time.sleep(1)
    # clear the last line and print final message
    print(Y+"\r\033[K✅ Process started...")


def validate_settings(data):
    required_keys = ["owner_number", "owner_password", "member1_number", "member2_number", "member2_password", "total_attempts"]
    if not isinstance(data, dict):
        return False
    for key in required_keys:
        if key not in data:
            return False
    if not isinstance(data["total_attempts"], int) or data["total_attempts"] <= 0 or data["total_attempts"] > 20:
        return False
    return True

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            if validate_settings(data):
                return data
            else:
                print(R + "⚠️The settings format is incorrect, the input will be requested again. ")
                return None
        except Exception as e:
            print(R + f"⚠️ An error occurred while reading the settings: {e}")
            return None
    return None

def save_settings(data):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(G + f"💾 Settings saved in  {SETTINGS_FILE}")

def get_user_inputs():
    owner_number = input(Y+"Please enter the owner number: ")
    owner_password = input(Y+"Please enter the owner password: ")
    member1_number = input(Y+"Please enter the member1: ")
    member2_number = input(Y+"Please enter the member2: ")
    member2_password = input(Y+"Please enter the password member2: ")

    while True:
        try:
            total_attempts = int(input(Y+"Please enter the number of attempts: "))
            if total_attempts == 0:
                print(R+"0 attempts cannot be selected. ")
            elif total_attempts > 20:
                print(R+"The maximum number of attempts per time is 20. ⚠️")
            else:
                print(G+f"✅ {total_attempts} attempt selected .")
                break
        except ValueError:
            print(R+"⚠️ Please enter only a valid number.")

    return {
        "owner_number": owner_number,
        "owner_password": owner_password,
        "member1_number": member1_number,
        "member2_number": member2_number,
        "member2_password": member2_password,
        "total_attempts": total_attempts
    }

# ----------- تشغيل البرنامج -----------
settings = load_settings()

if settings:
    choice = input(Y + "📂Saved settings found, do you want to use them? (Y/N): ").strip().lower()
    if choice == "y":
        print(G + "✅ Settings loaded successfully. ")
        owner_number = settings["owner_number"]
        owner_password = settings["owner_password"]
        member1_number = settings["member1_number"]
        member2_number = settings["member2_number"]
        member2_password = settings["member2_password"]
        total_attempts = settings["total_attempts"]
    else:
        settings = get_user_inputs()
        owner_number = settings["owner_number"]
        owner_password = settings["owner_password"]
        member1_number = settings["member1_number"]
        member2_number = settings["member2_number"]
        member2_password = settings["member2_password"]
        total_attempts = settings["total_attempts"]

        save_choice = input(Y + "💾Do you want to save these settings for later use? (Y/N): ").strip().lower()
        if save_choice == "y":
            save_settings(settings)
else:
    settings = get_user_inputs()
    owner_number = settings["owner_number"]
    owner_password = settings["owner_password"]
    member1_number = settings["member1_number"]
    member2_number = settings["member2_number"]
    member2_password = settings["member2_password"]
    total_attempts = settings["total_attempts"]

    save_choice = input(Y + "💾Do you want to save these settings for later use? (Y/N):  ").strip().lower()
    if save_choice == "y":
        save_settings(settings)

try:
	print(Y+"Logging in to your owner account ")
	url = "https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
	payload = {
  'grant_type': "password",
  'username': owner_number,
  'password': owner_password,
  'client_secret': "95fd95fb-7489-4958-8ae6-d31a525cd20a",
  'client_id': "ana-vodafone-app"
}
	headers = {
  'User-Agent': "okhttp/4.11.0",
  'Accept': "application/json, text/plain, */*",
  'Accept-Encoding': "gzip",
  'silentLogin': "false",
  'x-agent-operatingsystem': "15",
  'Accept-Language': "ar",
  'x-agent-device': "HONOR ALI-NX1",
  'x-agent-version': "2024.11.2",
  'x-agent-build': "944",
  'digitalId': "297WAW1VKE02A"
}
	response = requests.post(url, data=payload, headers=headers)
	
	if "access_token" in response.text:
		print(G+"You have successfully logged into your account. ")
		
		refresh1 = response.json()["refresh_token"]
	elif "Invalid user credentials" in response.text:
		print(R+"Error in the number or password of the owner ")
		sys.exit()
	else:
		print(R+"A connection error occurred.")
		sys.exit()
	
except:
	print(R+"A connection error occurred. ")
	sys.exit()

wait_timer(10)
try:
	print(Y+"Logging in to your individual account ")
	url = "https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
	payload = {
  'grant_type': "password",
  'username': member2_number,
  'password': member2_password,
  'client_secret': "95fd95fb-7489-4958-8ae6-d31a525cd20a",
  'client_id': "ana-vodafone-app"
}
	headers = {
  'User-Agent': "okhttp/4.11.0",
  'Accept': "application/json, text/plain, */*",
  'Accept-Encoding': "gzip",
  'silentLogin': "false",
  'x-agent-operatingsystem': "15",
  'Accept-Language': "ar",
  'x-agent-device': "HONOR ALI-NX1",
  'x-agent-version': "2024.11.2",
  'x-agent-build': "944",
  'digitalId': "297WAW1VKE02A"
}
	response = requests.post(url, data=payload, headers=headers)
	
	if "access_token" in response.text:
		print(G+"You have successfully logged into your individual account. ")
		
		refresh2 = response.json()["refresh_token"]
	elif "Invalid user credentials" in response.text:
		print(R+"Error in the individual number or password ")
		sys.exit()
	else:
		print(R+"A connection error occurred. ")
		sys.exit()
	
except:
	print(R+"A connection error occurred. ")
	sys.exit()




def Refresh_Token():
	global refresh1, jwt1
	print(Y+"Honor session is being updated....")
	try:
		url = "https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
		payload = {
  'refresh_token': refresh1,
  'grant_type': "refresh_token",
  'client_secret': "95fd95fb-7489-4958-8ae6-d31a525cd20a",
  'client_id': "ana-vodafone-app"
}
		headers = {
  'User-Agent': "okhttp/4.11.0",
  'Accept': "application/json, text/plain, */*",
  'Accept-Encoding': "gzip",
  'silentLogin': "true",
  'firstTimeLogin': "true",
  'x-agent-operatingsystem': "15",
  'Accept-Language': "ar",
  'x-agent-device': "HONOR ALI-NX1",
  'x-agent-version': "2024.11.2",
  'x-agent-build': "944",
  'digitalId': "297WAW1VKE02A",
  
  
}
		response = requests.post(url, data=payload, headers=headers)
		if "access_token" in response.text:
			print(G+"The owner session has been updated successfully. ")
			jwt1=response.json()["access_token"]
			refresh1 = response.json()["refresh_token"]
		else:
			print(R+"An unexpected error occurred while updating the session. ")
	except:
		print(R+"A connection error occurred. ")
		sys.exit()



def Refresh_Token1():
	global refresh2, jwt2
	print(Y+"Updating individual session...")
	try:
		url = "https://mobile.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token"
		payload = {
  'refresh_token': refresh2,
  'grant_type': "refresh_token",
  'client_secret': "95fd95fb-7489-4958-8ae6-d31a525cd20a",
  'client_id': "ana-vodafone-app"
}
		headers = {
  'User-Agent': "okhttp/4.11.0",
  'Accept': "application/json, text/plain, */*",
  'Accept-Encoding': "gzip",
  'silentLogin': "true",
  'firstTimeLogin': "true",
  'x-agent-operatingsystem': "15",
  'Accept-Language': "ar",
  'x-agent-device': "HONOR ALI-NX1",
  'x-agent-version': "2024.11.2",
  'x-agent-build': "944",
  'digitalId': "297WAW1VKE02A",
  
  
}
		response = requests.post(url, data=payload, headers=headers)
		if "access_token" in response.text:
			print(G+"The individual session has been updated successfully. ")
			jwt2=response.json()["access_token"]
			refresh2 = response.json()["refresh_token"]
		else:
			print(R+"An unexpected error occurred while updating the session. ")
	except:
		print(R+"A connection error occurred. ")
		sys.exit()

def Add_member():
	print(Y+"Sending an additional request")
	try:
		url = "https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"
		payload = {
  "category": [
    {
      "listHierarchyId": "PackageID",
      "value": "523"
    },
    {
      "listHierarchyId": "TemplateID",
      "value": "47"
    },
    {
      "listHierarchyId": "TierID",
      "value": "523"
    }
  ],
  "parts": {
    "characteristicsValue": {
      "characteristicsValue": [
        {
          "characteristicName": "quotaDist1",
          "type": "percentage",
          "value": "40"
        }
      ]
    },
    "member": [
      {
        "id": [
          {
            "schemeName": "MSISDN",
            "value": owner_number
          }
        ],
        "type": "Owner"
      },
      {
        "id": [
          {
            "schemeName": "MSISDN",
            "value": member2_number
          }
        ],
        "type": "Member"
      }
    ]
  },
  "type": "SendInvitation"
}
		headers = {
  'User-Agent': "okhttp/4.11.0",
  'Connection': "Keep-Alive",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'Content-Type': "application/json",
  'Authorization': f"Bearer {jwt1}",
  'api-version': "v2",
  'x-agent-operatingsystem': "15",
  'clientId': "AnaVodafoneAndroid",
  'x-agent-device': "HONOR ALI-NX1",
  'x-agent-version': "2024.11.2",
  'x-agent-build': "944",
  'msisdn': owner_number,
  'Accept-Language': "ar",
  'Content-Type': "application/json; charset=UTF-8"
}
		response = requests.post(url, data=json.dumps(payload), headers=headers)
		if "{}" in response.text:
			print(G+"The addition request has been sent successfully. ")
		else:
			print(R+"The addition request was not sent. ")
	except:
		print(R+"A connection error occurred. ")
	
		










def Change_quota():
	try:
		url = "https://web.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"
		payload = {
  "name": "FlexFamily",
  "type": "QuotaRedistribution",
  "category": [
    {
      "value": "47",
      "listHierarchyId": "TemplateID"
    },
    {
      "value": "percentage",
      "listHierarchyId": "familybehavior"
    }
  ],
  "parts": {
    "member": [
      {
        "id": [
          {
            "value": owner_number,
            "schemeName": "MSISDN"
          }
        ],
        "type": "Owner"
      },
      {
        "id": [
          {
            "value": member1_number,
            "schemeName": "MSISDN"
          }
        ],
        "type": "Member"
      }
    ],
    "characteristicsValue": {
      "characteristicsValue": [
        {
          "characteristicName": "quotaDist1",
          "value": "40",
          "type": "percentage"
        }
      ]
    }
  }
}
		headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
  'Accept': "application/json",
  'Content-Type': "application/json",
  'sec-ch-ua': "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
  'msisdn': owner_number,
  'Accept-Language': "AR",
  'sec-ch-ua-mobile': "?1",
  'Authorization': f"Bearer {jwt1}",
  'x-dtpc': "22$338290014_964h10vCCPBHMOAWUIFECSEHGUJJWRJUOJJQFKV-0e0",
  'clientId': "WebsiteConsumer",
  'sec-ch-ua-platform': "\"Android\"",
  'Origin': "https://web.vodafone.com.eg",
  'Sec-Fetch-Site': "same-origin",
  'Sec-Fetch-Mode': "cors",
  'Sec-Fetch-Dest': "empty",
  'Referer': "https://web.vodafone.com.eg/spa/familySharing/manageFamily"
}
		response = requests.patch(url, data=json.dumps(payload), headers=headers)
		if "{}" in response.text:
			print(G+"The percentage has been modified successfully. ")
		else:
			print(R+"The percentage has not been modified. ")
	except:
		print(R+"A connection error occurred. ")



def Accept_addition():
	try:
		url = "https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"
		payload = {
  "category": [
    {
      "listHierarchyId": "TemplateID",
      "value": "47"
    }
  ],
  "name": "FlexFamily",
  "parts": {
    "member": [
      {
        "id": [
          {
            "schemeName": "MSISDN",
            "value": owner_number
          }
        ],
        "type": "Owner"
      },
      {
        "id": [
          {
            "schemeName": "MSISDN",
            "value": member2_number
          }
        ],
        "type": "Member"
      }
    ]
  },
  "type": "AcceptInvitation"
}
		headers = {
  'User-Agent': "okhttp/4.11.0",
  'Connection': "Keep-Alive",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'Content-Type': "application/json",
  'api_id': "APP",
  'Authorization': f"Bearer {jwt2}",
  'api-version': "v2",
  'x-agent-operatingsystem': "15",
  'clientId': "AnaVodafoneAndroid",
  'x-agent-device': "HONOR ALI-NX1",
  'x-agent-version': "2024.11.2",
  'x-agent-build': "944",
  'msisdn': member2_number,
  'Accept-Language': "ar",
  'Content-Type': "application/json; charset=UTF-8"
}
		response = requests.patch(url, data=json.dumps(payload), headers=headers)
		if "{}" in response.text:
			print(G+"The addition request has been successfully accepted. ")
		else:
			print(R+"Sorry, your addition request was not accepted. ")
	except:
		print(R+"A connection error occurred. ")




def Delete_member():
	try:
		url = "https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup?type=Family"
		headers = {
  'User-Agent': "okhttp/4.11.0",
  'Connection': "Keep-Alive",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'Authorization': f"Bearer {jwt1}",
  'api-version': "v2",
  'x-agent-operatingsystem': "15",
  'clientId': "AnaVodafoneAndroid",
  'x-agent-device': "HONOR ALI-NX1",
  'x-agent-version': "2024.11.2",
  'x-agent-build': "944",
  'msisdn': owner_number,
  'Content-Type': "application/json",
  'Accept-Language': "ar"
}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			data = json.loads(response.text)
			number = f"2{member2_number}"
			members = data[0]["parts"]["member"]
			found = False
			for member in members:
				msisdn = member["id"][0]["value"]
				status = member["status"]
				if msisdn == number:
					found = True
					if status == "1":
						url = "https://mobile.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"
						payload = {
  "category": [
    {
      "listHierarchyId": "TemplateID",
      "value": "47"
    }
  ],
  "createdBy": {
    "value": "MobileApp"
  },
  "parts": {
    "characteristicsValue": {
      "characteristicsValue": [
        {
          "characteristicName": "Disconnect",
          "value": "0"
        },
        {
          "characteristicName": "LastMemberDeletion",
          "value": "1"
        }
      ]
    },
    "member": [
      {
        "id": [
          {
            "schemeName": "MSISDN",
            "value": owner_number
          }
        ],
        "type": "Owner"
      },
      {
        "id": [
          {
            "schemeName": "MSISDN",
            "value": member2_number
          }
        ],
        "type": "Member"
      }
    ]
  },
  "type": "FamilyRemoveMember"
}
						headers = {
  'User-Agent': "okhttp/4.11.0",
  'Connection': "Keep-Alive",
  'Accept': "application/json",
  'Accept-Encoding': "gzip",
  'Content-Type': "application/json",
  'Authorization': f"Bearer {jwt1}",
  'api-version': "v2",
  'x-agent-operatingsystem': "15",
  'clientId': "AnaVodafoneAndroid",
  'x-agent-device': "HONOR ALI-NX1",
  'x-agent-version': "2024.11.2",
  'x-agent-build': "944",
  'msisdn': owner_number,
  'Accept-Language': "ar",
  'Content-Type': "application/json; charset=UTF-8"
}
						response = requests.patch(url, data=json.dumps(payload), headers=headers)
						if "{}" in response.text:
							print(G+"The individual has been successfully deleted. ")
						else:
							print(R+"Sorry, failed to delete the individual. ")
							
					
					
						break
			if not found:
						print(R+f"❌The number {number} is not present in the family ")
		else:
			print(R+"An error occurred while deleting the individual. ")
	
	except:
		print(R+"A connection error occurred. ")




def Change_quota1():
	try:
		url = "https://web.vodafone.com.eg/services/dxl/cg/customerGroupAPI/customerGroup"
		payload = {
  "name": "FlexFamily",
  "type": "QuotaRedistribution",
  "category": [
    {
      "value": "47",
      "listHierarchyId": "TemplateID"
    },
    {
      "value": "percentage",
      "listHierarchyId": "familybehavior"
    }
  ],
  "parts": {
    "member": [
      {
        "id": [
          {
            "value": owner_number,
            "schemeName": "MSISDN"
          }
        ],
        "type": "Owner"
      },
      {
        "id": [
          {
            "value": member1_number,
            "schemeName": "MSISDN"
          }
        ],
        "type": "Member"
      }
    ],
    "characteristicsValue": {
      "characteristicsValue": [
        {
          "characteristicName": "quotaDist1",
          "value": "10",
          "type": "percentage"
        }
      ]
    }
  }
}
		headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
  'Accept': "application/json",
  'Content-Type': "application/json",
  'sec-ch-ua': "\"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
  'msisdn': owner_number,
  'Accept-Language': "AR",
  'sec-ch-ua-mobile': "?1",
  'Authorization': f"Bearer {jwt1}",
  'x-dtpc': "22$338290014_964h10vCCPBHMOAWUIFECSEHGUJJWRJUOJJQFKV-0e0",
  'clientId': "WebsiteConsumer",
  'sec-ch-ua-platform': "\"Android\"",
  'Origin': "https://web.vodafone.com.eg",
  'Sec-Fetch-Site': "same-origin",
  'Sec-Fetch-Mode': "cors",
  'Sec-Fetch-Dest': "empty",
  'Referer': "https://web.vodafone.com.eg/spa/familySharing/manageFamily"
}
		response = requests.patch(url, data=json.dumps(payload), headers=headers)
		if "{}" in response.text:
			print(G+"The percentage has been modified successfully. ")
		else:
			print(R+"The percentage has not been modified. ")
	except:
		print(R+"A connection error occurred. ")




def Get_flixes():
	try:
		url2 = f'https://web.vodafone.com.eg/services/dxl/usage/usageConsumptionReport?bucket.product.publicIdentifier={owner_number}&@type=aggregated'
		headers2 = {
        'channel': 'MOBILE',
        'useCase': 'Promo',
        'Authorization': f'Bearer {jwt1}',
        'api-version': 'v2',
        'x-agent-operatingsystem': '11',
        'clientId': 'AnaVodafoneAndroid',
        'x-agent-device': 'OPPO CPH2059',
        'x-agent-version': '2024.3.3',
        'x-agent-build': '593',
        'msisdn': owner_number,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Accept-Language': 'ar',
        'Host': 'web.vodafone.com.eg',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.11.0'
    }
		r2 = requests.get(url2, headers=headers2)
		pattern = r'"usageType":"limit","bucketBalance":\[\{"remainingValue":\{"amount":(.*?),"units":"FLEX"'
		match = re.search(pattern, r2.text)
		if match:
			flex = int(float(match.group(1)))
			if flex == 0:
				print(G+"Number of flexes over 30,000 ")
			else:
				print(G+f"Your flex count is: {flex} ")
		else:
			print(R+"The number of flexes was not found. ")
			
		
		
		
		
		
		
		
	except:
		print(R+"A connection error occurred. ")







def main():
    for attempt in range(total_attempts):
        print(Y + f"🔄 Attempt number {attempt+1} of {total_attempts} ")
        
        thread1 = threading.Thread(target=Refresh_Token)
        thread1.start()
        thread1.join()
        wait_timer(10)
        thread2 = threading.Thread(target=Refresh_Token1)
        thread2.start()
        thread2.join()
        wait_timer(10)
        
        thread3 = threading.Thread(target=Add_member)
        thread3.start()
        thread3.join()
        wait_timer(10)
        
        thread4 = threading.Thread(target=Change_quota)
        thread5 = threading.Thread(target=Accept_addition)
        thread4.start()
        thread5.start()
        thread5.join()
        thread4.join()
        wait_timer(10)
        
        
        thread6 = threading.Thread(target=Get_flixes)
        thread6.start()
        thread6.join()
        wait_timer(10)
        
        thread7 = threading.Thread(target=Delete_member)
        thread7.start()
        thread7.join()
        wait_timer(300)
        
        thread7 = threading.Thread(target=Change_quota1)
        thread7.start()
        thread7.join()
        wait_timer(300)
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    main()
