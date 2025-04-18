import streamlit as st

def calculate_bmi(weight, height):
    if height == 0:
        return None  # Avoid division by zero
    bmi = weight / (height ** 2)
    return bmi

def main():
    st.title("BMI Calculator")
    st.write("Enter your weight and height to calculate your BMI")

    weight = st.number_input("Weight (in kg)", min_value=0.0)
    height = st.number_input("Height (in meters)", min_value=0.0)

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)

        if bmi is None:
            st.error("Height cannot be zero. Please enter a valid height.")
        else:
            st.write(f"Your BMI is: {bmi:.2f}")

            if bmi < 18.5:
                st.write("You are underweight")
            elif bmi < 25:
                st.write("You are normal weight")
            elif bmi < 30:
                st.write("You are overweight")
            else:
                st.write("You are obese")

if __name__ == "__main__":
    main()
