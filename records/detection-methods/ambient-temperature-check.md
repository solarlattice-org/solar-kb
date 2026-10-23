---
id: method:ambient-temperature-check
type: DetectionMethod
name: Ambient temperature check
aliases:
- Tamb
- Temp. Ambient
claims:
- claim_id: c1
  rel: produces
  target: meas:ambient-temperature-above-limit
  note: Manuals tie temperature-protection alarms to high ambient readings near the inverter (above 60C
    in Solis/CSI alarm tables); SMA event 8003 guidance refers to a +40°C ambient limit. These are device
    limits, not temperature rises.
  quote: Inverter detects high ambient temperature >60C
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=13.r2
    h: 964e9de8f4f7
  - src: src:csi-csi-manual-50-66ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r3
    h: c82d4746cefc
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=8.r3
    h: c82d4746cefc
  - src: src:sma-kb-event-8003
    loc: sec=h1
    h: e88390fb403b
  - src: src:sma-kb-event-8003-in-terms-of-sunny-tripower-core1-stp50-40-stp50-41
    loc: sec=h1
    h: 0bf710148ab2
  review: drafted
---
An ambient temperature check measures the air temperature near the inverter and compares it with the maximum ambient temperature allowed for that device. It is a standard troubleshooting step when an inverter reports overtemperature shutdowns or thermal derating, as in SMA events 6501, 6502, 6509 and 8003. Do it together with cleaning the cooling fins and air ducts, checking ventilation and clearances, testing the fans, and making sure the inverter is not in direct sun. A high reading confirms that the site conditions are causing inverter overheating. If the temperature is within range, some manuals say the fault lies in the inverter itself and the inverter should be replaced. Readings can come from a dedicated ambient air sensor, a weather station, or a sensor module connected to the inverter. A sensor mounted inside a case that sits in the sun does not read true shaded air temperature. Its readings follow module temperature more closely, so check where the sensor is mounted before trusting the value.

<!-- review notes
- sentence 3: support check: partial - Cleaning fins/ducts, ventilation, fan test, clearance and direct-sun checks appear together across passages, but no single passage combines them all, and the passages don't say to do them 'together' with the ambient check.
- sentence 4: support check: partial - Manuals say 'if temp is in range replace inverter', but no passage says a high reading confirms site conditions cause overheating.
- sentence 5: support check: partial - Passages show an ambient air temperature sensor and an SMA sensor module capturing ambient temperature, but no weather station is mentioned.
-->
