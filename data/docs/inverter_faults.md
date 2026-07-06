# Inverter Faults and Failure Modes

The inverter is the most failure-prone component in a PV plant: industry O&M
data consistently attributes 40-60% of energy-loss events and the majority of
service tickets to inverters, even though modules dominate capital cost.

## Common failure modes

Cooling-system failures (blocked filters, failed fans) cause thermal derating
long before total failure: the inverter clips output on hot afternoons and the
loss appears as flattened power peaks. DC-link capacitor ageing is a leading
cause of end-of-life failure, typically after 10-15 years. IGBT power-stage
failures cause abrupt total outages, often after grid transients. Firmware
and communication faults produce nuisance trips that look like intermittent
outages in monitoring data.

## Fault signatures in monitoring data

A healthy inverter tracks the irradiance curve. Thermal derating shows as a
plateau below rated power correlated with ambient temperature. Repeated
morning start-up failures suggest insulation resistance (Riso) trips from
overnight moisture ingress - the inverter refuses to connect until the array
dries out. A string-level current imbalance with normal voltage points at
string fuses or connectors upstream rather than the inverter itself.

## Response

Check the inverter event log first: modern inverters record fault codes with
timestamps that distinguish grid faults, DC insulation faults, and internal
hardware errors. Clean or replace air filters on the preventive schedule,
verify fan operation under load, and thermally scan the AC and DC connections
annually. Keep firmware current, but stage updates on one unit before fleet
rollout.
