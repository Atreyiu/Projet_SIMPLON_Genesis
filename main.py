# coding=utf-8

# PYTHON VERSION 3.6 DUE TO PYGAME PACKAGE

# Import libraries
import sys
sys.path.insert(0, '../../')
import os
import pygame
import pygame_menu
# FROM Pygame import sound modue named mixer
from pygame import mixer
# Module allow to open URL
import webbrowser
# module abble to connect an APP with a Workbench DATABASE
import mysql.connector # Package name mysql-connector-python
# Switch named ahri to obtain correct sounds / images / description
import Ahri as ahri

#yoles sangs
# -----------------------------------------------------------------------------
# Constants and global variables
# -----------------------------------------------------------------------------
# Frame per Second
FPS = 60.0
# Screen Window Size
WINDOW_SIZE = (1024, 780)

sound = None  # type: pygame_menu.sound.Sound
surface = None  # type: pygame.Surface
main_menu = None  # type: pygame_menu.Menu

# ABOUT Constants
ABOUT = ['Personnal LoL Trainer Alpha Version {0}'.format(pygame_menu.__version__), '',
         'Developed by : {0}'.format(pygame_menu.__author__),'', 'Jonathan Michel', 'Sacha Kojic', 'Yoann Lucido', 'Romain Grimaldi','',
         'Emails: {0}'.format(pygame_menu.__email__),'', 'jonathanremymichel@laposte.net', 'Kojic.sacha@gmail.com', 'yoann.lucido.data@gmail.com', 'Romain.grimaldi.data@gmail.com']

# DIFFICULTY SET TO EASY BY DEFAULT
DIFFICULTY = ['EASY']

# HELP MENU Constants
HELP = ['Press ESC to enable/disable Menu',
        'Press ENTER to access a Sub-Menu or use an option',
        'Press UP/DOWN to move through Menu',
        'Press LEFT/RIGHT to move through Selectors']

# -----------------------------------------------------------------------------
# Methods engineering
# -----------------------------------------------------------------------------
def main_background():
    """
    Background color of the main menu, on this function user can plot
    images, play sounds, etc.

    :return: None
    """
    global surface
    surface.fill((40, 40, 40))


def check_name_test(value):
    """
    This function tests the text input widget.

    :param value: The widget value
    :type value: str
    :return: None
    """
    print('User name: {0}'.format(value))


# noinspection PyUnusedLocal
def update_menu_sound(value, enabled):
    """
    Update menu sound.

    :param value: Value of the selector (Label and index)
    :type value: tuple
    :param enabled: Parameter of the selector, (True/False)
    :type enabled: bool
    :return: None
    """
    global main_menu
    global sound
    if enabled:
        main_menu.set_sound(sound, recursive=True)
        print('Menu sounds were enabled')
    else:
        main_menu.set_sound(None, recursive=True)
        print('Menu sounds were disabled')


def main(test=False):
    """
    Main program.

    :param test: Indicate function is being tested
    :type test: bool
    :return: None
    """

    # -------------------------------------------------------------------------
    # URL LINKS METHODS
    # -------------------------------------------------------------------------
    def open_youtube_playlist():
        webbrowser.open_new("https://www.youtube.com/watch?v=P3oDTQqexPM&list=PLhPzoh2sEnmVR4X0AxCNR_S4xD2QCqESC")

    def open_youtube():
        webbrowser.open_new("http://www.youtube.com")

    def open_compte_nickel():
        webbrowser.open_new("https://mon.compte-nickel.fr/identifiez-vous")

    def open_google_drive():
        webbrowser.open_new("https://drive.google.com/drive/my-drive")

    def open_TF1_Direct():
        webbrowser.open_new("https://www.tf1.fr/tf1/direct")

    def open_Facebook():
        webbrowser.open_new("https://www.facebook.com/")

    def open_Twitter():
        webbrowser.open_new("https://twitter.com/home")

    def open_Instagram():
        webbrowser.open_new("https://www.instagram.com/?hl=fr")

    def open_Journal_le_monde():
        webbrowser.open_new("https://www.lemonde.fr/")

    def open_Journal_Mediapart():
        webbrowser.open_new("https://www.mediapart.fr/")



    # -------------------------------------------------------------------------
    # Globals
    # -------------------------------------------------------------------------
    global main_menu
    global sound
    global surface

    # -------------------------------------------------------------------------
    # Init pygame
    # -------------------------------------------------------------------------
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # Create pygame screen and objects
    surface = pygame.display.set_mode(WINDOW_SIZE)
    # WINDOW TITLE
    pygame.display.set_caption('@ Personnal LoL Trainer')
    clock = pygame.time.Clock()

    # Init Mixer
    mixer.init()

    #Init DB
    baseDeDonnees = mysql.connector.connect(host="localhost", user="root", password="j0nathan13",
                                            database="champions_list")
    cursor = baseDeDonnees.cursor()

    # REFRESH TABLE IN CASE WE USE
    # cursor.execute("DROP TABLE IF EXISTS Results_games;")
    # cursor.execute("CREATE TABLE Results_games (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, nom VARCHAR(50) NOT NULL, prenom VARCHAR(50) NOT NULL, age VARCHAR(50), pseudo VARCHAR(50), password VARCHAR(50), difficulty VARCHAR(10) )ENGINE=InnoDB DEFAULT CHARSET=utf8;")
    # LOAD DATABASE ENTRY
    baseDeDonnees.commit()
    # CLOSE DATABASE
    baseDeDonnees.close()


    # -------------------------------------------------------------------------
    # Set sounds
    # -------------------------------------------------------------------------
    sound = pygame_menu.sound.Sound()

    # Load example sounds
    sound.load_example_sounds()

    # Disable a sound
    sound.set_sound(pygame_menu.sound.SOUND_TYPE_ERROR, None)

    # -------------------------------------------------------------------------
    # Create menus: Profil Settings
    # -------------------------------------------------------------------------
    settings_menu_theme = pygame_menu.themes.THEME_BLUE.copy()
    settings_menu_theme.title_offset = (5, -2)
    settings_menu_theme.widget_alignment = pygame_menu.locals.ALIGN_CENTER
    settings_menu_theme.widget_font = pygame_menu.font.FONT_OPEN_SANS_LIGHT
    settings_menu_theme.widget_font_size = 20

    settings_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.85,
        onclose=pygame_menu.events.DISABLE_CLOSE,
        theme=settings_menu_theme,
        title='Profil Settings',
        width=WINDOW_SIZE[0] * 0.9,

    )


    # Add text inputs with different configurations

    wid1 = settings_menu.add_text_input('Name: ',
                                        default='',
                                        onreturn=check_name_test,
                                        textinput_id='first_name')
    wid2 = settings_menu.add_text_input('Last name: ',
                                        default='',
                                        maxchar=10,
                                        textinput_id='last_name')
    settings_menu.add_text_input('Your Age: ',
                                 default='',
                                 maxchar=3,
                                 maxwidth=3,
                                 textinput_id='age',
                                 input_type=pygame_menu.locals.INPUT_INT,
                                 cursor_selection_enable=False)
    settings_menu.add_text_input('Pseudo: ',
                                 default='',
                                 textinput_id='Pseudo',
                                 maxwidth=19)
    settings_menu.add_text_input('password: ',
                                 maxchar=8,
                                 password=True,
                                 textinput_id='password')

    # Create selector with 3 difficulty options
    settings_menu.add_selector('Select difficulty ',
                               [('Easy', 'EASY'),
                                ('Medium', 'MEDIUM'),
                                ('Hard', 'HARD')],
                               selector_id='difficulty',
                               default=1)



    # FUCNTION CALLED WITH STORE DATA BUTTON ( TAKE CSV PARAMETERS AND WORKBENCH )

    def data_fun():
        """
        Print data of the menu.

        :return: None
        """
        # CONNECTION TO MYSQL WORKBENCH DATABASE
        baseDeDonnees = mysql.connector.connect(host="localhost",user="root",password="j0nathan13", database="performances_LoL")
        cursor = baseDeDonnees.cursor()


        # WE CREATE DATA VARIABLE TO ASSIGN THE INPUT VALUES ON FORM
        data = settings_menu.get_input_data()
        print('Printing DATA PLEASE WAIT.....')
        # WE STOCK IN VARIABLE THE FIRST NAME INPUT
        # DATA.GET IS A METHOD TO GET THE INPUT DATA
        nom = data.get('first_name')
        prenom = data.get('last_name')
        ages = data.get('age')
        pseudo = data.get('Pseudo')
        password = data.get('password')
        difficulte = data.get('difficulty')



        # WE CREATE INSERT VARIABLE TO INJECT THE SQL REQUEST
        # INTO A VARIABLE NAMED "INSERT"  WE ASSIGN COLUMN NAMES ID, name, etc WITH EMPTY VALUES
        insert = "INSERT INTO Results_games (nom, prenom, age, pseudo, password, difficulty) VALUES (%s, %s, %s, %s, %s, %s)"
        # INTO A VARIABLE NAMED "VAL" WE TAKE THE INPUT USER WITH ALL VALUES
        val = (nom, prenom, ages, pseudo, password, "test")
        # INJECT IN DATABASE THE COLUMNS NAMES IN VARIABLE NAMED "INSERT" WITH THE VALUES VARIABLES NAMED "VAL" FROM INPUT USER
        cursor.execute(insert, val)

        # LOAD DATABASE ENTRY
        baseDeDonnees.commit()
        # CLOSE DATABASE
        baseDeDonnees.close()
        print('DATA SAVED INTO DATABASE SUCCESSFULLY !')

    settings_menu.add_button('Store data', data_fun)  # Call function
    settings_menu.add_button('Back to Main Menu', pygame_menu.events.BACK,
                             align=pygame_menu.locals.ALIGN_CENTER)




    # -------------------------------------------------------------------------
    # Create menus: Main menu
    # -------------------------------------------------------------------------
    main_menu_theme = pygame_menu.themes.THEME_BLUE.copy()
    main_menu_theme.widget_offset = (0, 0.09)
    main_menu_theme.title_font = pygame_menu.font.FONT_COMIC_NEUE
    main_menu_theme.widget_font = pygame_menu.font.FONT_COMIC_NEUE
    main_menu_theme.widget_font_size = 30




    # -------------------------------------------------------------------------
    # Create menus: Column buttons / DASHBOARD
    # -------------------------------------------------------------------------

    button_column_menu_theme = pygame_menu.themes.THEME_BLUE.copy()
    button_column_menu_theme.background_color = pygame_menu.baseimage.BaseImage(
        image_path=pygame_menu.baseimage.IMAGE_EXAMPLE_GRAY_LINES,
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY
    )
    button_column_menu_theme.widget_font_size = 25

    button_column_menu = pygame_menu.Menu(
        columns=3,
        height=WINDOW_SIZE[1] * 0.85,
        onclose=pygame_menu.events.DISABLE_CLOSE,
        rows=50,
        theme=button_column_menu_theme,
        title='Champions List',
        width=WINDOW_SIZE[0] * 0.9,
    )


    # Aatrox BUTTON IN DASHBOARD
    button_column_menu.add_button('Aatrox', ahri.perso_play('Aatrox', pygame_menu, WINDOW_SIZE))
    # AHRI BUTTON IN DASHBORD
    button_column_menu.add_button('Ahri', ahri.perso_play('Ahri', pygame_menu, WINDOW_SIZE))
    # AKALI BUTTON IN DASHBOARD
    button_column_menu.add_button('Akali', ahri.perso_play('Akali', pygame_menu, WINDOW_SIZE))
    # ALISTAR BUTTON IN DASHBOARD
    button_column_menu.add_button('Alistar', ahri.perso_play('Alistar', pygame_menu, WINDOW_SIZE))
    # AMUMU BUTTON IN DASHBOARD
    button_column_menu.add_button('Amumu', ahri.perso_play('Amumu', pygame_menu, WINDOW_SIZE))
    # ANIVIA BUTTON IN DASHBOARD
    button_column_menu.add_button('Anivia', ahri.perso_play('Anivia', pygame_menu, WINDOW_SIZE))
    # Annie BUTTON IN DASHBOARD
    button_column_menu.add_button('Annie', ahri.perso_play('Annie', pygame_menu, WINDOW_SIZE))
    # Aphelios BUTTON IN DASHBOARD
    button_column_menu.add_button('Aphelios', ahri.perso_play('Aphelios', pygame_menu, WINDOW_SIZE))
    # Ashe BUTTON IN DASHBOARD
    button_column_menu.add_button('Ashe', ahri.perso_play('Ashe', pygame_menu, WINDOW_SIZE))
    # Aurelion Sol BUTTON IN DASHBOARD
    button_column_menu.add_button('AurelionSol', ahri.perso_play('AurelionSol', pygame_menu, WINDOW_SIZE))
    # Azir Sol BUTTON IN DASHBOARD
    button_column_menu.add_button('Azir', ahri.perso_play('Azir', pygame_menu, WINDOW_SIZE))
    # BARD Sol BUTTON IN DASHBOARD
    button_column_menu.add_button('Bard', ahri.perso_play('Bard', pygame_menu, WINDOW_SIZE))
    # Blitzcrank Sol BUTTON IN DASHBOARD
    button_column_menu.add_button('Blitzcrank', ahri.perso_play('Blitzcrank', pygame_menu, WINDOW_SIZE))
    # Brand BUTTON IN DASHBOARD
    button_column_menu.add_button('Brand', ahri.perso_play('Brand', pygame_menu, WINDOW_SIZE))
    # Braum BUTTON IN DASHBOARD
    button_column_menu.add_button('Braum', ahri.perso_play('Braum', pygame_menu, WINDOW_SIZE))
    # Caitlyn BUTTON IN DASHBOARD
    button_column_menu.add_button('Caitlyn', ahri.perso_play('Caitlyn', pygame_menu, WINDOW_SIZE))
    # Camille BUTTON IN DASHBOARD
    button_column_menu.add_button('Camille', ahri.perso_play('Camille', pygame_menu, WINDOW_SIZE))
    # Cassiopeia BUTTON IN DASHBOARD
    button_column_menu.add_button('Cassiopeia', ahri.perso_play('Cassiopeia', pygame_menu, WINDOW_SIZE))
    # ChoGath BUTTON IN DASHBOARD
    button_column_menu.add_button('ChoGath', ahri.perso_play('ChoGath', pygame_menu, WINDOW_SIZE))
    # Corki BUTTON IN DASHBOARD
    button_column_menu.add_button('Corki', ahri.perso_play('Corki', pygame_menu, WINDOW_SIZE))
    # Darius BUTTON IN DASHBOARD
    button_column_menu.add_button('Darius', ahri.perso_play('Darius', pygame_menu, WINDOW_SIZE))
    # Diana BUTTON IN DASHBOARD
    button_column_menu.add_button('Diana', ahri.perso_play('Diana', pygame_menu, WINDOW_SIZE))
    # DrMundo BUTTON IN DASHBOARD
    button_column_menu.add_button('DrMundo', ahri.perso_play('DrMundo', pygame_menu, WINDOW_SIZE))
    # Draven BUTTON IN DASHBOARD
    button_column_menu.add_button('Draven', ahri.perso_play('Draven', pygame_menu, WINDOW_SIZE))
    # Ekko BUTTON IN DASHBOARD
    button_column_menu.add_button('Ekko', ahri.perso_play('Ekko', pygame_menu, WINDOW_SIZE))
    # Elise BUTTON IN DASHBOARD
    button_column_menu.add_button('Elise', ahri.perso_play('Elise', pygame_menu, WINDOW_SIZE))
    # Evelynn BUTTON IN DASHBOARD
    button_column_menu.add_button('Evelynn', ahri.perso_play('Evelynn', pygame_menu, WINDOW_SIZE))
    # Ezreal BUTTON IN DASHBOARD
    button_column_menu.add_button('Ezreal', ahri.perso_play('Ezreal', pygame_menu, WINDOW_SIZE))
    # Fiddlesticks BUTTON IN DASHBOARD
    button_column_menu.add_button('Fiddlesticks', ahri.perso_play('Fiddlesticks', pygame_menu, WINDOW_SIZE))
    # Fiora BUTTON IN DASHBOARD
    button_column_menu.add_button('Fiora', ahri.perso_play('Fiora', pygame_menu, WINDOW_SIZE))
    # Fizz BUTTON IN DASHBOARD
    button_column_menu.add_button('Fizz', ahri.perso_play('Fizz', pygame_menu, WINDOW_SIZE))
    # Galio BUTTON IN DASHBOARD
    button_column_menu.add_button('Galio', ahri.perso_play('Galio', pygame_menu, WINDOW_SIZE))
    # Gangplank BUTTON IN DASHBOARD
    button_column_menu.add_button('GangPlank', ahri.perso_play('GangPlank', pygame_menu, WINDOW_SIZE))
    # Garen BUTTON IN DASHBOARD
    button_column_menu.add_button('Garen', ahri.perso_play('Garen', pygame_menu, WINDOW_SIZE))
    # Gnar BUTTON IN DASHBOARD
    button_column_menu.add_button('Gnar', ahri.perso_play('Gnar', pygame_menu, WINDOW_SIZE))
    # Gragas BUTTON IN DASHBOARD
    button_column_menu.add_button('Gragas', ahri.perso_play('Gragas', pygame_menu, WINDOW_SIZE))
    # Graves BUTTON IN DASHBOARD
    button_column_menu.add_button('Graves', ahri.perso_play('Graves', pygame_menu, WINDOW_SIZE))
    # Hecarim BUTTON IN DASHBOARD
    button_column_menu.add_button('Hecarim', ahri.perso_play('Hecarim', pygame_menu, WINDOW_SIZE))
    # Heimerdinger BUTTON IN DASHBOARD
    button_column_menu.add_button('Heimerdinger', ahri.perso_play('Heimerdinger', pygame_menu, WINDOW_SIZE))
    # Illaoi BUTTON IN DASHBOARD
    button_column_menu.add_button('Illaoi', ahri.perso_play('Illaoi', pygame_menu, WINDOW_SIZE))
    # Irelia BUTTON IN DASHBOARD
    button_column_menu.add_button('Irelia', ahri.perso_play('Irelia', pygame_menu, WINDOW_SIZE))
    # Ivern BUTTON IN DASHBOARD
    button_column_menu.add_button('Ivern', ahri.perso_play('Ivern', pygame_menu, WINDOW_SIZE))
    # Janna BUTTON IN DASHBOARD
    button_column_menu.add_button('Janna', ahri.perso_play('Janna', pygame_menu, WINDOW_SIZE))
    # Jarvan IV BUTTON IN DASHBOARD
    button_column_menu.add_button('JarvanIV', ahri.perso_play('JarvanIV', pygame_menu, WINDOW_SIZE))
    # Jax BUTTON IN DASHBOARD
    button_column_menu.add_button('Jax', ahri.perso_play('Jax', pygame_menu, WINDOW_SIZE))
    # Jayce BUTTON IN DASHBOARD
    button_column_menu.add_button('Jayce', ahri.perso_play('Jayce', pygame_menu, WINDOW_SIZE))
    # Jhin BUTTON IN DASHBOARD
    button_column_menu.add_button('Jhin', ahri.perso_play('Jhin', pygame_menu, WINDOW_SIZE))
    # Jinx BUTTON IN DASHBOARD
    button_column_menu.add_button('Jinx', ahri.perso_play('Jinx', pygame_menu, WINDOW_SIZE))
    # KaiSa BUTTON IN DASHBOARD
    button_column_menu.add_button('KaiSa', ahri.perso_play('KaiSa', pygame_menu, WINDOW_SIZE))
    # Kalista BUTTON IN DASHBOARD
    button_column_menu.add_button('Kalista', ahri.perso_play('Kalista', pygame_menu, WINDOW_SIZE))
    # Karma BUTTON IN DASHBOARD
    button_column_menu.add_button('Karma', ahri.perso_play('Karma', pygame_menu, WINDOW_SIZE))
    # Karthus BUTTON IN DASHBOARD
    button_column_menu.add_button('Karthus', ahri.perso_play('Karthus', pygame_menu, WINDOW_SIZE))
    # Kassadin BUTTON IN DASHBOARD
    button_column_menu.add_button('Kassadin', ahri.perso_play('Kassadin', pygame_menu, WINDOW_SIZE))
    # Katarina BUTTON IN DASHBOARD
    button_column_menu.add_button('Katarina', ahri.perso_play('Katarina', pygame_menu, WINDOW_SIZE))
    # Kayle BUTTON IN DASHBOARD
    button_column_menu.add_button('Kayle', ahri.perso_play('Kayle', pygame_menu, WINDOW_SIZE))
    # Kayn BUTTON IN DASHBOARD
    button_column_menu.add_button('Kayn', ahri.perso_play('Kayn', pygame_menu, WINDOW_SIZE))
    # Kennen BUTTON IN DASHBOARD
    button_column_menu.add_button('Kennen', ahri.perso_play('Kennen', pygame_menu, WINDOW_SIZE))
    # KhaZix BUTTON IN DASHBOARD
    button_column_menu.add_button('KhaZix', ahri.perso_play('KhaZix', pygame_menu, WINDOW_SIZE))
    # Kindred BUTTON IN DASHBOARD
    button_column_menu.add_button('Kindred', ahri.perso_play('Kindred', pygame_menu, WINDOW_SIZE))
    # Kled BUTTON IN DASHBOARD
    button_column_menu.add_button('Kled', ahri.perso_play('Kled', pygame_menu, WINDOW_SIZE))
    # KogMaw BUTTON IN DASHBOARD
    button_column_menu.add_button('KogMaw', ahri.perso_play('KogMaw', pygame_menu, WINDOW_SIZE))
    # Leblanc BUTTON IN DASHBOARD
    button_column_menu.add_button('Leblanc', ahri.perso_play('Leblanc', pygame_menu, WINDOW_SIZE))
    # LeeSin BUTTON IN DASHBOARD
    button_column_menu.add_button('LeeSin', ahri.perso_play('LeeSin', pygame_menu, WINDOW_SIZE))
    # Leona BUTTON IN DASHBOARD
    button_column_menu.add_button('Leona', ahri.perso_play('Leona', pygame_menu, WINDOW_SIZE))
    # Lissandra BUTTON IN DASHBOARD
    button_column_menu.add_button('Lissandra', ahri.perso_play('Lissandra', pygame_menu, WINDOW_SIZE))
    # Lucian BUTTON IN DASHBOARD
    button_column_menu.add_button('Lucian', ahri.perso_play('Lucian', pygame_menu, WINDOW_SIZE))
    # Lulu BUTTON IN DASHBOARD
    button_column_menu.add_button('Lulu', ahri.perso_play('Lulu', pygame_menu, WINDOW_SIZE))
    # Lux BUTTON IN DASHBOARD
    button_column_menu.add_button('Lux', ahri.perso_play('Lux', pygame_menu, WINDOW_SIZE))
    # MaitreYi BUTTON IN DASHBOARD
    button_column_menu.add_button('MaitreYi', ahri.perso_play('MaitreYi', pygame_menu, WINDOW_SIZE))
    # Malphite BUTTON IN DASHBOARD
    button_column_menu.add_button('Malphite', ahri.perso_play('Malphite', pygame_menu, WINDOW_SIZE))
    # Malzahar BUTTON IN DASHBOARD
    button_column_menu.add_button('Malzahar', ahri.perso_play('Malzahar', pygame_menu, WINDOW_SIZE))
    # Maokai BUTTON IN DASHBOARD
    button_column_menu.add_button('Maokai', ahri.perso_play('Maokai', pygame_menu, WINDOW_SIZE))
    # MissFortune BUTTON IN DASHBOARD
    button_column_menu.add_button('MissFortune', ahri.perso_play('MissFortune', pygame_menu, WINDOW_SIZE))
    # Mordekaiser BUTTON IN DASHBOARD
    button_column_menu.add_button('Mordekaiser', ahri.perso_play('Mordekaiser', pygame_menu, WINDOW_SIZE))
    # Morgana BUTTON IN DASHBOARD
    button_column_menu.add_button('Morgana', ahri.perso_play('Morgana', pygame_menu, WINDOW_SIZE))
    # Nami BUTTON IN DASHBOARD
    button_column_menu.add_button('Nami', ahri.perso_play('Nami', pygame_menu, WINDOW_SIZE))
    # Nasus BUTTON IN DASHBOARD
    button_column_menu.add_button('Nasus', ahri.perso_play('Nasus', pygame_menu, WINDOW_SIZE))
    # Nautilus BUTTON IN DASHBOARD
    button_column_menu.add_button('Nautilus', ahri.perso_play('Nautilus', pygame_menu, WINDOW_SIZE))
    # Neeko BUTTON IN DASHBOARD
    button_column_menu.add_button('Neeko', ahri.perso_play('Neeko', pygame_menu, WINDOW_SIZE))
    # Nidalee BUTTON IN DASHBOARD
    button_column_menu.add_button('Nidalee', ahri.perso_play('Nidalee', pygame_menu, WINDOW_SIZE))
    # Nocturne BUTTON IN DASHBOARD
    button_column_menu.add_button('Nocturne', ahri.perso_play('Nocturne', pygame_menu, WINDOW_SIZE))
    # NunuEtWillump BUTTON IN DASHBOARD
    button_column_menu.add_button('NunuEtWillump', ahri.perso_play('NunuEtWillump', pygame_menu, WINDOW_SIZE))
    # Olaf BUTTON IN DASHBOARD
    button_column_menu.add_button('Olaf', ahri.perso_play('Olaf', pygame_menu, WINDOW_SIZE))
    # Orianna BUTTON IN DASHBOARD
    button_column_menu.add_button('Orianna', ahri.perso_play('Orianna', pygame_menu, WINDOW_SIZE))
    # Ornn BUTTON IN DASHBOARD
    button_column_menu.add_button('Ornn', ahri.perso_play('Ornn', pygame_menu, WINDOW_SIZE))
    # Pantheon BUTTON IN DASHBOARD
    button_column_menu.add_button('Pantheon', ahri.perso_play('Pantheon', pygame_menu, WINDOW_SIZE))
    # Poppy BUTTON IN DASHBOARD
    button_column_menu.add_button('Poppy', ahri.perso_play('Poppy', pygame_menu, WINDOW_SIZE))
    # Pyke BUTTON IN DASHBOARD
    button_column_menu.add_button('Pyke', ahri.perso_play('Pyke', pygame_menu, WINDOW_SIZE))
    # Qiyana BUTTON IN DASHBOARD
    button_column_menu.add_button('Qiyana', ahri.perso_play('Qiyana', pygame_menu, WINDOW_SIZE))
    # Quinn BUTTON IN DASHBOARD
    button_column_menu.add_button('Quinn', ahri.perso_play('Quinn', pygame_menu, WINDOW_SIZE))
    # Rakan BUTTON IN DASHBOARD
    button_column_menu.add_button('Rakan', ahri.perso_play('Rakan', pygame_menu, WINDOW_SIZE))
    # Rammus BUTTON IN DASHBOARD
    button_column_menu.add_button('Rammus', ahri.perso_play('Rammus', pygame_menu, WINDOW_SIZE))
    # RekSai BUTTON IN DASHBOARD
    button_column_menu.add_button('RekSai', ahri.perso_play('RekSai', pygame_menu, WINDOW_SIZE))
    # Renekton BUTTON IN DASHBOARD
    button_column_menu.add_button('Renekton', ahri.perso_play('Renekton', pygame_menu, WINDOW_SIZE))
    # Rengar BUTTON IN DASHBOARD
    button_column_menu.add_button('Rengar', ahri.perso_play('Rengar', pygame_menu, WINDOW_SIZE))
    # Riven BUTTON IN DASHBOARD
    button_column_menu.add_button('Riven', ahri.perso_play('Riven', pygame_menu, WINDOW_SIZE))
    # Rumble BUTTON IN DASHBOARD
    button_column_menu.add_button('Rumble', ahri.perso_play('Rumble', pygame_menu, WINDOW_SIZE))
    # Ryze BUTTON IN DASHBOARD
    button_column_menu.add_button('Ryze', ahri.perso_play('Ryze', pygame_menu, WINDOW_SIZE))
    # Sejuani BUTTON IN DASHBOARD
    button_column_menu.add_button('Sejuani', ahri.perso_play('Sejuani', pygame_menu, WINDOW_SIZE))
    # Senna BUTTON IN DASHBOARD
    button_column_menu.add_button('Senna', ahri.perso_play('Senna', pygame_menu, WINDOW_SIZE))
    # Sett BUTTON IN DASHBOARD
    button_column_menu.add_button('Sett', ahri.perso_play('Sett', pygame_menu, WINDOW_SIZE))
    # Shaco BUTTON IN DASHBOARD
    button_column_menu.add_button('Shaco', ahri.perso_play('Shaco', pygame_menu, WINDOW_SIZE))
    # Shen BUTTON IN DASHBOARD
    button_column_menu.add_button('Shen', ahri.perso_play('Shen', pygame_menu, WINDOW_SIZE))
    # Shyvana BUTTON IN DASHBOARD
    button_column_menu.add_button('Shyvana', ahri.perso_play('Shyvana', pygame_menu, WINDOW_SIZE))
    # Singed BUTTON IN DASHBOARD
    button_column_menu.add_button('Singed', ahri.perso_play('Singed', pygame_menu, WINDOW_SIZE))
    # Sion BUTTON IN DASHBOARD
    button_column_menu.add_button('Sion', ahri.perso_play('Sion', pygame_menu, WINDOW_SIZE))
    # Sivir BUTTON IN DASHBOARD
    button_column_menu.add_button('Sivir', ahri.perso_play('Sivir', pygame_menu, WINDOW_SIZE))
    # Skarner BUTTON IN DASHBOARD
    button_column_menu.add_button('Skarner', ahri.perso_play('Skarner', pygame_menu, WINDOW_SIZE))
    # Sona BUTTON IN DASHBOARD
    button_column_menu.add_button('Sona', ahri.perso_play('Sona', pygame_menu, WINDOW_SIZE))
    # Soraka BUTTON IN DASHBOARD
    button_column_menu.add_button('Soraka', ahri.perso_play('Soraka', pygame_menu, WINDOW_SIZE))
    # Swain BUTTON IN DASHBOARD
    button_column_menu.add_button('Swain', ahri.perso_play('Swain', pygame_menu, WINDOW_SIZE))
    # Sylas BUTTON IN DASHBOARD
    button_column_menu.add_button('Sylas', ahri.perso_play('Sylas', pygame_menu, WINDOW_SIZE))
    # Syndra BUTTON IN DASHBOARD
    button_column_menu.add_button('Syndra', ahri.perso_play('Syndra', pygame_menu, WINDOW_SIZE))
    # Tahm Kench BUTTON IN DASHBOARD
    button_column_menu.add_button('TahmKench', ahri.perso_play('TahmKench', pygame_menu, WINDOW_SIZE))
    # Taliyah BUTTON IN DASHBOARD
    button_column_menu.add_button('Taliyah', ahri.perso_play('Taliyah', pygame_menu, WINDOW_SIZE))
    # Talon BUTTON IN DASHBOARD
    button_column_menu.add_button('Talon', ahri.perso_play('Talon', pygame_menu, WINDOW_SIZE))
    # Taric BUTTON IN DASHBOARD
    button_column_menu.add_button('Taric', ahri.perso_play('Taric', pygame_menu, WINDOW_SIZE))
    # Teemo BUTTON IN DASHBOARD
    button_column_menu.add_button('Teemo', ahri.perso_play('Teemo', pygame_menu, WINDOW_SIZE))
    # Thresh BUTTON IN DASHBOARD
    button_column_menu.add_button('Thresh', ahri.perso_play('Thresh', pygame_menu, WINDOW_SIZE))
    # Tristana BUTTON IN DASHBOARD
    button_column_menu.add_button('Tristana', ahri.perso_play('Tristana', pygame_menu, WINDOW_SIZE))
    # Trundle BUTTON IN DASHBOARD
    button_column_menu.add_button('Trundle', ahri.perso_play('Trundle', pygame_menu, WINDOW_SIZE))
    # Tryndamere BUTTON IN DASHBOARD
    button_column_menu.add_button('Tryndamere', ahri.perso_play('Tryndamere', pygame_menu, WINDOW_SIZE))
    # TwistedFate BUTTON IN DASHBOARD
    button_column_menu.add_button('TwistedFate', ahri.perso_play('TwistedFate', pygame_menu, WINDOW_SIZE))
    # Twitch BUTTON IN DASHBOARD
    button_column_menu.add_button('Twitch', ahri.perso_play('Twitch', pygame_menu, WINDOW_SIZE))
    # Udyr BUTTON IN DASHBOARD
    button_column_menu.add_button('Udyr', ahri.perso_play('Udyr', pygame_menu, WINDOW_SIZE))
    # Urgot BUTTON IN DASHBOARD
    button_column_menu.add_button('Urgot', ahri.perso_play('Urgot', pygame_menu, WINDOW_SIZE))
    # Varus BUTTON IN DASHBOARD
    button_column_menu.add_button('Varus', ahri.perso_play('Varus', pygame_menu, WINDOW_SIZE))
    # Vayne BUTTON IN DASHBOARD
    button_column_menu.add_button('Vayne', ahri.perso_play('Vayne', pygame_menu, WINDOW_SIZE))
    # Veigar BUTTON IN DASHBOARD
    button_column_menu.add_button('Veigar', ahri.perso_play('Veigar', pygame_menu, WINDOW_SIZE))
    # VelKoz BUTTON IN DASHBOARD
    button_column_menu.add_button('VelKoz', ahri.perso_play('VelKoz', pygame_menu, WINDOW_SIZE))
    # Vi BUTTON IN DASHBOARD
    button_column_menu.add_button('Vi', ahri.perso_play('Vi', pygame_menu, WINDOW_SIZE))
    # Viktor BUTTON IN DASHBOARD
    button_column_menu.add_button('Viktor', ahri.perso_play('Viktor', pygame_menu, WINDOW_SIZE))
    # Vladimir BUTTON IN DASHBOARD
    button_column_menu.add_button('Vladimir', ahri.perso_play('Vladimir', pygame_menu, WINDOW_SIZE))
    # Volibear BUTTON IN DASHBOARD
    button_column_menu.add_button('Volibear', ahri.perso_play('Volibear', pygame_menu, WINDOW_SIZE))
    # Warwick BUTTON IN DASHBOARD
    button_column_menu.add_button('Warwick', ahri.perso_play('Warwick', pygame_menu, WINDOW_SIZE))
    # Wukong BUTTON IN DASHBOARD
    button_column_menu.add_button('Wukong', ahri.perso_play('Wukong', pygame_menu, WINDOW_SIZE))
    # Xayah BUTTON IN DASHBOARD
    button_column_menu.add_button('Xayah', ahri.perso_play('Xayah', pygame_menu, WINDOW_SIZE))
    # Xerath BUTTON IN DASHBOARD
    button_column_menu.add_button('Xerath', ahri.perso_play('Xerath', pygame_menu, WINDOW_SIZE))
    # XinZhao BUTTON IN DASHBOARD
    button_column_menu.add_button('XinZhao', ahri.perso_play('XinZhao', pygame_menu, WINDOW_SIZE))
    # Yasuo BUTTON IN DASHBOARD
    button_column_menu.add_button('Yasuo', ahri.perso_play('Yasuo', pygame_menu, WINDOW_SIZE))
    # Yorick BUTTON IN DASHBOARD
    button_column_menu.add_button('Yorick', ahri.perso_play('Yorick', pygame_menu, WINDOW_SIZE))
    # Yuumi BUTTON IN DASHBOARD
    button_column_menu.add_button('Yuumi', ahri.perso_play('Yuumi', pygame_menu, WINDOW_SIZE))
    # Zac BUTTON IN DASHBOARD
    button_column_menu.add_button('Zac', ahri.perso_play('Zac', pygame_menu, WINDOW_SIZE))
    # Zed BUTTON IN DASHBOARD
    button_column_menu.add_button('Zed', ahri.perso_play('Zed', pygame_menu, WINDOW_SIZE))
    # Ziggs BUTTON IN DASHBOARD
    button_column_menu.add_button('Ziggs', ahri.perso_play('Ziggs', pygame_menu, WINDOW_SIZE))
    # Zilean BUTTON IN DASHBOARD
    button_column_menu.add_button('Zilean', ahri.perso_play('Zilean', pygame_menu, WINDOW_SIZE))
    # Zoe BUTTON IN DASHBOARD
    button_column_menu.add_button('Zoe', ahri.perso_play('Zoe', pygame_menu, WINDOW_SIZE))
    # Zyra BUTTON IN DASHBOARD
    button_column_menu.add_button('Zyra', ahri.perso_play('Zyra', pygame_menu, WINDOW_SIZE))


    # -------------------------------------------------------------------------
    # Create menus: Help
    # -------------------------------------------------------------------------
    help_theme = pygame_menu.themes.Theme(
        background_color=(30, 50, 107, 190),  # 75% opacity
        title_background_color=(120, 45, 30, 190),
        title_font=pygame_menu.font.FONT_FRANCHISE,
        title_font_size=60,
        widget_font=pygame_menu.font.FONT_FRANCHISE,
        widget_font_color=(170, 170, 170),
        widget_font_size=45,
        widget_shadow=False,
        widget_shadow_position=pygame_menu.locals.POSITION_SOUTHEAST,
    )

    help_menu = pygame_menu.Menu(
        height=600,  # Fullscreen
        onclose=pygame_menu.events.DISABLE_CLOSE,  # Pressing ESC button does nothing
        theme=help_theme,
        title='Help',
        width=800,
    )
    for m in HELP:
        help_menu.add_label(m, align=pygame_menu.locals.ALIGN_CENTER)
    help_menu.add_vertical_margin(25)
    help_menu.add_button('Back to Main Menu', pygame_menu.events.BACK)

    # -------------------------------------------------------------------------
    # Create menus:About # NAMED AS CREDITS IN MENU #
    # -------------------------------------------------------------------------
    about_theme = pygame_menu.themes.THEME_BLUE.copy()
    about_theme.widget_margin = (0, 0)
    about_theme.widget_offset = (0, 0.05)

    about_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.8,
        onclose=pygame_menu.events.DISABLE_CLOSE,
        theme=about_theme,
        title='About',
        width=WINDOW_SIZE[0] * 0.8,
    )
    for m in ABOUT:
        about_menu.add_label(m, align=pygame_menu.locals.ALIGN_CENTER, font_size=20)
    about_menu.add_label('')
    about_menu.add_button('Back to Main Menu', pygame_menu.events.BACK)

    main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.7,
        width=WINDOW_SIZE[0] * 0.8,
        onclose=pygame_menu.events.EXIT,  # User press ESC button
        title='Main menu',
        theme=main_menu_theme,
    )


    main_menu.add_label("Welcome to Genesis SOFTWARE")
    main_menu.add_label("")

    main_menu.add_button('Champions List', button_column_menu)
    main_menu.add_button(help_menu.get_title(), help_menu)  # Add help submenu
    main_menu.add_button('Profil settings', settings_menu)

    #main_menu.add_button('More Settings', more_settings_menu)
    #main_menu.add_button('Menu in textures and columns', button_column_menu)
    main_menu.add_button('Credits', about_menu)
    main_menu.add_selector('Sounds Effects ',
                           [('Off', False), ('On', True)],
                           onchange=update_menu_sound)
    main_menu.add_label("")
    main_menu.add_button('Quit', pygame_menu.events.EXIT)

   # assert main_menu.get_widget('first_name', recursive=True) is wid1
   # assert main_menu.get_widget('last_name', recursive=True) is wid2
   # assert main_menu.get_widget('last_name') is None

    # WELCOME SOUND
    mixer.music.load('welcome.mp3')
    mixer.music.play()

    # -------------------------------------------------------------------------
    # Main loop
    # -------------------------------------------------------------------------
    while True:

        # Tick
        clock.tick(FPS)

        # Paint background
        main_background()

        # Main menu
        main_menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)

        # Flip surface
        pygame.display.flip()

        # At first loop returns
        if test:
            break

if __name__ == '__main__':
    main()
