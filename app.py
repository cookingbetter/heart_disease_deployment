import streamlit as st
import pickle
import numpy as np
model = pickle.load(open('pickle_model.pkl','rb'))



st.beta_set_page_config(
    page_title="Prediction App",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

from PIL import Image
image = Image.open('heart_disease.jpg')

st.image(image,
      use_column_width=True)


def predict_disease(age,sex,trestbps,thalach):
    input=np.array([[age,sex,trestbps,thalach]]).astype(np.float64)
    prediction = model.predict(input)
    #pred = '{0:.{1}f}'.format(prediction[0][0], 2)
    return int(prediction)


def main():
    #st.title("Abalone Age Prediction")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Abalone Age Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    age = st.text_input("Age")
    sex = st.text_input("Sex:0-female, 1-male")
    trestbps = st.text_input("Trestbps")
    thalach = st.text_input("Thalach")

    safe_html ="""  
      <div style="background-color:#80ff80; padding:10px >
      <h2 style="color:white;text-align:center;"> You probably do not have heart disease</h2>
      </div>
    """
    warn_html ="""  
      <div style="background-color:#F4D03F; padding:10px >
      <h2 style="color:white;text-align:center;"> You probably do have heart disease, you should go to doctor</h2>
      </div>
    """
    

    if st.button("Predict the age"):
        output = predict_disease(age,sex,trestbps,thalach)
        st.success('The answer is {}'.format(output))

        if output == 0:
            st.markdown(safe_html,unsafe_allow_html=True)
        elif output == 1:
            st.markdown(warn_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()
