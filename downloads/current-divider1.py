####################################################################################################

#!# This circuit is a fundamental block in electronic that permits to scale a current by an
#!# impedance ratio.

#cm# current-divider.m4

#!# The relation between the input and ouput current is:
#!#
#!# .. math::
#!#
#!#     \frac{I_{out}}{I_{in}} = \frac{R_1}{R_1 + R_2}
#!#
#!# This equation holds for any impedances like resistance, capacitance, inductance, etc.

####################################################################################################

import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()

####################################################################################################

from PySpice.Spice.Netlist import Circuit
from PySpice.Unit.Units import *

####################################################################################################

circuit = Circuit('Current Divider')

circuit.I('input', 1, circuit.gnd, 1) # Fixme: current value
circuit.R(1, 1, circuit.gnd, kilo(2))
circuit.R(2, 1, circuit.gnd, kilo(1))

for resistance in (circuit.R1, circuit.R2):
    resistance.minus.add_current_probe(circuit) # to get positive value

simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.operating_point()

# Fixme: current over resistor
for node in analysis.branches.values():
    print('Node {}: {:5.2f} A'.format(str(node), float(node))) # Fixme: format value + unit
#o#

####################################################################################################
#
# End
#
####################################################################################################