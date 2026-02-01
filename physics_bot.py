# FundzaSiveAI - EGCSE Physics Master Bot (Full Syllabus Version)
# Aligned with Eswatini EGCSE Physical Science (6888) 2024-2026

import math

def general_physics_p1_p3():
    print("\n--- [P1-P3: GENERAL PHYSICS] ---")
    print("1. Density (ρ = m/V)")
    print("2. Speed (v = d/t)")
    print("3. Weight (W = m * g)")
    
    choice = input("Select calculation: ")
    if choice == '1':
        m = float(input("Enter Mass (kg): "))
        v = float(input("Enter Volume (m³): "))
        print(f"Density = {round(m/v, 2)} kg/m³")
    elif choice == '2':
        d = float(input("Enter Distance (m): "))
        t = float(input("Enter Time (s): "))
        print(f"Speed = {round(d/t, 2)} m/s")
    elif choice == '3':
        m = float(input("Enter Mass (kg): "))
        g = 10 # Constant required by EGCSE syllabus P2.0
        print(f"Weight = {m*g} N")

def work_energy_power_p4():
    print("\n--- [P4.0: WORK, ENERGY & POWER] ---")
    print("1. Work Done (W = F * d)")
    print("2. Power (P = E / t)")
    print("3. Kinetic Energy (Ek = ½mv²)")
    print("4. Potential Energy (Ep = mgh)")
    
    choice = input("Select calculation: ")
    if choice == '1':
        f = float(input("Enter Force (N): "))
        d = float(input("Enter Distance (m): "))
        print(f"Work Done = {f*d} Joules")
    elif choice == '3':
        m = float(input("Enter Mass (kg): "))
        v = float(input("Enter Velocity (m/s): "))
        print(f"Kinetic Energy = {0.5 * m * (v**2)} J")

def waves_and_light_p5():
    print("\n--- [P5.0: WAVES & LIGHT] ---")
    print("1. Wave Equation (v = f * λ)")
    print("2. Refractive Index (n = sin i / sin r)")
    
    choice = input("Select calculation: ")
    if choice == '1':
        f = float(input("Enter Frequency (Hz): "))
        w = float(input("Enter Wavelength (m): "))
        print(f"Wave Speed (v) = {f * w} m/s")
    elif choice == '2':
        i = float(input("Enter Angle of Incidence (degrees): "))
        r = float(input("Enter Angle of Refraction (degrees): "))
        # Syllabus P5.2 requirement: n = sin i / sin r
        n = math.sin(math.radians(i)) / math.sin(math.radians(r))
        print(f"Refractive Index (n) = {round(n, 2)}")

def electricity_p8_p10():
    print("\n--- [P8-P10: ELECTRICITY] ---")
    print("1. Ohm's Law (V = I * R)")
    print("2. Charge (Q = I * t)")
    print("3. Electrical Energy (E = I * V * t)")
    
    choice = input("Select calculation: ")
    if choice == '1':
        i = float(input("Enter Current (A): "))
        r = float(input("Enter Resistance (Ω): "))
        print(f"Potential Difference (V) = {i * r} V")
    elif choice == '3':
        # Formula E = IVt aligned with Syllabus P8.1
        i = float(input("Enter Current (A): "))
        v = float(input("Enter Voltage (V): "))
        t = float(input("Enter Time (s): "))
        print(f"Energy (E) = {i * v * t} Joules")

def transformers_p11():
    print("\n--- [P11.0: ELECTROMAGNETISM] ---")
    print("Calculation: Transformer Equation (Vp/Vs = Np/Ns)")
    vp = float(input("Enter Primary Voltage (Vp): "))
    np = float(input("Enter Primary Turns (Np): "))
    ns = float(input("Enter Secondary Turns (Ns): "))
    # Solving for Vs: Vs = (Vp * Ns) / Np
    vs = (vp * ns) / np
    print(f"Secondary Voltage (Vs) = {vs} V")

def main_menu():
    while True:
        print("\n--- FUNDZASIVE AI: EGCSE PHYSICS MASTER ---")
        print("1. General Physics (P1-P3)")
        print("2. Work, Energy & Power (P4)")
        print("3. Waves & Light (P5)")
        print("4. Electricity (P8-P10)")
        print("5. Transformers (P11)")
        print("X. Exit")
        
        choice = input("\nSelect Syllabus Section: ").upper()
        if choice == '1': general_physics_p1_p3()
        elif choice == '2': work_energy_power_p4()
        elif choice == '3': waves_and_light_p5()
        elif choice == '4': electricity_p8_p10()
        elif choice == '5': transformers_p11()
        elif choice == 'X': break

if __name__ == "__main__":
    main_menu()
