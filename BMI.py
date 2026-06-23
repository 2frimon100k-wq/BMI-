import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "আন্ডারওয়েট (Underweight)"
    elif 18.5 <= bmi < 25:
        return "স্বাভাবিক (Normal)"
    elif 25 <= bmi < 30:
        return "অতিরিক্ত ওজন (Overweight)"
    else:
        return "স্থূলতা (Obese)"

st.title("======= BMI Calculator =======")

name = st.text_input("আপনার নাম লিখুন:")
weight = st.number_input("আপনার ওজন লিখুন (কেজিতে):", min_value=1.0)
height = st.number_input("আপনার উচ্চতা লিখুন (মিটারে, যেমন: 1.75):", min_value=0.1)

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    st.write("## ====== আপনার ফলাফল ======")
    st.write(f"**নাম       :** {name}")
    st.write(f"**ওজন       :** {weight} kg")
    st.write(f"**উচ্চতা    :** {height} m")
    st.write(f"**আপনার BMI :** {bmi}")
    st.write(f"**অবস্থা    :** {category}")
    st.write("**Produced by REDWAN**")
