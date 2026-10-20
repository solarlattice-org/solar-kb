---
id: fm:wifi-module-failure
type: FailureMode
name: Wi-Fi module failure
aliases:
- Wi-Fi module faulty
claims:
- claim_id: c1
  rel: affects
  target: comp:wifi-module
  note: The inverter reports that its built-in Wi-Fi module is defective.
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h231
    h: d241890c1ecd
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h314
    h: d241890c1ecd
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:inverter
  note: The Wi-Fi module sits inside the inverter.
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h231
    h: d241890c1ecd
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: sec=h314
    h: d241890c1ecd
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:firmware-update
  note: If the Wi-Fi module update fails, run the update again.
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r4
    h: 622dc8a01f0e
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r4
    h: 622dc8a01f0e
  review: drafted
  review_note: 'support check: partial - Retrying the update is stated for the update-failure message
    (7352), but not as a mitigation for the defective module fault; the firmware update is only a retry
    action.'
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Contact Service if the update-failure message comes back after a retry.
  cite:
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=10.r4
    h: 622dc8a01f0e
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=21.r4
    h: 622dc8a01f0e
  review: drafted
  review_note: 'support check: partial - Contact Service is stated for a repeated update-failure message,
    not for the faulty-module failure itself.'
---
This failure means the Wi-Fi module built into the inverter is defective, and the inverter reports it as a faulty Wi-Fi module. A related event message tells you that an update of the Wi-Fi module did not succeed. While the inverter is still updating the Wi-Fi module, it shows a separate status message, so wait for the update to finish before you judge the result. If the update fails, start it again. If the failure message shows up again after the retry, contact the manufacturer's Service.

<!-- review notes
- sentence 3: support check: partial - 7351 'Update Wi-Fi' status is stated as the updating message, but the passages don't say to wait for it to finish before judging the result.
-->
