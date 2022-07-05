import requests,bs4,json,os,sys,random,datetime,time,re

def chk():

  uuid = str(os.geteuid()) + str(os.getlogin()) 

  id = "|".join(uuid)

  print("\n\n\x1b[37;1m  YOUR ID : \033[94m"+id) 

  try: 

    httpCaht = requests.get("https://raw.githubusercontent.com/br5kly/test/main/subc.json").text 

    if id in httpCaht: 

      print("\033[92m  ﻞﻌﻔﻣ ﻱﺩ ﻱﻷﺍ. .......\033[97m") 

      msg = str(os.geteuid()) 

      time.sleep(1) 

      pass 

    else: 

      print("\033[0;96m   ﻡﺍﺮﻐﻠﻴﺗ ﻪﺘﻌﺑﺍﻭ ﻚﻳﺪﻳﺍ ﺦﺴﻧﺍ  ﻞﻌﻔﻣ ﺮﻴﻏ ﻚﻳﺩ ﻱﺍ BR3K  \033[0;91m#ﻲﻧﺎﺠﻣ ﺲﻴﻟ!!!") 

      os.system('xdg-open  https://t.me/sxtz0*')

      time.sleep(1) 

      sys.exit() 

  except: 

    sys.exit() 

    if name == '_main_': 

     print (logo)

     chk() 

     

chk()



start = int(input("Enter the number you want me to start counting in: "))
end = int(input("Enter the number you want me to end in:  "))


while start < end:
    start += 1
    print(start)


input(" Zeyad Alabany..")
