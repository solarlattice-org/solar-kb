---
id: comp:rapid-shutdown-device
type: Component
name: Module-level rapid shutdown device
aliases:
- RSD
- SunSpec Rapid Shutdown device
- module-level rapid shutdown
- module-level shutdown device
- TS4-R
- TS4-R-F
- rapid shutdown module
- PV isolation switch
- Rapid Shutdown Devices (RSDs)
- MLRSD
- PV Rapid Shutdown Device
- PV array disconnect switches
- PV module switch
- rapid shutdown receivers
- MLPE
claims:
- claim_id: c1
  attr: output_limit
  value:
    max: 0.6
    unit: unit:V
  conditions: Module output when rapid shutdown receivers stop getting the keep-alive signal and go into
    shutdown mode (Yaskawa Solectria PVI RSD wire box systems)
  cite:
  - src: src:yaskawa-pvi-25tl-208-36tl-v2-50-60tl-iom-docr-071086-c
    loc: sec=h32
    h: 1f1fbca75b2a
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c2
  attr: output_limit
  value:
    nominal: 0.6
    unit: unit:V
  conditions: Voltage measured across one PV panel with a Tigo TS4-R-F attached, before string connection
    and with no SunSpec permission-to-operate signal present
  note: The source expects a string of 10 such assemblies to read about 6 Vdc before commissioning.
  cite:
  - src: src:sma-kb-installing-tigo-ts4-r-f-rapid-shutdown-devices-onto-pv-panels
    loc: sec=h1
    h: 32d44e3827b9
  review: drafted
  review_note: 'support check: partial - The 0.6 Vdc per assembly and ~6 Vdc for 10 assemblies are stated,
    but the passage doesn''t say ''no SunSpec permission-to-operate signal present'' and it is a nominal
    reading, not a limit.; review: partial - The SMA passage gives 0.6 Vdc (nominal) per panel/TS4 assembly
    before stringing and about 6 Vdc for 10 assemblies, but it never mentions the absence of a SunSpec
    permission-to-operate signal, and it presents 0.6 V as an expected nominal reading…'
---
A module-level rapid shutdown device is a small unit fitted to each PV module. It brings module voltage down to a safe level so firefighters face less shock hazard. The inverter has a power line communication transmitter that sends a keep-alive or permission-to-operate signal over the DC string conductors. The devices let string voltage build only while they receive that signal. Opening the AC disconnect or breaker, losing the grid, or pressing the inverter's rapid shutdown switch stops the signal, and every device then switches into shutdown mode. Relevant requirements are NEC 690.12 and CSA C22.2 No. 330. Signalling may follow the SunSpec specification, and inverters are listed as PV rapid shutdown equipment under UL 1741. Always attach the device to its module before the module is wired into a string. Attaching it to a module that is already in a string can permanently damage the device through overvoltage. Selecting the wrong rapid shutdown mode is a common setup fault. For example, TS4-R-F devices need SunSpec Shutdown, and this setting should only be chosen after the strings are connected. With SunSpec shutdown, every module on the inverter must have a compliant device or the inverter cannot start feeding in. If rapid shutdown is enabled with no devices installed, the inverter can be damaged. Devices are matched to specific transmitters, so check the inverter maker's compatibility listing and follow the device maker's installation instructions.

<!-- review notes
- sentence 1: support check: partial - Passages support bringing panel voltage to a safe level to reduce firefighter shock hazard, but 'small unit fitted to each PV module' is not clearly stated (one canadian solar item is optional product; others mention RSDs on modules).
- sentence 6: support check: partial - TS4-R-F needing SunSpec Shutdown, set after strings are connected is stated, but the claim that wrong mode selection is a 'common setup fault' is not in the passages.
- sentence 1: review: partial - The passages back bringing panel voltage to a safe level to cut shock hazard for firefighters, but none say the device is a small unit fitted to each PV module.
-->
