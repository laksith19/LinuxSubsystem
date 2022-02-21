cp base.img sda.img
& 'C:\Program Files\qemu\qemu-img.exe' resize sda.img +10G 
& 'C:\Program Files\qemu\qemu-system-x86_64.exe' --accel whpx,kernel-irqchip=off  -m 1G -smp 1 -display none -device e1000,netdev=net0 -netdev user,id=net0,hostfwd=tcp::2222-:22 -drive file=sda.img -nodefaults -smbios type=1,serial="ds=nocloud-net;s=http://_gateway:8000/"