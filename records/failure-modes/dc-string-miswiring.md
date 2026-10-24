---
id: fm:dc-string-miswiring
type: FailureMode
name: DC string miswiring
aliases:
- cross connection between input A and B
- swapped string connections
- asymmetrical strings at input A
- interchanged cables in DC string box
- wiring error
- wiring mistakes
claims:
- claim_id: c1
  rel: caused_by
  target: stressor:long-dc-string-cables
  note: Designs with many long DC string cables make wiring mistakes more likely.
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h55
    h: 39c3b3bf73e2
  review: drafted
- claim_id: c2
  rel: presents_as
  target: symptom:reverse-polarity
  note: The inverter Reve-DC alarm is raised when a string is connected the wrong way round, or when string
    inputs have different module counts.
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r5
    h: 17bf1b9ad58a
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r10
    h: 8b1a0c30407d
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r6
    h: ae8f6533c032
  review: drafted
- claim_id: c3
  rel: presents_as
  target: symptom:string-reverse-current
  note: The String Current Reflux alarm can come from a string that has fewer modules than the others,
    or from wrong module wiring or configuration.
  cite:
  - src: src:kb-sungrow-fault-alarm-code-1548-1579-fault-alarm-name-string-current-reflux
    loc: sec=h1
    h: a9389cc35d58
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=45.r1
    h: 88548aa7f20a
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=36.r2
    h: bed4b65db7f2
  review: drafted
  review_note: 'support check: partial - Reflux alarm is tied to fewer modules in a string and wiring/configuration
    checks, but ''wrong module wiring'' as a cause is only implied by a check step, and shading/orientation
    are other causes.'
- claim_id: c4
  rel: detected_by
  target: method:polarity-measurement
  note: Use a voltmeter or multimeter to check the polarity of each string between positive and negative.
  cite:
  - src: src:abb-fimer-pvm-75-155-tl-us-user-product-manual-reva
    loc: sec=h166
    h: 1339ff50fb9a
  - src: src:huawei-huawei-sun2000-45ktl-us-hv-d0-user-manual
    loc: fig=129
    h: 60b6ecc4476e
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r5
    h: 17bf1b9ad58a
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r6
    h: ae8f6533c032
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:voc-measurement
  note: Measure the open-circuit voltage of each string and compare it with the expected module count.
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: sec=5.4.3
    h: 3dc8807e6c4b
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: sec=5.4.3.1.1
    h: 7384d8f95a15
  - src: src:kb-sungrow-fault-alarm-code-1548-1579-fault-alarm-name-string-current-reflux
    loc: sec=h1
    h: a9389cc35d58
  review: drafted
  review_note: 'support check: partial - Passages mention measuring VOC and checking string voltage versus
    panel count, but the steps aren''t given and comparison with expected module count is only loosely
    implied.'
- claim_id: c6
  rel: mitigated_by
  target: mit:polarity-correction
  note: Wait until string current falls below the safe level (for example at night), open the DC switches,
    then fix the polarity. Do not disconnect reversed strings while they carry load.
  cite:
  - src: src:abb-fimer-pvm-75-155-tl-us-user-product-manual-reva
    loc: sec=h166
    h: 1339ff50fb9a
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r5
    h: 17bf1b9ad58a
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=13.r10
    h: 8b1a0c30407d
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r6
    h: ae8f6533c032
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Change the system configuration so that all strings on the inputs have the same number of modules.
  cite:
  - src: src:kb-sungrow-fault-alarm-code-1548-1579-fault-alarm-name-string-current-reflux
    loc: sec=h1
    h: a9389cc35d58
  - src: src:sungrow-sg250hx-us-uen-ver17-202203
    loc: tbl=45.r1
    h: 88548aa7f20a
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=36.r2
    h: bed4b65db7f2
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=11.r5
    h: 17bf1b9ad58a
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=15.r6
    h: ae8f6533c032
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:dc-wiring-check
  note: Make sure the DC connection in the inverter is correct and check the string cabling.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h613
    h: d2a22308378b
  - src: src:sma-sbxx-us-1xp-41-ba-en-12
    loc: sec=h311
    h: d2a22308378b
  review: drafted
  review_note: 'support check: partial - Passages say to ensure the DC connection in the inverter is correct
    and check string cabling, but in a damage/fault context rather than specifically miswiring.'
- claim_id: c9
  rel: leads_to
  target: fm:arc-fault
  note: A reversed string can cause severe damage and an electric arc hazard.
  cite:
  - src: src:abb-fimer-pvm-75-155-tl-us-user-product-manual-reva
    loc: sec=h166
    h: 1339ff50fb9a
  review: drafted
---
DC string miswiring means strings are connected wrongly at the inverter: a string is reversed, or strings with different module counts share the inputs. Wiring mistakes are more likely in layouts with many long DC string cables. The inverter may raise a reverse-DC alarm or a string current reflux alarm. To confirm, measure each string with a meter to check polarity and open-circuit voltage, and count the panels in each string. A reversed string can cause severe damage and arcing, so never disconnect it under load or open the DC switches while current flows. Wait until string current is low, for example at night, then open the DC switches and fix the polarity or the module count.

<!-- review notes
- sentence 5: support check: partial - Warning says not to disconnect under load or turn off DC switches until current is below 0.5A, but this applies to reversed input strings; the general framing is slightly broader.
-->
