#!/usr/bin/

# Upload a file to FTP server.
host = "ftp.foo.com"
username = "jay"
password = "1234"
filename = "somefile.txt"

import ftplib
ftp_serv = ftplib.FTP(host,username,password)
# Open the file you want to send
f = open(filename, "rb")
# Send file to FTP server
resp = ftp_serv.storybinary("STOR " + filename, f)
# Close the connection
ftp_serv.close
