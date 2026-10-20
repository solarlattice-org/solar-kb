---
id: mit:model-input-documentation
type: Mitigation
name: Model input version control
---
Model input version control means recording exactly which PAN file was used in a yield model, including where it came from and which version it is, and treating that file as a controlled modeling input. It addresses Flawed PAN File Yield Losses, where a wrong or unrepresentative module file skews simulated performance so that expected yield differs from field behavior even though nothing is physically wrong with the plant. A PAN file holds the module's electrical, temperature, low-light and incidence-angle parameters. If those parameters are optimistic or do not match the modules actually delivered, modeled energy can be overstated. In practice, start by identifying the exact file behind the energy estimate, including its source, version and any manual edits. Then compare it with datasheets, independent lab measurements, third-party files and measured site behavior. Keeping inputs controlled stops teams from comparing designs or diagnosing operations with inconsistent module representations, and it helps keep a model-baseline problem from being mistaken for a repairable field defect. Common modeling errors include entering module data incorrectly or entering the wrong number of modules per string or parallel strings, so these entries should also be checked. Version control works alongside using validated module files, running sensitivity analysis and updating forecasts when independent testing shows material parameter differences. On its own, it does not correct a flawed file.

<!-- review notes
- sentence 1: support check: partial - Passages say to treat PAN provenance as a controlled input and document source and version, but don't define 'model input version control' as such.
- sentence 6: support check: partial - Passages list module data and parallel strings or modules in string entered incorrectly as modelling causes, but don't say to check them in this context or call them common errors.
- sentence 7: support check: partial - Mitigation lists documenting source and version alongside validated files, sensitivity analysis and forecast updates, but the claim that version control alone doesn't correct a flawed file is not stated.
-->
