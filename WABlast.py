import pywhatkit as pwt
import pyautogui
import time



caption = """

caption in here 

"""

 
#mode safe --> 1 Per minute
number = ['+628xxxxxxxxxx','+628xxxxxxxxxx','+628xxxxxxxxxx','+628xxxxxxxxxx']
for i in range(len(number)):
    try:
        pwt.sendwhats_image(number[i], 'image.png',caption=caption, wait_time=30)
        time.sleep(7)
        pyautogui.click(x=1292, y=806)
        pyautogui.press('enter')
        time.sleep(7)
        pyautogui.hotkey('ctrl','w')
        print(i)
    except:
        print('eror')
        print(i)
