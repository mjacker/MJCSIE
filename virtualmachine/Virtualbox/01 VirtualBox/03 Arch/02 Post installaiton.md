## Post installation on Arch linux
1. Update The system  
First things, ipdate the system with the pacman command:  
`$ sudo pacman -Syyu`  

2. Install a Display Server
To get a GUI environment, need to install a Display Server.
`$ sudo pacman -S xorg`

3. Install A Desktop Environment
- Xfce4
`sudo pacman -S xfce4 xfce40goodies`
`pacman -S lxdm`
`sudo systemctl enable lxdm.service`

4. Install video driver
`pacman -S xf86-video-vesa` // no tested yet
