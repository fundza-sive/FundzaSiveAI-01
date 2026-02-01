import random

def quiz_general_physics():
    print("\n--- 📝 QUICK QUIZ: GENERAL PHYSICS ---")
    # Generate random numbers for a mass and volume question
    mass = random.randint(10, 100)
    volume = random.randint(2, 10)
    correct_density = round(mass / volume, 2)
    
    print(f"Question: An object has a mass of {mass}kg and a volume of {volume}m³.")
    print("What is its Density? (Round to 2 decimal places)")
    
    answer = float(input("Your Answer: "))
    
    if answer == correct_density:
        print("✅ Correct! Excellent work.")
    else:
        print(f"❌ Not quite. Remember: Density = Mass / Volume.")
        print(f"So: {mass} / {volume} = {correct_density} kg/m³")

def general_physics_tutor():
    print("\n--- [P1-P3: TUTOR MODE] ---")
    print("Topic: Density (Syllabus P1.2)")
    print("Definition: Density is the ratio of mass to volume.")
    print("Unit: kg/m³ or g/cm³")
    
    choice = input("\nDo you want to (1) Calculate or (2) Take a Quiz? ")
    if choice == '1':
        # ... your existing calculation code ...
        pass
    elif choice == '2':
        quiz_general_physics()
