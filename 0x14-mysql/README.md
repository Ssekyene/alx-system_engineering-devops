# 0x14. MySQL
## Learning objectives
- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- What operation should you regularly perform to make sure that your database backup strategy actually works
## Requirements
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- Your Bash script must pass `Shellcheck` (`version 0.3.7-5~ubuntu16.04.1` via `apt-get`) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
## Tasks
1. Install MySQL

First things first, let’s get MySQL installed on both your web-01 and web-02 servers.

### [How to : ] Fresh Reset and Install mysql 5.7

⚠️   **Before going through the guide try this command if it gonna install MySQL 5.7 correctly, when you see the white windows you can jump to step 9, and see what to choose :**
```
sudo wget -O mysql57 https://raw.githubusercontent.com/nuuxcode/alx-system_engineering-devops/master/scripts/mysql57 && sudo chmod +x mysql57 &&  sudo ./mysql57
```
If this command did not install 5.7 correctly you can continue reading the following guide.

**NOTE AS YOU PROCEED: At any point in this guide, don’t go to the next step if you have errors in the current step you are in, make sure there are no errors.**

[Click here for the guide](https://docs.google.com/document/d/1btVRofXP75Cj90_xq2x8AmzuMPOKq6D_Dt_SCDD6GrU/edit#heading=h.nu0sqigqw1o9)


2. Let us in!

We need you to create a user and password for **both** MySQL databases which will allow the checker access to them.

Create a MySQL user named `holberton_user` on both `web-01` and `web-02` with the host name set to `localhost` and the password `projectcorrection280hbtn`. This will allow the checker to access the replication status on both servers.

Make sure that `holberton_user` has permission to check the primary/replica status of your databases.

Example:
```
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
Enter password:
+-----------------------------------------------------------------+
| Grants for holberton_user@localhost                             |
+-----------------------------------------------------------------+
| GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' |
+-----------------------------------------------------------------+
ubuntu@229-web-01:~$
```

3. If only you could see what I've seen with your eyes

In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.

- Create a database named `tyrell_corp`.
- Within the `tyrell_corp` database create a table named `nexus6` and add at least one entry to it.
- Make sure that `holberton_user` has `SELECT` permissions on your table so that we can check that the table exists and is not empty.
```
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
Enter password:
+----+-------+
| id | name  |
+----+-------+
|  1 | Leon  |
+----+-------+
ubuntu@229-web-01:~$
```

4. Quite an experience to live in fear, isn't it?

Before you get started with your primary-replica synchronization, you need one more thing in place. On your **primary** MySQL server (web-01), create a new user for the replica server.
- The name of the new user should be `replica_user`, with the host name set to `%`, and can have whatever password you’d like. eg `CREATE USER  'replica_user'@'%' IDENTIFIED BY password`
- `replica_user` must have the appropriate permissions to replicate your primary MySQL server ie `GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%'`
- `holberton_user` will need SELECT privileges on the `mysql.user` table in order to check that `replica_user` was created with the correct permissions ie `GRANT SELECT ON mysql.user TO 'replica_user'@'%'`
```
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user'
+------------------+-----------------+
| user             | Repl_slave_priv |
+------------------+-----------------+
| root             | Y               |
| mysql.session    | N               |
| mysql.sys        | N               |
| debian-sys-maint | Y               |
| holberton_user   | N               |
| replica_user     | Y               |
+------------------+-----------------+
ubuntu@229-web-01:~$
```

