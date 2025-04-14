# Installing docker in VMs

## Alpine

Installation


Uncomment in /etc/apk/repositories the community repository
> If url to repo missing add:
```
#/media/cdrom/apks
http://dl-cdn.alpinelinux.org/alpine/v3.21/main
http://dl-cdn.alpinelinux.org/alpine/v3.21/community
```



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



