import pyautogui
import time
import keyboard
def ss ():
    captura_de_ecran = pyautogui.screenshot()
    captura_de_ecran.save('captura_de_ecran.png')
def cautare_google():
    if (pyautogui.locateOnScreen(r"search_bar.png")!=None):
        camp_google = pyautogui.locateOnScreen(r"search_bar.png")
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write("https://www.youtube.com/@DanCadar")
        pyautogui.press('enter')
        time.sleep(2)
        click_video()
        click_videoclip()
        click_subscribe()
def click_video():
    pyautogui.click(1794,545)
    time.sleep(1)
    pyautogui.scroll(-100)
def click_videoclip():
    time.sleep(2)
    pyautogui.click(1710,894)
def afisare_coordonate():
    while not keyboard.is_pressed('z'):
        print( pyautogui.position() )
        time.sleep(0.1)
def click_subscribe():
    time.sleep(1.5)
    pyautogui.click(1734, 625)
#afisare_coordonate()
cautare_google()
<https://teams.microsoft.com/l/message/19:Q-RhBgotadHrG4g304vdXTdXnvR2ZXBM1Z0NiVKl91k1@thread.tacv2/1729864331197?tenantId=69928ae8-265d-4c4c-b0fc-a6d50a791779&amp;groupId=8272d0f7-0f7a-403a-9b95-01253402e5e7&amp;parentMessageId=1729863901955&amp;teamName=[FR] MAP - SGR 1&amp;channelName=General&amp;createdTime=1729864331197&amp;allowXTenantAccess=false>