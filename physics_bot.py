# FundzaSiveAI - EGCSE Physics Master Tutor
import math

def general_physics_p1():
    print("\n--- 📖 TUTOR: SECTION P1.0 (DENSITY) ---")
    print("DEFINITION: Density is the mass per unit volume of a substance.")
    print("SYLLABUS TIP: If an object is less dense than a liquid, it will float!")
    
    
    choice = input("\nDo you want to (1) Calculate or (2) See Syllabus Tip? ")
    if choice == '1':
        m = float(input("Enter Mass (kg): "))
        v = float(input("Enter Volume (m³): "))
        ans = m / v
        print(f"Result: The Density is {ans} kg/m³")
    else:
        print("Tip: Units for density are kg/m³ or g/cm³.")

def electricity_p8():
    print("\n--- 📖 TUTOR: SECTION P8.0 (OHM'S LAW) ---")
    print("DEFINITION: The current through a conductor is proportional to the voltage.")
    print("FORMULA: V = I × R")
    
    
    v = float(input("Enter Voltage (V): "))
    r = float(input("Enter Resistance (Ω): "))
    print(f"Result: The Current (I) is {v/r} Amperes (A)")

def main():
    while True:
        print("\n--- 🏫 FUNDZASIVE AI: PHYSICS TUTOR ---")
        print("1. Density (P1.0)")
        print("2. Electricity (P8.0)")
        print("X. Exit")
        
        choice = input("\nSelect a topic to learn: ")
        if choice == '1': general_physics_p1()
        elif choice == '2': electricity_p8()
        elif choice == 'X': break

if __name__ == "__main__":
    main()
