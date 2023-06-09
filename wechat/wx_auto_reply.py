import time
import pyautogui
import pyperclip

try:
    # 切换对话框到文件传输助手
    pos_search = pyautogui.locateOnScreen('./search.png')
    pyautogui.click(pos_search)
    pyperclip.copy('文件传输助手')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')

    while True:
        pos = pyautogui.locateOnScreen('./chat-dot0.png')
        if pos is not None:
            print("Start : %s" % time.ctime())
            time.sleep(1)
            print("End : %s" % time.ctime())
            continue
        else:
            for i in range(1, 10):
                pos = pyautogui.locateOnScreen('./chat-dot' + str(i) + '.png')
                if pos is not None:
                    # 双击未读消息
                    center = pyautogui.center(pos)
                    pyautogui.doubleClick(center)
                    # 打开到第一个未读消息对话框
                    pyautogui.moveRel(60, -20)
                    pyautogui.click()
                    # 回复消息
                    msg = '自动回复测试！！！'
                    pyperclip.copy(msg)
                    pyautogui.hotkey('ctrl', 'v')
                    pyautogui.press('enter')

                    # 切换对话框到文件传输助手
                    pos_search = pyautogui.locateOnScreen('./search.png')
                    pyautogui.click(pos_search)
                    pyperclip.copy('文件传输助手')
                    pyautogui.hotkey('ctrl', 'v')
                    pyautogui.press('enter')
                    time.sleep(0.5)
                    pyautogui.press('enter')
                    break
except KeyboardInterrupt:
    print('\n')
