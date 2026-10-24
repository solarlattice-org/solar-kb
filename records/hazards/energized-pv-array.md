---
id: hazard:energized-pv-array
type: Hazard
name: Energized PV array in daylight
aliases:
- PV modules energized when illuminated
- live DC conductors
- up to 90 V DC on module leads
category: Electrical
claims:
- claim_id: c1
  rel: subclass_of
  target: hazard:electric-shock
  note: Sunlight on the PV modules produces a DC voltage high enough to kill, so touching DC conductors
    or live inverter parts can cause a fatal shock.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: sec=h105
    h: 9d17c9026891
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: sec=h106
    h: 9d17c9026891
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h33
    h: 0064bc91228d
  - src: src:sma-stptl-us-10-ia-xx-22
    loc: sec=h88
    h: 0064bc91228d
  - src: src:iec-62446-1
    loc: sec=6.7.1
    h: d2eee856526d
  review: drafted
- claim_id: c2
  rel: controlled_by
  target: tool:insulating-gloves
  note: Wear these when working on or testing energized PV circuits. The PPE level needed depends on the
    circuit voltage and fault current.
  cite:
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=h6
    h: 2d04dbe72872
  review: drafted
- claim_id: c3
  rel: controlled_by
  target: tool:insulated-tools
  cite:
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=h6
    h: 2d04dbe72872
  review: drafted
- claim_id: c4
  rel: controlled_by
  target: tool:lockout-tagout-kit
  note: Work de-energized under documented lockout/tagout wherever that is possible.
  cite:
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=h6
    h: 2d04dbe72872
  - src: src:std-standards-neca-neca-90-15-comm-building-electrical-systems
    loc: sec=3.3
    h: 8fb0e8232bb0
  review: drafted
- claim_id: c5
  rel: controlled_by
  target: tool:hard-hat
  note: The guide calls for a nonconductive Class E hardhat.
  cite:
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=h6
    h: 2d04dbe72872
  review: drafted
- claim_id: c6
  rel: controlled_by
  target: tool:safety-glasses
  cite:
  - src: src:test-cx-manuals-seaward-pv-system-commissioning-and-testing-guide
    loc: sec=h6
    h: 2d04dbe72872
  review: drafted
- claim_id: c7
  rel: controlled_by
  target: mit:rapid-shutdown
  note: Rapid shutdown de-energizes controlled conductors outside the array boundary. On systems that
    shut down only the conductors leaving the array, the conductors inside the array stay energized in
    sunlight.
  cite:
  - src: src:std-standards-nec-2020-nec-2020-690
    loc: sec=h63
    h: d9001d99eb6a
  - src: src:ref-standards-nec-2017-2017-nec-notes-may-26-2017-4-02-pm
    loc: sec=h67
    h: a1a12af4e938
  - src: src:ref-standards-nec-2017-2017-nec-notes-may-26-2017-4-02-pm
    loc: sec=h122
    h: 7b8c30eed428
  review: drafted
---
Whenever light falls on PV modules, the array produces a dangerous DC voltage that can kill. That voltage is on the DC conductors and on live parts inside the inverter. Unlike an AC circuit, the array's DC circuits are live all through daylight and cannot be isolated at the source. Some tasks, such as insulation tests and I-V measurements, therefore have to be done on energized circuits. Microinverter systems carry the same warning: the DC conductors are ungrounded and may be energized when module leads are connected. Do not touch DC conductors, bare cable ends or live inverter parts. Disconnect the inverter from all voltage sources before working on it, and leave installation and fault repair to qualified persons. Work de-energized under lockout/tagout where you can. When you must work live, wear rubber insulating gloves, a Class E hardhat, EH-rated footwear and safety glasses, and use insulated tools. During live testing, keep other people out of the work area, and do not touch module frames, backsheets or terminals while the test is running. Rapid shutdown lowers the shock risk from conductors outside the array. Labels warn, however, that conductors inside the array stay energized in sunlight.

<!-- review notes
- sentence 2: support check: partial - u2 and u13 support live DC circuits that cannot be isolated and unavoidable energized measurements, but I-V measurements are not named explicitly as a live task (u25 only mentions the lethal shock hazard); "at the source" is also a slight paraphrase.
- sentence 3: support check: partial - The DANGER text about ungrounded, possibly energized DC conductors appears in the Enphase microinverter instructions, but the passages do not say it is the "same warning" as for other systems, and "when module leads are connected" is only loosely implied.
- sentence 5: support check: partial - LOTO, gloves, Class E hardhat, EH footwear, safety glasses and insulated tools are all in u13, but "rubber" gloves is not stated, and the passages do not give the live-work PPE set as one directive.
-->
