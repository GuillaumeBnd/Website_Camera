# Website_Camera

## Introduction
This project goal is to create a website on a raspberry pi, with a database identification that can give access to a camera stream also connected to the raspberry. 

/!\ this is still a work in progress /!\

### Install an Operating System on Raspberry Pi

I choose to install Ubuntu Mate on my Raspberry Pi
Download the image on internet and flash a usb drive with it, tutorial can be found online. 
Once the Raspberry Pi is configured you can do the rest of the tutorial via ssh. 

### Download apache2 
````
sudo apt update
sudo apt install apache2 
````
### Download php 
````
sudo apt-get install php libapache2-mod-php8.1
sudo a2enmod php8.1
sudo service apache2 reload
````

# MySQL configuration 

### Download MySql 
````
sudo apt install mysql-server
sudo systemctl start mysql.service
````
### Load with root user
````
mysql -u root -p
````
### Create a Database
````
CREATE DATABASE Website_Camera;
USE Website_Camera;
````
### Create the table 
````
CREATE TABLE IF NOT EXISTS `accounts` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`username` varchar(50) NOT NULL,
  	`password` varchar(255) NOT NULL,
  	`email` varchar(100) NOT NULL,
    `activation_code` varchar(50) DEFAULT ''
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
````
Modify the code in .php files to match the database name and config

# Implement the code

Go in the repository /var/www/
````
cd /var/www/
````
Create a folder with the name of you choice 

````
mkdir Website
````
copy there all the website code you need to. 

# Acess to your Website

To access your website on your local pc, you need to be connected to the same wifi network as your raspberry pi and to go to the http adress : ( change the name of the raspberry pi ip adress by yours) 
````
192.168.0.9/Website/index.html
````
