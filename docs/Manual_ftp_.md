# FTP
  
Connect and manage an FTP Server  

*Read this in other languages: [English](Manual_ftp_.md), [Português](Manual_ftp_.pr.md), [Español](Manual_ftp_.es.md)*
  
![banner](imgs/Banner_ftp_.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Connect to FTP
  
Connect to FTP to manage it with Rocketbot
|Parameters|Description|example|
| --- | --- | --- |
|Server|FTP server address|test.ftp.com|
|Port|FTP server port|5518|
|Assign result to variable|Variable where the result of the connection will be stored|Variable|
|User|FTP server user|user@test.com|
|Password|Password of the FTP server user|******|
|TLS|Enable TLS|True|
|Encoding|FTP server encoding|utf-8|
|Assign result to variable|Variable where the result of the connection will be stored|result|

### List directory
  
Lists the FTP directory in a Rocketbot variable
|Parameters|Description|example|
| --- | --- | --- |
|Store result in variable|Variable where the result will be stored|Variable|

### Create directory
  
Create directory in the current path
|Parameters|Description|example|
| --- | --- | --- |
|Directory name|Name of the directory to create|test|
|Assign result to variable|Variable where the result will be stored|Variable|

### Go to directory
  
Go to the specified directory
|Parameters|Description|example|
| --- | --- | --- |
|Directory name|Directory name to access|test|
|Save current directory in variable|Name of the variable where the current directory will be saved|Variable|

### Upload file
  
Upload file to current directory
|Parameters|Description|example|
| --- | --- | --- |
|File to upload|File that will be uploaded to the ftp directory|C:\Users\User\Desktop\test.png|
|Timeout|Maximum timeout in seconds|10|
|Assign result to variable|Variable where the result will be saved|Variable|

### Download file
  
Download the selected file
|Parameters|Description|example|
| --- | --- | --- |
|File name to download|File name that will be downloaded from the ftp directory|test.png|
|Path to download|Path where the file will be downloaded|C:\Users\User\Desktop|
|Assign result to variable|Assigns the result of the download to the selected variable|Variable|

### Download directory
  
Download the current directory
|Parameters|Description|example|
| --- | --- | --- |
|Path to download|Path where the current directory will be downloaded|C:/Users/User/Desktop|
|Include subdirectories|If checked, the subdirectories will be included in the download recursively|False|
|Assign result to variable|Assigns the result of the download to the selected variable|Variable|

### Delete file
  
Delete file in current directory
|Parameters|Description|example|
| --- | --- | --- |
|File name to delete|File name that will be deleted from the current directory|test.png|
|Assign result to variable|Variable where the result of the operation will be stored|Variable|

### Close Connection
  
Close FTP Connection
|Parameters|Description|example|
| --- | --- | --- |
