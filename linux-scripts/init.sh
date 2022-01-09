cp base.img sda.img
qemu-img resize sda.img +10G
qemu-system-x86_64 \
-accel kvm \
-cpu host \
-m 1G \
-smp 1 \
-device e1000,netdev=net0 \
-netdev user,id=net0,hostfwd=tcp::2222-:22 \
-drive file=sda.img \
-nographic \
-smbios type=1,serial="ds=nocloud-net;s=http://10.0.2.2:8000/"
