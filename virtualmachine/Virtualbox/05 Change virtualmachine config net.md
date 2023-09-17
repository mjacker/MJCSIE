# Change virtual machine config net
Before changing the net configuration like `nat, bridged, intnet, hostonly, generic, natnetwork`
first need to check the current net configuration used by the virutal machine.

1. Using showvminfo
`vboxmanage showvminfo --details <virtual machine name/UUID>
