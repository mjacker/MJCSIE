# mount host usb on vm.
1. Connect USB device to the host computer.
`vboxmanage list usbhost`

2. it will need:
- Vendor ID
- Product ID
- Serial Number

3. modifyvm <virtual machine name>
`VBoxManage modifyvm MJUbuntu --usbehci on --usbxhci on`

4. Review any USB filter already created.
`vboxmanage showvminfo MJUbuntu --machinereadable`

5. run filter
`vboxmanage usbfilter add 0 --target myvmname --name "MyExternalHardDrive" --vendorid 0BC2         --productid 331A --remote no --serialnumber NBBBXX5V`

6. login 

7. unplug the USB device and plug it back in to the host.
`$ sudo lshw -C disk`
