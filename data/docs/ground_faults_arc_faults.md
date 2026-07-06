# Ground Faults and Arc Faults

Ground faults and DC arc faults are the two most safety-critical electrical
faults in PV systems, both capable of starting fires if undetected.

## Ground faults

A ground fault is an unintended current path between a current-carrying
conductor and earth, most often caused by chafed cable insulation on sharp
rack edges, water ingress into connectors or junction boxes, or rodent
damage. Inverters detect them by monitoring insulation resistance (Riso)
before connection and residual current during operation. Morning Riso trips
that clear by mid-day indicate moisture-related insulation weakness - a
warning that should be traced, not ignored, because the "blind spot" of
older grounded systems allowed a second ground fault to flow undetected
with fire risk.

Locating a ground fault: isolate strings and megger-test each conductor to
ground, halving the search space at each step. Damp conditions reproduce
faults that vanish when dry.

## Arc faults

A series arc forms when a current-carrying connection separates slightly -
a cracked solder joint, a loose terminal, a mis-crimped connector - and
current jumps the gap as a sustained plasma arc at several thousand degrees.
Parallel arcs form between conductors of opposite polarity. DC arcs are
especially dangerous because there is no zero-crossing to extinguish them.

Arc-fault circuit interrupters (AFCI), required by many modern codes, detect
the broadband high-frequency noise an arc superimposes on the DC current and
shut down the affected circuit. Nuisance AFCI trips can be caused by inverter
switching noise; genuine trips warrant a physical inspection of every
connection on the affected string before re-energising.
