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


def predict_disease(age,sex,trestbps, chol, fbs, thalach, exang):
    input=np.array([[age,sex,trestbps, chol, fbs, thalach, exang]).astype(np.float64)
    #coefficient to translate from 'ммоль/л' to 'mg/dl'
    input[0][3] = input[0][3] * 38.46
    input[0][4] = (1 if (input[0][4] * 38.46) > 120 else 0)
    prediction = model.predict(input)
    #pred = '{0:.{1}f}'.format(prediction[0][0], 2)
    return int(prediction)


def main():
    #st.title("Heart Disease Prediction")
    html_temp = """
    <div style="background:#086116 ;padding:10px">
    <h2 style="color:white;text-align:center;">Heart disease prediction AI app </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    age = st.text_input("Возраст")
    sex = st.text_input("Пол:0-женщина, 1-мужчина")
    trestbps = st.text_input("Артериальное давление в покое")  
    chol = st.text_input("Уровень холестрерина в крови(ммоль/л)")
    #coefficient to translate from 'ммоль/л' to 'mg/dl'
    #chol = float(38.46) * chol
    fbs = st.text_input("Уровень сахара в крови натощак(ммоль/л)")
    #fbs = float(38.46) * fbs
    #fbs = (1 if float(fbs) > 120 else 0)
    thalach = st.text_input("Максимально количество ударов сердца в минуту")
    exang = st.text_input("Наличие ангины, вызванной физ. нагрузкой(0-нет, 1-да)")
    
    #['age', 'sex', 'trestbps', 'chol', 'fbs', 'thalach', 'exang']
    
    safe_html ="""  
      <div style="background-color:#80ff80; padding:10px >
      <h2 style="color:white;text-align:center;"> У вас вероятно нет болезней, связанных с сердцем</h2>
      </div>
    """
    warn_html ="""  
      <div style="background-color:#F4D03F; padding:10px >
      <h2 style="color:white;text-align:center;"> Скорее всего у вас проблемы с сердцем, стоит обратиться к врачу</h2>
      </div>
    """
    

    if st.button("Спрогнозировать болезнь"):
        output = predict_disease(age,sex,trestbps, chol, fbs, thalach, exang)
        st.success('Ответ:  {}'.format(output))

        if output == 0:
            st.markdown(safe_html,unsafe_allow_html=True)
        elif output == 1:
            st.markdown(warn_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()
