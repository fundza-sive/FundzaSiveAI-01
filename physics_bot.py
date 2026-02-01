# FundzaSiveAI - EGCSE Physics Master Bot
# Aligned with Syllabus 6888 (2024-2026)

def general_physics_p1_p3():
    print("\n--- [P1-P3: GENERAL PHYSICS] ---")
    print("1. Density (ρ = m/V)")
    print("2. Speed (v = d/t)")
    print("3. Weight (W = m*g)")
    print("4. Force (F = m*a)")
    
    choice = input("Select a calculation: ")
    if choice == '1':
        m = float(input("Enter Mass (kg): "))
        v = float(input("Enter Volume (m³): "))
        print(f"Density = {m/v} kg/m³")
    elif choice == '2':
        d = float(input("Enter Distance (m): "))
        t = float(input("Enter Time (s): "))
        print(f"Speed = {d/t} m/s")
    elif choice == '3':
        m = float(input("Enter Mass (kg): "))
        g = 10 # Syllabus P2.0 states g = 10 m/s²
        print(f"Weight = {m*g} N")

def energy_work_power_p4():
    print("\n--- [P4: WORK, ENERGY & POWER] ---")
    print("1. Work Done (W = F*d)")
    print("2. Power (P = W/t)")
    print("3. Kinetic Energy (Ek = ½mv²)")
    
    choice = input("Select a calculation: ")
    if choice == '1':
        f = float(input("Enter Force (N): "))
        d = float(input("Enter Distance (m): "))
        print(f"Work Done = {f*d} Joules")

def main_menu():
    while True:
        print("\n--- EGCSE PHYSICS STUDY BOT ---")
        print("A. General Physics (P1-P3)")
        print("B. Work, Energy & Power (P4)")
        print("X. Exit")
        
        choice = input("\nSelect Syllabus Section: ").upper()
        if choice == 'A': general_physics_p1_p3()
        elif choice == 'B': energy_work_power_p4()
        elif choice == 'X': break

if __name__ == "__main__":
    main_menu()
