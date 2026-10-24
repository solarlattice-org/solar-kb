---
id: concept:type-test
type: Concept
name: Type test and unit certificate
aliases:
- type test report
- unit certificate
- type-tested
- Type Test Reports
- Type Tested Equipment
- type approval
- device certificates
category: Certification
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: comp:mv-transformer
  note: As-built documentation for an MV/LV transformer is expected to include type test reports along
    with routine test reports, factory acceptance test reports and certificates.
  cite:
  - src: src:solarpower-europe-om-guidelines
    loc: sec=h171
    h: b0456e0ede59
  review: drafted
- claim_id: c2
  rel: related_to
  target: std:iec-61646
  note: IEC 61646 covers design qualification and type approval of thin-film terrestrial PV modules.
  cite:
  - src: src:trn-training-utility-scale-power-plants-a-guide-for-investors-and-developers
    loc: tbl=14.r2
    h: 89154f31d654
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:grid-code
  note: The power-generating unit protection test is part of the certificate for existing systems and
    part of the declaration of conformity for new systems. Parameter and accuracy class requirements come
    from grid connection guidelines or from the grid operator.
  cite:
  - src: src:sma-sc-up-scs-up-eze-sg-en-10
    loc: sec=4
    h: f14253b10712
  review: drafted
- claim_id: c4
  rel: related_to
  target: org:sma
  note: SMA posts unit certificates in its download area. The full device test report is available from
    SMA Service if a certifier or grid operator asks for it.
  cite:
  - src: src:sma-kb-unit-certificates-and-test-reports
    loc: sec=h1
    h: 2e8f5736ba5b
  review: drafted
---
A unit certificate is a document showing that a device model was tested and found compliant, and the full type test report holds the detailed test results behind it. Grid operators and system certifiers use these documents when they approve a system, and some ask for the full device test report on top of the unit certificate. Manufacturers such as SMA post unit certificates in their download areas, where you can find them by product family and document type. For PV system certification, the power-generating unit protection test is part of the certificate for existing systems and part of the declaration of conformity for new systems, so the test procedure must be fully documented. As-built documentation for a plant should include type test reports for equipment such as MV/LV transformers, along with routine test reports and certificates. Module standards such as IEC 61646 cover design qualification and type approval of a module design.

<!-- review notes
- sentence 1: support check: partial - The passages mention unit certificates and full test reports, but they don't define a certificate as showing a model was tested and found compliant, or say the report holds the detailed results.
- sentence 1: review: partial - The passages mention unit certificates, whole device test reports and type test reports, but do not define a certificate as proof that a model was tested and found compliant, or say the report holds the detailed results behind it.
-->
