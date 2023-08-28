import streamlit as st
from streamlit_option_menu import option_menu 
from PIL import Image
from pathlib import Path
import altair

st.set_page_config(page_title = 'Szymon Piątek', page_icon = ':blush:', layout = 'centered')

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

# ---- LOAD ASSETS ----
selfie = Image.open('images/szymon_piatek_selfie.jpg')
exchange_rate = Image.open('images/exchange-rate/exchange-rate.png')
exchange_rate2 = Image.open('images/exchange-rate/exchange-rate2.png')
pyassistant = Image.open('images/pyassistant/pyassistant.png')
pyassistant2 = Image.open('images/pyassistant/pyassistant2.png')
dice_roll_simulator = Image.open('images/dice-roll-simulator/dice-roll-simulator.png')
dice_roll_simulator2 = Image.open('images/dice-roll-simulator/dice-roll-simulator2.png')
dice_roll_simulator3 = Image.open('images/dice-roll-simulator/dice-roll-simulator3.png')
dice_roll_simulator4 = Image.open('images/dice-roll-simulator/dice-roll-simulator4.png')

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

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
        st.subheader('Python jest językiem, który wybrałem na samym początku mojej przygody z programowniem.')
        st.subheader('Lubię też uczyć się nowych rzeczy. Dlatego poznałem czym jest projektowanie stron internetowych z użyciem HTML i CSS oraz jak wykonywać podstawowe polecenia w bazach danych SQL.')

        '---'
        # ---- HOBBY ----
        st.title('Hobby')
        st.subheader('##')
        st.subheader('Jak już wspomniałem ... moim hobby jest muzyka i sport')
        st.subheader('Ponad 12 lat gram na pianinie. 🎹')
        st.subheader('Tworzę muzykę "for fun". 🎶')
        st.subheader('[Czasami coś wrzucam na SoundCloud ☁](https://soundcloud.com/shmn1)')
        st.subheader('W weekendy gram ze znajomymi w piłkę nożną. ⚽')
        st.subheader('Od pewnego czasu uczestniczę też w zmaganiach drużyny w lidzę amatorskiej organizowanej na terenie Warszawy.')

    elif selected == options[1]:
        st.title('Projekty')

        with st.container():
            left_column, right_column = st.columns(2)
            with left_column:
                st.subheader('Exchange rate')
                st.subheader('##')
                st.write('Jest to prosty program, który pobiera kursy walut (EUR i USD) ze strony internetowej. 💶💹')
                st.write('Dzięki temu programowi można przeliczyć daną wartość po danym kursie waluty z wybranego dnia na PLN. 💰')
                st.write('[Kurs jest podawany do 4 miejsca po przecinku]*')
            with right_column:
                st.image(exchange_rate2)
        
        with st.container():
            left_column, right_column = st.columns(2)
            with left_column:
                st.image(exchange_rate)
            with right_column:
                st.subheader('''W projekcie wykoszystałem takie biblioteki jak:
                             - customtkinter
    - tkinter
    - bs4 (BeautifulSoup)
    - pandas 
    - Requests 
    - Datetime
    - os
    - python-dotenv''')

        '---'
        
        with st.container():
            left_column, right_column = st.columns(2)
            with left_column:
                st.subheader('PyAssistant')
                st.subheader('##')
                st.write('PyAssistant to asystent głosowy. 🤖')
                st.write('Potrafi on między innymi:')
                st.write('- włączyć film/muzykę na Youtube 🎶')
                st.write('- otworzyć Facebook lub Messenger 💬')
                st.write('- wyszukiwać zapytania w Google 👀')
            with right_column:
                st.image(pyassistant2)
        
        with st.container():
            left_column, right_column = st.columns(2)
            with left_column:
                st.image(pyassistant)
            with right_column:
                st.subheader('''W projekcie wykorzystałem takie biblioteki jak:
                             - customtkinter
    - tkinter
    - sys
    - speech_recognition
    - nltk
    - pyttsx3
    - webbrowser
    - pywhatkit''')
                
        '---'

        with st.container():
            left_column, right_column = st.columns(2)
            with left_column:
                st.subheader('Dice roll simulator')
                st.write('Jest to prosta gra, która polega na rzucaniu kostką. 🎲')
                st.write('Gra się kończy, gdy zostanie zabrane 20 punktów życia ❤')
                st.write('lub gdy 10 razy wyrzuci się większą wartość od przeciwnika. 🤼')
                st.write('Zadawane obrażenia to różnica oczek wyrzuconych przez graczy. 💢')
            with right_column:
                st.image(dice_roll_simulator)
        
        with st.container():
            left_column, right_column = st.columns(2)
            with left_column:
                st.image(dice_roll_simulator4)
            with right_column:
                st.image(dice_roll_simulator2)

        with st.container():
            left_column, right_column = st.columns(2)
            with left_column:
                st.image(dice_roll_simulator3)
            with right_column:
                st.subheader('''W projekcie wykorzystałem takie biblioteki jak:
                             - customtkinter
    - tkinter
    - Pillow
    - random''')




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