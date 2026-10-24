---
id: method:inverter-data-log-export
type: DetectionMethod
name: Inverter event and data log export
aliases:
- Export events
- Event data file
- Data logging
- Service data logging
- Exporting plant data
- Parameter list export
- Parameter export
- Inverter Log
- Device logs
- Export Inverter Data
---
This method pulls the production data, event history and parameter list out of an inverter so they can be used for troubleshooting, monitoring or a warranty case. On inverters with a web user interface, log in as Installer or User and open the Events menu. Set the Information, Warning and Error filters as needed, then press Export events. To save the parameter set, use Device Parameters and its export button. To save measured values or service files, choose them under Data and use Export data. On inverters without a built-in web server, the PC tool can export daily files, monthly files or events as CSV. Some vendor mobile apps can export inverter alarm and performance logs and send them by email. Some inverters can also run an I-V curve measurement for each MPP tracker and export it as a PDF report or a CSV file. The CSV holds every measured data point. A plant controller has limited internal memory and deletes older data when space runs low, so copy the data to external storage, FTP or a portal at regular intervals. Set the inverter clock correctly first, because logging depends on it. Keep in mind that the accuracy of AC values recorded by an inverter is often unknown, and a data logger may average or resample the data before it reaches a database. Data loggers should record all inverter alarms in the manufacturer's own format, so that no information is lost.

<!-- review notes
- sentence 6: support check: partial - u15 supports limited memory, deletion of older data and saving to external memory, FTP or Sunny Portal, but only for the Cluster Controller with specific thresholds (10%/20%), and 'regular intervals' is stated only as advice to save externally.
-->
