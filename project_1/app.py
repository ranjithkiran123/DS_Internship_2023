import streamlit as st

st.title("Innomatics Data App")
st.snow()

btn_click = st.button("Click Here!")

if btn_click == True:
    st.subheader("You did it! :sunglasses:")
    st.balloons()