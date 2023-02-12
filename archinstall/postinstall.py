import os

de = ['Budgie','Cinnemon','Cutefish','Deepin','Enlightment','GNOME','KDE plasma','LXDE','LXQT','MATE','Xfce']
fwm = ['2bwm','9wm','berry','blackbox','compiz','cwm','eggwm','evilwm','fluxbox','flwm','fvwm','gala','goomwm','icewm','jbwm','jwm','karmen','openbox']
twm = "bspwm exwm i3 i3-gaps dwm awesomewm"
twm = twm.split()

def fwm_install(wm):
    os.system(f"sudo pacman -S {wm}")

def de_install(DE):
    os.system(f"sudo pacman -S {DE}")
def twm_install(TWM):
    os.system(f"sudo pacman -S {TWM}")


prompt = input("""
               [1] > de
               [2] > wm

               [+] Enter option number : """)
if prompt == "1":
    k = 0
    for i in de:
        print(f"[{k}] > {i}")
        k = k + 1
        de_install(de[k])


elif prompt == "2":
    prompt = input("""
    [1] > floating wm
    [2] > tiling & dynamic wm

    [+] Enter option number : """)
 
    if prompt == "1":
        k = 0
        for i in fwm:
            print(f"[{k}] {i}")
            k = k + 1
            fwm_install(fwm[k])

    elif prompt == "2":
        k = 0
        for i in twm:
            print(f"[{k}] {i}")
            k = k +1
            twm_install(twm[k])

