import streamlit as st
import pandas as pd
from utils import *
from streamlit_extras.switch_page_button import switch_page
def main():
    x = st.slider("x", 0, 10)

    if x == 1:
        switch_page("page1")
    elif x==2:
        switch_page("page2")

            
if __name__ == "__main__":
    main()

# Local: streamlit run streamlit_tutorial.py
# Streamlit Sharing 
# render, heroku, AWS EC2
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)','petal width (cm)']
"""
    # Bienvenida y logeo
    st.title('Bienvendo al portal predictivo de la empresa XYZ')
    st.write('**Por favor ingrese su identificador de cliente para poder usar el servicio:**')
    client_id = st.number_input('Introduzca su ID de cliente', value=0)

    # Comprobar identidad
    if st.button('Iniciar Sesión'): # Botón para iniciar sesión
        is_valid = check_client_id(client_id)
        if not is_valid:
            st.write('**Identificador de cliente no válido, por favor ingrese un identificador válido.**')
        else:
            # Selección del servicio
            st.success('¡Inicio de sesión exitoso!')
            st.write('**Por favor seleccione qué sistema predictivo desea utilizar hoy:**')
            sist_pred = st.radio('Selecciona una opción:', ('Quiero predecir flores', 'Quiero predecir imágenes'))



    if sist_pred=='Quiero predecir flores':
        option = st.radio('¿Cómo desea realizar la predicción?:', ('Ingresando datos manualmente', 'Subiendo un archivo CSV'))

        if option == 'Ingresando datos manualmente':
            st.write('**Ingresa los datos para realizar la predicción de la flor:**')
            input_data = {}
            input_data['sepal length (cm)'] = [st.number_input('sepal length (cm)', value=0.0)]
            input_data['sepal width (cm)'] = [st.number_input('sepal width (cm)', value=0.0)]
            input_data['petal length (cm)'] = [st.number_input('petal length (cm)', value=0.0)]
            input_data['petal width (cm)'] = [st.number_input('petal width (cm)', value=0.0)]            
            if st.button('Realizar Predicción'):
                predicted_value = predict_flores(pd.DataFrame(input_data))
                st.write('El resultado de la predicción es:', predicted_value)

        elif option == 'Subiendo un archivo CSV':
            st.title('Predicción de flores en archivo CSV')
            uploaded_file = st.file_uploader("Selecciona un archivo CSV", type=['csv'])
            if uploaded_file is not None:              
                df = pd.read_csv(uploaded_file)
                st.write('**Vista Previa del DataFrame:**')
                st.write(df)
                st.subheader('Realizar Predicción')
                st.write('**Selecciona las columnas para la predicción:**')
                feature_cols = st.multiselect('Selecciona las características', df.columns)
                if st.button('Realizar Predicción con CSV'):
                    predicted_values = predict_flores(df[feature_cols])
                    st.write('Los resultados de la predicción son:')
                    st.write(predicted_values)
    elif sist_pred=='Quiero predecir imágenes':
        st.write('En construcción')
"""