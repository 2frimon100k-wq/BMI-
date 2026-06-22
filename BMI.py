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

# Input নেওয়া
print("======= BMI Calculator =======")
name = input("আপনার নাম লিখুন: ")
weight = float(input("আপনার ওজন লিখুন (কেজিতে): "))
height = float(input("আপনার উচ্চতা লিখুন (মিটারে, যেমন: 1.75): "))
bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)
print("\n====== আপনার ফলাফল ======")
print(f"নাম       : {name}")
print(f"ওজন       : {weight} kg")
print(f"উচ্চতা    : {height} m")
print(f"আপনার BMI : {bmi}")
print(f"অবস্থা    : {category}")
print("Produced by REDWAN")