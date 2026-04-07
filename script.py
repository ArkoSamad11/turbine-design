import math as math

# shaft power in kW
n20_shaft_power  = 13.25247034
e99_shaft_power  = 18.8961079
total_shaft_power_kW = n20_shaft_power + e99_shaft_power
# W
total_shaft_power_watts = total_shaft_power_kW * 1000
# hp
total_shaft_power_hp = total_shaft_power_kW * 1.341022

# revolutions per min, speed
RPM = 25000
# convert RPM into angular velocity rad/s
angular_velocity = RPM * ((2*math.pi)/60)

# turbine which has the blades on the tip
# so tip speed is basically blade speed
# assuming turbine diameter / 2 is rtip (inches)
r_tip = 2
# U = angular * radius (convert to m)
r_tip = 2 * .0254
# U = blade velocity
U = angular_velocity * r_tip

# mdot is GG mass flow rate (kg/s)
GG_massflow_rate = 0.1985641039

# specific work J/kg
spec_work = (total_shaft_power_watts) / (GG_massflow_rate)

# change in tangential component of absolute velocity of fluid V
change_in_V = (spec_work) / (U)

# finding (V1) velocity at the boundary between stator exit and rotor inlet 
# EVERYTHING BELOW THIS WILL BE UPDATED WITH BETTER ACCURACY, 04/07/26 - UNCERTAIN
Tknot = 1089
Pknot_Pa = 1.21e6
Pexit_Pa = 6.03e5 # update
spec_heat_ratio = 1.699610378 # reconsider
Mexhaust_kgmol = 18.215 / 1000
# mach number of gas at the stator exit
# ratio of the gas velocity to the local speed of sound at that point
# isentropic flow assumption 
M1 = math.sqrt((2)/(spec_heat_ratio - 1) * ((Pknot_Pa / Pexit_Pa)**((spec_heat_ratio - 1)/(spec_heat_ratio)) - 1))
# static temperature of the gas at the stator exit
T1 = (Tknot) / ((1) + ((spec_heat_ratio - 1)/(2) * (M1**2)))
# specific gas constant of your exhaust mixture
R = 8.314462618 / Mexhaust_kgmol
