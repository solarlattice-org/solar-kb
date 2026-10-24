---
id: prog:srec-reporting
type: Program
name: SREC production reporting
aliases:
- SREC registration
- SREC incentive reporting
- Automated Incentive Reporting
- Incentive Reporting Services
category: REC registry
program_kind: incentive
claims:
- claim_id: c1
  rel: issued_by
  target: org:locus-energy
  note: Locus Energy runs an automated incentive reporting team that validates and submits generation
    data to the programs.
  cite:
  - src: src:alsoenergy-kb-incentive-reporting-overview
    loc: sec=front
    h: df01fb209efa
  - src: src:alsoenergy-kb-ma-cec-pts-reporting-setup-guide
    loc: sec=front
    h: 68c8060227a5
  - src: src:alsoenergy-kb-gats-pjm-eis-reporting-setup-guide
    loc: sec=front
    h: 65e27c8bc1d1
  review: drafted
- claim_id: c2
  rel: applies_to
  target: prod:locus-energy-lgate
  note: The LGate production meter records generation at 5 minute intervals and holds about two months
    of data in internal memory.
  cite:
  - src: src:alsoenergy-kb-ma-cec-pts-reporting-setup-guide
    loc: sec=front
    h: 68c8060227a5
  - src: src:alsoenergy-kb-gats-pjm-eis-reporting-setup-guide
    loc: sec=front
    h: 65e27c8bc1d1
  review: drafted
- claim_id: c3
  rel: applies_to
  target: region:us
  note: Covers 11 incentive programs nationwide, including Mass CEC/PTS, PJM/GATS, NEPOOL, WREGIS, the
    CSI utilities and MRETS.
  cite:
  - src: src:alsoenergy-kb-incentive-reporting-overview
    loc: sec=front
    h: df01fb209efa
  review: drafted
- claim_id: c4
  rel: applies_to
  target: region:us-ma
  note: Reporting to the Massachusetts CEC PTS program; Locus must be designated as System Representative.
  cite:
  - src: src:alsoenergy-kb-ma-cec-pts-reporting-setup-guide
    loc: sec=front
    h: 68c8060227a5
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c5
  rel: applies_to
  target: region:pjm
  note: Reporting to GATS PJM-EIS; Locus must be designated as Third Party Reporter.
  cite:
  - src: src:alsoenergy-kb-gats-pjm-eis-reporting-setup-guide
    loc: sec=front
    h: 65e27c8bc1d1
  review: drafted
- claim_id: c6
  attr: warranty_term
  value:
    nominal: 10
    unit: unit:YR
  conditions: Longer of the two incentive reporting subscription contract options; renewal depends on
    the program and its enrollment rules
  cite:
  - src: src:alsoenergy-kb-incentive-reporting-overview
    loc: sec=front
    h: df01fb209efa
  review: drafted
  review_note: 'review: partial - The passage supports a 10-year contract as the longer of two subscription
    options, renewable depending on the program and its enrollment rules, but it describes a service subscription
    contract, not a warranty term, so the ''warranty term'' relation is not…'
---
Locus Energy offers an automated incentive reporting service. It validates and submits SREC generation data for 11 incentive programs across the country and also answers questions about SRECs. Interval data from the revenue-grade production meter is combined into a monthly submission. The program checks the data and then issues SRECs to the account holder. To enroll, register the system with the program, such as Mass CEC PTS or PJM GATS. Name Locus Energy as System Representative or Third Party Reporter, then email the completed reporting setup form to the Locus reporting team. For Massachusetts you also send the Automated Incentive Reporting Contract. The setup form asks for system IDs, the LGate comm device ID, the date in service and installer contact details. Setup forms must arrive by the last business day of the month to be reported for that month. If a form is late, no SRECs are lost, because the next report covers both periods. The LGate stores about two months of data. If it stays offline longer than that, send the reporting team a recent inverter or backup meter reading so the missing generation can be accounted for. Contracts run for five or 10 years and can be renewed, depending on the program.
