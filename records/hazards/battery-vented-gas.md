---
id: hazard:battery-vented-gas
type: Hazard
name: Vented battery gas
aliases:
- explosive gases
- hydrogen gas
- vented gas
- Vented Gas Hazard
- off-gassing
category: Battery
claims:
- claim_id: c1
  rel: controlled_by
  target: mit:bess-ventilation
  scope:
    standard: std:nfpa-70e-2009
  conditions: Batteries of the vented type; the same limit is also given for VRLA batteries
  quote: Ventilation shall be provided so as to prevent liberated hydrogen gas from exceeding 1 percent
    concentration.
  quote_source: NFPA 70E 2009 §320.4(C)
  cite:
  - src: src:std-standards-nfpa-nfpa-70e-2009
    loc: sec=h108
    h: 54c337885cf9
  review: drafted
- claim_id: c2
  rel: controlled_by
  target: mit:ignition-source-control
  note: Keep open flames, embers, sparks, hot plates, smoking and other ignition sources away from batteries,
    gas vent paths and any place where hydrogen can collect.
  cite:
  - src: src:sma-doc-259761
    loc: sec=h58
    h: 859a589beb2a
  - src: src:sma-doc-278742
    loc: sec=h60
    h: 859a589beb2a
  - src: src:std-standards-neca-neca-90-15-comm-building-electrical-systems
    loc: sec=3.4.3
    h: d5cc3a7e4bb1
  - src: src:sma-doc-244194
    loc: sec=h25
    h: 427d337107bd
  - src: src:sma-doc-278742
    loc: sec=h674
    h: 859a589beb2a
  - src: src:sma-doc-278742
    loc: sec=h714
    h: 859a589beb2a
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h108
    h: 588e1edd3d68
  - src: src:sma-doc-si44m-80h-13-bbf-ia-en-10
    loc: sec=h58
    h: 859a589beb2a
  review: drafted
- claim_id: c3
  rel: controlled_by
  target: mit:proper-installation
  note: Install, operate and maintain the battery as the manufacturer specifies. Do not heat it above
    its permitted temperature or burn it.
  cite:
  - src: src:sma-doc-259761
    loc: sec=h58
    h: 859a589beb2a
  - src: src:sma-doc-278742
    loc: sec=h60
    h: 859a589beb2a
  - src: src:sma-doc-244194
    loc: sec=h25
    h: 427d337107bd
  - src: src:sma-doc-278742
    loc: sec=h674
    h: 859a589beb2a
  - src: src:sma-doc-278742
    loc: sec=h714
    h: 859a589beb2a
  - src: src:sma-doc-si4548-6048-us-be-en-21w
    loc: sec=h108
    h: 588e1edd3d68
  - src: src:sma-doc-si44m-80h-13-bbf-ia-en-10
    loc: sec=h58
    h: 859a589beb2a
  review: drafted
- claim_id: c4
  rel: controlled_by
  target: mit:battery-chemical-hazard-signage
  scope:
    standard: std:nfpa-70e-2009
  note: Signs must warn of hydrogen explosion from open flame and smoking.
  cite:
  - src: src:std-standards-nfpa-nfpa-70e-2009
    loc: sec=h109
    h: d6cbddb6cd6a
  review: drafted
- claim_id: c5
  rel: controlled_by
  target: tool:non-sparking-tools
  scope:
    standard: std:nfpa-70e-2009
  note: Tools used on batteries must be non-sparking, with handles insulated for the maximum working voltage.
  cite:
  - src: src:std-standards-nfpa-nfpa-70e-2009
    loc: sec=h109
    h: d6cbddb6cd6a
  review: drafted
- claim_id: c6
  rel: controlled_by
  target: mit:flame-arrester-vent
  scope:
    standard: std:nfpa-70-2014
  note: Each vented cell needs a flame arrester so that an outside spark or flame cannot ignite the gas
    inside the cell.
  cite:
  - src: src:std-standards-nec-2014-nec2014-480
    loc: sec=h7
    h: 902c886728ba
  - src: src:std-standards-nfpa-nfpa-70e-2009
    loc: sec=h103
    h: 6914dda8d8c3
  review: drafted
- claim_id: c7
  rel: controlled_by
  target: mit:ventilation-airflow-alarm
  scope:
    standard: std:nfpa-70e-2009
  note: Where mechanical ventilation is used, airflow sensors must raise an alarm if the exhaust fan stops
    working.
  cite:
  - src: src:std-standards-nfpa-nfpa-70e-2009
    loc: sec=h108
    h: 54c337885cf9
  review: drafted
- claim_id: c8
  rel: controlled_by
  target: mit:body-static-discharge
  scope:
    standard: std:neca-90-2015
  note: Touch grounded metal first to discharge static from the body before touching batteries.
  cite:
  - src: src:std-standards-neca-neca-90-15-comm-building-electrical-systems
    loc: sec=3.4.3
    h: d5cc3a7e4bb1
  review: drafted
  review_note: 'support check: partial - The passage states the static-discharge instruction, but it comes
    from a different document than the NECA 90 scope, which the passages do not show.'
---
Batteries can release explosive gases, and if these gases are ignited they can explode and cause death or serious injury. Lead-acid batteries release hydrogen as they charge. Hydrogen has no colour or smell, spreads quickly, rises to the highest point of an enclosed space, and burns or explodes across a wide range from 4.1% to 74.2% by volume. Gas can also be released under abnormal conditions such as overheating. If the vented gas builds up near hot parts or another ignition source, the result can be a fire or an explosion. Powin storage manuals warn that off-gassing can create an atmosphere that is hazardous to life and may explode if the space is not properly ventilated. Ventilate battery rooms and enclosures so that hydrogen stays below 1 percent and cannot collect in pockets at the ceiling. If mechanical ventilation is used, fit airflow alarms that trigger when the fan fails. Keep flames, sparks, embers, smoking and hot plates away from batteries and gas paths. Use non-sparking tools, and touch grounded metal to discharge static before touching a battery. Install and maintain batteries as the manufacturer specifies and never heat them above their permitted temperature. Post signs that warn of the hydrogen explosion hazard.

<!-- review notes
- sentence 4: support check: partial - The passage defines the Vented Gas Hazard as a possibly explosive atmosphere if not ventilated, but it does not name Powin or say 'manuals'.
-->
