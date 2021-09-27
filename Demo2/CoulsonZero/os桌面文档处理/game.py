import win32gui
def get_window_info():
    wdname = u'传奇商店：经营与打造'
    handle = win32gui.FindWindow(0, wdname)
    if handle == 0:
        return None
    else:
        return win32gui.GetWindowRect(handle)
    
