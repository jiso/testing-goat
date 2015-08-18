Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
         ├── database
         ├── source
         ├── static
         └── virtualenv


## MISC Installation Notes for Docker Python Goat Exercises
* Have not been able to get the upstart file to work correctly

* Installation issues for fabric in chapter 9
  * apt-get install python-dev
  * pip2 install pycrypto
  * pip2 install ecdsa
  
  * References:
  * [http://stackoverflow.com/questions/11596839/installing-pycrypto-on-ubuntu-fatal-error-on-build](http://stackoverflow.com/questions/11596839/installing-pycrypto-on-ubuntu-fatal-error-on-build)