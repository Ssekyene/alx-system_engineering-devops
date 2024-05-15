# 0x05. Processes and signals
|File				|Description				|
|-----------------------|-----------------------------------|
|0-what-is-my-pid		|a Bash script that displays its own PID	|
|1-list_your_processes	|a Bash script that displays a list of currently running processes	|
|2-show_your_bash_pid	| a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process|
|3-show_your_bash_pid_made_easy |a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash` |
|4-to_infinity_and_beyond|a Bash script that displays `To infinity and beyond` indefinitely	|
|5-dont_stop_me_now	|a Bash script that stops `4-to_infinity_and_beyond` process. Open 2 terminals and start running `4-to_infinity_and_beyond` Bash script in terminal #0 and then move to terminal #1 and run `5-dont_stop_me_now` |
|6-stop_me_if_you_can	|a Bash script that stops `4-to_infinity_and_beyond` process. Open 2 terminals and start running `4-to_infinity_and_beyond` Bash script in terminal #0 and then move to terminal #1 and run `6-stop_me_if_you_can` |
|7-highlander		|a Bash script that displays `To infinity and beyond` indefinitely and `I am invincible!!!` when receiving a `SIGTERM` signal. Open 2 termianls and start running `7-highlander` in Terminal #0 and then move to terminal #1 and run `67-stop_me_if_you_can` |
|8-beheaded_process	|a Bash script that kills the process `7-highlander`. Open 2 terminals and start running `7-highlander` in terminal #0 and then move to terminal #1 and run `8-beheaded_process` |
|100-process_and_pid_file|a Bash script that combines several features from the recent files	|
|101-manage_my_process, manage_my_process| a Bash (init) script `101-manage_my_process` that manages `manage_my_process` |
|102-zombie.c		|a C program that creates 5 zombie processes. In terminal #0, Start by compiling and executing the file by `gcc 102-zombie.c -o zombie && ./zombie` and in terminal #1 run `ps aux \| grep -e 'Z+.*<defunct>'` to display the list of processes that are zombies	|
