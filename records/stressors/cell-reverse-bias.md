---
id: stressor:cell-reverse-bias
type: Stressor
name: Cell reverse bias
aliases:
- reverse biasing
- reverse bias operation
- reverse voltage
- reverse bias voltage
claims:
- claim_id: c1
  attr: temperature_rise
  value:
    max: 25
    unit: unit:K
  conditions: IBC half-cell module with a built-in Zener-type bypass behaviour, indoor hot-spot test at
    55°C module temperature per IEC 61215-2:2021; hot cell temperature compared with module temperature
  note: The source gives this as at most 25°C above module temperature. PERC and SHJ modules ran hotter
    under the same test. PERC avalanche breakdown below -20 V is a cell property, not a voltage drop,
    so it is not recorded as a quantity.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.4.1
    h: 1046d0084f9f
  review: drafted
---
Cell reverse bias happens when one cell makes less current than the rest of its string, for example because of shading, cracks or mismatch. The other cells then force it to run in reverse, so it absorbs power and heats up instead of producing power. It drives module hotspots and hot cells. In multicrystalline cells the heat collects at local junction breakdown points, while in monocrystalline cells the whole cell area warms evenly. Thin-film and perovskite cells are very sensitive to reverse bias. Junction breakdown forms shunt paths, and the current crowding into them causes point heating that can badly damage the module. Bypass diodes limit how far a cell can be driven into reverse. If a diode fails open, a cell can see a higher reverse voltage than it was designed for, which can cause hotspots, browning, burn marks or even fire. Crystalline silicon cells tolerate reverse bias when the bypass diode protection is well designed. For thin-film modules, bypass diodes may not be able to limit the reverse voltage. Exposure is reduced by sorting cells into current bins, screening out cells with low shunt resistance, fitting bypass diodes, and putting fewer cells on each diode. For thin-film modules, avoid cleaning tools that cast shadows and avoid running a module in short circuit. Look for reverse bias heating with infrared scans under stable, high irradiance while the inverter is running. Then confirm with string current, IV curve shape and a visual check.

<!-- review notes
- sentence 7: support check: partial - The workflow gives IR scan under clear stable conditions with inverter operating and high irradiance, then confirmation by string current, IV curve and visual inspection, but omits comparing against adjacent modules and does not mention reverse bias specifically.
-->
