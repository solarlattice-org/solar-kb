---
id: symptom:rapid-shutdown-failure
type: Symptom
name: Rapid shutdown failure
aliases:
- Error in Rapid Shutdown System
claims:
- claim_id: c1
  rel: observed_as
  target: meas:high-disconnect-standby-voltage
  note: Event 9034 lists as one cause a summed standby voltage of the PV array disconnect switches in
    a string above 30 V. The manual requires that sum to stay below 30 V for safe DC line discharge.
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12.r2
    h: a15113bcec60
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=23.r2
    h: a15113bcec60
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=12
    h: f5135afff656
  - src: src:sma-sma-stp-33-us-iom
    loc: sec=h79
    h: e0da560c67b6
  review: drafted
---
The SMA inverter reports a rapid shutdown failure as event 9034, Error in Rapid Shutdown System. It reports event 9038 when the redundant rapid shutdown discharge function is not ensured. Possible causes of event 9034: the Rapid Shutdown function is set up wrong, the PV array could not be disconnected so voltage may still be on the DC inputs, or the summed standby voltage of a string's disconnect switches is above 30 V. First, check that the Rapid Shutdown operating mode matches the DC disconnection unit installed. Then check that the PV array disconnect switches work and measure their standby voltage. A complete rapid shutdown system needs the inverter, PV array disconnect switches and an initiation device. Together they must bring the DC conductors below 30 V within 30 seconds. If the function is enabled but no disconnect switches are installed, the inverter cannot discharge the DC input conductors and may be damaged. The function is disabled by default. With SunSpec signalling, every module on the inverter needs a SunSpec-compliant disconnect switch. Otherwise the inverter cannot start feeding in. Event 9038 cannot be fixed in the field: the manufacturer's Service team has to find the cause.

<!-- review notes
- sentence 3: support check: partial - The corrective measures list these checks, but the passages don't state an order ('first... then'), and 'measure' is a mild paraphrase of 'check'.
- sentence 7: support check: partial - The passages say the cause must be determined by the Service, but 9038 also lists checking the SunSpec switches' functionality, and nothing says it can't be fixed in the field or names the manufacturer's team.
-->
