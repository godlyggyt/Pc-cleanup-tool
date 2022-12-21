import os
import subprocess

def cleanup():
    # Delete temporary files
    temp_dir = os.environ['TEMP']
    subprocess.run(f"rd /s /q {temp_dir}", shell=True)
    
    # Uninstall unnecessary programs
    subprocess.run("wmic product where name='Program 1' call uninstall", shell=True)
    subprocess.run("wmic product where name='Program 2' call uninstall", shell=True)
    
    # Free up disk space
    subprocess.run("cleanmgr /sagerun:1", shell=True)

if __name__ == "__main__":
    cleanup()
