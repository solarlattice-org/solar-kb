---
id: concept:permission-to-operate
type: Concept
name: Permission to operate
aliases:
- PTO
category: Grid
concept_kind: market
claims:
- claim_id: c1
  rel: related_to
  target: concept:interconnection-process
  note: A PTO letter emailed by the utility's interconnection group serves as proof of authorization to
    interconnect.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-sgip-documents-sgip-partner
    loc: tbl=6.r3
    h: 78ea594dc6f0
  review: drafted
  review_note: 'support check: partial - The passage shows a PTO letter emailed from utility interconnection
    as proof of authorization to interconnect, but does not name the interconnection process concept explicitly
    beyond this.'
- claim_id: c2
  rel: related_to
  target: role:utility-approval
  note: The PTO letter is issued by the utility's interconnection group.
  cite:
  - src: src:eq-equip-bess-stem-partner-content-library-brochures-ebooks-infographics-sgip-documents-sgip-partner
    loc: tbl=6.r3
    h: 78ea594dc6f0
  review: drafted
- claim_id: c3
  rel: related_to
  target: func:export-limitation
  note: While a PWRcell system waits for PTO, it may run with Export Override turned on so that it does
    not export to the utility grid.
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: sec=h144
    h: 14dc7efc4743
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: sec=h132
    h: 14dc7efc4743
  review: drafted
- claim_id: c4
  rel: related_to
  target: prod:generac-pwrcell-inverter
  note: The manuals describe two allowed system states before PTO (operating without export, or disabled)
    and how to activate the system once PTO is granted.
  cite:
  - src: src:generac-generac-pwrcell-1ph-inverter-install-and-owners-manual-rev-j
    loc: sec=h144
    h: 14dc7efc4743
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: sec=h132
    h: 14dc7efc4743
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=2.r21
    h: a012a9f52942
  review: drafted
  review_note: 'support check: partial - The two pre-PTO states are described, and the heading on activating
    post-PTO appears, but the activation steps are not given in the passages.'
- claim_id: c5
  rel: related_to
  target: role:area-eps-operator
  note: In SMA operating-state descriptions, the system operator can withdraw permission to operate (Operation.OpMod
    = Stop).
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: tbl=19.r9
    h: cbc82bbd61be
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: tbl=19.r11
    h: 193a7c9f3dee
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: tbl=19.r8
    h: 565db8fcf0bd
  review: drafted
- claim_id: c6
  rel: related_to
  target: state:standby
  note: An SMA inverter moves from RUN to STANDBY when the system operator withdraws permission to operate.
  cite:
  - src: src:eq-equip-inverters-sma-inverter-firmware-fw4-01-05-r-stpxx-us-41-info-nsm-gg10-ti-en-16
    loc: tbl=19.r8
    h: 565db8fcf0bd
  review: drafted
- claim_id: c7
  rel: related_to
  target: proto:sunspec-rapid-shutdown-signal
  note: 'This is a separate meaning of the term: the SunSpec rapid shutdown keep-alive is called a ''permission
    to operate'' signal. It is not the utility approval.'
  cite:
  - src: src:eq-equip-inverters-sma-stp-core1-us-rss-ti-en-11
    loc: sec=h15
    h: 71680ad772d9
  review: drafted
---
Permission to operate, or PTO, is the approval a system needs after installation and inspection before it may run normally connected to the grid. The utility usually gives this approval as a PTO letter from its interconnection group, and incentive programs such as SGIP accept that letter as proof of authorization to interconnect. While a Generac PWRcell system waits for PTO, it can either run with Export Override on, so it sends no power to the grid, or stay fully disabled. If a battery system with a protected loads panel is left disabled while waiting, keep the inverter grid breaker and the Protected Loads Disconnect on so the protected loads still get power. On SMA inverters, the system operator can withdraw permission to operate with the stop operating mode, which sends the inverter into standby or a locked state. Do not confuse PTO with the SunSpec rapid shutdown keep-alive, which is also called a permission to operate signal and stops during a grid outage.

<!-- review notes
- sentence 1: support check: partial - Passages say a system must be inspected and granted PTO and may be operating without export or disabled while awaiting it, but do not say it may not run normally grid-connected without it.
- sentence 2: support check: partial - The PTO letter from utility interconnection as proof of authorization is shown, but SGIP/incentive programs accepting it and 'usually' are not stated.
- sentence 6: support check: partial - The passage shows the SunSpec 'permission to operate' signal stops on a grid outage, but nothing about not confusing it with utility PTO beyond that.
-->
