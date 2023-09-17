# no tiene sentido agregar port forwarding
# sisolo quieron conectar entre virtual machines
# el port forwarding es para saca un puerto de la virtual machine
# a un puerto real del host para conectarse desde afuera
vboxmanage controlvm MJKali natpf1 "ssh,tcp,127.0.0.1,8222,10.0.2.15,22"
