---
id: fm:backup-unit-fault
type: FailureMode
name: Automatic backup unit fault
aliases:
- Backup module error
- Automatic Backup Unit error
- backup box hardware error
- backup module relay error
- backup module installation error
- backup module faulty configuration
- Automatic transfer switching device error
- Backup module bimetal switch
claims:
- claim_id: c1
  rel: affects
  target: comp:transfer-relay
  note: 'Event 9208: relay in the automatic transfer switching device is faulty.'
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c2
  rel: affects
  target: comp:transfer-switch-controller
  note: SMA Backup Unit Controller installed in the automatic transfer switch.
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  review: drafted
- claim_id: c3
  rel: caused_by
  target: fm:relay-failure
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  review: drafted
- claim_id: c4
  rel: caused_by
  target: stressor:installation-error
  note: SPS IN and SPS OUT cables miswired or swapped; installation of the transfer device to be checked
    on overtemperature.
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  - src: src:kb-sma-bu-slct-us-50-troubleshooting
    loc: tbl=1.r3
    h: 53638835c842
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: tbl=18.r3
    h: c7b40a34efa6
  - src: src:kb-sma-bu-slct-us-50-troubleshooting
    loc: sec=h1
    h: 5233ab3eb379
  review: drafted
- claim_id: c5
  rel: caused_by
  target: stressor:inverter-settings
  note: Backup type parameter not set to automatic backup operation, or switch-on delay not yet elapsed.
  cite:
  - src: src:kb-sma-bu-slct-us-50-troubleshooting
    loc: tbl=1.r3
    h: 53638835c842
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: tbl=18.r3
    h: c7b40a34efa6
  - src: src:kb-sma-bu-slct-us-50-troubleshooting
    loc: sec=h1
    h: 5233ab3eb379
  review: drafted
- claim_id: c6
  rel: presents_as
  target: symptom:backup-mode-unavailable
  cite:
  - src: src:kb-sma-bu-slct-us-50-troubleshooting
    loc: tbl=1.r3
    h: 53638835c842
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: tbl=18.r3
    h: c7b40a34efa6
  - src: src:kb-sma-bu-slct-us-50-troubleshooting
    loc: sec=h1
    h: 5233ab3eb379
  review: drafted
- claim_id: c7
  rel: presents_as
  target: symptom:transfer-switch-transfer-failure
  note: Device does not switch on grid failure, or switches but backup loads stay unpowered.
  cite:
  - src: src:kb-sma-bu-slct-us-50-troubleshooting
    loc: tbl=1.r3
    h: 53638835c842
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: tbl=18.r3
    h: c7b40a34efa6
  - src: src:kb-sma-bu-slct-us-50-troubleshooting
    loc: tbl=1.r2
    h: 09c03201685a
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: tbl=18.r2
    h: 863af509f134
  review: drafted
- claim_id: c8
  rel: presents_as
  target: symptom:backup-unit-overtemperature
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  review: drafted
- claim_id: c9
  rel: presents_as
  target: symptom:communication-loss
  note: Communication between inverter and Backup Unit Controller disrupted.
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  review: drafted
- claim_id: c10
  rel: presents_as
  target: symptom:firmware-update-failure
  note: Backup Unit Controller update failed.
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  review: drafted
- claim_id: c11
  rel: presents_as
  target: symptom:backup-ac-overvoltage
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r8
    h: bcf28adc0525
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r8
    h: bcf28adc0525
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r18
    h: 1f509fcb78de
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r18
    h: 1f509fcb78de
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r18
    h: 1f509fcb78de
  review: drafted
  review_note: 'support check: partial - OV-Vbackup backup overvoltage messages exist, but they are inverter
    alarms and the passages do not tie them to the automatic backup unit fault.; review: partial - The
    Solis rows describe a backup overvoltage (OV-VBackup) alarm on the inverter''s backup port, but none
    of them connect it to an automatic backup unit or transfer switch fault.'
- claim_id: c12
  rel: detected_by
  target: method:backup-transition-test
  note: Simulate a grid failure by switching off the pre-meter fuse and listen for the transfer click.
  cite:
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: sec=h85
    h: d64eb21249a5
  review: drafted
- claim_id: c13
  rel: detected_by
  target: method:communication-test
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  review: drafted
- claim_id: c14
  rel: mitigated_by
  target: mit:external-fuse-check
  note: Check transfer device fuses; B6 pre-fuse and monitoring relay pre-fuse must be switched on.
  cite:
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: tbl=18.r6
    h: 37782d83b92e
  - src: src:kb-sma-bu-slct-us-50-troubleshooting
    loc: tbl=1.r6
    h: ac7d628f14eb
  - src: src:kb-sma-bu-slct-us-50-troubleshooting
    loc: tbl=1.r3
    h: 53638835c842
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: tbl=18.r3
    h: c7b40a34efa6
  - src: src:kb-sma-bu-slct-us-50-troubleshooting
    loc: sec=h1
    h: 5233ab3eb379
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: tbl=18.r5
    h: c030ffda712e
  review: drafted
  review_note: 'support check: partial - Checking transfer device fuses, the B6 pre-fuse and the monitoring
    relay pre-fuse appear, but the B6 passages describe backup continuing after grid return, not a cause
    of this fault.'
- claim_id: c15
  rel: mitigated_by
  target: mit:communication-cable-check
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  review: drafted
- claim_id: c16
  rel: mitigated_by
  target: mit:inverter-settings-review
  cite:
  - src: src:kb-sma-bu-slct-us-50-troubleshooting
    loc: tbl=1.r3
    h: 53638835c842
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: tbl=18.r3
    h: c7b40a34efa6
  - src: src:kb-sma-bu-slct-us-50-troubleshooting
    loc: sec=h1
    h: 5233ab3eb379
  review: drafted
- claim_id: c17
  rel: mitigated_by
  target: mit:firmware-update
  note: Inverter firmware 3.12.15.R or later needed to set backup parameters.
  cite:
  - src: src:kb-sma-bu-slct-us-50-troubleshooting
    loc: tbl=1.r3
    h: 53638835c842
  - src: src:sma-doc-smabackupselect-ia-en-11
    loc: tbl=18.r3
    h: c7b40a34efa6
  - src: src:kb-sma-bu-slct-us-50-troubleshooting
    loc: sec=h1
    h: 5233ab3eb379
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c18
  rel: mitigated_by
  target: mit:wiring-terminal-check
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r18
    h: 1f509fcb78de
  - src: src:kb-sma-bu-slct-us-50-troubleshooting
    loc: tbl=1.r3
    h: 53638835c842
  - src: src:solis-solis-manual-s6-eh2p-9-6-16-k-sv-yd-l-us-v2-7-20260305
    loc: tbl=19.r18
    h: 1f509fcb78de
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=26.r18
    h: 1f509fcb78de
  review: drafted
- claim_id: c19
  rel: mitigated_by
  target: mit:backup-load-reduction
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=29.r15
    h: 3c5c09781487
  - src: src:solis-solis-manual-s6-eh3p-30-60-k-nv-yd-h-us-21a-v1-0-20260908
    loc: tbl=28.r16
    h: 3c5c09781487
  review: drafted
  review_note: 'support check: partial - Reducing backup loads appears for backup short circuit and LLC
    overcurrent, not directly for the automatic transfer switch fault.'
- claim_id: c20
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:solis-solis-manual-rhi-1p-5-10-k-hv-usa-v1-1
    loc: tbl=10.r8
    h: bcf28adc0525
  - src: src:solis-solis-manual-s6-eh1p-3-8-11-4-k-h-us-v-5-6-20260413
    loc: tbl=14.r8
    h: bcf28adc0525
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=27.r18
    h: 1f509fcb78de
  review: drafted
  review_note: 'support check: partial - Restarting the inverter appears only for the OV-Vbackup alarm,
    not as a general mitigation for the transfer unit fault.'
- claim_id: c21
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Contact the manufacturer of the automatic transfer switching device for relay, bimetal switch
    or N-PE monitoring errors.
  cite:
  - src: src:kb-sma-sbsxx-us-10-event-messages
    loc: sec=h1
    h: a056be6df42b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
This fault covers problems in the automatic transfer switch or backup module that moves loads to the battery-backup supply when the grid fails. Typical signs are event messages for a faulty relay, the bimetal switch, N-PE monitoring, overtemperature, or lost communication with the backup unit controller. In the field, the switch may not transfer when the grid fails, or it may click over while the backup loads still get no power. To confirm, simulate a grid failure by switching off the pre-meter fuse, wait for the set delay and listen for the transfer click. Check the transfer switch fuses and the B6 pre-fuse, make sure the backup type is set to automatic backup operation, and make sure the SPS IN and SPS OUT cables are not swapped. Check that the communication cable meets its requirements, then run a communication test; for backup overvoltage, check the backup port wiring and restart. If the relay or other hardware in the transfer switch is faulty, contact the manufacturer of the switching device.
