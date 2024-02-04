from bmi_lib import bmi_calc, bmi_catogorize, solti_input

def babu():
    print("Welcome to the Saibabu BMI Calculator!")

    weight, height = solti_input()

    bmi = bmi_calc(weight, height)
    category = bmi_catogorize(bmi)

    print("\nBMI Result:")
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    babu()
