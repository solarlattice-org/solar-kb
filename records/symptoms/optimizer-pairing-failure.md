---
id: symptom:optimizer-pairing-failure
type: Symptom
name: Optimizer pairing failure
aliases:
- Pairing failed
- power optimizers not paired
- pairing will fail
claims:
- claim_id: c1
  rel: observed_as
  target: meas:inverter-fault-code-display
  note: When the pairing process fails, the inverter shows an error on its display; repeat pairing and
    follow the power optimizer troubleshooting section.
  cite:
  - src: src:solaredge-solaredge-single-and-three-phase-inverter-user-manual-na
    loc: sec=h112
    h: 80d4e6a24f8f
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
- claim_id: c2
  rel: observed_as
  target: meas:optimizer-paired-count-low
  note: The pairing status shows a POK count of paired optimizers. Optimizers do not produce power until
    they are paired, and after a remote pairing you wait for the next reporting period to confirm that
    every optimizer shows production.
  cite:
  - src: src:se-academy-advanced-monitoring-platform-na-technical-01-remote-troubleshooting-power-optimizers-using-the-moni
    loc: sec=h4
    h: 6a1a2e5ff47f
  - src: src:se-academy-no-call-rma-na-technical-01-no-call-rma
    loc: sec=h33
    h: accc809b1283
  - src: src:se-academy-monitoring-platform-03-remote-power-optimizer-pairing-video
    loc: sec=h1
    h: 53f71e0804f4
  - src: src:solaredge-solaredge-single-and-three-phase-inverter-user-manual-na
    loc: sec=h112
    h: 80d4e6a24f8f
  review: drafted
  review_note: 'support check: partial - The passages support that optimizers don''t produce power until
    paired, the POK ##/## count, and waiting for the next reporting period. They don''t state a low reporting
    count as the observable, or the specific W signals, such as AC power staying at zero.; review: partial
    - The passages support the POK ##/## count, that optimizers produce no power until paired, and waiting
    for the next reporting period after remote pairing, but none says a low count is what a pairing failure
    looks like.'
---
Pairing links each power optimizer to its inverter and starts optimizer operation. Optimizers produce no power until they are paired. If pairing fails, the inverter shows an error, and the system does not start producing power. The usual cause listed is shaded optimizers. Optimizers need power to pair, so pair only in good light, and check for snow cover in winter. If the inverter is connected to the monitoring platform, retry pairing remotely in daylight. Leave the inverter ON/OFF switch on and check that S_OK appears on the status screen. Remote pairing needs the right permissions on the installer account. It takes about 15 to 20 minutes, and you should wait for the next reporting period to confirm that all optimizers show production. Pairing has to be repeated after the string length changes or an optimizer is replaced. Check for earlier replacements and update the serial number in the portal logical layout. If repeated pairing still fails, follow the power optimizer troubleshooting steps and then contact manufacturer support.

<!-- review notes
- sentence 2: support check: partial - The passage says an error is displayed on failure and that optimizers don't produce power until paired. It doesn't explicitly say the system doesn't start producing after a failed pairing.
-->
