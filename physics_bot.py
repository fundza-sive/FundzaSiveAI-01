# FundzaSiveAI - EGCSE Physics Master Tutor
import math

def physics_p1():
    print("\n--- 📖 TUTOR: SECTION P1.0 (INTRODUCTION TO PHYSICS - DENSITY) ---")
    print("DEFINITION: Density is the mass per unit volume of a substance.")
    print("SYLLABUS TIP: If an object is less dense than a liquid, it will float!")
    
    # Quiz to check understanding
    print("\n--- ❓ QUIZ TIME: Let's see if you understand! ---")
    print("Question: What is the formula for density?")
    print("A) Density = Volume / Mass")
    print("B) Density = Mass / Volume")
    print("C) Density = Mass * Volume")
    
    answer = input("Enter your choice (A, B, or C): ").upper()
    if answer == 'B':
        print("Great job! That's correct. Density = Mass / Volume.")
    else:
        print("Oops, that's not quite right. Let me explain gently:")
        print("Step 1: Density measures how much mass is packed into a given volume.")
        print("Step 2: So, it's mass divided by volume, not the other way around or multiplied.")
        print("Correct answer: B) Density = Mass / Volume")
    
    # Proceed to calculation if desired
    choice = input("\nDo you want to (1) Calculate density or (2) See another Syllabus Tip? Or (X) Back to menu: ").upper()
    if choice == '1':
        try:
            m = float(input("Enter Mass (kg): "))
            v = float(input("Enter Volume (m³): "))
            if v == 0:
                print("Volume can't be zero! Let's try again.")
                return
            ans = m / v
            print(f"Result: The Density is {ans:.2f} kg/m³")
        except ValueError:
            print("Please enter valid numbers. Let's try again next time.")
    elif choice == '2':
        print("Tip: Units for density are kg/m³ or g/cm³.")

def physics_p2():
    print("\n--- 📖 TUTOR: SECTION P2.0 (SPEED, VELOCITY AND ACCELERATION) ---")
    print("DEFINITION: Speed is the distance traveled per unit time. Velocity is speed in a given direction. Acceleration is the change in velocity per unit time.")
    print("SYLLABUS TIP: Acceleration due to gravity near Earth is constant at 10 m/s².")
    
    # Quiz to check understanding
    print("\n--- ❓ QUIZ TIME: Let's see if you understand! ---")
    print("Question: What is the difference between speed and velocity?")
    print("A) Speed is a vector, velocity is scalar")
    print("B) Speed is scalar, velocity is a vector")
    print("C) They are the same")
    
    answer = input("Enter your choice (A, B, or C): ").upper()
    if answer == 'B':
        print("Great job! That's correct. Speed has magnitude only, velocity has magnitude and direction.")
    else:
        print("Not quite. Let me correct you step by step:")
        print("Step 1: Scalar quantities have only magnitude.")
        print("Step 2: Vector quantities have magnitude and direction.")
        print("Step 3: Speed is how fast, velocity is how fast and in which direction.")
        print("Correct answer: B) Speed is scalar, velocity is a vector")
    
    # Proceed to calculation
    choice = input("\nDo you want to (1) Calculate speed or (2) Calculate acceleration? Or (X) Back to menu: ").upper()
    if choice == '1':
        try:
            d = float(input("Enter Distance (m): "))
            t = float(input("Enter Time (s): "))
            if t == 0:
                print("Time can't be zero! Let's try again.")
                return
            ans = d / t
            print(f"Result: The Speed is {ans:.2f} m/s")
        except ValueError:
            print("Please enter valid numbers.")
    elif choice == '2':
        try:
            v_final = float(input("Enter Final Velocity (m/s): "))
            v_initial = float(input("Enter Initial Velocity (m/s): "))
            t = float(input("Enter Time (s): "))
            if t == 0:
                print("Time can't be zero! Let's try again.")
                return
            ans = (v_final - v_initial) / t
            print(f"Result: The Acceleration is {ans:.2f} m/s²")
        except ValueError:
            print("Please enter valid numbers.")

def physics_p3():
    print("\n--- 📖 TUTOR: SECTION P3.0 (MASS AND FORCE) ---")
    print("DEFINITION: Mass is the amount of matter in a body. Force is a push or pull that can change motion.")
    print("SYLLABUS TIP: Weight = mass × gravity (w = mg), with g ≈ 10 m/s² on Earth.")
    
    # Quiz
    print("\n--- ❓ QUIZ TIME: Let's see if you understand! ---")
    print("Question: What is the relationship between mass and weight?")
    print("A) They are the same")
    print("B) Weight is mass times gravity")
    print("C) Mass is weight times gravity")
    
    answer = input("Enter your choice (A, B, or C): ").upper()
    if answer == 'B':
        print("Correct! Weight is a force due to gravity on mass.")
    else:
        print("Let's clarify:")
        print("Step 1: Mass is invariant, measures inertia.")
        print("Step 2: Weight is mg, where g is gravitational acceleration.")
        print("Correct: B)")
    
    # Calculation
    choice = input("\nDo you want to (1) Calculate weight or (X) Back to menu: ").upper()
    if choice == '1':
        try:
            m = float(input("Enter Mass (kg): "))
            g = 10  # As per syllabus
            ans = m * g
            print(f"Result: The Weight is {ans:.2f} N")
        except ValueError:
            print("Invalid input.")

def physics_p4():
    print("\n--- 📖 TUTOR: SECTION P4.0 (WORK, ENERGY AND POWER) ---")
    print("DEFINITION: Work is done when a force moves an object in the direction of the force. Energy is the ability to do work. Power is the rate of doing work or transferring energy.")
    print("SYLLABUS TIP: Energy cannot be created or destroyed, only transferred or transformed (principle of conservation of energy).")
    
    # Quiz
    print("\n--- ❓ QUIZ TIME: Let's see if you understand! ---")
    print("Question: Which formula correctly gives kinetic energy?")
    print("A) KE = m × g × h")
    print("B) KE = ½ × m × v²")
    print("C) KE = force × distance")
    
    answer = input("Enter your choice (A, B, or C): ").upper()
    if answer == 'B':
        print("Excellent! Kinetic energy = ½ m v² (energy due to motion).")
    else:
        print("Not quite. Let me correct you step by step:")
        print("Step 1: Kinetic energy depends on mass and speed (velocity squared).")
        print("Step 2: Gravitational potential energy is mgh (A is for PE).")
        print("Step 3: Work done is force × distance (C), but not KE.")
        print("Correct answer: B) KE = ½ × m × v²")
    
    # Calculation options
    choice = input("\nDo you want to (1) Calculate kinetic energy, (2) Calculate power, or (X) Back to menu: ").upper()
    if choice == '1':
        try:
            m = float(input("Enter Mass (kg): "))
            v = float(input("Enter Speed (m/s): "))
            ke = 0.5 * m * v**2
            print(f"Result: Kinetic Energy is {ke:.2f} J")
        except ValueError:
            print("Please enter valid numbers.")
    elif choice == '2':
        try:
            w = float(input("Enter Work done (J) or Energy transferred (J): "))
            t = float(input("Enter Time (s): "))
            if t == 0:
                print("Time can't be zero!")
                return
            power = w / t
            print(f"Result: Power is {power:.2f} W")
        except ValueError:
            print("Please enter valid numbers.")

def physics_p5():
    print("\n--- 📖 TUTOR: SECTION P5.0 (WAVES) ---")
    print("DEFINITION: A wave is a disturbance that transfers energy without transferring matter. Waves can be transverse (oscillations perpendicular to direction) or longitudinal (parallel).")
    print("SYLLABUS TIP: Wave speed = frequency × wavelength (v = f λ). All electromagnetic waves travel at the same speed in vacuum (3 × 10⁸ m/s).")
    
    # Quiz
    print("\n--- ❓ QUIZ TIME: Let's see if you understand! ---")
    print("Question: What is the relationship for wave speed?")
    print("A) Speed = frequency + wavelength")
    print("B) Speed = frequency × wavelength")
    print("C) Speed = frequency / wavelength")
    
    answer = input("Enter your choice (A, B, or C): ").upper()
    if answer == 'B':
        print("Great job! v = f × λ is correct.")
    else:
        print("Let's fix that gently:")
        print("Step 1: Frequency is waves per second, wavelength is distance per wave.")
        print("Step 2: In one second, number of waves × distance per wave = total distance traveled (speed).")
        print("Step 3: So multiply, not add or divide.")
        print("Correct answer: B) Speed = frequency × wavelength")
    
    # Calculation
    choice = input("\nDo you want to (1) Calculate wave speed or (X) Back to menu: ").upper()
    if choice == '1':
        try:
            f = float(input("Enter Frequency (Hz): "))
            lam = float(input("Enter Wavelength (m): "))
            speed = f * lam
            print(f"Result: Wave speed is {speed:.2f} m/s")
        except ValueError:
            print("Please enter valid numbers.")

def physics_p8():
    print("\n--- 📖 TUTOR: SECTION P8.0 (ELECTRICITY - OHM'S LAW) ---")
    print("DEFINITION: The current through a conductor is proportional to the voltage across it, provided the temperature remains constant.")
    print("FORMULA: V = I × R")
    
    # Quiz to check understanding
    print("\n--- ❓ QUIZ TIME: Let's see if you understand! ---")
    print("Question: If voltage increases and resistance stays the same, what happens to current?")
    print("A) Current decreases")
    print("B) Current increases")
    print("C) Current stays the same")
    
    answer = input("Enter your choice (A, B, or C): ").upper()
    if answer == 'B':
        print("Excellent! That's correct. Since V = I × R, if V increases and R is constant, I must increase.")
    else:
        print("Not quite. Let me correct you step by step:")
        print("Step 1: Ohm's Law states V = I × R.")
        print("Step 2: Solving for I, we get I = V / R.")
        print("Step 3: If V goes up and R doesn't change, I goes up too.")
        print("Correct answer: B) Current increases")
    
    # Proceed to calculation
    choice = input("\nDo you want to (1) Calculate current or (X) Back to menu: ").upper()
    if choice == '1':
        try:
            v = float(input("Enter Voltage (V): "))
            r = float(input("Enter Resistance (Ω): "))
            if r == 0:
                print("Resistance can't be zero! That would cause infinite current. Let's try again.")
                return
            ans = v / r
            print(f"Result: The Current (I) is {ans:.2f} Amperes (A)")
        except ValueError:
            print("Please enter valid numbers. Let's try again next time.")

def main():
    while True:
        print("\n--- 🏫 FUNDZASIVE AI: PHYSICS TUTOR ---")
        print("1. Introduction to Physics - Density (P1.0)")
        print("2. Speed, Velocity and Acceleration (P2.0)")
        print("3. Mass and Force (P3.0)")
        print("4. Work, Energy and Power (P4.0)")
        print("5. Waves (P5.0)")
        print("6. Thermal Physics (P6.0) [Coming soon]")
        print("7. Electrostatics (P7.0) [Coming soon]")
        print("8. Electricity - Ohm's Law (P8.0)")
        print("9. Electric Circuits (P9.0) [Coming soon]")
        print("10. Practical Electricity (P10.0) [Coming soon]")
        print("11. Magnetism (P11.0) [Coming soon]")
        print("12. Digital Electronics (P12.0) [Coming soon]")
        print("13. Electromagnetic Effects (P13.0) [Coming soon]")
        print("14. Atomic Physics (P14.0) [Coming soon]")
        print("15. LED Monitors (P15.0) [Coming soon]")
        print("X. Exit")
        
        choice = input("\nSelect a topic to learn: ").upper()
        if choice == '1':
            physics_p1()
        elif choice == '2':
            physics_p2()
        elif choice == '3':
            physics_p3()
        elif choice == '4':
            physics_p4()
        elif choice == '5':
            physics_p5()
        elif choice == '8':
            physics_p8()
        elif choice == 'X':
            break
        else:
            print("Invalid choice or section not yet implemented. Please select an available topic (1-5,8 for now).")

if __name__ == "__main__":
    main()
