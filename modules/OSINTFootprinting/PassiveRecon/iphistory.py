#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


from core.methods.tor import session
from bs4 import *
import time
import lxml
import urllib3
import json
from core.Core.colors import *

info = "Display the history of the target's IP."
searchinfo = "IP History lookup"
properties = {}

def iphistory(web):
    requests = session()
    try:
        #print(R+'\n    =====================')
        #print(R+'     I P   H I S T O R Y')
        #print(R+'    =====================\n')
        from core.methods.print import posintpas
        posintpas("ip history")
        print(GR+' [*] Parsing Url...')
        web0 = web.split('//')[-1]
        if "@" in web0:
            web0 = web0.split("@")[1]

        print(web0)

        print(C+' [!] Making the request...')
        html = requests.get('http://viewdns.info/iphistory/?domain=' + web0).text
        print(GR+' [*] Parsing raw-data...')
        time.sleep(0.7)
        soup = BeautifulSoup(html,'lxml')
        print(C+' [!] Setting parameters...')
        table = soup.findAll('table', attrs={'border':'1'})[0]
        print(C+' [!] Finding IP history instances...')
        trs = table.findAll('tr')
        trs.pop(0)

        print(C+'\n [+] Following instances were found...')

        for tr in trs:
            td = tr.findAll('td')
            info = {'ip' : td[0].text, 'owner' : td[2].text.rstrip(), 'last' : td[3].text}
            print(O+' [+] Instance :' +C+color.TR3+C+G+ info['ip'] + ' => ' + info['owner'] + ' - (' + info['last'] + ')'+C+color.TR2+C)
            time.sleep(0.02)

    except:
        print(R+' [-] No instances of IP History found...')

def attack(web):
    iphistory(web)