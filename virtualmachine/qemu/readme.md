# Qemu 


### Creating a Virtual Disk

`qemu-img create -f qcow2 myvm.qcow2 20G`

### Running from  an ISO Image

`qemu-system-x86_64 -m 2048 -cdrom ubuntu.iso -boot d`

### Running with KVM

`qemu-system-86_64 -enable-kvm -m 2048 -hda myvm.qcow2`

### Networking

- Bridged Networking

```
-netdev bridge,id=net0
-device virtio-net,netdev=net0
```

- Port Forwarding
```
-net user,hostfwd=tcp::2222-:22
```

## Managing VMs with QEMU

List running VM: `ps aux | grep qemu`
Suspend a VM: `kill -STOP <qemu_pid>`
Resume a VM: `kill -CONT <qemu_pid>`
Save VM state to a file: `qemu-system-86_64 -incoming "exec: cat snapshot.save"`
Monitor a running VM: `nc localhost 4444`
