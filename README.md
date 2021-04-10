# Log Analysis Project

## Project description:

This project is part of the [Udacity's Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)
<p>In the end we want to build a reporting tool that will allow us to extract important data from a given database. In our case a newspapaer website.</p> 
<p>This task will sharpen our SQL database skills while building queries for three questions:<p>

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of the requests lead to errors?

## Technologies used:
1. [Python 3](https://www.python.org/downloads/)
2. [Vagrant](https://www.vagrantup.com/) - for building and maintaing portable virtual software development environments
3. [VirtualBox](https://www.virtualbox.org/) - for running a virtual machine on your computer
4. [Git](https://git-scm.com/) - an open source version control system
5. [psql](https://www.postgresql.org/) - relational database management system

## Setting up the project

1. Download and install the latest version of [Python](https://www.python.org/downloads/).
2. Download and install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).
3. Download these vagrant [configuration files](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) provided by Udacity, for this project. These file have all the tools needed to run this project.
4. Download the [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip it and place it in the vagrant folder with the rest of this project.
5. Navigate in your bash interface to the vagrant folder and run the following commands:

- `vagrant up` to start the VirtualMachine
- `vagrant ssh` to log into the VirtualMachine
- `cd /vagrant` to change to your directory

6. Load the database by running this:

- `psql -d news -f newsdata.sql`

7. Run the database by running this:

- `psql -d news`

8. Create the views given below and after exit psql with Ctrl + D
9. And finally execute the Python file with:

- `python logs_analysis.py`

## CREATE THESE VIEWS BEFORE EXECUTING THE PROGRAM

The first view logs for the third question:

    CREATE VIEW logs AS
    SELECT to_char(time, 'DD-MON-YYYY') as Date,
    COUNT(*) as logcount
    FROM log
    GROUP BY Date;

And the secod view errorlogs:

    CREATE VIEW errorlogs AS
    SELECT to_char(time, 'DD-MON-YYYY') as Date,
    COUNT(*) as errorcount
    FROM log
    WHERE STATUS '404 NOT FOUND'
    GROUP BY Date;
