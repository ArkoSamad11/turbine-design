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
r_tip_inches = 2
# U = angular * radius (convert to m)
r_tip_meters = r_tip_inches * .0254
# U = blade velocity
U = angular_velocity * r_tip_meters
print('Blade Velocity is ' + str(U))

# ASSUMPTION - ISENTROPIC SPOUTING VELOCITY
Cp = 1108.853
Cv = 652.4159975    
GGSpecHeat = Cp
TurbineInletTemp = 900 # Kelvin
GGSpecHeatRatio = Cp / Cv
PR = 6
C0 = math.sqrt(2 * GGSpecHeat * TurbineInletTemp * (1 - (1/PR)**((GGSpecHeatRatio - 1)/GGSpecHeatRatio)))
print('Isentropic Spouting Velocity is ' + str(C0))

# specific work J/kg
TurbineEfficiency = 0.75 * (1 - ((U/C0 - 0.5) / 0.5)**2)
actual_spec_work = (TurbineEfficiency * GGSpecHeat * TurbineInletTemp * (1 - (1 / PR)**((GGSpecHeatRatio - 1) / (GGSpecHeatRatio)))) 
print('Turbine Efficiency is ' + str(TurbineEfficiency))
print('Actual Specific Work is ' + str(actual_spec_work))

# mdot is GG mass flow rate (kg/s)
GG_massflow_rate = (total_shaft_power_watts) / actual_spec_work
print('GG Mass Flow Rate is ' + str(GG_massflow_rate))

# change in swirl velocity - the difference in tangential absolute gas velocity between rotor inlet and rotor exit.
change_in_C = (actual_spec_work) / (U)
print('The difference in tangential absolute gas velocity between rotor inlet and rotor exit is ' + str(change_in_C))
# ASSUMPTION - NOZZLE IS 95% EFFICIENT
C1 = math.sqrt(.95) * C0
print(C1)
# ZERO SWIRL AT ROTOR EXIT
# nozzle_exit_angle_degrees = math.degrees(math.asin(change_in_C / C1))
 # print('Nozzle Exit Angle: ' + str(nozzle_exit_angle_degrees) + ' degrees')
print('------------------------------------------------------------------------------------------')
# solves for minimum radius - keeps RPM constant
while ((change_in_C) / (C1)) > 1:
    r_tip_inches += 0.01
    r_tip = r_tip_inches * 0.0254
    U = angular_velocity * r_tip
    TurbineEfficiency = 0.75 * (1 - ((U/C0 - 0.5) / 0.5)**2)
    actual_spec_work = (TurbineEfficiency * GGSpecHeat * TurbineInletTemp * (1 - (1 / PR)**((GGSpecHeatRatio - 1) / (GGSpecHeatRatio))))
    change_in_C = actual_spec_work / U
    C1 = math.sqrt(0.95) * C0

print('Final r_tip inches: ' + str(r_tip_inches))
print('Final Blade Velocity: ' + str(U))
print('Final Turbine Efficiency: ' + str(TurbineEfficiency))
print('Final Actual Specific Work: ' + str(actual_spec_work))
print('Final GG Mass Flow Rate: ' + str(total_shaft_power_watts / actual_spec_work))
print('Final difference in tangential absolute gas velocity between rotor inlet and rotor exit: ' + str(change_in_C))
print('Final C1: ' + str(C1))
print('Final U/C0: ' + str(U/C0))
nozzle_exit_angle = math.degrees(math.asin(change_in_C / C1))
print('Nozzle Exit Angle: ' + str(nozzle_exit_angle) + ' degrees')