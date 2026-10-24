---
id: prog:pjm-gats
type: Program
name: PJM GATS
aliases:
- Generation Attribute Tracking System
- PJM-GATS
- GATS-PJM
- GATS PJM-EIS
- GATS
category: REC registry
program_kind: incentive
claims:
- claim_id: c1
  rel: issued_by
  target: org:pjm-eis
  note: Production data is submitted monthly to the GATS PJM-EIS program, which uses it to award renewable
    energy certificates.
  cite:
  - src: src:alsoenergy-kb-gats-pjm-eis-reporting-setup-guide
    loc: sec=front
    h: 65e27c8bc1d1
  review: drafted
  review_note: 'support check: partial - Monthly submission to GATS PJM-EIS to award RECs is stated, but
    the passages never say PJM GATS is issued by PJM Environmental Information Services (org:pjm-eis);
    they only use the name PJM-EIS.'
---
PJM GATS is an incentive tracking program. It takes monthly solar production data and awards renewable energy certificates (SRECs) to the account holder of each registered system. The system must first be registered with the GATS PJM program. During registration, a monitoring company such as Locus Energy can be named as the Third Party Reporter. The registration approval letter gives a five-digit Generator ID for the system and a separate Account ID that the SRECs are paid into. A revenue-grade production meter logs generation. The reporter then combines the data and submits it monthly, and the program checks it before issuing SRECs. To confirm that a third party will report for the system, log into the PJM GATS portal and check that the reporter is designated there. If the monitoring device is offline for more than two months, contact a GATS administrator. Ask whether they will accept a backup dome meter reading to cover the lost generation.
