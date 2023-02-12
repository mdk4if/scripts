import os
import subprocess
import shutil
import sys

banner = """    
                   -`                    
                  .o+`                   
                `+oooo:                  
               `+oooooo:                  
               -+oooooo+:                
             `/:-:++oooo+:               
           `/++++++++++++++:            
          `/+++ooooooooooooo/`           
         ./ooosssso++osssssso+`          
        .oossssso-````/ossssss+`         
       -osssssso.      :ssssssso.        
      :osssssss/        osssso+++.       
     /ossssssss/        +ssssooo/-       
   `/ossssso+/:-        -:/+osssso+-     
  `+sso+:-`                 `.-/+oso:    
 `++:.                           `-/+/   
 .`                                 `/   


Author : ghost(y)
                                         
"""
print(banner)
sure = input("U sure bro (y/n): ")
if sure != "y" or sure != "Y":
    print("[+] Coward ;)")
    sys.exit(0)


if os.system("ping -c 1 -w 1 www.google.com"):
    pass
else:
    print("[+] U don't have a internet connection dude/babe")
    sys.exit(0)



print("[+] Installing arch ")
print("[+] Udating system clock ")
os.system("timedatectl status")

path = "/dev"
disks = os.listdir(path)
number = "1 2 3 4 5 6 7 8 9 0"
number_list = number.split() 

drives =[]
for disk in disks:
    if disk.startswith("sd") and disk[-1] not in number_list:
        drives.append(disk)
k = 0
print(drives)
for i in drives:
    print(f"[{k}] > {i}")
    k = k + 1
disk_prompt = input("[+] Enter option number : ")
index = int(disk_prompt)
install_disk = drives[index]

def install_grub():
    Type = input("""
                [1] > ufi 
                [2] > bios
                
                [+] Enter option number : """)
    if Type == "1":
        os.system("grub-install --target=x86_64-efi --efi-directory=esp --bootloader-id=GRUB --boot-directory=/mnt/boot")
    elif Type == "2":
        os.system(f"grub-install --target=i386-pc --boot-directory={install_disk}")
    else:
        print("[!] Invalid selection . Abort")
        quit()


def install_arch():
    partition()
    
    temp = install_disk
    temp = temp + "1"
    # Format the partitions
    print("[+] Formating partitions")
    subprocess.run(['mkfs.ext4', temp])
    temp = install_disk
    temp = temp + "2"
    subprocess.run(['mkfs.ext4', temp])
    temp = install_disk
    temp = temp + "3"
    subprocess.run(['mkfs.ext4', temp])

    # Mount the partitions
    print("[+] Mounting partitions ")
    subprocess.run(['mount', '/dev/sda2', '/mnt'])
    subprocess.run(['mkdir', '/mnt/boot'])
    subprocess.run(['mkdir', '/mnt/home'])
    subprocess.run(['mount', '/dev/sda1', '/mnt/boot'])
    subprocess.run(['mount', '/dev/sda3', '/mnt/home'])

    # Install the base system
    print("[+] Installing base system ")
    subprocess.run(['pacstrap', '/mnt', 'base','linux','linux-firmware','base devel','grub','networkmanager'])

    # Generate an fstab file
    print("[+] Generating fstab ")
    subprocess.run(['genfstab', '-U', '/mnt', '>>', '/mnt/etc/fstab'])
    print("[+] Installing  grub ")
    install_grub()
    reboot = input("""
                   [1] > reboot
                   [2] > arch-chroot

                   [+] Enter option number : """)
    if reboot == "1":
        os.system("reboot")
    elif reboot == "2":
        os.system("arch-chroot /mnt")

install_arch()



def partition():
    
    path = "/dev/" + install_disk

    # Get the total size and available space of the hard drive
    total_size, available_space = shutil.disk_usage(path)

    # Calculate the sizes of the partitions
    boot_size = 512 * 1024 * 1024  # 512MB
    root_size = 30 * 1024 * 1024 * 1024  # 30GB
    home_size = available_space - boot_size - root_size  # remainder of the available space
    print("[+] Partitioning drive into boot root home")

    # Run the 'parted' utility to create a new partition table on the hard drive
    subprocess.run(['parted', install_disk , 'mklabel', 'gpt'])

    # Create the 'boot' partition using the 'mkpart' command
    subprocess.run(['parted', install_disk , 'mkpart', 'primary', 'ext4', '1MiB', str(boot_size)])

    # Create the 'root' partition using the 'mkpart' command
    subprocess.run(['parted', install_disk , 'mkpart', 'primary', 'ext4', str(boot_size), str(boot_size + root_size)])

    # Create the 'home' partition using the 'mkpart' command
    subprocess.run(['parted', install_disk , 'mkpart', 'primary', 'ext4', str(boot_size + root_size), '100%'])

    # Set the 'boot' partition as bootable using the 'set' command
    subprocess.run(['parted', install_disk , 'set', '1', 'boot', 'on'])


