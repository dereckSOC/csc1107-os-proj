#!/bin/bash

MODULE_NAME="usb_comm_module"      # Kernel module filename
DEVICE_NAME="usb_comm"             # Device file name under /dev
C_FILE="user_space_comm.c"         # C source file for user space
USER_BINARY="user_comm"            # Compiled binary for user space program

echo "Detecting peripheral devices..."

init_count=$(lsusb | wc -l)        # Initial USB device count
prev_count=$init_count

while true; do
    current_count=$(lsusb | wc -l)  # Check current number of USB devices

    # USB device inserted
    if (( current_count > prev_count )); then
        echo "[*] USB device detected. Total: $(($current_count - $init_count))"

        # Compile kernel module if not yet built
        if [ ! -f "$MODULE_NAME.ko" ]; then
            echo "[*] Compiling kernel module..."
            make
        fi

        # Insert kernel module, same module can be used for multiple different USBs devices as it is not device specific
        if lsmod | grep -q "$MODULE_NAME"; then
            echo "[*] Kernel module already inserted."
        else
            echo "[*] Inserting kernel module..."
            sudo insmod $MODULE_NAME.ko
        fi

        # Wait and extract major number from /proc/devices
        sleep 1
        major=$(awk "\$2==\"$DEVICE_NAME\" {print \$1}" /proc/devices)

        # Create the device file under /dev
        echo "[*] Creating /dev/$DEVICE_NAME..."
        sudo mknod /dev/$DEVICE_NAME c $major 0 2>/dev/null
        sudo chmod 666 /dev/$DEVICE_NAME

        # Compile user space program only once
        if [ ! -f "$USER_BINARY" ]; then
            echo "[*] Compiling user space program..."
            gcc -o $USER_BINARY $C_FILE
        fi

        # Run the user space program
        echo "[*] Running user space program..."
        ./$USER_BINARY

        # Show last kernel messages
        echo "[*] Kernel messages:"
        dmesg | tail -n 10

    # USB device removed
    elif (( current_count < prev_count )); then
        echo "[*] USB device removed. Remaining: $(($current_count - $init_count))"

        if (( current_count == init_count )); then
            echo "[*] All USBs removed. Cleaning up..."

            # Unload kernel module and remove device file
            sudo rmmod $MODULE_NAME
            sudo rm -f /dev/$DEVICE_NAME

            # Clean build artifacts
            echo "[*] Cleaning module build only..."
            make clean
            rm -f $USER_BINARY
        fi
    fi

    prev_count=$current_count  # Update device count
    sleep 2                    # Wait before checking again
done
