---
id: fm:grid-code-misconfiguration
type: FailureMode
name: Incorrect or unset grid code
aliases:
- wrong country data set
- country data set not set
- No country data set set
- wrong grid type
- country code not set
- no country data set
- incorrect country setup
- SMA default
- country data set
- grid type
- country standard
- Grid code
- country code
claims:
- claim_id: c1
  rel: affects
  target: comp:inverter
  note: The grid code or country data set is an inverter parameter (for example Set country standard under
    Grid monitoring).
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=24.r1
    h: 08b17e435759
  - src: src:sma-doc-259761
    loc: sec=h323
    h: d68178149130
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: tbl=34
    h: 46801c51f609
  - src: src:sma-doc-280451
    loc: tbl=3.r1
    h: d352f96fc19c
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:installation-error
  note: The installer picks a country data set or grid type that does not fit the country, the local standards
    or the system properties.
  cite:
  - src: src:sma-doc-280451
    loc: sec=h16
    h: b6e62ef0fd02
  - src: src:sma-doc-278742
    loc: sec=h339
    h: b6e62ef0fd02
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h233
    h: b6e62ef0fd02
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h402
    h: b6e62ef0fd02
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h234
    h: 8871fd16517d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h403
    h: 7b53c9f55dc0
  - src: src:kb-sma-sbsexx-us-50-parameters-for-country-data-set
    loc: sec=h3
    h: 48eb59b6cb5a
  review: drafted
- claim_id: c3
  rel: presents_as
  target: symptom:grid-instability
  note: SMA warns that a wrong country data set or grid type can disturb the PV system and cause problems
    with the grid operator.
  cite:
  - src: src:sma-doc-280451
    loc: sec=h16
    h: b6e62ef0fd02
  - src: src:sma-doc-278742
    loc: sec=h339
    h: b6e62ef0fd02
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h233
    h: b6e62ef0fd02
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h402
    h: b6e62ef0fd02
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h234
    h: 8871fd16517d
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h403
    h: 7b53c9f55dc0
  - src: src:kb-sma-sbsexx-us-50-parameters-for-country-data-set
    loc: sec=h3
    h: 48eb59b6cb5a
  review: drafted
  review_note: 'support check: partial - Passages say wrong data set/grid type can disturb the PV system
    and cause grid operator problems, but not literally ''grid instability''.'
- claim_id: c4
  rel: presents_as
  target: symptom:parameter-change-rejected
  note: When you try to correct the setting with a wrong SMA Grid Guard code, event 9002 appears and the
    grid parameters stay locked.
  cite:
  - src: src:sma-doc-259761
    loc: tbl=72.r2
    h: ce2ed8a1ddf6
  - src: src:sma-doc-278742
    loc: tbl=76.r2
    h: ce2ed8a1ddf6
  - src: src:sma-sbxx-us-1xp-40-ba-en-13
    loc: sec=h249
    h: e1adee9857f4
  - src: src:kb-sma-shpxxus20-event-messages
    loc: tbl=1.r49
    h: 6a9b8c71bb4f
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r2
    h: ac6479fb8aba
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: sec=h441
    h: 7b9916244398
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r2
    h: ac6479fb8aba
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r2
    h: ac6479fb8aba
  - src: src:kb-sma-stpxx-us-41-event-messages
    loc: tbl=1.r50
    h: 6a9b8c71bb4f
  review: drafted
  review_note: 'support check: partial - Event 9002 with locked parameters on a wrong Grid Guard code
    is stated, but its link to correcting an incorrect grid code is inferred, not stated.'
- claim_id: c5
  rel: detected_by
  target: method:inverter-settings-review
  note: Check the Set country standard parameter (channel CntrySet or Country) in the Grid monitoring
    group.
  cite:
  - src: src:sma-doc-259761
    loc: sec=h323
    h: d68178149130
  - src: src:sma-doc-278742
    loc: sec=h341
    h: 077a63957340
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: tbl=34
    h: 46801c51f609
  - src: src:sma-doc-280451
    loc: tbl=3.r1
    h: d352f96fc19c
  - src: src:sma-doc-280451
    loc: tbl=3
    h: 4a946ae27040
  - src: src:kb-sma-sbsxx-us-10-configuring-the-country-data-set
    loc: sec=h1
    h: 89ecd79fa258
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h70
    h: d68178149130
  review: drafted
  review_note: 'support check: partial - Passages identify the Set country standard parameter and its
    group/channels, but only as the setting procedure, not as a detection/review step.'
- claim_id: c6
  rel: mitigated_by
  target: mit:grid-settings-check
  note: Set the required country data set or grid code for the country or region and the application.
    SolarEdge sets the general USA country code to get typical IEEE 1547 settings.
  cite:
  - src: src:sma-doc-259761
    loc: sec=h323
    h: d68178149130
  - src: src:sma-doc-278742
    loc: sec=h341
    h: 077a63957340
  - src: src:kb-sma-sbsxx-us-10-configuring-the-country-data-set
    loc: sec=h1
    h: 89ecd79fa258
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: sec=h70
    h: d68178149130
  - src: src:solaredge-iso-new-england-configuration-instructions-na
    loc: sec=h6
    h: a5ac09456aca
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=24.r1
    h: 08b17e435759
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c7
  rel: mitigated_by
  target: mit:utility-consultation
  note: Contact the grid operator if you are unsure which standards and directives apply.
  cite:
  - src: src:sma-doc-280451
    loc: sec=h16
    h: b6e62ef0fd02
  - src: src:sma-doc-278742
    loc: sec=h339
    h: b6e62ef0fd02
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h233
    h: b6e62ef0fd02
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h402
    h: b6e62ef0fd02
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c8
  rel: mitigated_by
  target: mit:enter-access-code
  note: After the first 10 operating hours, the grid-relevant parameters can only be changed with the
    personal SMA Grid Guard code.
  cite:
  - src: src:sma-doc-259761
    loc: tbl=72.r2
    h: ce2ed8a1ddf6
  - src: src:sma-doc-278742
    loc: tbl=76.r2
    h: ce2ed8a1ddf6
  - src: src:kb-sma-shpxxus20-event-messages
    loc: tbl=1.r49
    h: 6a9b8c71bb4f
  - src: src:sma-stp33-62-us-41-ops-manual
    loc: tbl=11.r2
    h: ac6479fb8aba
  - src: src:sma-stp33-62-us-41-ba-en-13
    loc: tbl=22.r2
    h: ac6479fb8aba
  - src: src:sma-stp33-62-us-41-ba-en-14
    loc: tbl=23.r2
    h: ac6479fb8aba
  - src: src:kb-sma-stpxx-us-41-event-messages
    loc: tbl=1.r50
    h: 6a9b8c71bb4f
  - src: src:sma-doc-278879
    loc: fig=41
    h: 9ee6e7e9fa55
  - src: src:sma-doc-278879
    loc: sec=5.2.4
    h: d6e65891750e
  - src: src:sma-doc-278742
    loc: tbl=39.r7
    h: f466fb31510c
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
This fault happens when the inverter's grid code, country data set or grid type is missing or does not match the country, the local standards or the site. A wrong setting can disturb the PV system and cause problems with the grid operator. The grid code changes grid-related parameters such as the power factor and reactive power settings, so the inverter can run with the wrong protection and control behavior. To confirm, open the Grid monitoring parameter group and check the Set country standard parameter. To fix it, select the country data set or grid code that fits the site and its application. After the first 10 operating hours, SMA inverters need the installer's SMA Grid Guard code before grid parameters can be changed, and a wrong code leaves them locked. If you are not sure which standard applies, contact the grid operator before you change the setting.

<!-- review notes
- sentence 3: support check: partial - Passages show grid-code-dependent PF and Q(U) parameter defaults, but not that the inverter runs with wrong protection and control behavior.
- sentence 7: support check: partial - Passages say to contact the grid operator if unsure, but do not specify doing so before changing the setting (though implied by the selection context).
- sentence 1: review: partial - The passages support a country data set, grid type or grid code that is wrong for the country, its standards or the system, but say nothing about a missing or unset code.
-->
