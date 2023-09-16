## Run Virtual machine
`VboxManage startvm "virtual pc name" --type headless` // not working

---
## Run as Headless Virtual machine
- Power On Headless: ```VBoxHeadless -s "virtual pc name"```\
- Power OFF: ```VBoxManage controlvm "virtual pc name" poweroff```\

## Information
- Get Version: `VboxManage --version`\
- Listing Virtual machines `VboxManage list vms`\
- Show Virtual Machine info: `VboxManage showvminfo "<virtual machine name>"`\

## Network Settings reference
https://www.nakivo.com/blog/virtualbox-network-setting-guide/
