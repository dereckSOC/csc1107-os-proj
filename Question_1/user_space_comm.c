#include <string.h>  // For strlen()
#include <stdio.h>   // For printf()
#include <fcntl.h>   // For open()
#include <unistd.h>  // For read(), write(), close()

int main() {
    char buffer[100];  // Buffer to store message received from kernel

    // Open the device file for reading and writing
    int fd = open("/dev/usb_comm", O_RDWR);
    if (fd < 0) {
        perror("Failed to open device");
        return 1;
    }

    // Prepare message to send to kernel
    char *msg = "Hello World from the user space";

    // Write message to the device by calling kernel module's write() system call
    if (write(fd, msg, strlen(msg)) < 0) {
        perror("Write failed");
    } else {
        printf("Sent to kernel: %s\n", msg);
    }

    // Read message from the device by calling kernel module's read() system call
    if (read(fd, buffer, sizeof(buffer)) < 0) {
        perror("Read failed");
    } else {
        printf("Received from kernel: %s\n", buffer);
    }

    close(fd);  // Close the device file
    return 0;
}