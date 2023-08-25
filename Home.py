import streamlit as st
from streamlit_option_menu import option_menu 
from PIL import Image

st.set_page_config(page_title = 'My site', page_icon = ':blush:')

# ---- LOAD ASSETS ----
selfie = Image.open('images/szymon_piatek_selfie.jpg')

# # ---- HIDE STREAMLIT STYLE ----
# hide_st_style = """
# <style>
# fotter {visibility: hidden;}
# header {visibility: hidden;}
# </style>
# """
# st.markdown(hide_st_style, unsave_allow_html = True)

options = ['O mnie', 'Projekty', 'Kontakt']
icons = ['house', 'book', 'envelope']

def st_nav_menu():
    selected = option_menu(
        menu_title = None,
        options = options,
        icons = icons,
        menu_icon = 'cast',
        default_index = 0,
        orientation = 'horizontal')
    return selected

selected = st_nav_menu()

if selected:
    if selected == options[0]:
        # ---- HEADER SECTION ----
        with st.container():
            left_column, right_column = st.columns(2)
            with left_column:
                st.title('O mnie')
                st.subheader('##')
                st.subheader('Nazywam się Szymon 😁')
                st.subheader('##')
                st.subheader('Mam 21 lat i uczę się programować. 🤓')
                st.subheader('Języki programowania jakich się uczę to Python oraz R. 🧐')
                st.subheader('Znam też podstawy HTML, CSS oraz SQL. 😉')
                st.subheader('Moim hobby jest muzyka oraz sport. ⚽')
            with right_column:
                st.image(selfie)
        
        '---'
        # ---- WHAT I DO ----
        st.title('Czym się zajmuję')
        st.subheader('##')
        st.subheader('Na codzień zajmuję się pracą, ale w wolnym czasie skupiam się na programowaniu.')
        st.subheader('Python jest językiem, który wybrałem na samym początku mojej przygody z programowniem. Decyzji nie żałuję!')
        st.subheader('Lubię też uczyć się nowych rzeczy. Dlatego poznałem czym jest projektowanie stron internetowych z użyciem HTML i CSS oraz jak wykonywać podstawowe polecenia w bazach danych SQL.')

        '---'
        # ---- HOBBY ----
        st.title('Hobby')
        st.subheader('Jak już wspomniałem ... moim hobby jest muzyka i sport')
        st.subheader('Ponad 12 lat gram na pianinie. 🎹')
        st.subheader('Tworzę muzykę "for fun". 🎶')
        st.subheader('[Czasami coś wrzucam na SoundCloud ☁](https://soundcloud.com/shmn1)')
        st.subheader('W weekendy gram ze znajomymi w piłkę nożną. ⚽')
        st.subheader('Od pewnego czasu uczestniczę też w zmaganiach drużyny w lidzę amatorskiej organizowanej na terenie Warszawy.')

    elif selected == options[1]:
        pass

    elif selected == options[2]:
        st.title('Kontakt')
        st.title('##')
        with st.container():
            left_column, right_column = st.columns(2)
            with left_column:
                st.subheader('📞 Telefon komórkowy:')
                st.subheader('📧 Adres e-mail:')
            with right_column:
                st.subheader('+48 XXX-XXX-XXX')
                st.subheader('szymon.piatek125@gmail.com')
            