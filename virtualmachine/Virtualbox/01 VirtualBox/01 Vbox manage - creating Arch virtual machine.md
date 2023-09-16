## VBoxManage
- Create the virtual machine  
`VBoxManage createvm --name MJArch --ostype ArchLinux_64 --register`

- Check virtual machine details with\
`VBoxManage showvminfo MJArch`

- Set Memory Ram  
`VBoxManage modifyvm MJArch --memory 1024`

- Set Vram if needed   
`VBoxManage modifyvm [MACHINE NAME] --memory 1024 --vram 128

- Network configuration
> Maybe need to config ethernet with 
> `VBoxManage modifyvm MJArch --bridgeadapter1 msk1` //this does not work in my computer because it does not have same device 
 
> Need find with `vboxmanage list bridgedifs` then computer network adapter  
> `vboxmanage modifyvm "vmname" --bridgeadapter# "host-network-adapter-name"`  // command  
> `VBoxManage modifyvm MJArch --bridgeadapter1 Realtek 8822CE Wireless LAN 802.11ac PCI-E NIC` // this works for me  
> `VBoxManage modifyvm MJArch --nic1 bridged`  


- Create a Hard Drive and Attach it  
	- `VBoxManage createhd --filename MJArchSD.vdi -size 8000	--format VDI`   
	- `VBoxManage storagectl MJArch --name "SATA Controller" --add sata --controller IntelAhci`  
	- `VBoxMAnage storageattach MJArch --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium MJArchSD.vdi`  

- Mount a CD-ROM
	- `VBoxManage storagectl MJArch --name "IDE Controller" --add ide --controller PIIX4`
	- `VBoxManage storageattach MJArch --storagectl "IDE Controller" --port 1 --device 0 --type dvddrive --medium archlinux-2022.10.01-x86_64.iso` //DID DOES NOT WORK - I added manually the dvd controller from VirtualBox GUI.
	 
- Enable RDP (Remote Desktop Protocol)
	- `VBoxManage modifyvm MJArch --vrde on`
	- `VBoxManage modifyvm MJArch --vrdemulticon on --vrdeport 3390`

- Listing Virtual machines
	- `VboxManage.exe list vms`

- Start the Virtual Machine
	- `VBoxManage startvm MJArch`					 // Use Virtual box gui.
	- `VBoxManage startvm MJArch --type headless` // can be connected from RDP
	- `VBoxHeadless --startvm MJArch`            // can be connecte from RDP 

- Check VRDE / Remote display IP Address
`VBoxManage showvminfo MJArch | find /i "VRDE"`
- Modify VRDE / Remote IP Address
`VBoxManage modifyvm MJArch --vrdeaddress 127.0.0.1`

- Exit the Virtual Machine  

## References 
`VBoxManage  controlvm MJArch poweroff` 
 
- Oracle Manual for 
VBoxManage reference https://docs.oracle.com/en/virtualization/virtualbox/6.0/user/vboxmanage-storagectl.html

- Create Virtual Machine  
https://networking.ringofsaturn.com/Unix/Create_Virtual_Machine_VBoxManage.php
