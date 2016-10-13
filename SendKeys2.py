#encoding:utf-8
from ctypes import *
import time
import win32con
import win32api
import win32ui

#Structure for a keycode input
class KeyBdInput(Structure):
    _fields_ = [
            ("wVk",c_ushort),
            ("wScan",c_ushort),
            ("dwFlags",c_ulong),
            ("time",c_ulong),
            ("dwExtraInfo",POINTER(c_ulong))
            ]
#dwFlags can be certain combinations of the following values
KEYEVENTF_EXTENDEDKEY = 0x0001  #If specified, the scan code was preceded by a prefix byte that has the value 0xE0 (224).
KEYEVENTF_KEYUP = 0x0002  #If specified, the key is being released. If not specified, #the key is being pressed.
KEYEVENTF_SCANCODE = 0x0008 #If specified, wScan identifies the key and wVk is ignored. 
KEYEVENTF_UNICODE = 0x0004  #If specified, the system synthesizes a VK_PACKET keystroke. The wVk parameter must be zero. This flag can only be combined with the KEYEVENTF_KEYUP flag.


#remark:
#dwFalgs default set 0 .
#when  1 >= keycode <= 254  set wVk = keycode and set wScan = 0
#when  keycode>254(unicode) set wScan = keycode and set wVk = 0 
#      and set dwFlags |= KEYEVENTF_UNICODE 
# 
class HardwareInput(Structure):
        _fields_ = [("uMsg", c_ulong),("wParamL", c_short),("wParamH", c_ushort)]

class MouseInput(Structure):
        _fields_ = [("dx", c_long),("dy", c_long),("mouseData", c_ulong),("dwFlags", c_ulong),("time",c_ulong),("dwExtraInfo", POINTER(c_ulong))]

class Union_Input(Union):
        _fields_ = [("ki", KeyBdInput),("mi", MouseInput),("hi", HardwareInput)]

class Input(Structure):
    _fields_=[
            ("type",c_ulong),
            ("ui",Union_Input)
            ]
#type can be one of the following value
INPUT_MOUSE = 0  #The event is a mouse event. Use the mi structure of the union.
INPUT_KEYBOARD = 1 #The event is a keyboard event. Use the ki structure of the union.
INPUT_HARDWARE = 2 #The event is a hardware event. Use the hi structure of the union.




def send_key_event(keyCode,isKeyup):

    Inputs = Input * 1
    inputs = Inputs()

    inputs[0].type = INPUT_KEYBOARD
    inputs[0].ui.ki.wVk = keyCode
    if isKeyup == True:
        inputs[0].ui.ki.dwFlags = KEYEVENTF_KEYUP
    windll.user32.SendInput(1, pointer(inputs), sizeof(inputs[0]))
    win32api.Sleep(3)

def KeyDown(keyCode):
    send_key_event(keyCode,False)

def KeyUp(keyCode):
    send_key_event(keyCode,True)


#char in 1~255 key press
def KeyPress(keyCode,isShift):
    if isShift == True:
        send_key_event(win32con.VK_SHIFT,False)
    send_key_event(keyCode,False)
    send_key_event(keyCode,True)
    if isShift == True:
        send_key_event(win32con.VK_SHIFT,True)


#unicode char key press
def UniKeyPress(keyCode):
    Inputs = Input * 2
    inputs = Inputs()

    inputs[0].type = INPUT_KEYBOARD
    inputs[0].ui.ki.wVk = 0
    inputs[0].ui.ki.wScan = keyCode
    inputs[0].ui.ki.dwFlags = KEYEVENTF_UNICODE

    inputs[1].type = INPUT_KEYBOARD
    inputs[1].ui.ki.wVk = 0
    inputs[1].ui.ki.wScan = keyCode
    inputs[1].ui.ki.dwFlags = KEYEVENTF_UNICODE | KEYEVENTF_KEYUP
    windll.user32.SendInput(2, pointer(inputs), sizeof(inputs[0]))
    win32api.Sleep(5)

def SendString(Keys):
    for c in Keys:
        cC = ord(c)
        if cC>=0 and cC<256:
            vk = win32api.VkKeyScan(c)
            if vk == -1:
                UniKeyPress(cC)
            else:
                if vk < 0:
                    vk = ~vk + 0x1
                shift = ( vk >> 8 & 0x1  == 0x1 )
                if win32api.GetKeyState(win32con.VK_CAPITAL) & 0x1 == 0x1:
                    if ( c >= 'a' and c <= 'z' ) or ( c >= 'A' and c <= 'Z' ):
                        shift = not shift
                KeyPress(vk & 0xFF , shift)
        else:
            UniKeyPress(cC)