import subprocess

def open_resolve():
    app_path = "/Applications/DaVinci Resolve/DaVinci Resolve.app"
    subprocess.Popen(["open", app_path])  # doesn't block

if __name__=="__main__":
    open_resolve()
