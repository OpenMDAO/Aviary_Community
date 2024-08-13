import aviary.api as av

phase_info = {
    "pre_mission": {"include_takeoff": False, "optimize_mass": True},
    "climb_1": {
        "subsystem_options": {"core_aerodynamics": {"method": "computed"}},
        "user_options": {
            "optimize_mach": False,
            "optimize_altitude": False,
            "polynomial_control_order": 1,
            "use_polynomial_control": True,
            "num_segments": 2,
            "order": 3,
            "solve_for_distance": False,
            "initial_mach": (0.2, "unitless"),
            "final_mach": (0.57, "unitless"),
            "mach_bounds": ((0.180, 0.59), "unitless"),
            "initial_altitude": (0.0, "ft"),
            "final_altitude": (28000.0, "ft"),
            "altitude_bounds": ((0.0, 28500.0), "ft"),
            "throttle_enforcement": "path_constraint",
            "fix_initial": True,
            "constrain_final": False,
            "fix_duration": False,
            "no_descent": True,
            "initial_bounds": ((0.0, 0.0), "min"),
            "duration_bounds": ((21.5, 64.5), "min"),
        },
        "initial_guesses": {"time": ([0, 43], "min")},
    },
    "cruise_1": {
        "subsystem_options": {"core_aerodynamics": {"method": "computed"}},
        "user_options": {
            "optimize_mach": False,
            "optimize_altitude": False,
            "polynomial_control_order": 1,
            "use_polynomial_control": True,
            "num_segments": 2,
            "order": 3,
            "solve_for_distance": False,
            "initial_mach": (0.57, "unitless"),
            "final_mach": (0.57, "unitless"),
            "mach_bounds": ((0.55, 0.59), "unitless"),
            "initial_altitude": (28000.0, "ft"),
            "final_altitude": (28000.0, "ft"),
            "altitude_bounds": ((27500.0, 28500.0), "ft"),
            "throttle_enforcement": "boundary_constraint",
            "fix_initial": False,
            "constrain_final": False,
            "fix_duration": False,
            "initial_bounds": ((21.5, 64.5), "min"),
            "duration_bounds": ((127.0, 381.0), "min"),
        },
        "initial_guesses": {"time": ([43, 254], "min")},
    },
    "descent_1": {
        "subsystem_options": {"core_aerodynamics": {"method": "computed"}},
        "user_options": {
            "optimize_mach": False,
            "optimize_altitude": False,
            "polynomial_control_order": 1,
            "use_polynomial_control": True,
            "num_segments": 2,
            "order": 3,
            "solve_for_distance": False,
            "initial_mach": (0.57, "unitless"),
            "final_mach": (0.2, "unitless"),
            "mach_bounds": ((0.180, 0.59), "unitless"),
            "initial_altitude": (28000.0, "ft"),
            "final_altitude": (1000.0, "ft"),
            "altitude_bounds": ((500.0, 28500.0), "ft"),
            "throttle_enforcement": "path_constraint",
            "fix_initial": False,
            "constrain_final": True,
            "fix_duration": False,
            "no_climb": True,
            "initial_bounds": ((148.5, 445.5), "min"),
            "duration_bounds": ((26.5, 79.5), "min"),
        },
        "initial_guesses": {"time": ([297, 53], "min")},
    },
    "post_mission": {
        "include_landing": False,
        "constrain_range": True,
        "target_range": (2020, "nmi"),
    },
}


csv_path = "models/test_aircraft/c130j.csv"       #input custom .csv
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
prob.run_aviary_problem(record_filename='level2_C130J.db', suppress_solver_print=True, make_plots=True)

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
#https://www.scribd.com/document/369618581/C130JPocketGuide
#https://en.wikipedia.org/wiki/Lockheed_Martin_C-130J_Super_Hercules
#https://man.fas.org/dod-101/sys/ac/c-130.htm
#https://www.af.mil/About-Us/Fact-Sheets/Display/Article/1555054/c-130-hercules/
