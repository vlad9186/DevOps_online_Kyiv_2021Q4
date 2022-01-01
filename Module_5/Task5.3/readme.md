TASK5.3
Part1

1. How many states could has a process in Linux?

Processes in Linux have a several status:
R – Running or runnable;
D – Uninterruptible sleep or wait writing on the disk;
S – Interruptible sleep;
T – Stopped, either by a job control signal or because it is being traced;
Z – Defunct (“zombie”) process, terminated but not closed by the parent process that created it.

2. Examine the pstree command. Make output (highlight) the chain (ancestors) of the current process.

 ![screenshots](screenshots/1.png)

3. What is a proc file system?

 ![screenshots](screenshots/2.png)

4. Print information about the processor (its type, supported technologies, etc.).

 ![screenshots](screenshots/3.png)

 ![screenshots](screenshots/4.png)

5. Use the ps command to get information about the process. The information should be as follows: the owner of the process, the arguments with which the process was launched for execution, the group owner of this process, etc.

 ![screenshots](screenshots/5.png)

6. How to define kernel processes and user processes?

 ![screenshots](screenshots/6.png)

7. Print the list of processes to the terminal. Briefly describe the statuses of the processes. What condition are they in, or can they be arriving in?

 ![screenshots](screenshots/7.png)

8. Display only the processes of a specific user.

 ![screenshots](screenshots/8.png)

9. What utilities can be used to analyze existing running tasks (by analyzing the help for the ps command)?

 ![screenshots](screenshots/9.png)

 ![screenshots](screenshots/10.png)

 ![screenshots](screenshots/11.png)

10. What information does top command display?

Top command is used to show the Linux processes.
This Linux command will sort the list by CPU usage, so the process which consumes the most resources will be placed at the top.

11. Display the processes of the specific user using the top command.

 ![screenshots](screenshots/12.png)

12. What interactive commands can be used to control the top command? Give a couple of 
examples.

There are some interactive commands that can be used during top command work:

A - see group of process, Z - change color of info
 ![screenshots](screenshots/13.png)

h - see manual
 ![screenshots](screenshots/14.png)

13. Sort the contents of the processes window using various parameters (for example, the 
amount of processor time taken up, etc.)

Shift + N - by PID
 ![screenshots](screenshots/15.png)

Shift + T - by working time
 ![screenshots](screenshots/16.png)

14. Concept of priority, what commands are used to set priority?

 ![screenshots](screenshots/17.png)

15. Can I change the priority of a process using the top command? If so, how?

Use r command
 ![screenshots](screenshots/18.png)

16. Examine the kill command. How to send with the kill command
process control signal? Give an example of commonly used signals.

 ![screenshots](screenshots/19.png)

17. Commands jobs, fg, bg, nohup. What are they for? Use the sleep, yes command to 
demonstrate the process control mechanism with fg, bg.

 ![screenshots](screenshots/20.png)

Part2

1. Check the implementability of the most frequently used OPENSSH commands in the MS 
Windows operating system. (Description of the expected result of the commands + 
screenshots: command – result should be presented)

 ![screenshots](screenshots/26.png)

 ![screenshots](screenshots/27.png)

2. Implement basic SSH settings to increase the security of the client-server connection (at least 

 ![screenshots](screenshots/21.png)

3. List the options for choosing keys for encryption in SSH. Implement 3 of them.

 ![screenshots](screenshots/22.png)

 ![screenshots](screenshots/23.png)

 ![screenshots](screenshots/23.1.png)

 ![screenshots](screenshots/23.2.png)

 ![screenshots](screenshots/23.3.png)

4. Implement port forwarding for the SSH client from the host machine to the guest Linux virtual machine behind NAT.

 ![screenshots](screenshots/24.png)

5*. Intercept (capture) traffic (tcpdump, wireshark) while authorizing the remote client on the server using ssh, telnet, rlogin. Analyze the result

 ![screenshots](screenshots/25.png)

 ![screenshots](screenshots/25.0.png)

 ![screenshots](screenshots/25.1.png)
