## Installing Arch
- Check internet conection  
`ping archlinux.org`

- Update the system clock  
`timedatectl status`  

- Partition disks  
`fdisk -l`  

- Explore on /dev and find any sda/sdb/sdc
In my case my VirtualBox disk is on sda

> Listing information about block devices
`lsblk` // here you can find details about sda disk.

## Edit partition with fdisk or cfdisk
### fdisk
- Check partition
`fdisk /dev/sda`
`m` // for help
`p` // print the partition table

`n` // for new partition
`p` // primary partition
`1` // partition one
`[enter]` // first sector set by default
`[enter]` // last sector set by default
`w` // write changes.

- Format partition
`mkfs.ext` // tab to see options
`mkfs.ext4 /dev/sda`

> Warning FIRST NEED UNMOINT THE DISK
`umoint /dev/sda`

### cfdisk
- Label gpt
- New Partition size: 550MB // recomended from wiki for acrh.
- change sda1 type to "EFI system"
- new partition sda2 for swap: 1Gb
- new partition sda3 for linux filesystem: the rest space.

## Formating partitions created sda1/sda2/sda3
- sda1: Efi  
`mkfs.fat -f32 /dev/sda1`  

- sda2: swap  
`mkswap /dev/sda2`  
`swapon /dev/sda2`

- sda3: linux file system ext4
`mkfs.ext3 /dev/sda3`

## Mounting sda3
`mount /dev/sda3 /mnt`


## Installing arch
`pacstrap /mnt base linux linux-firmware`

---
## Configure the system
- 1. Generate an fstab file
`genfstab -U /mnt >> /mnt/etc/fstab`

- 2. Change root into a new system
`arch-chroot /mnt`

- 3. Set System time zone
`ls /user/share/zoneinfo/` // search your region
`ls /user/share/zoneinfo/REGIO/`// search your city  
`ln -sf /user/share/zoneinfo/REGION/CITY /etc/localtime`  

`hwclock --systohc`

- 4. Set Localization
Edit /etc/locale.gen
`nano /etc/locale.gen` | `vim /etc/locale.gen` // install a editor

`pacman -S nano` | `pacman -S vim`

then uncomment your locale language like "en_US"

finally generate locale with:
`locale-gen`

## Network configuration
- vim /etc/hostname
`Mjarchker`

- Local network hostname resolution
Edit /etc/hosts
`vim /etc/hosts`

```
127.0.0.1       localhost
::1             localhost
127.0.1.1       MJarchker.localdomain   MJarchker
```

## Manage users
- Update root password
`passwd` // set new password

- Add User
`useradd -m CamperSan`
`passwd CamperSan` // set pass for CamperSan
`usermod -aG  wheel,audio,video,optical,storage CamperSan`

install sudo
`pacman -S sudo`

- edit visudo
`EDITOR=vim visudo`
uncomment %whell all=(all) all


## install grup
`pacman -S grub`
`patcman -S efibootmgr dosfstools os-prober mtools`

creating directory on /boot
`mkdir /boot/EFI`

mounting partition
`mount /dev/sda1` /boot/EFI

install the grub on /boot/EFI
`grub-install --target=x86_64-efi --bootloader-id=grub_uefi --recheck`  

> this part fails, probably because i am on a virtual machine.

Trying another grub-install for virtual machine
`grub-install --target=x86_64-efi --efi-directory=/boot/EFI/ --bootloader-id=Arch


`grub-mkconfig -o /boot/grub/grub.cfg`


## recomended to install networking before restart OS
`pacman -S networkmanager git` 

enable network manager
`systemctl enable NetworkManager`

## Exit and reboot
`exit`
`umount -l /mnt` // for lazy flag
`shutdown -r now`

> First reboot does not work

---
-changed /dev/sda1 from IFE to bios_grub 
`parted /dev/sda1 set 1 bios_grub on`
Update fstab
`genfstab -U /mnt >> /mnt/etc/fstab`

`grub-install /dev/sda`
`grub-mkconfig -o /boot/grub/grub.cfg`
