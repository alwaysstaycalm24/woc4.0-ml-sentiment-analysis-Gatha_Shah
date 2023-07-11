import subprocess


def calculator():
    subprocess.Popen("C:\Windows\System32\calc.exe")


def character_map():
    subprocess.Popen("C:\Windows\System32\charmap.exe")


def cmd():
    subprocess.Popen("C:\Windows\System32\cmd.exe")


def console():
    subprocess.Popen("C:\Windows\System32\conhost.exe")


def control_panel():
    subprocess.Popen("C:\Windows\System32\control.exe")


def paint():
    subprocess.Popen("C:\Windows\System32\mspaint.exe")


def notepad():
    subprocess.Popen(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad.lnk")


def taskmanager():
    subprocess.Popen("C:\Windows\System32\Taskmgr.exe")


def androidstudio():
    subprocess.Popen("C:\ProgramFiles\Android\AndroidStudio\bin\studio64.exe")
