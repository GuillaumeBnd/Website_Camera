# Website_Camera

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
