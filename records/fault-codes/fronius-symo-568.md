---
id: fc:fronius-symo-568
type: FaultCode
name: Fronius Symo 568
aliases:
- '568'
- Fronius 568
- Incorrect input signal at the multifunctional power interface
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '568'
code_key: '568'
display_message: Incorrect input signal at the multifunctional power interface
vendor_severity: Class 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r15
    h: 90247f520522
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h23
    h: c4a64ba354f6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:invalid-external-signal
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r15
    h: 90247f520522
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:io-module
  note: Multifunction power interface and the devices connected to it.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r15
    h: 90247f520522
  review: drafted
  review_note: 'support check: partial - The multifunctional power interface and connected devices are
    named, but ''I/O module'' is only implied.'
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  note: Applies when the signal input trigger type is set to warning.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r15
    h: 90247f520522
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Acknowledge and check connected devices; if it persists, contact the installer.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r15
    h: 90247f520522
  review: drafted
  review_note: 'support check: partial - Acknowledge and check devices are stated, but the contact-installer
    note is not in the passage.'
---
