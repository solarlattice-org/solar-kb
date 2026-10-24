---
id: concept:register-data-encoding
type: Concept
name: Register data encoding
aliases:
- scale factor
- byte order
- word order
- 32-bit registers
- Data Encoding
- Data Representation
- 32-bit Word Order
- 32-bit Endianness
category: Communication
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: proto:modbus
  note: Modbus defines only 16-bit registers; wider values and scaling are vendor conventions layered
    on top.
  cite:
  - src: src:eq-equip-meters-elkor-wattson-ii-elkor-wattson-manual-pdf
    loc: sec=h45
    h: cba11f518d4d
  - src: src:eq-equip-inverters-chint-50-60-kw-inverter-50-60kw-modbus-map-spec
    loc: sec=h6
    h: 279617a2d2d1
  - src: src:eq-equip-inverters-solaredge-sunspec-implementation-technical-note
    loc: sec=h54
    h: d923f5bc660a
  - src: src:chint-cps-sca100k-t-sca50k-t-modbus-map-2026-02-05
    loc: sec=0.3
    h: '62e288106418'
  - src: src:eq-equip-meters-elkor-wattson-ii-wattson-mark-ii-manual-complete
    loc: sec=6.1.3
    h: 07d610535dff
  review: drafted
- claim_id: c2
  rel: related_to
  target: proto:sunspec-modbus
  note: SunSpec maps carry separate scale-factor registers (e.g. M_AC_PF_SF) and require 32-bit values
    to be written in one transaction.
  cite:
  - src: src:eq-equip-inverters-solaredge-sunspec-implementation-technical-note
    loc: sec=h54
    h: d923f5bc660a
  - src: src:eq-equip-meters-veris-e51cx-full-i0e2
    loc: tbl=26.r4
    h: 8bda84e9df75
  - src: src:eq-equip-meters-veris-e51cx-full-i0e2
    loc: tbl=24.r25
    h: a1dbb7f1aaf3
  review: drafted
  review_note: 'support check: partial - Passages show SunSpec scale-factor registers (M_AC_PF_SF) and
    the single-transaction write requirement, but don''t tie the write rule explicitly to SunSpec.'
- claim_id: c3
  rel: related_to
  target: concept:modbus-addressing
  note: Word order is defined by which register address (lower or higher) holds the high-order word.
  cite:
  - src: src:eq-equip-meters-elkor-wattson-ii-wattson-mark-ii-manual-complete
    loc: sec=6.4.6
    h: 6d3d22565181
  - src: src:eq-equip-meters-elkor-wattson-ii-wattson-mark-ii-manual-complete
    loc: sec=6.1.3
    h: 07d610535dff
  review: drafted
---
Register data encoding is the set of rules a device uses to pack numbers and text into Modbus registers, and the Modbus specification itself only clearly covers 16-bit integers, so vendors differ. A 32-bit value is built from two consecutive registers; by default the register at the lower address usually holds the upper word, but some meters let you flip this word order with a configuration bit. If the word order in your monitoring software does not match the device, 32-bit readings such as energy totals will decode to wrong values. Instead of floating point, many inverters and meters send integers with a scale factor that moves the decimal point, for example a raw 3895 with scale factor -1 means 389.5 V. Some maps use fixed scale values per register or separate scale-factor registers, while others send true floats spanning two registers. Text strings are stored as characters packed two per register, padded or terminated with a null, and unused points return a defined Not Implemented value such as 0xFFFF for an unsigned 16-bit field. When writing a 32-bit setpoint, send both registers in one Write Multiple Registers request rather than two single-register writes.

<!-- review notes
- sentence 3: support check: partial - Passages describe the word-order difference and reversal option but never explicitly state that a mismatch yields wrong decoded values.
- sentence 6: support check: partial - Null padding/termination and Not Implemented 0xFFFF for uint16 are stated, and ASCII fills MSB then LSB (two chars per register), but 'many' packing is only implied by the example.
- sentence 4: review: partial - The scale-factor mechanism and the 3895 with scale factor -1 = 389.5 V example are stated, but only for Chint's CPS protocol, so 'many inverters and meters' goes beyond the passage.
-->
