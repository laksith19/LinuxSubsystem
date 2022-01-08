## Linux Subsystem

The aim of this project is to create a cross platform qemu wrapper that will allow the creation of a "Linux Sybsystem" on the host machine using appropriate hardware acceleration for each platform.

Documentation regarding usage and requirements will be added in future commits as the project develops.

#QEMU commands explained
In this section I'll go into slightly more detail about the commands used in the background, solely for the purposes of documentation, skip this section if you just want to use the script.

qemu-system-x86_64 \
    -accel kvm \
    -cpu host \
    -m 1G \
    -smp 1 \
    -drive file=sda.img \
    -nographic \ 
    -smbios type=1,serial="ds=nocloud-net;s=http://10.0.2.2:8000/"
