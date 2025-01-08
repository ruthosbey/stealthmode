import os
import ctypes
import subprocess
import shutil

def clear_recent_files():
    try:
        recent_folder = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Recent')
        for file in os.listdir(recent_folder):
            file_path = os.path.join(recent_folder, file)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        print("Recent files cleared.")
    except Exception as e:
        print(f"Error clearing recent files: {e}")

def disable_file_sharing():
    try:
        subprocess.run(['net', 'share', 'C$', '/delete'], check=True)
        subprocess.run(['net', 'share', 'ADMIN$', '/delete'], check=True)
        print("File sharing disabled.")
    except subprocess.CalledProcessError as e:
        print(f"Error disabling file sharing: {e}")

def disable_remote_assistance():
    try:
        key = r'SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services'
        reg_value = 0x00000000
        with ctypes.windll.advapi32.RegOpenKeyExW(ctypes.windll.advapi32.HKEY_LOCAL_MACHINE, key, 0, ctypes.windll.advapi32.KEY_SET_VALUE) as hkey:
            ctypes.windll.advapi32.RegSetValueExW(hkey, 'fAllowToGetHelp', 0, 4, ctypes.byref(ctypes.c_ulong(reg_value)), 4)
        print("Remote assistance disabled.")
    except Exception as e:
        print(f"Error disabling remote assistance: {e}")

def clear_temp_files():
    try:
        temp_folder = os.environ.get('TEMP', '')
        shutil.rmtree(temp_folder, ignore_errors=True)
        os.makedirs(temp_folder, exist_ok=True)
        print("Temporary files cleared.")
    except Exception as e:
        print(f"Error clearing temporary files: {e}")

def enable_stealth_mode():
    clear_recent_files()
    disable_file_sharing()
    disable_remote_assistance()
    clear_temp_files()
    print("Stealth mode enabled.")

if __name__ == '__main__':
    enable_stealth_mode()