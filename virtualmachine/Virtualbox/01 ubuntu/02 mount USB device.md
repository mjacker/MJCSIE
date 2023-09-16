# Mount USB device
1. check storage device
`sudo disk -l`

2. Create a mount point for your USB device.
`$ sudo mkdir /media/[mountPointName]i`

3. Mount 
`$ sudo mount -t vfat /dev/sdb1 /media/USB -o [securityoption]`
psecurityoption:
- uid=1000
- gid=1000
- Utf8
- dmask=027
- fmask=137

uid=1000 : total control

`sudo mount -t vfat /dev/sdb /media/mjusb -o uid=1000`

# How to Unmount USB device
`$ sudo umount /dev/sdb1`
and also
`$ sudo umount /media/mjusb`

