# FundzaSiveAI - EGCSE Physics FULL TUTOR BOT (6888 Syllabus)
import random
import math

def tutor_quiz(topic, formula, unit, question_text, correct_calc):
    print(f"\n--- 📖 TUTOR MODE: {topic} ---")
    print(f"Definition: {question_text}")
    print(f"Formula: {formula} | Unit: {unit}")
    
    mode = input("\nChoose: (1) Calculate for me or (2) Quiz me: ")
    if mode == '2':
        # Simple quiz logic with random numbers
        val1 = random.randint(5, 20)
        val2 = random.randint(2, 10)
        ans = round(correct_calc(val1, val2), 2)
        print(f"\n📝 QUIZ: If we have values of {val1} and {val2}, what is the result?")
        user_ans = float(input("Your answer: "))
        if user_ans == ans:
            print("✅ Correct! You've mastered this syllabus point.")
        else:
            print(f"❌ Not quite. The answer is {ans} {unit}. Keep practicing!")
    return mode

def main_menu():
    while True:
        print("\n--- 🏫 FUNDZASIVE AI: PHYSICS TUTOR ---")
        print("P1. General Physics (Density/Speed)")
        print("P4. Energy & Work")
        print("P5. Waves & Light")
        print("P8. Electricity")
        print("P11. Transformers")
        print("X. Exit")
        
        choice = input("\nSelect Section: ").upper()
        
        if choice == 'P1':
            m = tutor_quiz("Density", "ρ = m/V", "kg/m³", "Density is mass per unit volume.", lambda x, y: x/y)
            if m == '1':
                mass = float(input("Enter Mass (kg): "))
                vol = float(input("Enter Volume (m³): "))
                print(f"Density = {mass/vol} kg/m³")

        elif choice == 'P4':
            m = tutor_quiz("Work Done", "W = F x d", "Joules", "Work is done when a force moves an object.", lambda x, y: x*y)
            if m == '1':
                f = float(input("Enter Force (N): "))
                d = float(input("Enter Distance (m): "))
                print(f"Work Done = {f*d} J")

        elif choice == 'P5':
            m = tutor_quiz("Wave Speed", "v = f x λ", "m/s", "Wave speed is frequency multiplied by wavelength.", lambda x, y: x*y)
            if m == '1':
                f = float(input("Enter Frequency (Hz): "))
                w = float(input("Enter Wavelength (m): "))
                print(f"Speed = {f*w} m/s")

        elif choice == 'P8':
            m = tutor_quiz("Ohm's Law", "V = I x R", "Volts", "Voltage is current times resistance.", lambda x, y: x*y)
            if m == '1':
                i = float(input("Enter Current (A): "))
                r = float(input("Enter Resistance (Ω): "))
                print(f"Voltage = {i*r} V")

        elif choice == 'X': break

if __name__ == "__main__":
    main_menu()
