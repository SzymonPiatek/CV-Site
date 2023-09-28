import streamlit as st
from streamlit_option_menu import option_menu 
from pathlib import Path

st.set_page_config(page_title = 'Szymon Piątek', page_icon = ':blush:', layout = 'wide')

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown(
    """
    <style>
        .stApp {
            max-width: 160vh;
            display: inline-block;
            vertical-align: middle;
            margin: auto;
        }
        .block-container {
            margin: 0;
            padding-top: 0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

options_menu = ['O mnie', 'Projekty', 'Kontakt']
icons_menu = ['house', 'book', 'envelope']

def st_nav_menu():
    selected = option_menu(
        menu_title = None,
        options = options_menu,
        icons = icons_menu,
        menu_icon = 'cast',
        default_index = 0,
        orientation = 'horizontal')
    return selected

selected_main = st_nav_menu()

if selected_main:
    if selected_main == options_menu[0]:

        # ---- HEADER SECTION ----
        with st.container():
            left_column, right_column = st.columns(2)
            with left_column:
                st.title('O mnie')
                st.subheader('##')
                st.subheader('Nazywam się Szymon 😁')
                st.subheader('##')
                st.subheader('Mam 21 lat i uczę się programować. 🤓')
                st.subheader('Moim głównym językiem programowania jest Python. 🧐')
                st.subheader('Znam też podstawy HTML, CSS, SQL, JavaScript, R oraz C++. 😉')
                st.subheader('Moim hobby jest muzyka oraz sport. ⚽')
            with right_column:
                # ---- WHAT I DO ----
                st.title('Czym się zajmuję')
                st.subheader('##')
                st.subheader('Na codzień zajmuję się pracą, ale w wolnym czasie skupiam się na programowaniu.')
                st.subheader('Python jest językiem programowania, którego używam na co dzień, ale lubię też uczyć się nowych rzeczy.')
                st.subheader('Dlatego poznałem czym jest projektowanie stron internetowych z użyciem HTML i CSS, jak wykonywać podstawowe polecenia w bazach danych SQL oraz jak przeprowadzać analizy i tworzyć różnego rodzaju wykresy za pomocą języka R i programu R Studio.')
        '---'

        # ---- SKILLS ----
        with st.container():
            st.title('Umięjętnośći')
            st.subheader('##')
            left_column, right_column = st.columns(2)
            with left_column:
                st.subheader('Języki programowania:')
                left, right = st.columns(2)
                with left:
                    st.subheader('⭐⭐⭐Python')
                    st.subheader('⭐R')
                    st.subheader('⭐C++')
                with right:
                    st.subheader('⭐HTML')
                    st.subheader('⭐CSS')
                    st.subheader('⭐JavaScript')
            with right_column:
                st.subheader('Programy:')
                left, right = st.columns(2)
                with left:
                    st.subheader('◽ Visual Studio Code')
                    st.subheader('◽ R Studio')
                    st.subheader('◽ GitHub Desktop')
                    st.subheader('◽ Anaconda')
                with right:
                    st.subheader('◽ Jupyter Notebook')
                    st.subheader('◽ Microsoft Office')
                    st.subheader('◽ AutoCAD / GstarCAD')
                    st.subheader('◽ FL Studio')
        '---'

        # ---- HOBBY ----
        with st.container():
            st.title('Hobby')
            st.subheader('##')
            left_column, right_column = st.columns(2)
            with left_column:
                st.subheader('Jak już wspomniałem ... moim hobby jest muzyka i sport')
                st.subheader('Ponad 12 lat gram na pianinie. 🎹')
                st.subheader('Tworzę muzykę "for fun". 🎶')
                st.subheader('[Czasami coś wrzucam na SoundCloud ☁](https://soundcloud.com/shmn1)')
            with right_column:
                st.subheader('W weekendy gram ze znajomymi w piłkę nożną. ⚽')
                st.subheader('Od pewnego czasu uczestniczę też w zmaganiach drużyny w lidzę amatorskiej organizowanej na terenie Warszawy. 🧜‍♀️') 
                st.subheader('[Liga fanów 🏟](https://ligafanow.pl/statystyki/pilkarz/8939/)')

    elif selected_main == options_menu[1]:
        options_projects = ['Exchange rate v2', 'Exchange rate v1', 'PyAssistant', 'Dice roll simulator']
        amount_projects = len(options_projects)

        left_column, right_column = st.columns((1,2))
        with left_column:
            selected_project = st.selectbox(f'Wybierz projekt: ({amount_projects})', options_projects)
                
        if selected_project == options_projects[options_projects.index('Exchange rate v2')]:

            # ---- EXCHANGE-RATE-V2 ----
            with st.container():
                st.title('Exchange rate v2')
                st.subheader('##')
                left, right = st.columns(2)
                with left:
                    st.write("Jest to strona internetowa stworzona za pomocą python'a i biblioteki streamlit. 🐍")
                    st.write('Na tej stronie możesz przeliczyć daną wartość danej waluty z wybranego dnia na PLN. 💰')
                    st.write('Możesz też wybrać opcję wygenerowania wykresu z 7/14/21/28 dni wstecz')
                    st.write('Kurs jest podawany do 4 miejsca po przecinku, a wynik może być podany do 4 lub 2 miejsca po przecinku. 💶')
                    st.write('Na stronie jest możliwość zalogowania się za pomocą konta google oraz opcja subskrypcji (włączony tryb testowy). 👍')
                    st.subheader('##')
                    st.subheader('''W projekcie wykorzystałem takie biblioteki jak:
                                - streamlit
    - st_paywall
    - bs4 (BeautifulSoup)
    - pandas 
    - lxml
    - requests 
    - datetime
    - os
    - plotly''')
                    st.subheader('[Zobacz projekt na GitHub](https://github.com/SzymonPiatek/Exchange-rate)')
                with right:
                    st.write('Video in preparation...')

        elif selected_project == options_projects[options_projects.index('Exchange rate v1')]:

            # ---- EXCHANGE-RATE-V1 ----
            with st.container():
                st.title('Exchange rate v1')
                st.subheader('##')
                left, right = st.columns(2)
                with left:
                    st.write('Jest to prosty program, który pobiera kursy walut (EUR i USD) ze strony internetowej. 💹')
                    st.write('Dzięki temu programowi można przeliczyć daną wartość po danym kursie waluty z wybranego dnia na PLN. 💰')
                    st.write('Kurs jest podawany do 4 miejsca po przecinku. 💶')
                    st.subheader('##')
                    st.subheader('''W projekcie wykorzystałem takie biblioteki jak:
                                - customtkinter
    - tkinter
    - bs4 (BeautifulSoup)
    - pandas 
    - Requests 
    - Datetime
    - os
    - python-dotenv''')
                    st.subheader('[Zobacz projekt na GitHub](https://github.com/SzymonPiatek/ExchangeRate-Streamlit)')
                with right:
                    st.write('Video in preparation...')

        elif selected_project == options_projects[options_projects.index('PyAssistant')]: 

            # ---- PYASSISTANT ----
            with st.container():
                st.title('PyAssistant')
                st.subheader('##')
                left, right = st.columns(2)
                with left:
                    st.write('PyAssistant to asystent głosowy. 🤖')
                    st.write('Potrafi on między innymi:')
                    st.write('- włączyć film/muzykę na Youtube 🎶')
                    st.write('- otworzyć Facebook lub Messenger 💬')
                    st.write('- wyszukiwać zapytania w Google 👀')
                    st.subheader('''W projekcie wykorzystałem takie biblioteki jak:
                                - customtkinter
    - tkinter
    - sys
    - speech_recognition
    - nltk
    - pyttsx3
    - webbrowser
    - pywhatkit''')
                    st.subheader('[Zobacz projekt na GitHub](https://github.com/SzymonPiatek/PyAssistant)')
                with right:
                    st.write('Video in preparation...')

        elif selected_project == options_projects[options_projects.index('Dice roll simulator')]: 

            # ---- DICE-ROLL-SIMULATOR
            with st.container():
                st.title('Dice roll simulator')
                st.subheader('##')
                left, right = st.columns(2)
                with left:
                    st.write('Jest to prosta gra, która polega na rzucaniu kostką. 🎲')
                    st.write('Gra się kończy, gdy zostanie zabrane 20 punktów życia ❤')
                    st.write('lub gdy 10 razy wyrzuci się większą wartość od przeciwnika. 🤼')
                    st.write('Zadawane obrażenia to różnica oczek wyrzuconych przez graczy. 💢')
                    st.subheader('''W projekcie wykorzystałem takie biblioteki jak:
                                    - customtkinter
    - tkinter
    - Pillow
    - random''')
                    st.subheader('[Zobacz projekt na GitHub](https://github.com/SzymonPiatek/Dice-roll-simulator)')
                with right:
                    st.write('Video in preparation...')

    elif selected_main == options_menu[2]:

        # ---- CONTACT ----
        st.title('Kontakt')
        st.title('##')
        with st.container():
            left_column, right_column = st.columns((3, 5))
            with left_column:
                st.subheader('📞 Telefon komórkowy:')
            with right_column:
                st.subheader('+48 XXX-XXX-XXX')

            left_column, right_column = st.columns((3, 5))
            with left_column:
                st.subheader('📧 Adres e-mail:')
            with right_column:
                st.subheader('szymon.piatek125@gmail.com')
        st.title('##')

        # ---- EXTERNAL-LINKS ----
        st.title('Linki zewnętrzne')
        st.title('##')
        with st.container():
            left_column, right_column = st.columns((3, 5))
            with left_column:
                st.subheader('💻 GitHub:')
            with right_column:
                st.subheader('https://github.com/SzymonPiatek')

            left_column, right_column = st.columns((3, 5))
            with left_column:
                st.subheader('💼 LinkedIn:')
            with right_column:
                st.subheader('https://www.linkedin.com/in/szymon-pi%C4%85tek-19347024a')

            left_column, right_column = st.columns((3, 5))
            with left_column:
                st.subheader('💸 Exchange rate:')
            with right_column:
                st.subheader('https://exchange-rate.streamlit.app')

            left_column, right_column = st.columns((3, 5))
            with left_column:
                st.subheader('🎶 Soundcloud:')
            with right_column:
                st.subheader('https://soundcloud.com/shmn1')