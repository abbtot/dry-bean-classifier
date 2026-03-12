import streamlit as st
import joblib
import numpy as np

import streamlit as st
import joblib
import numpy as np

# DESIGN
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
h1 {
    text-align: center;
    color: white;
}
</style>
""", unsafe_allow_html=True)

model = joblib.load("best_model.pkl")


bean_names = {
0: "SEKER",
1: "BARBUNYA",
2: "BOMBAY",
3: "CALI",
4: "DERMASON",
5: "HOROZ",
6: "SIRA"
}

st.markdown("<h1>🌱 Dry Bean Classification System</h1>", unsafe_allow_html=True)

st.write("Enter Bean Features")

Area = st.number_input("Area")
Perimeter = st.number_input("Perimeter")
MajorAxisLength = st.number_input("MajorAxisLength")
MinorAxisLength = st.number_input("MinorAxisLength")
AspectRation = st.number_input("AspectRation")
Eccentricity = st.number_input("Eccentricity")
ConvexArea = st.number_input("ConvexArea")
EquivDiameter = st.number_input("EquivDiameter")
Extent = st.number_input("Extent")
Solidity = st.number_input("Solidity")
Roundness = st.number_input("Roundness")
Compactness = st.number_input("Compactness")
ShapeFactor1 = st.number_input("ShapeFactor1")
ShapeFactor2 = st.number_input("ShapeFactor2")
ShapeFactor3 = st.number_input("ShapeFactor3")
ShapeFactor4 = st.number_input("ShapeFactor4")

if st.button("Predict"):

    features = np.array([[Area, Perimeter, MajorAxisLength, MinorAxisLength,
                          AspectRation, Eccentricity, ConvexArea, EquivDiameter,
                          Extent, Solidity, Roundness, Compactness,
                          ShapeFactor1, ShapeFactor2, ShapeFactor3, ShapeFactor4]])

    prediction = model.predict(features)[0]

    bean_name = bean_names[prediction]

    st.success(f"Predicted Bean Class: {bean_name}")
    
    recommendations = {"SEKER": "Store in small-bean inventory category.",
                       "BARBUNYA": "Assign to premium packaging.",
                       "BOMBAY": "Send to bulk processing.",
                       "CALI": "Suitable for export-quality packaging.",
                       "DERMASON": "Standard storage for local market.",
                       "HOROZ": "Inspect bean quality before packaging.",
                       "SIRA": "Separate for further quality inspection."   }

    st.info(f"Recommended Action: {recommendations[bean_name]}")
