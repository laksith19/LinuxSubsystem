qemu-system-x86_64 \
-accel kvm \
-cpu max \
-m 1G \
-smp 1 \
-device e1000,netdev=net0 \
-netdev user,id=net0,hostfwd=tcp::2222-:22 \
-drive file=sda.img \
-nographic \
