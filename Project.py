
import ctypes
import platform
import socket

import GPUtil
import psutil
import requests
import speedtest
import wmi
from windows_tools.installed_software import get_installed_software

print("1. All installed software's list: ")
for software in get_installed_software():
    print(software['name'], software['version'], software['publisher'])
    
    


def get_internet_speed():
    # Measure internet speed
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    return download_speed, upload_speed


print("2. InterNet speed")

internet_speed = get_internet_speed()
print(f" Download Speed: {internet_speed[0]:.2f} Mbps")
print(f" Upload Speed: {internet_speed[1]:.2f} Mbps")



from screeninfo import get_monitors

print("3. Screen resolution: ")


user32 = ctypes.windll.user32

def get_system_info():
    # Fetch system information using WMI (Windows Management Instrumentation)
    w = wmi.WMI()
    system_info = w.Win32_ComputerSystem()[0]
    screen_resolution = f"{getattr(system_info, 'ScreenWidth',user32.GetSystemMetrics(0))}x{getattr(system_info, 'ScreenHeight',user32.GetSystemMetrics(1))}"
    
    return {
        '- screen_resolution': screen_resolution,
    }
print(get_system_info())



print("4. Cpu model : " + platform.processor())


print(f'5. No of core and thread :  {psutil.cpu_count()}, {psutil.cpu_count(logical=False)}')


print(f'6.  GPU Model:  {GPUtil.getAvailable()}') # null in case of no GPU available in PC


print(f'7. RAM size of pc:   {psutil.virtual_memory().total } Bytes') 

#Screen size
for m in get_monitors():
    print("8. Screen size: "+str(m))

#Python Program to Get IP Address

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("9. Wifi Address is:" + IPAddr)



#public Ip address




def get_public_ip():
    response = requests.get('https://api.ipify.org').text
    return response

while True:
    public_ip = get_public_ip()
    print(f'10. Public IP Address: {public_ip}')
    break


#Windows version


print(f'11. Windows version:  {platform.platform()}' )


 
