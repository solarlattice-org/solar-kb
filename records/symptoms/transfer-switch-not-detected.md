---
id: symptom:transfer-switch-not-detected
type: Symptom
name: Transfer switch not detected
aliases:
- no ATS has been detected
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: Generac PWRcell inverter shows wiring error code 0X7720 when it is set up for AC generator integration
    but cannot detect an ATS.
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: tbl=34.r1
    h: 5213cec6a6f6
  review: drafted
---
A Generac PWRcell inverter reports wiring error 0X7720 when it is set up for AC generator integration but cannot find an automatic transfer switch (ATS). The NumTranSwtchs setpoint tells the inverter how many external transfer switches are installed and turns on transfer switch control. It must be 2 for AC generator integration and 1 for AC coupled PV. Check first that the Cat 5 cables for the ATS and the CTs are undamaged and plugged into the correct inverter ports. Then confirm that the ATS limit switch is wired to the Auxiliary Contact port on the PWRcell ATS Controller. The reverse condition, code 0X7721, means an ATS was detected but the inverter is not configured for one. Fix it by setting NumTranSwtchs to match the number of installed ATSes. AC generator integration does not support a single-ATS setup or transfer switches from other manufacturers. Confirm the hardware matches the supported layout.
