import platform
import os

# if platform.system() == "Windows":
#    raise Exception("""Oops, we won't be able to install the application on windows""")

with os.popen("whoami") as current_user:
    if current_user != "root":
        raise Exception("Please login into root first")

package_name = "libpam-google-authenticator"
print(f"Installing {package_name}...")
os.system(f"sudo apt update && sudo apt install {package_name}")

base_path = "etc/"
print(f"Writing to {base_path}pam.d/sshd")
with os.popen(f"{base_path}pam.d/sshd", "a") as ssh_file:
    ssh_file.write("auth required pam_google_authenticator.so")

