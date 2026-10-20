---
id: symptom:communication-loss
type: Symptom
name: Communication loss
aliases:
- Communication failure
- CommErr
- Loss of Megapack Communication
- Loss of Meter Communication
- MIA
claims:
- claim_id: c1
  rel: observed_as
  target: meas:device-mia-flag
  note: Tesla system controller points flag loss of communication with a meter, the Megapack, aggregated
    meters or the islanding controller. The islanding controller flag is set after communication has been
    lost for more than 2 seconds, and a meter MIA clears only after communication has been restored for
    a configurable clear time.
  cite:
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=165.r6
    h: 86f0bcea1070
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=186.r4
    h: 86f0bcea1070
  - src: src:tesla-mp-utility-controls-and-communications-manual-v1-7
    loc: tbl=15.r8
    h: c534de89f579
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=78.r1
    h: 0ab6d41070ff
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=175.r1
    h: dab9093e2063
  - src: src:tesla-controls-and-comms-manual-ci-v1-3
    loc: tbl=60.r12
    h: e1fdd147a53e
  - src: src:tesla-controls-and-communications-manual-ci-v1-5
    loc: tbl=87.r7
    h: 7b29ae16c046
  review: drafted
- claim_id: c2
  rel: observed_as
  target: meas:network-comm-alert
  note: A monitoring-platform rule detects local network failures on devices connected by TCP and RS-485.
    Default communication alerts can include delays so that short, transient dropouts do not trigger notifications.
  cite:
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: tbl=11.r4
    h: 0b0e0447d7ec
  - src: src:alsoenergy-powertrackuserguide-reva-1-25
    loc: sec=h113
    h: 47b893f2dd69
  review: drafted
---
Communication loss means a device stops exchanging data, either inside the inverter or between the inverter, meters, controllers and the monitoring system. For CommErr, first wait 5 minutes to see whether the alarm clears on its own. If it does not, switch the external AC disconnect off and back on to reboot. Contact post-sales service if the alarm is still there. At plant level, controller points flag lost communication with meters, battery units or the islanding controller. Monitoring platforms can raise alerts for local network failures on TCP and RS-485 devices. Set delays on communication alerts so that short dropouts do not cause false alarms. Also check the RS485 communication board and its cabling in the inverter wirebox.

<!-- review notes
- sentence 4: support check: partial - Delays for transient issues are supported, but the passages never advise checking the RS485 board and cabling in the wirebox for communication loss; they only describe the board and interfaces.
-->
