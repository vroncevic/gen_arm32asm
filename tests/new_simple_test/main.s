@
@ @brief   new_simple_test
@ @version 1.0.2
@ @date    2025-01-29
@ @company None, free software to use 2025
@ @author  Vladimir Roncevic <elektron.ronca@gmail.com>
@

.global _start

_start:
    @ Prepare the arguments for the write syscall
    mov r0, #1          @ File descriptor: 1 (stdout)
    ldr r1, =message    @ Pointer to the message to write
    mov r2, #13         @ Length of the message
    mov r7, #4          @ Syscall number for write (4)
    swi 0               @ Make the syscall

    @ Exit the program
    mov r0, #0          @ Exit status code (0 for success)
    mov r7, #1          @ Syscall number for exit (1)
    swi 0               @ Make the syscall

.data
message:
    .asciz "Hello, ARM!\n"
