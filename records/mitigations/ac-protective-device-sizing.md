---
id: mit:ac-protective-device-sizing
type: Mitigation
name: AC protective device sizing
aliases:
- breaker rating 1.2x max AC output current
- breaker ambient derate
- external Type A RCD rating
- upsize circuit breaker
- one breaker per inverter
- 100% rated breaker
- Circuit Breaker Selection
- enclosure shading/orientation
- OCPD
- Over-Current Protection Device
- AC circuit breaker
- Load protection breaker
- AC disconnect switch
- AC Breaker Selection
claims:
- claim_id: c1
  attr: temperature_rise
  value:
    nominal: 28
    unit: unit:K
  conditions: Temperature inside an AC circuit breaker enclosure above outside air temperature, recorded
    at one typical Florida site in July
  note: The rise depends on enclosure color, which way it faces the sun, and heat from breakers and conductors.
    Enclosures with their largest faces toward east and west tend to gain the most solar heat in the evening.
    At this site the enclosure interior reached 60 °C, giving a worst-case breaker derate of 81%.
  cite:
  - src: src:chint-cps-3phs-inverter-site-design-guidelines
    loc: sec=h1
    h: 6bc3042240d9
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
This action means choosing the right overcurrent and leakage protection for the inverter's AC output, usually a circuit breaker and, where required, an external residual current device. Its main purpose is to prevent AC breaker thermal nuisance tripping, where a breaker trips in hot weather because its rating was not derated for the temperature inside its enclosure. Rate the breaker at 1.2 times the inverter's maximum AC output current, and avoid breakers that have their own built-in current protection. Derate the breaker for the air temperature inside its enclosure, not the outside air temperature. Enclosure color, which way it faces the sun, and heat from the breakers and conductors all push the inside temperature up. Breakers should never run above 70 °C, and their terminals are typically rated at 75 °C. In one Florida example, temperature derating meant a 60kW inverter needed a 125A breaker. Use the manufacturer's breaker tables where they exist. Examples: a 3-pole, 600 V, bi-directional thermal-magnetic breaker rated 100 A for the PVS-60, a 100 A 3-pole breaker for the PVI 25TL, and a 60 A breaker for the PVI 36TL. For several Solis single-phase inverters, the recommended external residual current device is Type A rated at 100mA. Published breaker ratings assume one inverter per breaker. Thermal and other derating factors for the actual site still have to be applied on top.

<!-- review notes
- sentence 1: support check: partial - Passages recommend over-current and leakage protection for the inverter, but they don't say it is usually a circuit breaker plus an external RCD where required.
- sentence 2: support check: partial - Derating to prevent nuisance tripping in high temperatures is stated, but 'main purpose' framing of this action is somewhat inferred; the core is present.
- sentence 1: review: partial - The passages back choosing overcurrent and leakage protection for the inverter AC side, and they mention a breaker, but none of the cited passages mentions an external residual current device.
-->
