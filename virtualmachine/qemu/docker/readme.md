# Installing docker in VMs

## Alpine

Installation


Uncomment in /etc/apk/repositories the community repository

```
su
apk update && apk add docker
```

### Docker as root

```
rc-update add docker default
service docker start
addgroup ${USER} docker
```

### Test docker

`docker run hello-world`



