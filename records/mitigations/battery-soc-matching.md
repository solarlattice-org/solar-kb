---
id: mit:battery-soc-matching
type: Mitigation
name: Battery SOC matching before module extension
aliases:
- manual recharging of the battery
- bring battery to same SOC
- manual battery charge
- Manual Charging of the Battery
---
Before you replace a battery module or add new modules, bring the existing battery to the same state of charge (SOC) as the new modules. Most battery manufacturers advise doing this before the new modules are connected. The battery manufacturer's instructions always take priority over this general procedure. To lower the SOC, disconnect the PV plant and run some loads until the battery reaches the target SOC. To raise the SOC on a Sunny Boy Storage 3.7, 5.0 or 6.0, open the web interface, charge the battery manually from the performance profile in the user settings, then save the settings. On an SBS2.5-1VL-10, use the Sunny Portal time window control for charging the battery-storage system instead. This feature is not available in Webconnect systems. Matching the SOC matters because modules at different SOC levels charge unevenly. The displayed SOC is only an average, so it can look normal while charging is blocked because one module is already full. On some SMA Home Storage systems, newer battery firmware balances the modules automatically, which reduces SOC differences between them. Manual matching is still done when modules are replaced or extended.

<!-- review notes
- sentence 6: support check: partial - The module balancing article supports uneven charge, the averaged SOC display and charging blocked by a full module. It does not say that matching SOC at replacement is important for this reason.
- sentence 7: support check: partial - The passages say firmware 1.1.3x.B eliminates manual module balancing and that balancing is automatic. They do not say manual SOC matching is still done on module replacement or extension; the u1 article only describes it as the manufacturer advice.
-->
