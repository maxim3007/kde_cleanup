import os
import subprocess as sb

package_man = ""

if os.path.exists('/var/lib/dpkg/'):
    print("Detected apt package manager!")
    package_man = "apt"
elif os.path.exists('/var/lib/pacman/'):
    print("Detected pacman package manager!")
    package_man = "pacman"
else:
    print('Unknown package manager')
    quit()

if os.geteuid() != 0:
    print("you MUST run this script as root!")
    quit()

kde_games = ["kanagram", "bomber", "granatier", "kapman", "kblocks", "kbounce", "kbreakout", "kgoldrunner", "kolf", "kollision", "ksnakeduel", "kspaceduel", "atlantik", "bovo", "kajongg", "kblackbox", "kfourinline", "kigo", "kiriki", "kmahjongg", "knights", "kreversi", "kshisen", "ksquares", "blinken", "katomic", "kdiamond", "khangman", "killbots", "klickety", "kmines", "knetwalk", "konquest", "ksirk", "ksudoku", "lskat", "palapeli", "picmi"]

def removepkg(name):
    if package_man == "apt":
        cmd = f"apt remove -y {name}"
    else:
        cmd = f"pacman -Rs {name} --noconfirm"
    proc = sb.Popen(cmd, shell=True)
    proc.wait()
    if proc.returncode == 0:
        print(f"removed {pkg}")
    else:
        print(f"{package_man} exited with non-zero code!")

for pkg in kde_games:
    confirmation = input(f"Would you like to remove {pkg} (y/n): ").lower()
    if confirmation.startswith("y"):
        print(f"removing {pkg}")
        removepkg(pkg)
    else:
        print(f"skipped {pkg}")

print("exiting")

