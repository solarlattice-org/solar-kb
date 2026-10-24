---
id: proto:https-rest-api
type: Protocol
name: HTTPS REST API
aliases:
- REST API
- cloud API
- monitoring API
- RESTful service
- Representational State Transfer
category: Communication
protocol_kind: application
---
An HTTPS REST API is an application-layer web interface. Other software uses it to read data from a monitoring system through predictable, resource-oriented URLs, request parameters and standard HTTP response codes. The SolarEdge Monitoring Platform offers this kind of API at monitoringapi.solaredge.com. It is reachable over HTTPS only and returns results as XML, JSON or CSV. Every SolarEdge API request needs a valid access token, passed as the URL parameter api_key. A site-level key gives access to one system and an account-level key gives access to every site in an account. The Locus Energy v3 API gives programmatic access to LocusNOC data and returns it in JSON format. LocusNOC API credentials, including the client secret, are found under Settings and then API Credentials. Only the admin login can see them. If API access has not been enabled, contact the sales representative. The AlsoEnergy API first takes a username and password at its token endpoint. The returned bearer token then goes in the Authorization header of each data request. On a Tesla Powerpack site, the API is reached by connecting to the Tesla Site Controller over Ethernet on LAN 1. TCP port 10443 must be open, and requests go to the controller IP address on that port under the api path. The FIMER PVM inverter manual lists a REST API among its cloud services, next to Aurora Vision Plant Portfolio Manager. Enphase owners can grant Locus Energy read-only API access to their systems through their Enlighten account.

<!-- review notes
- sentence 5: support check: partial - Settings > API Credentials, admin-only visibility, and contacting sales are supported, but the client secret is hidden until 'show' is clicked; the core claims hold, though 'Only the admin login' is fine; the detail is minor but 'contact sales representative' is fine—main gap is none significant except client secret requires clicking show.
-->
