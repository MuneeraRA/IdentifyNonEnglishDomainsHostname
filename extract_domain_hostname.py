# Created on Wed Oct 19 04:57:12 2019
# @author: Muneerah
# Extract Age From Cluster Stat
#  
#===================================#

import glob
import os
import json
import ntpath
import hashlib
import json
import collections
import time
import re


#  TLD without stars
PSL_PATH = "/Users/imanory/Desktop/ArabicDomainsIdentification/PSLNP" #ChangePath
PSL_list = {}
with open(PSL_PATH) as f:  
    for line in f:
            line = line.replace("\n", "")
            PSL_list[line] = line
    f.close()

#  TLD with stars
PSLS_PATH = "/Users/imanory/Desktop/ArabicDomainsIdentification/PSLSNP" #ChangePath
PSLS_list = {}
with open(PSLS_PATH) as f:  
    for line in f:
            line = line.replace("\n", "")
            PSLS_list[line] = line
    f.close()


def FindApex(NS,TLD):
    try:
        if(TLD == NS):
            return NS
        TLDIndex = NS.rfind(TLD)
        RemoveTLD = NS[:TLDIndex][:-1]
        IndexDot = RemoveTLD.rfind(".")
        return NS[IndexDot+1:]
    except:
        print("error")

def FindApexPrivateTLD(NS,TLD):
    try:
        if(TLD == NS):
            return NS
        TLDIndex = NS.rfind(TLD)
        RemoveTLD = NS[:TLDIndex][:-1]
        IndexDot = RemoveTLD.rfind(".")
        StarRemove = NS[:IndexDot][:-1]
        StarDot = StarRemove.rfind(".")
        return NS[StarDot+1:]
    except:
        print("error")


def getHostName(domain):
    if (not domain.endswith('.')):
        domain = domain + '.'
    if(domain.endswith(".") == False):
        if(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])', domain) and domain.count(".") == 4):  
            return "IPv4"
        elif(re.match(r'^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))', domain) and domain.count(".") == 1):
            return "IPv6"
    else:
        CountDot = domain.count(".")
        InTLD = False
        DomainApex = ""
        TLD = ""
        for i in range(CountDot):
            Check = ".".join(domain.split(".",i)[i:])
            TLD = PSLS_list.get(Check,None)
            if(TLD != None):
                DomainApex = FindApexPrivateTLD(domain,TLD)
                InTLD = True
                return DomainApex[:DomainApex.index(TLD)]
        if(InTLD == False):                        
            for i in range(CountDot):
                Check = ".".join(domain.split(".",i)[i:])
                TLD = PSL_list.get(Check,None)
                if(TLD != None):
                    DomainApex = FindApex(domain,TLD)
                    InTLD = True
                    return DomainApex[:DomainApex.index(TLD)]
    if(InTLD == False):
        return domain
