# EGCSE Physical Science Master Bot
# Section: Physics - General Physics

def calculate_density():
    print("\n--- Density Calculator (ρ = m / V) ---")
    m = float(input("Enter mass (kg): "))
    v = float(input("Enter volume (m³): "))
    density = m / v
    print(f"The Density is {density} kg/m³")

def calculate_speed():
    print("\n--- Speed Calculator (v = d / t) ---")
    d = float(input("Enter distance (m): "))
    t = float(input("Enter time (s): "))
    speed = d / t
    print(f"The Speed is {speed} m/s")

def main_menu():
    print("Welcome to FundzaSiveAI Physics Bot")
    print("1. Calculate Density")
    print("2. Calculate Speed")
    print("3. Exit")
    
    choice = input("Select an option: ")
    if choice == '1':
        calculate_density()
    elif choice == '2':
        calculate_speed()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main_menu()
