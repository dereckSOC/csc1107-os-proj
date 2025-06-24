#include <linux/module.h>     // Core header for loading LKMs into the kernel
#include <linux/fs.h>         // For file operations like read() and write()
#include <linux/uaccess.h>    // For copy_to_user and copy_from_user
#include <linux/string.h>     // For strlen()

#define DEVICE_NAME "usb_comm"  // Device name shown in /proc/devices
#define BUF_LEN 100             // Buffer size for kernel message storage

static int major;                       // Device major number assigned dynamically
static char kernel_buffer[BUF_LEN];     // Buffer to store message from user

// Read operation: sends a message from kernel to user space
static ssize_t device_read(struct file *file, char __user *buf, size_t count, loff_t *ppos) {
    char *message = "Hello World from the kernel space";  // Message to send

    // Try and copy message from kernel space to user space, if not successful then print out error message to log
    if (copy_to_user(buf, message, strlen(message) + 1) != 0) {
        printk(KERN_WARNING "usb_comm: copy_to_user failed\n");
        return -EFAULT;
    }

    // Print message to log if copy is sucessful
    printk(KERN_INFO "usb_comm: Sent message to user\n");
    return strlen(message) + 1;  // Return number of bytes sent
}

// Write operation: receives a message from user space
static ssize_t device_write(struct file *file, const char __user *buf, size_t count, loff_t *ppos) {
    if (count >= BUF_LEN) count = BUF_LEN - 1;  // Ensure we don’t exceed buffer

    // Try and copy data from user space to kernel buffer, if not successful then print out error message to log
    if (copy_from_user(kernel_buffer, buf, count) != 0) {
        printk(KERN_WARNING "usb_comm: copy_from_user failed\n");
        return -EFAULT;
    }

    // Print message to log if copy is successful
    kernel_buffer[count] = '\0';  // Null-terminate the received string
    printk(KERN_INFO "usb_comm: Received from user: %s\n", kernel_buffer);
    return count;  // Return number of bytes received
}

// File operation structure: binds system calls to read and write functions
static struct file_operations fops = {
    .owner = THIS_MODULE,
    .read = device_read,
    .write = device_write,
};

// Module initialization: runs when module is loaded
static int __init usb_comm_init(void) {
    // Register character device and get major number
    major = register_chrdev(0, DEVICE_NAME, &fops);
    if (major < 0) {
        printk(KERN_ALERT "usb_comm: Failed to register device\n");
        return major;
    }
    printk(KERN_INFO "usb_comm: Module loaded with device major %d\n", major);
    return 0;
}

// Module cleanup: runs when module is removed
static void __exit usb_comm_exit(void) {
    unregister_chrdev(major, DEVICE_NAME);  // Unregister the character device
    printk(KERN_INFO "usb_comm: Module unloaded\n");
}

module_init(usb_comm_init);  // Declare entry point
module_exit(usb_comm_exit);  // Declare exit point

MODULE_LICENSE("GPL");  // Open source license