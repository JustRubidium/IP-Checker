import subprocess
import time
import colorama

colorama.init(autoreset=False)

print(colorama.Fore.GREEN + "--- IP Checker ---")
hedef_ip = input(colorama.Fore.WHITE + "Enter a IP adress: ")

print(
    f"\n[+] Watching {hedef_ip} . If you wanna stop press"
    " Ctrl + C \n"
)

while True:
  try:
    process = subprocess.Popen(
        ["netstat", "-an"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    baglanti_var_mi = False

    for line in process.stdout:
      if hedef_ip in line:
        print(colorama.Fore.GREEN + f"[!] [FLOW] Connection: {line.strip()}")
        baglanti_var_mi = True

        time.sleep(0.3)

    if not baglanti_var_mi:
      time.sleep(1)

  except KeyboardInterrupt:
    exit()

  except Exception as e:
    print(colorama.Fore.RED + f"Error: {e}")
    break

#JSTRBDM2
