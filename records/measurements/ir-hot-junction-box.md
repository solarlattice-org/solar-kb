---
id: meas:ir-hot-junction-box
type: Measurement
name: Hot junction box in IR
aliases:
- hotspot Jbox
---
In an infrared image, this signature is a junction box that runs hotter than the junction boxes on comparable modules. Some warming around the junction box is normal, because heat escapes less well there than from the rest of the module. Compare it with neighbouring boxes before calling it a fault. The usual cause is bad contacts or corrosion inside the box. These raise the resistance and heat the box, which is a sign of junction box interconnection failure or general junction box failure. A loose electrical connection inside the box can show up as a junction box hotspot in an infrared camera image. A box that is hotter than the others can point to a cold solder joint. In some failure types, though, that heating only shows while the module is shaded or during a night bypass diode reverse-bias test. Look for related signs: discoloured or burnt encapsulant or backsheet around the box, a deformed or burnt box from bypass diode failure, and power loss you can confirm by measuring module or string Voc. Treat a hot box as a fire risk because internal arcing can follow. Isolate it safely and replace the module rather than repairing the box.

<!-- review notes
- sentence 7: support check: partial - The passages support the fire risk from arcing and replacing the module rather than repairing the box (u11). Safe isolation is supported by u5 only for arcing or burn evidence, not for every hot box.
-->
