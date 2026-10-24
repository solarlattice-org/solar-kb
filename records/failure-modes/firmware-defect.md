---
id: fm:firmware-defect
type: FailureMode
name: Device firmware defect
aliases:
- Firmware bug
- unexpected behavior of the inverter software
- software bug
- communication interrupt after firmware update
- Firmware failure
- non-existent fault detected
- false triggering
- Modbus TCP communication loss
- Software problem
- Firmware programming failure
claims:
- claim_id: c1
  rel: affects
  target: comp:inverter
  cite:
  - src: src:sma-kb-stpxx-50-communication-interrupt-with-ennexos-portal-after-fw-update
    loc: sec=h1
    h: 9baa54672267
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r14
    h: 62a188b75c86
  review: drafted
- claim_id: c2
  rel: presents_as
  target: symptom:communication-loss
  note: In rare cases, after a firmware update the link between an STPxx-50 inverter and the ennexOS portal
    drops and does not restart by itself.
  cite:
  - src: src:sma-kb-stpxx-50-communication-interrupt-with-ennexos-portal-after-fw-update
    loc: sec=h1
    h: 9baa54672267
  review: drafted
- claim_id: c3
  rel: presents_as
  target: symptom:control-fallback-operation
  note: The communication loss caused by the firmware issue can trigger fall-back modes, if they are configured.
  cite:
  - src: src:sma-kb-stpxx-50-communication-interrupt-with-ennexos-portal-after-fw-update
    loc: sec=h1
    h: 9baa54672267
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c4
  rel: presents_as
  target: symptom:spurious-fault-event
  note: Firmware changelog bugfixes cover false trips of several state codes and false Arc Guard triggering.
  cite:
  - src: src:fronius-fronius-snapinverter-galvo-symo-primo-firmware-changelog
    loc: sec=h213
    h: 422048a9970a
  review: drafted
- claim_id: c5
  rel: leads_to
  target: fm:afci-nuisance-trip
  note: A firmware release reduced false triggering of the Arc Guard.
  cite:
  - src: src:fronius-fronius-snapinverter-galvo-symo-primo-firmware-changelog
    loc: sec=h213
    h: 422048a9970a
  review: drafted
- claim_id: c6
  rel: presents_as
  target: symptom:software-version-mismatch
  note: Extension clusters can run different firmware from the main cluster, or internal devices can carry
    incompatible firmware versions.
  cite:
  - src: src:sma-doc-278742
    loc: tbl=75.r5
    h: f5de6b7cabf9
  - src: src:sma-doc-259761
    loc: tbl=71.r5
    h: acfa537571e5
  - src: src:abb-fimer-pvm-75-155-tl-us-user-product-manual-reva
    loc: sec=h268
    h: 4fa3b4c5c1c3
  review: drafted
- claim_id: c7
  rel: presents_as
  target: symptom:firmware-update-failure
  note: Programming firmware from an SD card can fail, and the update file can be defective or damaged.
  cite:
  - src: src:abb-fimer-pvs-60-tl-us-product-manual-revb
    loc: sec=h173
    h: d427985877e8
  - src: src:sma-doc-259761
    loc: tbl=65.r5
    h: daed1a94a969
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=44
    h: 1f5b39a30613
  review: drafted
- claim_id: c8
  rel: caused_by
  target: stressor:power-supply-interruption
  note: Cutting the DC or AC supply, or pulling the USB stick, during an update can damage the software
    or the device.
  cite:
  - src: src:kaco-kaco-blueplanet-87-0-165-tl3-operating-manual-en-2020-10-siemens-hosted-copy
    loc: sec=h243
    h: 27ad31779984
  review: drafted
  review_note: 'support check: partial - u18 says an interrupted power supply can damage the software
    or device and that the USB stick should not be removed, but it frames this as an update failure and
    not a firmware defect, and the passages do not list AC or DC cut or USB removal as a cause of a firmware
    defect.'
- claim_id: c9
  rel: mitigated_by
  target: mit:firmware-update
  note: For example, version 2.2.12.R or higher fixes the STPxx-50 portal communication issue.
  cite:
  - src: src:sma-kb-stpxx-50-communication-interrupt-with-ennexos-portal-after-fw-update
    loc: sec=h1
    h: 9baa54672267
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r14
    h: 62a188b75c86
  - src: src:sma-doc-278742
    loc: tbl=75.r5
    h: f5de6b7cabf9
  - src: src:sma-doc-259761
    loc: tbl=71.r5
    h: acfa537571e5
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c10
  rel: mitigated_by
  target: mit:retry-update
  note: If the update file is defective, repeat the firmware update.
  cite:
  - src: src:sma-doc-259761
    loc: tbl=65.r5
    h: daed1a94a969
  review: drafted
  review_note: 'review: partial - The row supports repeating the update when the update file is defective,
    but a defective update file is a failed update, not clearly a defect in the device firmware, so the
    mitigation link to this failure mode is only loosely…'
- claim_id: c11
  rel: mitigated_by
  target: mit:inverter-restart
  note: For a software problem code, an AC reset (switching the circuit breaker off and on) is the first
    remedy.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r14
    h: 62a188b75c86
  review: drafted
- claim_id: c12
  rel: detected_by
  target: method:inverter-data-log-export
  note: Check the event logs and the installed firmware version to confirm whether an update finished
    and how communication behaved.
  cite:
  - src: src:sma-kb-communication-problem-to-3rd-party-monitoring-modbus-tcp
    loc: sec=h1
    h: 234a5b21f1c1
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h260
    h: dea7e0f7a51b
  review: drafted
  review_note: 'support check: partial - u9 asks for the inverter event logs and the installed firmware
    version, and u22 says to check the events to see whether a firmware update completed, but the passages
    do not frame this as detecting a firmware defect, and u9 does not tie it to confirming an update.'
- claim_id: c13
  rel: distinguished_from
  target: fm:monitoring-network-fault
  by: method:communication-test
  note: Switch the Modbus TCP server parameter off and back on. If communication returns, the problem
    is limited to Modbus TCP. If it stays down, check the network cabling and RJ45 connections.
  cite:
  - src: src:sma-kb-communication-problem-to-3rd-party-monitoring-modbus-tcp
    loc: sec=h1
    h: 234a5b21f1c1
  review: drafted
  review_note: 'support check: partial - u9 describes toggling the Modbus TCP Server parameter to check
    whether the problem is limited to Modbus TCP and mentions checking network cabling, but it does not
    compare this with a firmware defect or say that persistent loss means checking the RJ45 connections.'
---
A firmware defect is a fault in the device software that makes an inverter behave wrongly even when its hardware is fine. It can show up as communication to the monitoring portal dropping after a firmware update and not coming back by itself, which may also trigger configured fall-back modes. Other signs include false trips of fault codes or of the arc fault detector, a software-problem code with no grid feed-in, and firmware versions that do not match between devices or clusters. Check the event log and the installed firmware version to confirm. For Modbus TCP loss, switch the Modbus TCP server parameter off and on to see whether the issue is software-side before you check the cabling. The usual fix is an AC reset and then updating to the firmware version that corrects the bug. If the update file is defective, repeat the update. Never cut DC or AC power or pull the USB stick during an update, because that can damage the software or the device. An internal communication error shown during a firmware update is normal and is not a fault.

<!-- review notes
- sentence 1: support check: partial - u38 and u35 show software problems and bugfixes that cause wrong behavior, but nothing says the hardware is fine or defines a firmware defect.
- sentence 4: support check: partial - u9 and u22 support checking event logs and firmware version and toggling the Modbus TCP server before checking cabling, but the passages do not say that toggling shows whether the issue is software-side.
- sentence 5: support check: partial - u38 gives an AC reset followed by a firmware update, and u4 says to repeat the update for a defective file, but calling this the usual fix for every firmware defect goes beyond the passages.
- sentence 1: review: partial - The passages show software problems and firmware bugs causing false trips and no feed-in, but nothing says the hardware is fine or defines a firmware defect.
- sentence 4: review: partial - The SMA article supports collecting event logs and the firmware version, and toggling Modbus TCP Server On before checking cabling, but it says the toggle tests whether the problem is only with Modbus TCP communications, not whether it is software-side.
-->
