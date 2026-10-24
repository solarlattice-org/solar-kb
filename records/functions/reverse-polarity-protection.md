---
id: func:reverse-polarity-protection
type: Function
name: Reverse polarity protection
aliases:
- DC reverse polarity protection
- Input reverse polarity protection
- Polarity safeguard
category: Protection
function_kind: protection
---
Reverse polarity protection keeps the inverter's DC inputs safe when a PV string is wired with its polarity reversed. In Sunny Tripower TL-US, Sunny Tripower US-50 and STP 50-US-41 / 62-US-41 inverters, SMA implements it with a short-circuit diode. The FIMER TRIO-20.0/27.6-TL-OUTD has it, but the datasheet calls it passive inverter protection only. The Fronius Galvo, Primo and Symo inverters list reverse polarity protection as integrated. The KACO blueplanet 125 TL3 US lists no polarity safeguard, so string polarity must be checked before connecting it.

<!-- review notes
- sentence 2: support check: partial - STP 50-US-41 and 62-US-41 are shown with a short-circuit diode, but the passages don't name Sunny Tripower TL-US or US-50 products, and STP 33-US-41 is blank.
- sentence 5: support check: partial - Polarity safeguard 'no' for the 125 TL3 US is stated, but the instruction to check string polarity before connecting is not in the passages.
-->
