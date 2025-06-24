KDIR := /home/pi/project/linux  # Working full kernel source (edit path to linux kernel if necessary)

# Tell kernel to build usb_comm_module.c into a loadable kernel module
obj-m += usb_comm_module.o

all:
        # Compile the module
        make -C $(KDIR) M=$(PWD) modules

clean:
        # Remove module object files (artifacts)
        make -C $(KDIR) M=$(PWD) clean
