from codecs import Codec


Codec: https://github.com/ELFBAR/Spyrod-v2
# License:  MPL-2.0 license

import requests, json # type: ignore
import os
import time
from platform import system

class Colors:
    red="\033[31;1m]


os.system("clear")
logo = Colors.red+ '''
             uu$:$:$:$:$:$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
         u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$*   *$$$*   *$$$$$$u
       *$$$$*      u$u       $$$$*
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         *$$$$uu$$$   $$$uu$$$$*
          *$$$$$$$*   *$$$$$$$*
            u$$$$$$$u$$$$$$$u
             u$*$*$*$*$*$*$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$u$u$u$u$u$$       u$$$$
  $$$$$uu      *$$$$$$$$$*     uu$$$$$$
u$$$$$$$$$$$      *****    uuuu$$$$$$$$$
$$$$***$$$$$$$$$$uuu   uu$$$$$$$$$***$$$*
 ***      **$$$$$$$$$$$uu **$***
          uuuu **$$$$$$$$$$uuu
 u$$$uuu$$$$$$$$$uu **$$$$$$$$$$$uuu$$$
 $$$$$$$$$$****           **$$$$$$$$$$$*
   *$$$$$*                      **$$$$**
     $$$*    ___________________  $$$$*
            |Made by: ELFBAR    |
            |___________________|
            | Spyrod Version: v5|
            |___________________|
     
     '''  

try:
  print (logo)
  print ('[~] Write the victim's IP')
  ip = input('[~] IP: ')
  print(f'[~] Searching for data from: {ip}')
  time.sleep(2)
  api = f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone, offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=es"

  data = requests.get(api).json()
  ##-----------Query---------##
  print("\n[~] [Victim's IP]:", data['query'])
  ##--------------ISP----------##
  print("[~] [ISP] :", data['isp'])
  if data['isp'] == False:
    print('[~] [ISP not found!]')
  ##------------Org-----------##
  print("[~] [Organization]:", data['org'])
  if data['org'] == False:
    print('[~] [Organization not found!]')
  ##-----------City------------##
  print("[~] [City]:", data['city'])
  if data['city'] == False:
    print('[~] [City not found!]')
  ##-----------Country-------------##
  print("[~] [Country name]:", data['country'])
  if data['country'] == False:
    print('[~] [Country name not found!]'
##----------Region-------##
  print("[~] [Region]:", data['region'])
  if data['region'] == False:
    print('[~] [Region not found!]')
  ##---------Continent name---##
  print("[~] [Continent name]:", data['continent'])
  if data['country'] == False:
    print('[~] [Continent name not found!]')
  #-----------Region/State-------##
  print("[~] [Region/state]:", data['regionName'])
  if data['regionName'] == False:
    print('[~] [Region / State not found!]')
  ##----------2 letters continent##---##
  print("[~] [Two-letter continent code]:", data['continentCode'])
  if data['country'] == False:
    print('[~] [Two-letter continent code not found!]')
  #---Latitude----##
  print("[~] [Latitude]:", data['lat'])
  if data['lat'] == False:
    print('[~] [Latitude not found!]')
  ##----------Length------##
  print("[~] [Length]:", data['lon'])
  if data['lon'] == False:
    print('[~] [Length not found!]')
  ##--------------Timezone---------##
  print("[~] [Timezone]:", data['timezone'])
  if data['timezone'] == False:
    print('[~] [Time zone not found!]')
  ##-------------- ZIP--------------##
  print("[~] [Zip code]:", data['zip'])
  if data['zip'] == False:
    print('[~] [Zip code not found!]')
  ##------------ AS -------------------##
  print("[~] [AS number and organization]:", data['as'])
  if data['as'] == False:
    print('[~] [AS number and organization not found!]')
  ##-----------Countrycode-----##
  print("[~] [Two-letter country code]:", data['countryCode'])
  if data['countryCode'] == False:
    print('[~] [Two-letter country code not found!]')
  ##-----------Reverse IP---------##
  print("[~] [IP Reverse DNS]: ", data['reverse'])
  if data['reverse'] == False:
    print('[~] [IP Reverse DNS!]')
  ##--------------Mobile------##
  print("[~] [Mobile connection (cellular)]:", data['mobile'])
  if data['mobile'] == False:
    print('[~] [Mobile connection not found!]')
  ##----currency----##
  print('[~] [National currency]:', data['currency'])
  if data['currency'] == False:
    print('[~] [National currency not found!]')
  #-----district----#
  print('[~] [District (city subdivision)]:', data['district'])
  if data['district'] == False:
    print('[~] [District not found!]')
  #-------Proxy-----#
  print('[~] [Proxy, VPN or Tor]:', data['proxy'])
  if data['proxy'] == False:
    print('[~] [Proxy, VPN or Tor not found!]')

exceptKeyboardInterrupt:
        print('\nExiting the program...')
        time.sleep(1)
        local coreGui = game:GetService("CoreGui")
End ()
