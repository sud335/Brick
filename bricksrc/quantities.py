from rdflib import Literal
from .namespaces import SKOS, OWL, BRICK, QUDTQK


quantity_definitions = {
    "Air_Quality": {
        "subclasses": {
            "CO2_Level": {},
            "PM10_Level": {},
            "PM25_Level": {},
            "TVOC_Level": {},
        },
    },
    "Angle": {OWL.sameAs: QUDTQK["Angle"]},
    "Conductivity": {OWL.sameAs: QUDTQK["Conductivity"]},
    "Capacity": {OWL.sameAs: QUDTQK["Capacity"]},
    "Enthalpy": {
        SKOS.definition: Literal(
            "(also known as heat content), thermodynamic quantity equal to the sum of the internal energy of a system plus the product of the pressure volume work done on the system. H = E + pv, where H = enthalpy or total heat content, E = internal energy of the system, p = pressure, and v = volume. (Compare to [[specific enthalpy]].)"
        ),
        OWL.sameAs: QUDTQK["Enthalpy"],
    },
    "Grains": {},
    "Power": {
        OWL.sameAs: QUDTQK["Power"],
        "subclasses": {
            "Electric_Power": {
                OWL.sameAs: QUDTQK["ElectricPower"],
                "subclasses": {
                    "Apparent_Power": {OWL.sameAs: QUDTQK["ApparentPower"]},
                    "Active_Power": {
                        OWL.sameAs: QUDTQK["ActivePower"],
                        OWL.equivalentClass: BRICK["Real_Power"],
                    },
                    "Real_Power": {},
                    "Reactive_Power": {OWL.sameAs: QUDTQK["ReactivePower"]},
                    "Complex_Power": {OWL.sameAs: QUDTQK["ComplexPower"]},
                },
            },
            "Peak_Power": {
                SKOS.definition: Literal(
                    "Tracks the highest (peak) observed power in some interval"
                )
            },
            "Thermal_Power": {},
        },
    },
    "Cloudage": {},
    "Current": {
        "subclasses": {
            "Electric_Current": {
                OWL.sameAs: QUDTQK["ElectricCurrent"],
                "subclasses": {
                    "Current_Angle": {},
                    "Current_Magnitude": {},
                    "Current_Imbalance": {},
                    "Current_Total_Harmonic_Distortion": {},
                    "Alternating_Current_Frequency": {},
                },
            },
        },
    },
    "Voltage": {
        OWL.sameAs: QUDTQK["Voltage"],
        "subclasses": {
            "Electric_Voltage": {
                "subclasses": {
                    "Voltage_Magnitude": {},
                    "Voltage_Angle": {},
                    "Voltage_Imbalance": {},
                },
            },
        },
    },
    "Daytime": {},
    "Dewpoint": {OWL.sameAs: QUDTQK["DewPointTemperature"]},
    "Direction": {"subclasses": {"Wind_Direction": {}}},
    "Energy": {
        OWL.sameAs: QUDTQK["Energy"],
        "subclasses": {
            "Electric_Energy": {},
            "Thermal_Energy": {OWL.sameAs: QUDTQK["ThermalEnergy"]},
        },
    },
    "Flow": {OWL.sameAs: QUDTQK["VolumeFlowRate"], "subclasses": {"Flow_Loss": {}}},
    "Frequency": {
        OWL.sameAs: QUDTQK["Frequency"],
        "subclasses": {"Alternating_Current_Frequency": {}},
    },
    "Humidity": {
        "subclasses": {
            "Relative_Humidity": {OWL.sameAs: QUDTQK["RelativeHumidity"]},
            "Absolute_Humidity": {OWL.sameAs: QUDTQK["AbsoluteHumidity"]},
        }
    },
    "Illuminance": {OWL.sameAs: QUDTQK["Illuminance"]},
    "Irradiance": {
        OWL.sameAs: QUDTQK["Irradiance"],
        "subclasses": {"Solar_Irradiance": {}},
    },
    "Level": {
        "subclasses": {
            "CO2_Level": {},
            "PM10_Level": {},
            "PM25_Level": {},
            "TVOC_Level": {},
        },
    },
    "Luminance": {
        OWL.sameAs: QUDTQK["Luminance"],
        "subclasses": {
            "Luminous_Flux": {OWL.sameAs: QUDTQK["LuminousFlux"]},
            "Luminous_Intensity": {OWL.sameAs: QUDTQK["LuminousIntensity"]},
        },
    },
    "Occupancy": {"subclasses": {"Occupancy_Count": {}, "Occupancy_Percentage": {}}},
    "Position": {},
    "Power_Factor": {OWL.sameAs: QUDTQK["PowerFactor"]},
    "Precipitation": {},
    "Pressure": {
        OWL.sameAs: QUDTQK["Pressure"],
        "subclasses": {
            "Atmospheric_Pressure": {OWL.sameAs: QUDTQK["AtmosphericPressure"]},
            "Dynamic_Pressure": {},
            "Static_Pressure": {OWL.sameAs: QUDTQK["StaticPressure"]},
            "Velocity_Pressure": {
                OWL.sameAs: QUDTQK["DynamicPressure"],
                OWL.equivalentClass: BRICK["Dynamic_Pressure"],
            },
        },
    },
    "Radiance": {OWL.sameAs: QUDTQK["Radiance"], "subclasses": {"Solar_Radiance": {}}},
    "Speed": {OWL.sameAs: QUDTQK["Speed"], "subclasses": {"Wind_Speed": {}}},
    "Temperature": {
        OWL.sameAs: QUDTQK["Temperature"],
        "subclasses": {
            "Operative_Temperature": {},
            "Radiant_Temperature": {},
            "Dry_Bulb_Temperature": {},
            "Wet_Bulb_Temperature": {},
        },
    },
    "Time": {
        OWL.sameAs: QUDTQK["Time"],
        "subclasses": {"Acceleration_Time": {}, "Deceleration_Time": {}},
    },
    "Torque": {OWL.sameAs: QUDTQK["Torque"]},
    "Weather_Condition": {},
}
