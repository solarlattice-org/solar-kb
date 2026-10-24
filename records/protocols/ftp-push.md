---
id: proto:ftp-push
type: Protocol
name: FTP push
aliases:
- FTP upload
- FTP push function
- FTP-Push service
- FTP uploads
category: Communication
protocol_kind: application
claims:
- claim_id: c1
  rel: subclass_of
  target: proto:ftp
  note: FTP push sends logger data to the server over standard FTP, without encryption on the SMA Data
    Manager M.
  cite:
  - src: src:eq-equip-inverters-sma-data-manager-m-manual-edmm-10-be-en-17
    loc: sec=h70
    h: 7fabbb3283f2
  - src: src:eq-equip-inverters-sma-data-manager-m-edmm-10-be-en-23
    loc: sec=h72
    h: f803336b71c5
  - src: src:eq-equip-inverters-sma-data-manager-m-firmware-edmm-10-be-en-26
    loc: sec=h80
    h: f803336b71c5
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
FTP push is an application-level function: a data logger uploads the plant data it has collected as files to an external FTP server that you choose. Products that offer it include the SMA Cluster Controller, the Sunny WebBox, the SMA Data Manager M, the communication unit of the Sunny Central UP-US and the Huawei SmartLogger. On the Cluster Controller, open Further Applications > FTP Push. Choose CSV or XML export and enter the login, port, password, server path and server. Then run the connection test and check that the result shows OK. The Cluster Controller uses port 21 by default and uploads every 15 minutes, so port 21 has to be allowed through the router firewall. The Data Manager M uploads in a fixed XML format up to once an hour. It sends the data and the login over plain FTP with no encryption. On a Huawei SmartLogger, log in as Advanced User and open Settings > FTP. Enter the server as a domain name or IP address (a domain name needs a correct DNS setting), plus the user name, password and an optional remote directory, then enable data export. To upload a SmartLogger to PowerTrack, use the server for your regional instance and the credentials for that site, with File format set to Format 2. Run the report test and confirm the status changes to Success. The Sunny Central UP-US can push using active FTP, passive FTP, FTPS or SFTP. SFTP uses port 22 by default and the other three use port 21.

<!-- review notes
- sentence 8: support check: partial - The four protocols and ports (SFTP 22, others 21) are listed, though the passage layout is jumbled; Passive FTP's port is not clearly stated as 21 beyond ambiguous listing.
-->
