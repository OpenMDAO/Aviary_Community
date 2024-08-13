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
            "final_mach": (0.7, "unitless"),
            "mach_bounds": ((0.23, 0.72), "unitless"),
            "initial_altitude": (250.0, "ft"),
            "final_altitude": (35000.0, "ft"),
            "altitude_bounds": ((0.0, 35500.0), "ft"),
            "throttle_enforcement": "path_constraint",
            "fix_initial": True,
            "constrain_final": False,
            "fix_duration": False,
            "no_descent": True,
            "initial_bounds": ((0.0, 0.0), "min"),
            "duration_bounds": ((55.0, 165.0), "min"),
        },
        "initial_guesses": {"time": ([0.0, 110.0], "min")},
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
            "initial_mach": (0.7, "unitless"),
            "final_mach": (0.7, "unitless"),
            "mach_bounds": ((0.6799999999999999, 0.72), "unitless"),
            "initial_altitude": (35000.0, "ft"),
            "final_altitude": (35000.0, "ft"),
            "altitude_bounds": ((34500.0, 35500.0), "ft"),
            "throttle_enforcement": "boundary_constraint",
            "fix_initial": False,
            "constrain_final": False,
            "fix_duration": False,
            "initial_bounds": ((55.0, 165.0), "min"),
            "duration_bounds": ((122.5, 367.5), "min"),
        },
        "initial_guesses": {"time": ([110.0, 245.0], "min")},
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
            "initial_mach": (0.7, "unitless"),
            "final_mach": (0.25, "unitless"),
            "mach_bounds": ((0.23, 0.72), "unitless"),
            "initial_altitude": (35000.0, "ft"),
            "final_altitude": (500.0, "ft"),
            "altitude_bounds": ((0.0, 35500.0), "ft"),
            "throttle_enforcement": "path_constraint",
            "fix_initial": False,
            "constrain_final": True,
            "fix_duration": False,
            "no_climb": True,
            "initial_bounds": ((177.5, 532.5), "min"),
            "duration_bounds": ((35.0, 105.0), "min"),
        },
        "initial_guesses": {"time": ([355.0, 70.0], "min")},
    },
    "post_mission": {
        "include_landing": True,
        "constrain_range": True,
        "target_range": (2855.86, "nmi"),
    },
}


csv_path = "models/test_aircraft/Boeing-720.csv"         #input custom .csv
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
prob.run_aviary_problem(record_filename='level2_B720.db', suppress_solver_print=True, make_plots=True)

#All Model Inputs,Calculations, and Arrays
# prob.model.list_inputs()                                
# prob.model.list_outputs()                               
# prob.model.list_outputs(print_arrays=True,units=True) 

#All Mission.Summary values
print("Cruise Mach:            ", prob.get_val(av.Mission.Summary.CRUISE_MACH, units='unitless')[0])
print('Reserve Fuel Burned:    ', prob.get_val(av.Mission.Summary.RESERVE_FUEL_BURNED, units='lbm')[0],'lbm')
print('Fuel Burn:              ', prob.get_val(av.Mission.Summary.FUEL_BURNED, units='lbm')[0],'lbm')
print('Total Fuel Mass:        ', prob.get_val(av.Mission.Summary.TOTAL_FUEL_MASS, units='lbm')[0],'lbm')

###Sources###
#https://en.wikipedia.org/wiki/Boeing_720
#https://www.flugzeuginfo.net/acdata_php/acdata_720_en.php
