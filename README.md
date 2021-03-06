# Logs-Analysis
This project extract information from a database using DB-API in Vagrant.  It is a small simulation about data extraction from real world web applications. 

## How to run:
1. Download and install [Python3](https://www.python.org/download/releases/3.0/), [Vagrant](https://www.vagrantup.com/), and [VirtualBox](https://www.virtualbox.org/).
1. Replace vagrant default confiduration with Vagrantfile from this directory.
1. Download the [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
1. Unzip this file and extract newsdata.sql.

### Launching Vagrant Virtual Machine:
 1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository with:

    `$ vagrant up`

 2. Then Log into:

    `$ vagrant ssh`

 3. Change directory to `/vagrant`.
 
 ### Setting up the database:
  1. Load the data in local database using:

     `psql -d news -f newsdata.sql`

  2. Connect to the database with `psql -d news`.
  
 ### Creating view:
  1. Create a view of errors using:
  
     ```sql
     CREATE VIEW error_table AS
     SELECT date(time),
         ROUND(100.0 * SUM(CASE log.status WHEN '200 OK' THEN 0 ELSE 1 END)/
         COUNT(log.status),2) AS con_error
     FROM log
     GROUP BY date(time) 
     ORDER BY con_error DESC;
      
     ```

 ### Checkint the logs:
  1. From /vagrant directory run logsNews.py:
  
     `python logsNews.py`
