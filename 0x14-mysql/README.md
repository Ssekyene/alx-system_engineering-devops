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

⚠️ B**Before going through the guide try this command if it gonna install MySQL 5.7 correctly, when you see the white windows you can jump to step 9, and see what to choose :**
```
sudo wget -O mysql57 https://raw.githubusercontent.com/nuuxcode/alx-system_engineering-devops/master/scripts/mysql57 && sudo chmod +x mysql57 &&  sudo ./mysql57
```
If this command did not install 5.7 correctly you can continue reading the following guide.

**NOTE AS YOU PROCEED: At any point in this guide, don’t go to the next step if you have errors in the current step you are in, make sure there are no errors.**

[Click here for the guide](https://docs.google.com/document/d/1btVRofXP75Cj90_xq2x8AmzuMPOKq6D_Dt_SCDD6GrU/edit#heading=h.nu0sqigqw1o9)


