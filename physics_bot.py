# FundzaSiveAI - EGCSE Physics FULL MASTER (P1-P13)
import random

def physics_tutor():
    while True:
        print("\n--- 🏫 EGCSE PHYSICS MASTER TUTOR ---")
        print("1. P1-P3: General Physics (Density/Speed/Force)")
        print("2. P4: Work, Energy & Power")
        print("3. P5: Waves & Light")
        print("4. P6: Thermal Physics (Heat)")
        print("5. P8-P10: Electricity & Circuits")
        print("6. P12: Digital Electronics (Logic Gates)")
        print("7. P13: Transformers")
        print("X. Exit")

        choice = input("\nSelect Syllabus Section: ").upper()

        if choice == '1':
            print("\n[P3.1 Mass vs Weight]")
            print("Definition: Weight is a force. It is the effect of a gravitational field on a mass.")
            print("Syllabus Tip: Gravity (g) on Earth is constant at 10 m/s².")
            m = float(input("Enter mass in kg to find weight: "))
            print(f"Weight = {m * 10} Newtons (N)")

        elif choice == '4':
            print("\n[P6.1 Thermal Physics]")
            print("Definition: Expansion is when particles move further apart due to increased kinetic energy.")
                        print("Quiz: Does a gas expand more or less than a solid when heated?")
            ans = input("Your answer (more/less): ").lower()
            if 'more' in ans: print("✅ Correct! Gases expand the most.")

        elif choice == '6':
            print("\n[P12.0 Digital Electronics]")
            print("Logic Gate: AND Gate")
            print("Rule: The output is HIGH (1) only if BOTH inputs are HIGH (1).")
                        in1 = input("Input A (0 or 1): ")
            in2 = input("Input B (0 or 1): ")
            out = "1" if in1=="1" and in2=="1" else "0"
            print(f"The AND gate output is: {out}")

        elif choice == 'X':
            break
