---
id: prod:burndy-hydent
type: Product
name: Burndy HYDENT compression connectors
aliases:
- HYDENT
- Medium & Large HYDENT
category: Connectors and cable
make: burndy
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:burndy
  cite:
  - src: src:eq-connectors-burndy-brundy-compression
    loc: sec=h14
    h: fcea3a28d3a3
  - src: src:eq-connectors-burndy-brundy-compression
    loc: sec=h1
    h: bc4971359be1
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:compression-connector
  note: HYDENT connectors and terminals are installed by crimping.
  cite:
  - src: src:eq-connectors-burndy-burndy-connector-theory-and-application
    loc: sec=2.2.5
    h: 019ff9743725
  - src: src:eq-connectors-burndy-brundy-compression
    loc: sec=h14
    h: fcea3a28d3a3
  review: drafted
- claim_id: c3
  rel: requires
  target: tool:compression-crimping-tool
  note: Burndy says its dies, connectors and tools are designed as one coordinated system.
  cite:
  - src: src:eq-connectors-burndy-burndy-connector-theory-and-application
    loc: sec=2.2.5
    h: 019ff9743725
  - src: src:eq-connectors-burndy-brundy-compression
    loc: sec=h2
    h: b8d539f46265
  review: drafted
  review_note: 'support check: partial - Passages say compression systems use specific installation tools
    and coordinated tools, but don''t explicitly name a crimping tool required for HYDENT.'
- claim_id: c4
  rel: requires
  target: tool:compression-die
  note: The die must match the connector; Burndy coordinates dies with its connectors and tools.
  cite:
  - src: src:eq-connectors-burndy-burndy-connector-theory-and-application
    loc: sec=2.2.5
    h: 019ff9743725
  - src: src:eq-connectors-burndy-brundy-compression
    loc: sec=h2
    h: b8d539f46265
  review: drafted
  review_note: 'support check: partial - Compression systems use specific dies and Burndy coordinates
    dies with connectors, but HYDENT-specific die requirement isn''t explicitly stated.'
- claim_id: c5
  rel: requires
  target: tool:wire-stripper
  note: Used to strip the insulation to the needed length before crimping.
  cite:
  - src: src:eq-connectors-burndy-brundy-compression
    loc: sec=h14
    h: fcea3a28d3a3
  review: drafted
  review_note: 'support check: partial - Passage says strip with a wire stripper or similar tool, so a
    wire stripper is not strictly required.'
---
Burndy HYDENT is a family of compression connectors and terminals, including Medium and Large HYDENT terminals, that are installed by crimping. Use them with matching Burndy dies and installation tools, because Burndy designs its connectors, dies and tools to work together as one engineered system. Before crimping, pick the HYDENT connector that suits the conductor, check that the markings on the conductor and connector match, and strip the insulation to the needed length. Connectors for Class A, B and AA code conductors carry solid colour bands on the barrel, while those for flexible Class G, H, I, K and M conductors use colour-coded lettering and narrow bands. On a seamless barrel the crimp orientation is not critical, and alternating the crimp direction on Medium and Large terminals does not harm the connection. The aluminium connectors are dual rated for both aluminium and copper code conductors.

<!-- review notes
- sentence 1: support check: partial - Medium and Large HYDENT terminals and crimping are supported, but 'family of connectors and terminals' is only loosely implied.
-->
