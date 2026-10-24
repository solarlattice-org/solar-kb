---
id: fm:battery-thermal-management-failure
type: FailureMode
name: Battery thermal management failure
aliases:
- Battery system thermal management defective
- Battery system heating procedure unsuccessful
- battery heating failure
- Thermal management of battery system
- Event 9353
- battery system heating procedure
claims:
- claim_id: c1
  rel: affects
  target: comp:battery-storage
  cite:
  - src: src:kb-sma-sixx-20-us-event-messages
    loc: sec=h60
    h: 66024105cc48
  - src: src:kb-sma-stpsxxus-20-event-messages
    loc: sec=h68
    h: 66024105cc48
  - src: src:sma-kb-event-9353-with-sbsx-x-us-10
    loc: sec=h1
    h: 40e2ed92ca3f
  review: drafted
- claim_id: c2
  rel: caused_by
  target: fm:firmware-defect
  note: The SMA knowledge base says event 9353 most likely comes from a battery firmware issue.
  cite:
  - src: src:sma-kb-event-9353-with-sbsx-x-us-10
    loc: sec=h1
    h: 40e2ed92ca3f
  review: drafted
- claim_id: c3
  rel: presents_as
  target: symptom:battery-error
  note: Shows on the storage inverter as event 9353, which points to a problem with the battery.
  cite:
  - src: src:sma-kb-event-9353-with-sbsx-x-us-10
    loc: sec=h1
    h: 40e2ed92ca3f
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:firmware-update
  note: Check whether the battery has newer firmware and install it. For BYD systems, battery firmware
    should be 3.013.C or later.
  cite:
  - src: src:kb-sma-sixx-20-us-event-messages
    loc: sec=h60
    h: 66024105cc48
  - src: src:kb-sma-stpsxxus-20-event-messages
    loc: sec=h68
    h: 66024105cc48
  - src: src:sma-kb-event-9353-with-sbsx-x-us-10
    loc: sec=h1
    h: 40e2ed92ca3f
  - src: src:sma-kb-event-9354-with-sbsx-x-10-us-10
    loc: sec=h1
    h: aaf5531ba5c2
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Contact the Service if the message comes back after the update, or contact the battery manufacturer
    for next steps.
  cite:
  - src: src:kb-sma-sixx-20-us-event-messages
    loc: sec=h60
    h: 66024105cc48
  - src: src:kb-sma-stpsxxus-20-event-messages
    loc: sec=h68
    h: 66024105cc48
  - src: src:sma-kb-event-9353-with-sbsx-x-us-10
    loc: sec=h1
    h: 40e2ed92ca3f
  - src: src:sma-kb-event-9354-with-sbsx-x-10-us-10
    loc: sec=h1
    h: aaf5531ba5c2
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-installer
  note: System owners are told to contact their installer.
  cite:
  - src: src:sma-kb-event-9353-with-sbsx-x-us-10
    loc: sec=h1
    h: 40e2ed92ca3f
  - src: src:sma-kb-event-9354-with-sbsx-x-10-us-10
    loc: sec=h1
    h: aaf5531ba5c2
  review: drafted
---
The system that controls the battery's temperature has reported itself as defective. On SMA storage inverters it shows as event 9353, which points to a problem with the battery. A related event says the battery heating procedure did not succeed. The usual cause is the battery firmware, so first check whether newer battery firmware is available and install it. For BYD batteries, the firmware should be version 3.013.C or later. If the message comes back after the update, contact the Service or the battery manufacturer. Owners should contact their installer.
