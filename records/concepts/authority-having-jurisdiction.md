---
id: concept:authority-having-jurisdiction
type: Concept
name: Authority having jurisdiction
aliases:
- AHJ
- Authorities Having Jurisdiction
category: Grid
concept_kind: market
claims:
- claim_id: c1
  rel: related_to
  target: role:electrical-inspector
  note: An electrical inspector is one example of who can act as the AHJ; others include fire officials,
    building officials and insurance representatives.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=h178
    h: f519883871fe
  - src: src:std-standards-nfpa-780-lightning-protection-systems
    loc: sec=h186
    h: 5024e9e1ea9d
  - src: src:std-standards-nfpa-nfpa-70e-2009
    loc: sec=h34
    h: fd20325689b6
  - src: src:std-standards-states-state-ma-fire-code-ma-fire-code-527-cmr-1-00-2019
    loc: sec=3.2.2
    h: a38e71258b6a
  review: drafted
- claim_id: c2
  rel: related_to
  target: std:nfpa-780
  note: Annex A explains the term and says the AHJ may decide things such as whether a structure counts
    as a Faraday-like shield.
  cite:
  - src: src:std-standards-nfpa-780-lightning-protection-systems
    loc: tbl=38.r14
    h: 214c15197e90
  - src: src:std-standards-nfpa-780-lightning-protection-systems
    loc: sec=h186
    h: 5024e9e1ea9d
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:listed-equipment
  note: The AHJ can rely on listing and labeling by a product evaluation organization when it accepts
    equipment.
  cite:
  - src: src:std-standards-nfpa-780-lightning-protection-systems
    loc: sec=h186
    h: 5024e9e1ea9d
  - src: src:std-standards-nfpa-nfpa-70e-2009
    loc: sec=h34
    h: fd20325689b6
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:permit-plan-set
  note: The AHJ reviews and approves the drawings and inspects construction to confirm the installation
    matches the permit set.
  cite:
  - src: src:trn-training-very-basics-of-pv-lesson-1
    loc: sec=h42
    h: 219057bc5789
  review: drafted
---
The authority having jurisdiction, or AHJ, is the organization, office or person who enforces a code or standard and approves equipment, materials, installations or procedures. Who the AHJ is depends on the place and the purpose. It can be a fire chief, fire marshal, building official, electrical inspector, an insurance representative, or sometimes the property owner. On solar projects the AHJ is usually a city or county inspector who can inspect and approve the design and the construction. The AHJ reviews and approves the drawings, inspects the plant during construction to check that it matches the permit set, and gives the final sign-off before commercial operation. Designers should check for any restrictions set by the utility or the AHJ early in a project. When deciding whether to accept equipment, the AHJ may rely on compliance with recognized standards or on listing and labeling by a product evaluation organization. More than one AHJ can cover the same work. For example, a building official and an inspector of wires can each be responsible for different parts of one installation.

<!-- review notes
- sentence 3: support check: partial - u3 gives city or county inspectors as examples with the right to inspect and approve design and construction, but it does not say they are usually the AHJ, and nothing ties this to solar projects specifically.
- sentence 5: support check: partial - u2 lists confirming utility/AHJ restrictions as a checklist item, but it does not say designers should do this early in a project.
-->
