---
id: fc:canadian-solar-75-100k-t480gl02-inifault
type: FaultCode
name: Canadian Solar 75-100K-T480GL02 INI-FAULT
aliases:
- INI-FAULT
- inifault
- Canadian Solar INI-FAULT
- Initialization Protect ion
category: Inverters
make: canadian-solar
make_name: Canadian Solar
model_family: 75-100k-t480gl02
family_name: CSI-75/80/90/100K-T480GL02-U
code: INI-FAULT
code_key: inifault
display_message: Initialization Protect ion
page: 36
claims:
- claim_id: c1
  rel: defined_in
  target: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
  cite:
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r1
    h: eed118aa3df4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-device-fault
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r2
    h: eed118aa3df4
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r2
    h: eed118aa3df4
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r1
    h: eed118aa3df4
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r1
    h: a8241047b34f
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:digital-signal-processor
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r2
    h: eed118aa3df4
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r2
    h: eed118aa3df4
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r1
    h: eed118aa3df4
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r2
    h: eed118aa3df4
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r2
    h: eed118aa3df4
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r1
    h: eed118aa3df4
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r1
    h: a8241047b34f
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Only if restart does not clear the mismatch between the two processors.
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r2
    h: eed118aa3df4
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r2
    h: eed118aa3df4
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r1
    h: eed118aa3df4
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r2
    h: eed118aa3df4
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r1
    h: a8241047b34f
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
  review_note: 'support check: partial - Rows describe an initialization system fault needing restart,
    but nothing explicit about stopping; fault class is only implied.'
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Restart by DC switch power cycle first; replacement or installer contact if it persists.
  cite:
  - src: src:csi-csi-installation-manual-25-40k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=12.r2
    h: eed118aa3df4
  - src: src:csi-csi-installation-manual-50-66k-t480gl01-ub-lsw-usa-v1-1
    loc: tbl=14.r2
    h: eed118aa3df4
  - src: src:csi-csi-installation-manual-75-100k-t480gl02-u-usa-v1-1-20211116
    loc: tbl=10.r1
    h: eed118aa3df4
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r1
    h: a8241047b34f
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
