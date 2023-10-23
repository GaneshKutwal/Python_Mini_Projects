import psutil
from plyer import notification
import time
import os

flag = True

def pluged_in_fun(percent):
   
    notification.notify(
        title="Battery Percentage",
        app_icon = "D:\\Status-battery-charging.ico",
        message=str(percent)+"% Battery charged",
        timeout=10
    )

def noty_after_95(percent):
    current_path = os.getcwd()
    img_path = os.path.join(current_path,"Status-battery-charging.ico")
   
    notification.notify(
        title="Battery Percentage",
        app_icon = img_path,
        message=str(percent)+"% Battery charged,plz remove plug",
        timeout=10
    )
        

while 1:
    battery = psutil.sensors_battery()
    percent = battery.percent
    plug_in = battery.power_plugged

    
    if plug_in == False:
        flag = True
  
    if flag == plug_in:
        pluged_in_fun(percent)
        flag = False
    
    if percent >= 95 and plug_in == True:
        noty_after_95(percent)



    time.sleep(60)

