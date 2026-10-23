---
id: meas:login-lockout-event
type: Measurement
name: Login lockout event
aliases:
- Login via [protocol] locked
- Event 10282
---
On SMA inverters, a login lockout shows up in the event log as event 10282 with a message saying login for a user group over a given protocol is locked. The inverter logs this event after several wrong login attempts in a row and then blocks login for a limited time. The lock lasts 15 minutes for the User login and 12 hours for the Grid Guard login. To clear it, wait until the lock period has run out and then try to log in again.
