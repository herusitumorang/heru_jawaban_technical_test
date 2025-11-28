#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re

# Message Alert A dan B
message_a = """
<b>SQL Monitoring Alert:</b>
Time : 2/12/2024 4:15:53 PM
Alert ID : 202421216155315

TGR-PRD-BWRECDB(101.200.15.123,1444) : [High]Blocked process expectancy is under 1secs ( Current: 0.00 )

Please follow up immediately !!!
"""

message_b = """
<b>SQL Monitoring Alert:</b>
Time : 2/11/2024 9:45:38 PM
Alert ID : 20242112145385

TGR-PRD-CRMDB(103.143.15.205) : [High]Blocking Session(s) are running over 300 seconds. ( Current Max(sec): 1,227.00 )

Please follow up immediately !!!
"""

def cek_tipe_alert(pesan):
    if re.search(r'blocked process|blocking session', pesan, re.IGNORECASE):
        if re.search(r'\(\d{1,3}(?:\.\d{1,3}){3},\d+\)', pesan):
            return "Alert A"
        elif re.search(r'\(\d{1,3}(?:\.\d{1,3}){3}\)', pesan):
            return "Alert B"
    return "Tidak diketahui"

print("Message A →", cek_tipe_alert(message_a))  # Harus keluar output "Alert A"
print("Message B →", cek_tipe_alert(message_b))  # Harus keluar output "Alert B"


# In[ ]:




