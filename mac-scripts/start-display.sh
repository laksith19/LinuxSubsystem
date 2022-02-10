qemu-system-x86_64 \
-accel hvf \
-cpu host \
-m 1G \
-smp 1 \
-device e1000,netdev=net0 \
-netdev user,id=net0,hostfwd=tcp::2222-:22 \
-drive file=sda.img \
