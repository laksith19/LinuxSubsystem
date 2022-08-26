qemu-system-x86_64 \
-accel kvm \
-cpu host \
-m 4G \
-smp 4 \
-device e1000,netdev=net0 \
-netdev user,id=net0,hostfwd=tcp::2222-:22 \
-drive file=sda.img \
-display none \
-nodefaults \
