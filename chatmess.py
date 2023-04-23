!pip install streamlit-chat
import streamlit as st
from streamlit_chat import message
import random
from time import sleep
st.title('Dự đoán mức độ ưu nhìn')
# st.write('Word matching game')
st.write('Một sản phẩm của Salmon')


def generate_response(user_input):
    lst = ['Chào ', 'Tôi yêu bạn, ', 'Một ngày tốt lành, ']
    return lst[random.randint(0, 2)] + user_input + " mức độ xinh đẹp của bạn là: " + str(random.randint(0, 100)) + '%'

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    input_text = st.empty()
    input_text = st.text_input('Tên của bạn: ', key = "input")
    return input_text

user_input = get_text()



if user_input:
    with st.spinner('ChatSalmon đang nhập...'):
        output = generate_response(user_input)
        sleep(0.5)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        seed_bot = "Baby&backgroundType[]&eyes=bulging&face=round01&mouth=smile01&sides=antenna01&texture=circuits&top=antennaCrooked"
        seed_user = "Callie&backgroundColor=transparent&backgroundType[]&accessories[]&accessoriesColor[]&clothesColor=262e33&clothing=collarAndSweater&clothingGraphic[]&eyebrows=upDown&eyes=default&facialHair[]&facialHairColor[]&hairColor=2c1b18&hatColor=262e33&mouth=smile&skinColor=edb98a&top=shortFlat"
        message(st.session_state['generated'][i], key = str(i+10), is_user=False, avatar_style="bottts", seed = seed_bot)
        message(st.session_state['past'][i], key = str(i+100), is_user = True, avatar_style="avataaars", seed = seed_user)
