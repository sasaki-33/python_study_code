#関数の呼出し
import pyautogui

#この画面を伏せる
pyautogui.moveTo(1749,33)
pyautogui.click()

#シークレットタブを開く
pyautogui.hotkey('ctrlleft','altleft','c')
pyautogui.sleep(5)

#日本語入力に変換し、YouTubeを打ち込み検索
pyautogui.hotkey('ctrlleft','capslock')
pyautogui.typewrite('yu-tyu-bu')
pyautogui.press('space')
pyautogui.press('enter')
pyautogui.press('enter')

#サイズを最大化
pyautogui.hotkey('winleft','up')
pyautogui.sleep(3)

#YouTubeサイトを開く
pyautogui.moveTo(320,410)
pyautogui.click()
pyautogui.sleep(5)

#ログインを行う。
pyautogui.moveTo(1780,140)
pyautogui.click()
pyautogui.sleep(3)

#カーソルを合わせ、IDを表示させ、クリック
pyautogui.moveTo(1000,490)
pyautogui.click()
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.sleep(5)

#パスワードを打ち込みログイン
pyautogui.typewrite('パスワード')
pyautogui.press('enter')