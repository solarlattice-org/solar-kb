---
id: symptom:software-version-mismatch
type: Symptom
name: Software version mismatch
aliases:
- Version Mismatch
- Software Version Unmatch
- Vsense Mismatch
- Voltage Sensing Firmware Mismatch
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: 'Shows up as an inverter alarm or event code: Huawei alarm 504 (minor severity), the Yaskawa SGI-XTM
    Vsense Mismatch event (Modbus fault value 3328, hex 0D00), and SMA event 8620, raised when an extension
    cluster runs different firmware from the main cluster.'
  cite:
  - src: src:huawei-huawei-sun2000-25-30ktl-us-user-manual
    loc: tbl=43.r4
    h: 131d1beb27bc
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: tbl=59.r2
    h: 993b6fc1aaf9
  - src: src:yaskawa-sgi-500-750xtm-iom-docr-070506-d
    loc: tbl=33.r5
    h: c659813f867e
  - src: src:yaskawa-modbus-level-9-sgi-xtm-docr-071003-a
    loc: tbl=38.r13
    h: 0ab32af741bb
  - src: src:sma-doc-278742
    loc: tbl=75.r5
    h: f5de6b7cabf9
  - src: src:sma-doc-259761
    loc: tbl=71.r5
    h: acfa537571e5
  review: drafted
---
A software version mismatch is reported by the inverter itself as an alarm or event code, not as a loss of power in the monitoring data. On Huawei SUN2000 string inverters it shows as alarm 504, rated minor. It means the wrong software version was loaded during a software upgrade. On Yaskawa Solectria SGI-XTM central inverters it shows as Vsense Mismatch, which means the wrong voltage-sensing firmware version was used. Over Modbus it is reported as a voltage sensing firmware mismatch fault. On SMA systems, event 8620 reports that at least one extension cluster runs different firmware from the main cluster. First, find out whether a software or firmware upgrade was done recently. If it was, load the correct version again (Huawei) or update the firmware (SMA). Do not confuse Vsense Mismatch with the separate Vsense Error, which points to an internal failure of the voltage sensing circuit. Both Yaskawa events may need an authorized service provider. On Huawei units, a mismatch caused by a wrong version is not the same as Upgrade Failed (alarm 505), which means the upgrade did not finish normally and should be run again. To check the installed versions, read the software version on the inverter display or app version screen. On some units it is also listed in the inverter info menu.

<!-- review notes
- sentence 1: support check: partial - Passages show these are alarm/event codes, but nothing says they are not reported as a loss of power in monitoring data.
- sentence 3: support check: partial - Vsense Mismatch with wrong voltage sensing firmware and the Modbus fault are stated, but the passages don't name the Solectria SGI-XTM central inverter product explicitly.
- sentence 5: support check: partial - Huawei check-for-recent-upgrade then re-upgrade is stated, but SMA only says update the firmware, with no check for a recent upgrade.
-->
