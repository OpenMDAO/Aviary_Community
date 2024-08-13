#Aviary run script for C5 example problem

#---------- Imports ----------
import aviary.api as av
from C5_phase_info import mission_select as mission

#---------- Opt/Simulation Parameters ----------
Opt_mach = False
Opt_alt = False
Opt_mass = True
takeoff = False
landing = False
polynomial_control_order = 2
num_segments = 3
order = 3

#---------- Run Aviary ----------
phase_info = mission("mission1" , Opt_mach , Opt_alt , Opt_mass , takeoff , landing , polynomial_control_order , num_segments)
C5_csv = "define_C5.csv"
prob = av.AviaryProblem()
prob.load_inputs(C5_csv , phase_info)
prob.check_and_preprocess_inputs()
prob.add_pre_mission_systems()
prob.add_phases()
prob.add_post_mission_systems()
prob.link_phases()
prob.add_driver("SLSQP" , max_iter = 100)
prob.add_design_variables()
prob.add_objective(objective_type = "mass", ref=-1e5)
prob.setup()
prob.set_initial_guesses()
prob.run_aviary_problem(record_filename = 'Level2_C5.db' , suppress_solver_print = True , make_plots = True)