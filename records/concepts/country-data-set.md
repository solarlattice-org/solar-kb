---
id: concept:country-data-set
type: Concept
name: Grid code setting
aliases:
- country data set
- grid profile
- country code
- grid code selection
- country standard
- grid code
- Country Setting
- Netzrichtlinien
category: Grid
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:grid-code
  note: The setting loads the requirements of the local grid code into the inverter.
  cite:
  - src: src:eq-equip-inverters-delta-m60u-m80u-20190806-m80-60u-manual-old
    loc: sec=4.3.7.3
    h: 3ec1db3a8475
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=24.r1
    h: 08b17e435759
  - src: src:kb-solis-44002504766-s6-hybrid-series-soliscloud-app-local-bluetooth-connection-guide
    loc: sec=h1
    h: ad52628e7cf6
  review: drafted
- claim_id: c2
  rel: related_to
  target: std:ieee-1547
  note: 'SolarEdge: choosing the general USA country code for the grid configuration sets typical IEEE
    1547 settings.'
  cite:
  - src: src:solaredge-iso-new-england-configuration-instructions-na
    loc: sec=h6
    h: a5ac09456aca
  - src: src:eq-equip-inverters-solaredge-design-installation-iso-new-england-iso-ne-configuration-instructions
    loc: sec=h6
    h: a5ac09456aca
  review: drafted
- claim_id: c3
  rel: related_to
  target: std:ieee-1547
  scope:
    products:
    - prod:delta-electronics-m60u-m80u
    - prod:delta-electronics-m36u-m42u
  note: Delta string inverters in North America use the IEEE 1547 480V grid code setting.
  cite:
  - src: src:eq-equip-inverters-delta-m60u-m80u-20190806-m80-60u-manual-old
    loc: sec=4.3.7.3
    h: 3ec1db3a8475
  - src: src:eq-equip-inverters-delta-m36u-m42u-20191015-m42-36u-manual
    loc: sec=4.3.7.3
    h: 3ec1db3a8475
  review: drafted
  review_note: 'support check: partial - Passage says in NA the setting is IEEE 1547 480V, but doesn''t
    name Delta products or M60U/M36U models in the text.'
- claim_id: c4
  rel: related_to
  target: std:ieee-1547-2018
  scope:
    products:
    - prod:solis-s6-gu-ehv-us
    regions:
    - region:us
    - region:ca
  note: For US and Canadian installations, select the IEEE1547-2018 grid code.
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: sec=6.1.2
    h: 7bf6824cc25f
  review: drafted
- claim_id: c5
  rel: related_to
  target: std:vde-ar-n-4105-2018
  scope:
    regions:
    - region:de
  note: Example grid code entry for Germany, which must be entered and then confirmed.
  cite:
  - src: src:sma-doc-275848
    loc: sec=3.7
    h: 3563c0b8e775
  review: drafted
- claim_id: c6
  rel: related_to
  target: param:sma-set-country-standard
  note: SMA parameter under Grid monitoring that selects the country data set.
  cite:
  - src: src:sma-doc-259761
    loc: sec=h323
    h: d68178149130
  - src: src:kb-sma-sbsxx-us-10-configuring-the-country-data-set
    loc: sec=h1
    h: 89ecd79fa258
  - src: src:sma-shpxxx-us-21-be-en-11
    loc: tbl=34.r1
    h: d40467c5bf86
  - src: src:sma-doc-280451
    loc: tbl=3.r1
    h: d352f96fc19c
  review: drafted
- claim_id: c7
  rel: related_to
  target: role:grid-guard-code-holder
  scope:
    products:
    - prod:sma-sunny-island
  note: The country standard parameter is protected by SMA Grid Guard.
  cite:
  - src: src:sma-doc-si30m-44m-60h-80h-be-en-33w
    loc: tbl=145.r11
    h: 1f5ff7bc17af
  review: drafted
  review_note: 'support check: partial - Row says Country/Set country standard is protected by SMA Grid
    Guard, but doesn''t mention Sunny Island product scope.'
- claim_id: c8
  rel: related_to
  target: tool:sma-lcs-tool
  note: The LCS-Tool is used to select the country and grid code.
  cite:
  - src: src:sma-doc-278879
    loc: fig=35
    h: 3c3c7525a3cc
  - src: src:sma-doc-278879
    loc: fig=98
    h: '9796e6758067'
  review: drafted
  review_note: 'support check: partial - Figure caption shows LCS-Tool for selecting country and grid
    code, but only as a figure caption.'
- claim_id: c9
  rel: related_to
  target: fm:grid-code-misconfiguration
  scope:
    products:
    - prod:sma-sbse-us-50
  note: A wrong grid type selection can disturb the PV system and cause problems with the grid operator.
  cite:
  - src: src:sma-sbsexx-us-50-be-en-11
    loc: sec=h234
    h: 8871fd16517d
  review: drafted
- claim_id: c10
  rel: related_to
  target: concept:reactive-power
  note: The reference size for the reactive power setting is normally already set by the country data
    set.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: tbl=45
    h: 8276ef84ccad
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: tbl=45.r1
    h: 38f20b788a52
  review: drafted
- claim_id: c11
  rel: related_to
  target: func:low-voltage-ride-through
  scope:
    products:
    - prod:sungrow-sg60ku-m
  note: Choosing a medium-voltage grid code lets you enable or disable LVRT.
  cite:
  - src: src:eq-equip-inverters-sungrow-sungrow-sg60ku-m-user-manual-ver14
    loc: sec=10.11.1
    h: fabfc24d6ed3
  review: drafted
  review_note: 'support check: partial - Passage supports MV grid code enabling/disabling LVRT, but doesn''t
    name the SG60KU-M product.'
- claim_id: c12
  rel: related_to
  target: func:frequency-watt
  note: The advanced grid code settings include frequency derating, which reduces output during over-frequency.
  cite:
  - src: src:kb-solis-44002504766-s6-hybrid-series-soliscloud-app-local-bluetooth-connection-guide
    loc: sec=h1
    h: ad52628e7cf6
  review: drafted
- claim_id: c13
  rel: related_to
  target: func:export-limitation
  scope:
    products:
    - prod:enphase-iq8-commercial
  note: The grid profile carries an export limit setting.
  cite:
  - src: src:enphase-enphase-power-export-limit-iq8-commercial-tech-brief
    loc: fig=9
    h: 3e8a06bd3bd2
  review: drafted
  review_note: 'support check: partial - Only a figure caption mentions a grid profile export limit setting;
    no product scope or detail.'
---
The grid code setting, also called the country data set, country code or grid profile, tells the inverter which country's or region's grid rules to follow. It sets up the inverter's control system to match the local grid voltage, frequency and basic grid configuration. Choose it based on the grid code of the installation country or region and on how the inverter is used. If you are unsure which one applies, ask the local utility. The selection loads protection limits and other settings that depend on it, such as the reactive power reference, frequency derating and ride-through options. In North America, the grid code is usually an IEEE 1547 profile, for example IEEE 1547 480V or IEEE1547-2018. On SMA inverters you set it with the Set country standard parameter under Grid monitoring. This parameter can be protected by SMA Grid Guard. Choosing the wrong grid type can disturb the PV system and cause problems with the grid operator, so check this setting at commissioning.

<!-- review notes
- sentence 4: support check: partial - Passages cover LVRT, reactive power reference and frequency derating, but not that selection loads all these together as stated; reasonably implied but loose.
- sentence 7: support check: partial - Passage supports the consequences of a wrong grid type, but not the 'check at commissioning' advice explicitly.
-->
