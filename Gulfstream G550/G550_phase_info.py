phase_info = {
    "pre_mission": {"include_takeoff": False, "optimize_mass": True},
    "climb_1": {
        "subsystem_options": {"core_aerodynamics": {"method": "computed"}},
        "user_options": {
            "optimize_mach": False,
            "optimize_altitude": False,
            "polynomial_control_order": 1,
            "use_polynomial_control": True,
            "num_segments": 3,
            "order": 3,
            "solve_for_distance": False,
            "initial_mach": (0.3, "unitless"),
            "final_mach": (0.76, "unitless"),
            "mach_bounds": ((0.27999999999999997, 0.78), "unitless"),
            "initial_altitude": (0.0, "ft"),
            "final_altitude": (35000.0, "ft"),
            "altitude_bounds": ((0.0, 35500.0), "ft"),
            "throttle_enforcement": "path_constraint",
            "fix_initial": True,
            "constrain_final": False,
            "fix_duration": False,
            "initial_bounds": ((0.0, 0.0), "min"),
            "duration_bounds": ((18.5, 55.5), "min"),
        },
        "initial_guesses": {"time": ([0.0, 37.0], "min")},
    },
    "cruise_1": {
        "subsystem_options": {"core_aerodynamics": {"method": "computed"}},
        "user_options": {
            "optimize_mach": False,
            "optimize_altitude": False,
            "polynomial_control_order": 1,
            "use_polynomial_control": True,
            "num_segments": 3,
            "order": 3,
            "solve_for_distance": False,
            "initial_mach": (0.76, "unitless"),
            "final_mach": (0.76, "unitless"),
            "mach_bounds": ((0.74, 0.78), "unitless"),
            "initial_altitude": (35000.0, "ft"),
            "final_altitude": (35000.0, "ft"),
            "altitude_bounds": ((34500.0, 35500.0), "ft"),
            "throttle_enforcement": "boundary_constraint",
            "fix_initial": False,
            "constrain_final": False,
            "fix_duration": False,
            "initial_bounds": ((18.5, 55.5), "min"),
            "duration_bounds": ((381.5, 1144.5), "min"),
        },
        "initial_guesses": {"time": ([37.0, 763.0], "min")},
    },
    "descent_1": {
        "subsystem_options": {"core_aerodynamics": {"method": "computed"}},
        "user_options": {
            "optimize_mach": False,
            "optimize_altitude": False,
            "polynomial_control_order": 1,
            "use_polynomial_control": True,
            "num_segments": 3,
            "order": 3,
            "solve_for_distance": False,
            "initial_mach": (0.76, "unitless"),
            "final_mach": (0.3, "unitless"),
            "mach_bounds": ((0.27999999999999997, 0.78), "unitless"),
            "initial_altitude": (35000.0, "ft"),
            "final_altitude": (254.0, "ft"),
            "altitude_bounds": ((0.0, 35500.0), "ft"),
            "throttle_enforcement": "path_constraint",
            "fix_initial": False,
            "constrain_final": True,
            "fix_duration": False,
            "initial_bounds": ((400.0, 1200.0), "min"),
            "duration_bounds": ((17.5, 52.5), "min"),
        },
        "initial_guesses": {"time": ([800.0, 35.0], "min")},
    },
    "post_mission": {
        "include_landing": False,
        "constrain_range": True,
        "target_range": (6867.85, "nmi"),
    },
}