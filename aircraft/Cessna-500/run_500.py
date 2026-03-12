import aviary.api as av

phase_info = {
    "pre_mission": {"include_takeoff": False, "optimize_mass": True},
    "climb_1": {
        "subsystem_options": {"core_aerodynamics": {"method": "computed"}},
        "user_options": {
            "optimize_mach": False,
            "optimize_altitude": False,
            "polynomial_control_order": 3,
            "use_polynomial_control": True,
            "num_segments": 3,
            "order": 3,
            "solve_for_distance": True,
            "initial_mach": (0.25, "unitless"),
            "final_mach": (0.5, "unitless"),
            "mach_bounds": ((0.23, 0.52), "unitless"),
            "initial_altitude": (0.0, "ft"),
            "final_altitude": (35000.0, "ft"),
            "altitude_bounds": ((0.0, 35500.0), "ft"),
            "throttle_enforcement": "path_constraint",
            "fix_initial": True,
            "constrain_final": False,
            "fix_duration": False,
            "no_descent": True,
            "initial_bounds": ((0.0, 0.0), "min"),
            "duration_bounds": ((16.5, 49.5), "min"),
        },
        "initial_guesses": {"time": ([0.0, 33.0], "min")},
    },
    "cruise_1": {
        "subsystem_options": {"core_aerodynamics": {"method": "computed"}},
        "user_options": {
            "optimize_mach": False,
            "optimize_altitude": False,
            "polynomial_control_order": 3,
            "use_polynomial_control": True,
            "num_segments": 3,
            "order": 3,
            "solve_for_distance": True,
            "initial_mach": (0.5, "unitless"),
            "final_mach": (0.5, "unitless"),
            "mach_bounds": ((0.48, 0.52), "unitless"),
            "initial_altitude": (35000.0, "ft"),
            "final_altitude": (35000.0, "ft"),
            "altitude_bounds": ((34500.0, 35500.0), "ft"),
            "throttle_enforcement": "boundary_constraint",
            "fix_initial": False,
            "constrain_final": False,
            "fix_duration": False,
            "initial_bounds": ((16.5, 49.5), "min"),
            "duration_bounds": ((34.5, 103.5), "min"),
        },
        "initial_guesses": {"time": ([33.0, 69.0], "min")},
    },
    "descent_1": {
        "subsystem_options": {"core_aerodynamics": {"method": "computed"}},
        "user_options": {
            "optimize_mach": False,
            "optimize_altitude": False,
            "polynomial_control_order": 3,
            "use_polynomial_control": True,
            "num_segments": 3,
            "order": 3,
            "solve_for_distance": True,
            "initial_mach": (0.5, "unitless"),
            "final_mach": (0.25, "unitless"),
            "mach_bounds": ((0.23, 0.52), "unitless"),
            "initial_altitude": (35000.0, "ft"),
            "final_altitude": (500.0, "ft"),
            "altitude_bounds": ((0.0, 35500.0), "ft"),
            "throttle_enforcement": "path_constraint",
            "fix_initial": False,
            "constrain_final": True,
            "fix_duration": False,
            "no_climb": True,
            "initial_bounds": ((51.0, 153.0), "min"),
            "duration_bounds": ((24.0, 72.0), "min"),
        },
        "initial_guesses": {"time": ([102.0, 48.0], "min")},
    },
    "post_mission": {
        "include_landing": True,
        "constrain_range": True,
        "target_range": (720.91, "nmi"),
    },
}


csv_path = "models/test_aircraft/Cessna-500.csv"       #input custom .csv
prob = av.AviaryProblem() 
prob.load_inputs(csv_path, phase_info)
prob.check_and_preprocess_inputs()
prob.add_pre_mission_systems()
prob.add_phases()
prob.add_post_mission_systems()
prob.link_phases()
prob.add_driver("SLSQP", max_iter=15)               #set driver and iteration count
prob.add_design_variables()
prob.add_objective(objective_type="mass", ref=-1e5)
prob.setup()
prob.set_initial_guesses()
prob.run_aviary_problem(record_filename='level2_C500.db', suppress_solver_print=True, make_plots=True)

# All Model Inputs,Calculations, and Arrays
# prob.model.list_inputs()                                
# prob.model.list_outputs()                               
# prob.model.list_outputs(print_arrays=True,units=True) 

#All Mission.Summary values
print("Cruise Mach:            ", prob.get_val(av.Mission.Summary.CRUISE_MACH, units='unitless')[0])
print('Reserve Fuel Burned:    ', prob.get_val(av.Mission.Summary.RESERVE_FUEL_BURNED, units='lbm')[0],'lbm')
print('Fuel Burn:              ', prob.get_val(av.Mission.Summary.FUEL_BURNED, units='lbm')[0],'lbm')
print('Total Fuel Mass:        ', prob.get_val(av.Mission.Summary.TOTAL_FUEL_MASS, units='lbm')[0],'lbm')

###Sources###
#https://en.wikipedia.org/wiki/Cessna_Citation_I
#https://www.bjtonline.com/aircraft/cessna-citation-500
#https://conklindedecker.jetsupport.com/details/Cessna%20Citation%20500#summary
#https://www.globalair.com/aircraft-for-sale/specifications?specid=179