## VBoxManage
Updated: 20230223

### Create the virtual machine  
`VBoxManage createvm --name MJUbuntu--ostype ArchLinux_64 --register`

### Check virtual machine details with\
`VBoxManage showvminfo MJArch`

### Set Memory Ram  
`VBoxManage modifyvm MJUbuntu --memory 1024`

### Set Vram if needed   
`VBoxManage modifyvm [MACHINE NAME] --memory 1024 --vram 128

### Network configuration > Maybe need to config ethernet with 
> `VBoxManage modifyvm MJArch --bridgeadapter1 msk1` //this does not work in my computer because it does not have same device 
 
> Need find with `vboxmanage list bridgedifs` then computer network adapter  
> `vboxmanage modifyvm "vmname" --bridgeadapter# "host-network-adapter-name"`  // command  
> `VBoxManage modifyvm MJUbuntu --bridgeadapter1 Realtek 8822CE Wireless LAN 802.11ac PCI-E NIC` // this works for me  
> `VBoxManage modifyvm MJUbuntu --nic1 bridged`  


### Modify number of CPUs
`Vbosmanage modifyvm MJUbuntu --cpus 4`

### Create a Hard Drive and Attach it  
	- `VBoxManage createhd --filename MJUbuntuHDD.vdi -size 20480	--format VDI`   
	- `VBoxManage storagectl MJUbuntu --name "SATA Controller" --add sata --controller IntelAhci`  
	- `VBoxMAnage storageattach MJUbuntu --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium MJUbuntuHDD.vdi`  


### Mount a CD-ROM
	- `VBoxManage storagectl MJUbuntu --name "IDE Controller" --add ide --controller PIIX4`
	- `VBoxManage storageattach MJUbuntu --storagectl "IDE Controller" --port 1 --device 0 --type dvddrive --medium ubuntu-22.04.1-desktop-amd64.iso` //DID DOES NOT WORK - I added manually the dvd controller from VirtualBox GUI.
	 
### Enable RDP (Remote Desktop Protocol)
	- `VBoxManage modifyvm MJUbuntu --vrde on`
	- `VBoxManage modifyvm MJUbuntu --vrdemulticon on --vrdeport 3390`

### Listing Virtual machines
	- `VboxManage.exe list vms`

### Check IP connection
- Check VRDE / Remote display IP Address
`VBoxManage showvminfo MJUbuntu | find /i "VRDE"`
> Here probably need to set an IP adress
- Modify VRDE / Remote IP Address
`VBoxManage modifyvm MJUbuntu --vrdeaddress 127.0.0.1`

### Port Forwarding for ssh client (while the virtual machine is running
VBoxManage.exe  controlvm MJUbuntu natpf1 "ssh,tcp,127.0.0.1,9222,10.0.2.15,22"

> if not running the virutal machine use modifyvm instead of controlvm. (not tested)

### Configure firewall and open port 22
```
$ sudo ufw allow ssh
$ sudo ufw enable
$ sudo ufw status
```



### Start the Virtual Machine
	- `VBoxManage startvm MJUbuntu`					 // Use Virtual box gui.
	- `VBoxManage startvm MJUbuntu --type headless` // can be connected from RDP
	- `VBoxHeadless --startvm MJUbuntu`            // can be connecte from RDP 

### Exit the Virtual Machine  
`VBoxManage  controlvm MJUbuntu poweroff` 


---

## References 
 
- Oracle Manual for 
VBoxManage reference https://docs.oracle.com/en/virtualization/virtualbox/6.0/user/vboxmanage-storagectl.html

- Create Virtual Machine  
https://networking.ringofsaturn.com/Unix/Create_Virtual_Machine_VBoxManage.php
