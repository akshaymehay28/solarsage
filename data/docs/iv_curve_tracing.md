# IV Curve Tracing for Fault Diagnosis

An IV curve trace sweeps a string or module from short-circuit current (Isc)
to open-circuit voltage (Voc), recording the full current-voltage
characteristic. It is the most information-dense single measurement in PV
diagnostics because different faults deform the curve in distinct ways.

## Reading the curve

A healthy curve is a smooth knee between Isc and Voc. Key signatures:

Reduced Isc with normal shape indicates uniform light reduction - soiling,
uniform degradation, or an irradiance measurement error. Compare against a
clean reference module to separate soiling from degradation.

Steps or notches in the curve indicate mismatch: some substring is limited
and its bypass diode conducts part of the sweep. Causes include partial
shading, cracked cells, or a failed substring. One step per affected
substring.

Reduced Voc in exact multiples of a substring voltage indicates shorted
bypass diodes or a shorted substring.

Reduced fill factor (softer knee) with normal Isc and Voc indicates
increased series resistance - corroded connections, degraded solder joints,
or undersized wiring.

A shallower slope near Isc indicates reduced shunt resistance - PID,
cell damage, or potential hot spot risk.

## Practice

Trace curves at stable irradiance above 600 W/m2, translate to STC using
measured irradiance and cell temperature, and compare like-for-like against
baseline traces from commissioning. Annual sample tracing plus targeted
tracing of underperforming strings found by monitoring is a cost-effective
regime for utility-scale plants.
