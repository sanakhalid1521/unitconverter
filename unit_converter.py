import streamlit as st

# ✅ Sabse pehle page config lagayen!
st.set_page_config(page_title="Unit Converter", layout="centered")

# Custom CSS for Styling
st.markdown("""
    <style>
        /* Background Color */
        .stApp {
            background-color: #f7f7f7;
        }
        
        /* Title Styling */
        .title-container {
            background-color: #ff6600;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
        }
        .title-container h1 {
            color: white;
        }

        /* Button Styling */
        .stButton>button {
            background-color: #ff6600;
            color: white;
            border-radius: 10px;
            width: 100%;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #ff4500;
            transition: 0.3s;
        }

        /* Dropdown Styling */
        .stSelectbox>div>div {
            cursor: pointer !important;
            border: 2px solid #ff6600 !important;
            border-radius: 5px !important;
        }

        /* Input Box Styling */
        .stNumberInput>div>div>input {
            border: 2px solid #ff6600;
            border-radius: 5px;
            padding: 5px;
        }

        /* Custom Result Box */
        .result-box {
            background-color: #ffcc00;
            color: #000;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Global dictionary for unit conversions
conversions = {
    "Length": {"Meter": 1, "Kilometer": 0.001, "Mile": 0.000621371, "Yard": 1.09361},
    "Weight": {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274},
    "Temperature": {"Celsius": lambda c: c, "Fahrenheit": lambda c: c * 9/5 + 32},
    "Currency": {"USD": 1, "EUR": 0.92, "PKR": 277, "INR": 83}  # Example rates
}

def convert_units(value, from_unit, to_unit, unit_type):
    if unit_type == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return value * 9/5 + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        return value  # Same unit case

    return value * (conversions[unit_type][to_unit] / conversions[unit_type][from_unit])

# Title Section with Styling
st.markdown('<div class="title-container"><h1>🌟 Advanced Unit Converter 🌟</h1></div>', unsafe_allow_html=True)

# Dropdowns for unit types and specific units
unit_type = st.selectbox("Select Unit Type:", list(conversions.keys()))  

if unit_type:
    available_units = list(conversions[unit_type].keys())  
    col1, col2, col3 = st.columns(3)
    with col1:
        from_unit = st.selectbox("From Unit:", available_units)
    with col2:
        to_unit = st.selectbox("To Unit:", available_units)
    with col3:
        value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")
    
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit, unit_type)
        
        # 🎨 Custom Result Box with Yellow Background
        st.markdown(f"""
            <div class="result-box">
                {value} {from_unit} = {result:.2f} {to_unit}
            </div>
        """, unsafe_allow_html=True)
