# Tasks 


1. Kali qemu on termux installation.

## Requirements

Termux from fdroid

Download kali-for-qemu.7z

`wget https://kali.download/base-images/kali-2025.1a/kali-linux-2025.1a-qemu-amd64.7z`

Install p7zip and unzip it.
`7z x -aoa kali-linux-2025.1a-qemu-amd64.7z`

run the QEMU VM with 

`qemu-system-x86_64  -m 3G -smp 4 -drive file=kali-linux-2025.1a-qemu-amd64.qcow2,format=qcow2 -vnc 127.0.0.1:1`

Port forwarding if needed with

`socat TCP-LISTEN:5902,fork TCP:127.0.0.1:5901`

Connect from VNC viewer

![Imgur-connect-vnc](https://imgur.com/LhxHm3Y)

testing imgur image
![Imgur](https://imgur.com/wzdi0D8.png)
