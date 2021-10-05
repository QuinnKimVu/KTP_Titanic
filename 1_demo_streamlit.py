import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('train.csv')

st.title("Trung Tâm Tin Học")
st.header('Data Science')

menu = ['Display Test', 'Display Data', 'Display Chart', 'Display Interactive Widget']

choice = st.sidebar.selectbox('Menu', menu)
if choice == 'Display Text':
    st.subheader('Hành trang tốt nghiệp Data Science')
    st.text('Khóa học được thiết kết nhằm ôn tập và bổ sung kiến thức cho HV Data Science')
    st.markdown('### Có 5 chủ đề: ')
    st.write("""
    - Chủ đề 1
    - Chủ đề 2
    """)
    st.write('### Ngôn ngữ lập trình: Python')
    st.code("st.display_text_function('Nội dung')", language='python')
elif choice == 'Display Chart':
    st.write('## Display Chart')
    count_Pclass = data[['PassengerId', 'Pclass']].groupby(['Pclass']).count()
    st.bar_chart(count_Pclass)
    fig, ax = plt.subplots()
    ax = sns.boxplot(x='Pclass', y='Fare', data=data)
    st.pyplot(fig)
else:
    st.write('## Display Interactive Widget')
    st.write('### input your information')
    name = st.text_input('name: ')
    sex = st.radio('Sex', option=['Male', 'Female'])
    age = st.slider('Age', 1, 100, 1)
    jobtime = st.selectbox('You have', options=['Part time job', 'Full time job'])
    hobbies = st.selectbox('Hobbies', options=['Cooking', 'Reading', 'Writing', 'Travel', 'Others'])
    house = st.checkbox('Have house/ apartment')
    submit = st.button('submit')
    if submit:
        st.write('#### Your Information: ')
        st.write('Name: ', name,
        '- Sex: ', sex,
        '- Age: ', age,
        '- You have a ', jobtime,
        'and a house/apartment' if house else '',
        '- Hobbies: ', ','.join(map(str, hobbies)))