---
id: method:bus-termination-resistance-check
type: DetectionMethod
name: Communication bus termination resistance check
aliases:
- terminating resistor check
- terminator resistance check
- terminator plug measurement
- COM connector resistance measurement
- 100 ohm termination
- 120-140 ohm between pins
- Communication bus termination check
- Bus termination resistance check
- termination resistance
- termination resistor
- RS-485 bus termination
- 120-ohm resistor placement
- Termination of the communication buses
---
This check confirms that the RS-485 communication bus is terminated correctly. On many inverters the termination is set with a selector or DIP switch on the communication board. The termination resistor is typically 120 ohms. Switching it ON activates it and switching it OFF removes it. The termination must be active on the first and last device of an RS-485 bus. Devices in between should not be terminated. Ideally the terminator matches the cable's characteristic impedance. Most twisted-pair cable falls between 100 and 130 ohms. An unterminated long line reflects signals from its ends. Termination absorbs the signal and reduces these reflections. Bus termination is one of the test points when checking the wiring of communication products, alongside the supply to those products. This helps locate communication bus wiring or termination faults. Termination is a site-by-site decision. It adds load that weakens the signal and changes the bus biasing needs, and it is usually not needed at low baud rates such as 9600 or 19200 bps. Where the monitoring system needs a specific end-of-line resistor placement, get the details from the monitoring supplier.

<!-- review notes
- sentence 1: support check: partial - Passages show termination selector/DIP switches on communication boards, but nothing says a 'check' confirms correct termination.
- sentence 3: support check: partial - First and last device must be terminated is stated, but nothing says intermediate devices should not be terminated.
- sentence 6: support check: partial - u35 lists termination of communication buses and electricity supply as test points, but not the purpose of locating wiring/termination faults.
- sentence 1: review: partial - Many passages show RS485 termination selector or DIP switches on communication boards, but none says what a check is for or that it confirms correct termination.
-->
