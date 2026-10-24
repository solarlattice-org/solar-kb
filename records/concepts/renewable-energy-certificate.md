---
id: concept:renewable-energy-certificate
type: Concept
name: Renewable energy certificate
aliases:
- REC
- SREC
- solar renewable energy certificate
- Renewable Energy Credits
category: Market
concept_kind: market
claims:
- claim_id: c1
  rel: related_to
  target: std:eversource-ct-rec-metering-procedures
  note: Utility metering procedures written specifically for PA 11-80 renewable energy credits.
  cite:
  - src: src:std-utilities-eversource-ct-rec-metering-procedures
    loc: sec=h1
    h: f6c3addbef62
  review: drafted
  review_note: 'support check: partial - The passage gives only the title of the MPREC document for PA
    11-80 RECs; it does not name Eversource or CT, or say it is a utility procedure.'
- claim_id: c2
  rel: related_to
  target: concept:distributed-energy-resource
  scope:
    regions:
    - region:us-ny
  note: In New York, DER projects do not earn Tier 1 RECs. They are paid for environmental attributes
    through the E component of the VDER value stack.
  cite:
  - src: src:trn-training-industry-reports-and-guides-nysun-2023-solar-guidebook
    loc: sec=2.1.2
    h: 9b6feba174b3
  review: drafted
---
A renewable energy certificate, or REC, is a certificate that a tracking system creates. It stands for the environmental attributes of one megawatt hour of electricity made from a renewable source such as solar or wind. New York's tracking system, NYGATS, is one example of a system that issues these certificates. RECs back up claims about using renewable energy. Those claims can be for a state-mandated compliance program or for voluntary goals such as a climate pledge. Because RECs can be both traded and traced, they let the holder claim the benefits of renewable generation. Not every project can earn every type of REC. In New York, only eligible large-scale renewable facilities can generate Tier 1 RECs, and distributed energy resource projects are paid for their environmental attributes through a separate value stack component.

<!-- review notes
- sentence 4: support check: partial - The passage calls RECs a tradable, traceable means of claiming renewable benefits, but it does not state the causal 'because' or mention a 'holder'.
-->
