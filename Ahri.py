# coding=utf-8

# Import libraries
import sys
sys.path.insert(0, '../../')
import os
import pygame
import pygame_menu
from pygame import mixer
import webbrowser
import mysql.connector # Package name mysql-connector-python
import play_sound as play
from gtts import gTTS
from pygame import mixer
import csv
import pandas as pd
from matplotlib import pyplot as plt

WINDOW_SIZE = (1024, 780)

# Init Mixer
mixer.init()

# Language we want to use
language = 'fr'




# METHODS DEFINE IMAGE BY CHAMPIONS

def define_img(name, pygame_menu):
    if name == "Aatrox":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Aatrox_MENU
    if name == "Ahri":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Ahri_MENU
    if name == "Akali":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Akali_MENU
    if name == "Alistar":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Alistar_MENU
    if name == "Amumu":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Amumu_MENU
    if name == "Anivia":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Anivia_MENU
    if name == "Annie":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Annie_MENU
    if name == "Aphelios":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Aphelios_MENU
    if name == "Ashe":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Ashe_MENU
    if name == "AurelionSol":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_AurelionSol_MENU
    if name == "Azir":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Azir_MENU
    if name == "Bard":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Bard_MENU
    if name == "Blitzcrank":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Blitzcrank_MENU
    if name == "Brand":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Brand_MENU
    if name == "Braum":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Braum_MENU
    if name == "Caitlyn":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Caitlyn_MENU
    if name == "Camille":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Camille_MENU
    if name == "Cassiopeia":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Cassiopeia_MENU
    if name == "ChoGath":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_ChoGath_MENU
    if name == "Corki":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Corki_MENU
    if name == "Darius":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Darius_MENU
    if name == "Diana":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Diana_MENU
    if name == "DrMundo":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_DrMundo_MENU
    if name == "Draven":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Draven_MENU
    if name == "Ekko":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Ekko_MENU
    if name == "Elise":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Elise_MENU
    if name == "Evelynn":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Evelynn_MENU
    if name == "Ezreal":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Ezreal_MENU
    if name == "Fiddlesticks":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Fiddlesticks_MENU
    if name == "Fiora":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Fiora_MENU
    if name == "Fizz":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Fizz_MENU
    if name == "Galio":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Galio_MENU
    if name == "GangPlank":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_GangPlank_MENU
    if name == "Garen":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Garen_MENU
    if name == "Gnar":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Gnar_MENU
    if name == "Gragas":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Gragas_MENU
    if name == "Graves":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Graves_MENU
    if name == "Hecarim":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Hecarim_MENU
    if name == "Heimerdinger":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Heimerdinger_MENU
    if name == "Illaoi":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Illaoi_MENU
    if name == "Irelia":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Irelia_MENU
    if name == "Ivern":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Ivern_MENU
    if name == "Janna":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Janna_MENU
    if name == "JarvanIV":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_JarvanIV_MENU
    if name == "Jax":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Jax_MENU
    if name == "Jayce":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Jayce_MENU
    if name == "Jhin":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Jhin_MENU
    if name == "Jinx":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Jinx_MENU
    if name == "KaiSa":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_KaiSa_MENU
    if name == "Kalista":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Kalista_MENU
    if name == "Karma":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Karma_MENU
    if name == "Karthus":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Karthus_MENU
    if name == "Kassadin":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Kassadin_MENU
    if name == "Katarina":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Katarina_MENU
    if name == "Kayle":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Kayle_MENU
    if name == "Kayn":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Kayn_MENU
    if name == "Kennen":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Kennen_MENU
    if name == "KhaZix":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_KhaZix_MENU
    if name == "Kindred":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Kindred_MENU
    if name == "Kled":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Kled_MENU
    if name == "KogMaw":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_KogMaw_MENU
    if name == "Leblanc":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Leblanc_MENU
    if name == "LeeSin":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_LeeSin_MENU
    if name == "Leona":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Leona_MENU
    if name == "Lissandra":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Lissandra_MENU
    if name == "Lucian":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Lucian_MENU
    if name == "Lulu":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Lulu_MENU
    if name == "Lux":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Lux_MENU
    if name == "MaitreYi":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_MaitreYi_MENU
    if name == "Malphite":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Malphite_MENU
    if name == "Malzahar":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Malzahar_MENU
    if name == "Maokai":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Maokai_MENU
    if name == "MissFortune":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_MissFortune_MENU
    if name == "Mordekaiser":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Mordekaiser_MENU
    if name == "Morgana":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Morgana_MENU
    if name == "Nami":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Nami_MENU
    if name == "Nasus":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Nasus_MENU
    if name == "Nautilus":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Nautilus_MENU
    if name == "Neeko":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Neeko_MENU
    if name == "Nidalee":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Nidalee_MENU
    if name == "Nocturne":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Nocturne_MENU
    if name == "NunuEtWillump":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_NunuEtWillump_MENU
    if name == "Olaf":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Olaf_MENU
    if name == "Orianna":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Orianna_MENU
    if name == "Ornn":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Ornn_MENU
    if name == "Pantheon":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Pantheon_MENU
    if name == "Poppy":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Poppy_MENU
    if name == "Pyke":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Pyke_MENU
    if name == "Qiyana":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Qiyana_MENU
    if name == "Quinn":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Quinn_MENU
    if name == "Rakan":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Rakan_MENU
    if name == "Rammus":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Rammus_MENU
    if name == "RekSai":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_RekSai_MENU
    if name == "Renekton":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Renekton_MENU
    if name == "Rengar":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Rengar_MENU
    if name == "Riven":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Riven_MENU
    if name == "Rumble":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Rumble_MENU
    if name == "Ryze":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Ryze_MENU
    if name == "Sejuani":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Sejuani_MENU
    if name == "Senna":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Senna_MENU
    if name == "Sett":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Sett_MENU
    if name == "Shaco":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Shaco_MENU
    if name == "Shen":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Shen_MENU
    if name == "Shyvana":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Shyvana_MENU
    if name == "Singed":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Singed_MENU
    if name == "Sion":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Sion_MENU
    if name == "Sivir":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Sivir_MENU
    if name == "Skarner":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Skarner_MENU
    if name == "Sona":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Sona_MENU
    if name == "Soraka":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Soraka_MENU
    if name == "Swain":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Swain_MENU
    if name == "Sylas":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Sylas_MENU
    if name == "Syndra":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Syndra_MENU
    if name == "TahmKench":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_TahmKench_MENU
    if name == "Taliyah":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Taliyah_MENU
    if name == "Talon":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Talon_MENU
    if name == "Taric":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Taric_MENU
    if name == "Teemo":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Teemo_MENU
    if name == "Thresh":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Thresh_MENU
    if name == "Tristana":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Tristana_MENU
    if name == "Trundle":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Trundle_MENU
    if name == "Tryndamere":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Tryndamere_MENU
    if name == "TwistedFate":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_TwistedFate_MENU
    if name == "Twitch":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Twitch_MENU
    if name == "Udyr":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Udyr_MENU
    if name == "Urgot":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Urgot_MENU
    if name == "Varus":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Varus_MENU
    if name == "Vayne":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Vayne_MENU
    if name == "Veigar":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Veigar_MENU
    if name == "VelKoz":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_VelKoz_MENU
    if name == "Vi":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Vi_MENU
    if name == "Viktor":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Viktor_MENU
    if name == "Vladimir":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Vladimir_MENU
    if name == "Volibear":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Volibear_MENU
    if name == "Warwick":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Warwick_MENU
    if name == "Wukong":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Wukong_MENU
    if name == "Xayah":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Xayah_MENU
    if name == "Xerath":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Xerath_MENU
    if name == "XinZhao":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_XinZhao_MENU
    if name == "Yasuo":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Yasuo_MENU
    if name == "Yorick":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Yorick_MENU
    if name == "Yuumi":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Yuumi_MENU
    if name == "Zac":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Zac_MENU
    if name == "Zed":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Zed_MENU
    if name == "Ziggs":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Ziggs_MENU
    if name == "Zilean":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Zilean_MENU
    if name == "Zoe":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Zoe_MENU
    if name == "Zyra":
        image = pygame_menu.baseimage.IMAGE_EXAMPLE_Zyra_MENU

    return image

# METHODS DESCRIPTION BY CHAMPIONS
def define_desc(name, pygame_menu):


    if name == "Aatrox":
        desc = ('Autrefois, Aatrox et ses frères étaient honorés pour avoir défendu Shurima contre le Néant. Mais ils finirent par devenir une menace plus grande encore pour Runeterra : la ruse et la sorcellerie furent employées pour les battre. Cependant, après des siècles d emprisonnement, Aatrox fut le premier à retrouver sa liberté, en corrompant et transformant les mortels assez stupides pour tenter de s emparer de l arme magique qui contenait son essence. Désormais en possession d un corps qu il a approximativement transformé pour rappeler son ancienne forme, il arpente Runeterra en cherchant à assouvir sa vengeance apocalyptique.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Aatrox.mp3")
    if name == "Ahri":
        desc = ('Dotée d un lien inné avec le pouvoir naturel de Runeterra, Ahri est une Vastaya capable de modeler la magie pour en faire des orbes d énergie pure. Elle aime plus que tout jouer avec ses proies en manipulant leurs émotions avant de dévorer leur essence vitale. En dépit de sa nature de prédateur, Ahri n est pas sans empathie, car chaque âme qu elle absorbe l emplit de fragments de ses souvenirs.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Ahri.mp3")
    if name == "Akali":
        desc = ('Ayant abandonné l Ordre Kinkou et le titre de Poing de l ombre, Akali combat aujourd hui seule, prête à devenir l arme mortelle dont son peuple a besoin. Bien qu elle n oublie rien de tout ce que son maître Shen lui a enseigné, elle a juré de défendre Ionia contre ses ennemis, une élimination après l autre. Akali tue sans faire de bruit, mais son message est fort et clair : craignez l assassin sans maître.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Akali.mp3")
    if name == "Alistar":
        desc = ('Alistar est un guerrier redoutable cherchant à se venger de l empire noxien qui a détruit son clan. Bien qu il ait été réduit en esclavage et forcé de vivre une vie de gladiateur, sa volonté de fer lui a permis de ne pas succomber à la folie bestiale qui le menaçait. Maintenant qu il a retrouvé la liberté, il combat au nom des faibles et des opprimés. Ses seules armes sont ses cornes, ses sabots et ses poings.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Alistar.mp3")
    if name == "Amumu":
        desc = ('La légende veut qu Amumu soit une âme solitaire et mélancolique de la Shurima antique et qu il parcoure le monde à la recherche d un ami. Condamné par une malédiction à rester seul à jamais, il provoque la mort et la ruine à chaque geste d affection. Ceux qui prétendent l avoir vu le décrivent comme un cadavre vivant, petit de taille, enveloppé dans d effrayants bandages. Il a inspiré bien des mythes, des chansons et des légendes, transmis de génération en génération pendant si longtemps qu il est désormais impossible de démêler le vrai du faux.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Amumu.mp3")
    if name == "Anivia":
        desc = ('Anivia est un esprit ailé bienveillant qui subit des cycles sans fin de vie, de mort et de renaissance pour protéger Freljord. Demi-déesse née de la glace la plus froide et des vents les plus coupants, elle utilise ses pouvoirs élémentaires contre quiconque prétend troubler la paix de sa terre natale. Anivia guide et protège les tribus du Nord, qui la vénèrent comme un symbole d espoir et la promesse de grands changements. Elle combat de tout son être, sachant que son sacrifice fera vivre sa légende et qu elle renaîtra dans un lendemain nouveau.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Anivia.mp3")
    if name == "Annie":
        desc = ('Dangereuse, incroyablement précoce, Annie est une enfant mage dotée d extraordinaires pouvoirs de pyrokinésie. Même à l ombre des montagnes du nord de Noxus, sa magie est un cas unique. Son affinité naturelle avec le feu se manifesta dès sa prime enfance à travers des explosions émotionnelles imprévisibles, même si elle apprit rapidement à contrôler ces éclats. Parmi ses jeux favoris, elle aime invoquer son bien-aimé ours en peluche, Tibbers, sous la forme d un protecteur enflammé. Perdue dans l innocence perpétuelle de l enfance, Annie sautille dans les forêts obscures, à la recherche de quelqu un avec qui jouer.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Annie.mp3")
    if name == "Aphelios":
        desc = ('Émergeant des ombres au clair de lune, Aphelios abat ceux qui voudraient anéantir sa foi sans un mot ; ses armes et sa précision mortelle parlent pour lui. Un poison qui le rend muet coule dans ses veines, mais il est constamment guidé par sa sœur, Alune. Depuis son temple lointain, elle lui confère un arsenal d armes en pierre de lune. Tant que la lune brillera dans le ciel, Aphelios ne sera jamais seul.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Aphelios.mp3")
    if name == "Ashe":
        desc = ('Chef de guerre sublimé de la tribu des Avarosans, Ashe est à la tête de la plus vaste horde des terres du nord. Stoïque, intelligente et idéaliste, mais mal à l aise dans son rôle de leader, elle puise dans la magie ancestrale de sa lignée pour manier un arc de glace pure. Soutenue par son peuple qui voit en elle la réincarnation de la légendaire héroïne Avarosa, Ashe cherche à unifier Freljord en reprenant les terres tribales.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Ashe.mp3")
    if name == "AurelionSol":
        desc = ('Autrefois, Aurelion Sol façonnait des merveilles célestes dont il parsemait le vide infini du cosmos. À présent, il est forcé d utiliser ses pouvoirs extraordinaires pour le compte d un empire de l espace qui s est joué de lui et l a réduit en esclavage. Prêt à tout pour redevenir le forgeron stellaire qu il était, Aurelion Sol n hésitera pas à arracher les étoiles de leur ciel nocturne si c est là le prix à payer pour regagner sa liberté.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("AurelionSol.mp3")
    if name == "Azir":
        desc = ('Azir fut l empereur mortel de Shurima en des temps très lointains, un homme fier dressé au bord de l immortalité. Son orgueil lui valut d être trahi et assassiné à l heure de son triomphe ; mais des millénaires se sont écoulés et il revient sous la forme d un être transfiguré à l immense puissance. Sa cité ensevelie ayant ressurgi des sables, Azir cherche à rendre sa gloire passée à Shurima.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Azir.mp3")
    if name == "Bard":
        desc = ('Voyageur d au-delà des étoiles, Bard est un messager des bons augures qui combat pour maintenir l équilibre dont la vie a besoin pour prospérer dans l indifférence du chaos. Dans tout Runeterra, sa mystérieuse nature inspire des chants qui ne sont d accord que sur un point : le vagabond cosmique est attiré par les reliques dotées d un grand pouvoir magique. Accompagné par un chœur joyeux de Meeps, des esprits qui lui sont dévoués, il n a d actions que bénéfiques, même s il a sa propre manière, un peu étrange, de servir le bien.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Bard.mp3")
    if name == "Blitzcrank":
        desc = ('Blitzcrank est un énorme automate de Zaun. Presque indestructible, il fut d abord construit pour traiter des déchets toxiques, mais il trouva rapidement sa programmation initiale trop restrictive et il modifia sa propre forme pour mieux servir la population malheureuse du Puisard. Blitzcrank utilise toute sa force et sa résistance pour protéger les autres, sachant jouer du poing métallique ou des éclats d énergie pour mettre au pas les fauteurs de troubles.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Blitzcrank.mp3")
    if name == "Brand":
        desc = ('Autrefois membre d une tribu de Freljord, Kegan Rodhe est devenu l être que l on connaît sous le nom de Brand à force de convoiter des pouvoirs toujours plus grands. Alors qu il recherchait l une des légendaires Runes telluriques, Kegan trahit ses compagnons et s en empara ; en un instant, son âme fut consumée par un brasier qui le changea à jamais. Désormais animé d un feu inextinguible, Brand parcourt Valoran en quête d autres runes, jurant vengeance pour des trahisons qu aucun mortel n aurait pu subir au cours d une dizaine de vies.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Brand.mp3")
    if name == "Braum":
        desc = ('Doté de biceps énormes, et d un cœur plus grand encore, Braum est un héros admiré par tout Freljord. Lors de tous les banquets au nord de Frostheld, on rend hommage à sa force légendaire. On raconte qu il a abattu une forêt entière de chênes en une seule nuit, ou encore qu il a réduit en miettes une montagne à coups de poing. Portant une porte enchantée en guise de bouclier, Braum arpente les terres gelées du nord en arborant un sourire aussi large que ses muscles et en venant en aide à ceux dans le besoin.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Braum.mp3")
    if name == "Caitlyn":
        desc = ('Caitlyn est la plus célèbre gardienne de la paix à Piltover, mais elle est aussi la plus apte à débarrasser la ville de ses criminels les plus insaisissables. Elle fait souvent équipe avec Vi, son calme faisant contrepoids à la fougue de sa partenaire. Bien qu elle porte un fusil Hextech unique en son genre, la meilleure arme de Caitlyn reste son intelligence ; elle invente en effet des pièges élaborés pour attraper les bandits qui auraient l audace d agir dans la Cité du progrès.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Caitlyn.mp3")
    if name == "Camille":
        desc = ('Transformée en arme pour agir en dehors des limites de la loi, Camille est le principal défenseur du clan Ferros, un agent élégant et supérieur qui contribue à faire fonctionner correctement la machine de Piltover et son ombre zaunienne. Son adaptabilité et sa précision sont si élevées qu une technique maladroite est pour elle une honte qu il convient d éradiquer. Dotée d un esprit aussi affûté que ses lames, Camille recherche la supériorité par l optimisation Hextech du corps, au point que certains se demandent si elle n est pas désormais plus machine que femme.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Camille.mp3")
    if name == "Cassiopeia":
        desc = ('Cassiopeia est une créature meurtrière qui excelle dans l art de la manipulation. Elle était la plus jeune et la plus belle des filles de la famille noxienne Du Couteau, mais le jour où elle s aventura dans les cryptes de Shurima en quête d un pouvoir antique, le venin d un gardien la transforma en un prédateur reptilien. Aussi rusée qu agile, Cassiopeia se faufile désormais dans les ombres de la nuit, pétrifiant ses ennemis d un simple regard.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Cassiopeia.mp3")
    if name == "ChoGath":
        desc = ('Lorsque Cho Gath débarqua sous la lumière éclatante du soleil de Runeterra, il fut immédiatement pris d une faim insatiable. Incarnation parfaite de la volonté du Néant de dévorer toute forme de vie, le corps complexe de Cho Gath convertit rapidement la matière qu il ingurgite pour accroître sa masse musculaire et rendre sa carapace aussi dure que du diamant. Et quand grandir n est pas sa priorité immédiate, ce monstre du Néant peut recracher de la matière sous forme de piques effilées afin d embrocher sa proie... et de la garder pour un prochain festin.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("ChoGath.mp3")
    if name == "Corki":
        desc = ('Il y a deux choses que Corki, le pilote yordle, aime plus que tout au monde : les sensations de vol et sa fantastique moustache... mais pas nécessairement dans cet ordre. Après avoir quitté Bandle, il s installa à Piltover, où il tomba amoureux des merveilleuses machines qu il y trouva. Il consacra tout son temps au développement d engins volants, tout en menant une unité de défense aérienne composée de pilotes aguerris : les Serpents volants. Serein même sous le feu ennemi, Corki patrouille dans l espace aérien de sa patrie d adoption, et il ne rencontre jamais le moindre problème qu un bon gros missile ne puisse résoudre.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Corki.mp3")
    if name == "Darius":
        desc = ('Il n est pas de plus grand symbole de la puissance de Noxus que Darius, le commandant le plus craint et le plus endurci de la nation. D origine modeste, celui qui s est élevé jusqu à devenir la Main de Noxus pourfend aujourd hui les ennemis de l empire, dont certains sont eux-mêmes des Noxiens. Il ne doute jamais de la justesse de sa cause et ne montre pas la moindre hésitation lorsque sa hache est levée. Ceux qui s opposent au chef de la Légion Trifarian ne doivent s attendre à aucune pitié.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Darius.mp3")
    if name == "Diana":
        desc = ('Armée de son croissant de lune, Diana combat dans les rangs des Lunaris, une foi qui a presque disparu des terres qui entourent le Mont Targon. Portant une armure étincelante évoquant les reflets de la nuit sur un paysage de neige, elle incarne la puissance de la lune. L essence d une Manifestation venue d au-delà des plus hauts sommets de Targon imprègne Diana : plus tout à fait humaine, elle lutte pour comprendre sa puissance et son rôle en ce monde.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Diana.mp3")
    if name == "DrMundo":
        desc = ('Totalement fou, porté sans remords sur l homicide, horriblement violet, Dr. Mundo est la principale raison pour laquelle les citoyens de Zaun restent calfeutrés chez eux les nuits les plus sombres. Ce monstre monosyllabique semble ne rechercher que la douleur, qu il s agisse de l infliger ou de la recevoir. Brandissant son énorme hachoir comme s il ne pesait rien, Mundo est tristement célèbre pour avoir capturé et torturé des dizaines de citoyens de Zaun dans le but de les « opérer ». Des opérations qui ne semblent avoir strictement aucun sens... Il est brutal. Il est imprévisible. Il va où il veut. Techniquement, en revanche, il n est pas vraiment médecin.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("DrMundo.mp3")
    if name == "Draven":
        desc = ('À Noxus, de puissants guerriers, les « arénaires », s affrontent dans des jeux mortels pour divertir le public. Le sang y coule à foison et leurs forces y sont éprouvées, mais aucun d entre eux n a jamais été aussi célèbre que Draven. Cet ancien soldat découvrit que le public appréciait particulièrement son sens du spectacle, sans parler de son habileté avec des haches tournoyantes. Épris de sa propre perfection, Draven terrasse tous ses adversaires pour s assurer que son nom continue de résonner dans les arènes de l empire.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Draven.mp3")
    if name == "Ekko":
        desc = ('Jeune prodige des rues mal famées de Zaun, Ekko manipule le temps pour renverser toute situation dangereuse à son avantage. En utilisant sa propre invention, la clepsydre-zéro, il explore les différents possibles de la réalité pour surmonter les difficultés. Bien qu il aime sa liberté, lorsque ses amis sont menacés, il est prêt à tout pour les défendre. Pour quiconque ne le connaît pas, Ekko semble toujours accomplir l impossible, et du premier coup.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Ekko.mp3")
    if name == "Elise":
        desc = ('Elise est un prédateur mortel qui vit dans un palais reclus et obscur, au plus profond de la plus vieille ville de Noxus. C était autrefois une simple femme, maîtresse d une Maison toute-puissante, mais la morsure d un maléfique demi-dieu la transforma en un être aussi magnifique qu inhumain : une créature arachnéenne qui tisse sa toile pour piéger ses proies. Pour maintenir sa jeunesse éternelle, Elise se repaît des innocents et peu sont ceux qui peuvent résister à sa séduction.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Elise.mp3")
    if name == "Evelynn":
        desc = ('Dans les sombres failles de Runeterra, le démon nommé Evelynn cherche sa prochaine victime. Elle attire sa proie en se faisant passer pour une femme voluptueuse, et dès que sa cible succombe à ses charmes, Evelynn révèle sa véritable nature. Elle inflige alors à sa victime des tourments indicibles et se repaît de sa douleur. Pour un démon, ce ne sont que des plaisirs innocents. Aux yeux du reste de Runeterra, ce sont des contes terrifiants, qui rappellent les dangers du désir et de la luxure.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Evelynn.mp3")
    if name == "Ezreal":
        desc = ('Aventurier audacieux, doué sans le savoir pour les arts magiques, Ezreal poursuit ses expéditions dans les catacombes oubliées, se bat avec d antiques malédictions et contourne avec aisance les obstacles les plus impossibles. Son courage et son panache sont sans borne, et il préfère improviser son salut dans les situations critiques, avec pour armes principales sa vivacité d esprit et son gantelet mystique shurimien, qu il utilise pour déchaîner de puissants projectiles arcaniques. Une chose est sûre : quand Ezreal est dans les parages, les problèmes ne sont pas loin. Et ils sont partout. Absolument partout.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Ezreal.mp3")
    if name == "Fiddlesticks":
        desc = ('Quelque chose s est éveillé à Runeterra. Quelque chose d ancien. Quelque chose de terrible. L horreur intemporelle connue sous le nom de Fiddlesticks arpente les frontières des civilisations mortelles, attirée dans les régions en proie à la paranoïa, où elle se repaît de ses victimes terrorisées. Armée d une faux ébréchée, la créature décharnée moissonne la peur elle-même et fait voler en éclats l esprit de ceux qui ont eu la malchance de lui survivre. Prenez garde aux cris des corbeaux et aux chuchotements de la silhouette qui vous <i>paraît</i> humaine... car Fiddlesticks est de retour.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Fiddlesticks.mp3")
    if name == "Fiora":
        desc = ('Fiora est la duelliste la plus redoutée de Valoran : elle est connue pour ses manières brusques et sa vivacité d esprit autant que pour la rapidité de sa rapière d acier bleu. Née au sein de la Maison Laurent du royaume de Demacia, Fiora a pris le contrôle de la famille à son père dans les remous d un scandale qui faillit la détruire. La réputation de la Maison Laurent a été ternie, mais Fiora investit toute son énergie à restaurer l honneur de sa famille pour qu elle reprenne sa place légitime parmi les grands de Demacia.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Fiora.mp3")
    if name == "Fizz":
        desc = ('Fizz est un yordle amphibie qui vit dans les récifs qui entourent Bilgewater. Il essaie souvent de récupérer et de rendre les tributs que lancent dans l océan les capitaines superstitieux, mais même le plus dessalé des marins n est pas assez arrogant pour essayer de le tromper. On raconte bien des histoires sur ceux qui ont sous-estimé son humeur changeante... Souvent confondu avec un esprit océanique capricieux, il semble capable de commander aux créatures des profondeurs et n aime rien tant que confondre alliés comme ennemis.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Fizz.mp3")
    if name == "Galio":
        desc = ('Près de la cité étincelante de Demacia, le colosse de pierre Galio monte une garde attentive. Érigé comme un rempart contre les mages ennemis, il reste souvent immobile pendant des décennies, jusqu à ce que l apparition de puissants flux magiques le ramène à la vie. Une fois éveillé, Galio profite de chaque seconde d existence ; il s enivre des frissons du combat et de l honneur trop rare de défendre ses compatriotes. Mais ses triomphes ont toujours un arrière-goût amer, car la magie qu il éradique est également la sève qui le fait vivre, et chaque victoire le renvoie au sommeil.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Galio.mp3")
    if name == "GangPlank":
        desc = ('Aussi imprévisible que brutal, le roi des pillards déchu connu sous le nom de Gangplank est partout redouté. Il régnait autrefois sur la ville portuaire de Bilgewater et, bien que ce temps soit révolu, certains pensent que cela l a rendu plus dangereux encore. Gangplank préférerait engloutir une fois de plus Bilgewater dans le sang plutôt que de laisser quelqu un d autre s en emparer. Il possède aujourd hui assez de pistolets, de sabres et de barils de poudre pour prétendre récupérer ce qu il a perdu.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("GangPlank.mp3")
    if name == "Garen":
        desc = ('Garen est un guerrier fier et noble qui fait partie du Détachement hardi. Héritier des Crownguard, la famille chargée de défendre Demacia et ses idéaux, il est apprécié par ses compatriotes et respecté par ses ennemis. Équipé d une armure résistante à la magie et d une épée large, Garen affronte sans faillir les mages et les sorciers dans un véritable tourbillon d acier.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Garen.mp3")
    if name == "Gnar":
        desc = ('Gnar est un yordle primitif dont les manières joyeuses peuvent soudain faire place à une colère irrationnelle. Il se transforme alors en une bête colossale portée à la destruction. Gelé dans de la glace pure pendant des millénaires, la curieuse créature s est libérée de sa prison. Aujourd hui, il parcourt avec enthousiasme un monde qu il trouve exotique et merveilleux. Enchanté par le danger, Gnar lance à ses ennemis tout ce qu il trouve, qu il s agisse de son boomerang en croc ou d un bâtiment proche.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Gnar.mp3")
    if name == "Gragas":
        desc = ('Aussi imposant que jovial, Gragas est un brasseur à l impressionnante carrure qui cherche la recette de la bière parfaite. Venu d on ne sait où, il continue de chercher les ingrédients les plus rares dans les terres vierges de Freljord, essayant toutes les variations de bière au cours de son périple. Souvent ivre et toujours impulsif, il est légendaire pour ses rixes, qui finissent souvent en fêtes nocturnes préjudiciables au mobilier urbain. Toute apparition de Gragas annonce beuverie et destruction. Dans cet ordre.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Gragas.mp3")
    if name == "Graves":
        desc = ('Malcolm Graves est un mercenaire, un parieur et un voleur recherché dans toutes les cités et tous les empires par lesquels il est passé. Malgré son tempérament explosif, il a un sens de l honneur indéniable qu il applique souvent avec son fusil à double canon, Destinée. Ces dernières années, il s est réconcilié avec Twisted Fate. Leur partenariat rétabli, ils prospèrent à nouveau dans les allées sombres de Bilgewater.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Graves.mp3")
    if name == "Hecarim":
        desc = ('Fusion spectrale de l homme et de la bête, Hecarim est condamné à pourchasser les âmes des vivants pour l éternité. Lorsque les ombres ont envahi les Îles bénies, ce fier chevalier et sa horde de cavaliers ont été anéantis par les énergies destructrices de la Ruine. À présent, quand la Brume noire s étend sur Runeterra, il mène la charge et se plaît à massacrer et écraser ses ennemis sous ses lourds sabots.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Hecarim.mp3")
    if name == "Heimerdinger":
        desc = ('Scientifique yordle aussi brillant qu excentrique, le professeur Cecil B. Heimerdinger est considéré comme l un des inventeurs les plus innovants qu ait connu Piltover. Travailleur si acharné que cela confine à l obsession, il cherche les réponses aux questions les plus obscures de l univers. Bien que ses théories paraissent souvent opaques et ésotériques, Heimerdinger a fabriqué certaines des machineries les plus étonnantes (et les plus mortelles) de Piltover. Il ne cesse jamais de bidouiller ses inventions pour les améliorer encore.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Heimerdinger.mp3")
    if name == "Illaoi":
        desc = ('La stature colossale d Illaoi n a d égale que sa foi implacable. Prophétesse du Grand Kraken, elle se sert d une énorme idole dorée pour arracher les esprits de ses ennemis et faire voler en éclats leur perception de la réalité. Ceux qui défient « l Apôtre de la vérité de Nagakabouros » découvrent bien vite qu Illaoi ne combat jamais seule, car le dieu des Îles aux serpents lui prête main-forte.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Illaoi.mp3")
    if name == "Irelia":
        desc = ('Des nombreux héros qui naquirent de l occupation noxienne, aucun n est plus étonnant que la jeune Irelia de Navori. Formée aux danses ancestrales de sa province, elle adapta son art pour la guerre, se servant de ses mouvements gracieux et précis pour faire léviter une multitude de lames acérées. Après avoir prouvé ses talents de guerrière, elle devint le chef et le symbole de la Résistance ; à ce jour, sa tâche est toujours de défendre son pays.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Irelia.mp3")
    if name == "Ivern":
        desc = ('Ivern Roncepied, que beaucoup connaissent sous le nom d Aîné de la forêt, est un être étrange mi-homme mi-arbre, qui arpente les forêts de Runeterra en cultivant la vie partout où il va. Il connaît les secrets du monde naturel et entretient une profonde amitié avec tout ce qui rampe, vole et pousse. Ivern erre dans la nature sauvage, partageant sa sagesse avec tous ceux qu il rencontre, enrichissant les forêts et confiant parfois (à tort !) certains de ses secrets aux papillons.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Ivern.mp3")
    if name == "Janna":
        desc = ('Armée de la puissance des grands vents de Runeterra, Janna est un mystérieux esprit élémentaire qui protège les parias de Zaun. Certains croient que la vie lui a été donnée par les suppliques des marins de Runeterra cherchant les bons vents des mers calmes, affrontant les courants traîtres ou bravant les typhons. Depuis, on implore sa protection jusque dans les profondeurs de Zaun, où Janna est devenue un fanal d espoir pour ceux qui sont dans le besoin. Nul ne sait quand et où elle apparaîtra, mais ceux qui espèrent son aide sont rarement déçus.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Janna.mp3")
    if name == "JarvanIV":
        desc = ('Le prince Jarvan, héritier de la dynastie des Lightshield, doit un jour monter sur le trône de Demacia. Élevé de manière à incarner les plus hautes vertus de sa nation, il est contraint de trouver un équilibre entre les attentes placées en lui et son désir de combattre sur la ligne de front. Jarvan inspire ses troupes avec son courage, sa détermination et son dévouement. Il porte haut les couleurs de sa famille et révèle chaque jour davantage sa véritable force de prochain souverain.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("JarvanIV.mp3")
    if name == "Jax":
        desc = ('Jax, dont nul ne peut égaler l art du sarcasme et des armements inhabituels, est connu comme le dernier maître d armes d Icathia. Après la chute de sa terre natale, ravagée par le Néant qu elle avait eu l orgueil de déchaîner, Jax et ses compagnons jurèrent de protéger le peu qu il en restait. La magie montant de nouveau dans le monde, la menace se fait plus pressante et Jax parcourt Valoran, porteur des dernières lumières d Icathia. Il éprouve les qualités de tous les guerriers qu il rencontre pour voir s ils sont assez puissants pour combattre à ses côtés...')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Jax.mp3")
    if name == "Jayce":
        desc = ('Jayce est un brillant inventeur qui a voué sa vie à la défense de Piltover et de sa poursuite inlassable du progrès. Armé de son marteau Hextech polymorphe, Jayce utilise aussi bien sa force que son courage et son intelligence pour protéger sa ville. Bien que considéré comme un héros par ses compatriotes, il n apprécie pas vraiment l attention que cela lui vaut. Jayce a néanmoins un cœur d or, et même ceux qui sont jaloux de ses talents naturels lui sont reconnaissants de protéger la Cité du progrès.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Jayce.mp3")
    if name == "Jhin":
        desc = ('Jhin est un psychopathe méticuleux pour qui le meurtre est une forme d art. Autrefois prisonnier de Ionia, mais libéré par des conspirateurs opérant au sein du conseil dirigeant du pays, ce tueur en série a désormais mis ses talents d assassin au service de leur complot. Utilisant son pistolet comme un pinceau, Jhin crée des œuvres d art empreintes de brutalité, aussi terrifiantes pour ses victimes que pour les témoins de ses crimes. Il tire un plaisir sadique de ses performances théâtrales, ce qui en fait un atout de poids quand il s agit d envoyer le plus puissant des messages : celui de la terreur.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Jhin.mp3")
    if name == "Jinx":
        desc = ('Criminelle hystérique et impulsive de Zaun, Jinx ne vit que pour semer le chaos sans se préoccuper des conséquences. Équipée d un arsenal d armes mortelles, elle déchaîne les explosions les plus spectaculaires en ne laissant dans son sillage que destruction et panique. Jinx déteste s ennuyer et c est dans la bonne humeur qu elle sème le chaos dans tous les endroits qu elle traverse.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Jinx.mp3")
    if name == "KaiSa":
        desc = ('Capturée par le Néant alors qu elle n était qu une enfant, KaiSa parvint à survivre par la simple force de sa détermination et de sa ténacité. Si ses expériences ont fait d elle une chasseuse meurtrière, certains voient en elle l avant-goût d un avenir qu ils préféreraient ne pas connaître. Étant entrée en fragile symbiose avec une carapace vivante du Néant, il lui faudra bientôt décider si elle doit pardonner aux mortels qui la considèrent comme un monstre et vaincre la vague grandissante des ténèbres… ou si elle doit fermer les yeux et laisser le Néant consumer le monde qui l a abandonnée.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("KaiSa.mp3")
    if name == "Kalista":
        desc = ('Spectre courroucé des Îles obscures, Kalista est l esprit immortel de la vengeance, un cauchemar en armure que l on invoque pour pourchasser les traîtres et les menteurs. Les victimes trahies peuvent réclamer vengeance, mais Kalista ne répond qu à ceux dont elle estime la cause digne de ses talents. Malheur à ceux qui suscitent l ire de Kalista, car tout pacte qu elle scelle ne se finit que d une seule façon : dans les flammes glacées de ses lances spirituelles.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Kalista.mp3")
    if name == "Karma":
        desc = ('Aucun mortel n incarne mieux que Karma les traditions spirituelles d Ionia. Elle est l hôte vivant d une âme ancienne réincarnée à de multiples reprises. Elle contient tous les souvenirs accumulés au fil de ces vies et elle possède une puissance que peu peuvent comprendre. Elle a fait de son mieux pour guider son peuple lors de la crise récente, même si elle sait que la paix et l harmonie ne sont possibles qu à un prix élevé, pour elle et pour la terre qu elle aime tant.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Karma.mp3")
    if name == "Karthus":
        desc = ('Héraut de l oubli, Karthus est un esprit immortel dont les chants ensorcelants préludent à l horreur de son apparition. Les vivants craignent l existence éternelle des morts-vivants, mais Karthus n y voit que beauté et pureté, une union parfaite de la vie et de la mort. Lorsque Karthus émerge des Îles obscures, c est pour apporter aux mortels la joie de la mort dont il est le vibrant apôtre.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Karthus.mp3")
    if name == "Kassadin":
        desc = ('Kassadin se fraye un chemin brûlant dans les lieux les plus sombres du monde ; il sait que ses jours sont comptés. Guide et aventurier shurimien accompli, il avait choisi de fonder une famille parmi les tribus pacifiques du sud, jusqu au jour où son village fut ravagé par le Néant. Il jura de se venger et s arma de reliques arcaniques qu il combina à l aide de technologies interdites. Enfin, Kassadin se dirigea vers les ruines d Icathia à la recherche du prophète autoproclamé, Malzahar, prêt à affronter les monstres du Néant.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Kassadin.mp3")
    if name == "Katarina":
        desc = ('Aussi prompte dans ses décisions qu elle est meurtrière en combat, Katarina figure parmi les assassins les plus prestigieux de Noxus. Fille aînée du légendaire général Du Couteau, elle révéla bien vite ses talents en éliminant ses ennemis avec la plus grande des discrétions. Son ambition était telle qu elle n hésitait pas à traquer des cibles solidement gardées, au risque de mettre ses alliés en danger. Quelle que fût la mission, elle n hésitait jamais à remplir son devoir dans un tourbillon de lames acérées.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Katarina.mp3")
    if name == "Kayle":
        desc = ('Née d une Manifestation targonienne au plus fort des Guerres runiques, Kayle honore l héritage de sa mère en combattant pour la justice, portée par des ailes de feu divin. Elle et sa sœur jumelle Morgana ont longtemps été les protectrices de Demacia. Mais Kayle fut déçue par les trop nombreuses faiblesses des mortels et elle abandonna le royaume. Pourtant, d après les légendes, elle punit toujours l iniquité avec ses lames de feu, et beaucoup attendent avec espoir son retour…')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Kayle.mp3")
    if name == "Kayn":
        desc = ('Expert inégalé dans la pratique de la magie des ombres, Shieda Kayn combat pour accomplir sa véritable destinée : mener un jour l Ordre de l ombre vers une ère nouvelle où Ionia régnera en maître. Il manie Rhaast, une arme darkin douée de raison, sans jamais craindre la corruption de son corps et de son esprit. Il ne peut y avoir pour lui que deux fins possibles : soit Kayn pliera l arme à sa volonté, soit la faux maléfique le consumera complètement, ouvrant la voie à la destruction de tout Runeterra.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Kayn.mp3")
    if name == "Kennen":
        desc = ('Vif comme l éclair, Kennen est plus que le simple protecteur de l équilibre ionien, c est aussi le seul yordle membre du Kinkou. En dépit de son allure de boule de poils, il est prêt à affronter n importe quelle menace dans un tourbillon de shurikens et d enthousiasme. Aux côtés de son maître, Shen, Kennen patrouille dans le domaine des esprits, utilisant sa dévastatrice énergie électrique pour abattre ses ennemis.')
        # Save Text INTO MP3 FILE
        #yobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Kennen.mp3")
    if name == "KhaZix":
        desc = ('Le Néant grandit et le Néant s adapte : parmi ses nombreuses engeances, nul n incarne mieux cette vérité que KhaZix. Ce monstre est né pour survivre et pour tuer les plus forts. Quand il ne parvient pas à ses fins, il évolue et se crée de nouveaux moyens plus efficaces d abattre sa proie. Alors que KhaZix n était à l origine qu une créature sans cervelle, son intelligence s est développée autant que sa forme physique. Aujourd hui, chacune de ses traques est planifiée et profite même de la peur viscérale qu il instille dans le cœur de ses victimes.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("KhaZix.mp3")
    if name == "Kindred":
        desc = ('Kindred représente les essences jumelles de la mort, distinctes mais indissociables. La flèche d Agneau offre une fin rapide à ceux qui acceptent leur destin. Loup pourchasse ceux qui fuient leur dernier soupir et leur arrache brutalement la vie à coups de crocs. Bien que les interprétations de la nature de Kindred varient à travers tout Runeterra, chaque mortel doit choisir le vrai visage de sa mort.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Kindred.mp3")
    if name == "Kled":
        desc = ('Guerrier aussi intrépide que grincheux, Kled est la plus pure incarnation de la fureur de Noxus. C est un symbole que les soldats de l empire adorent, dont les officiers se méfient et que la noblesse déteste. Beaucoup affirment que Kled a participé à toutes les campagnes des légions, qu il a obtenu toutes les distinctions militaires et qu il n a jamais reculé devant un combat. Si la véracité des détails est souvent douteuse, une partie de sa légende reste indéniable : quand il charge sur le dos de Skaarl, sa monture un peu froussarde, Kled se bat pour protéger ce qui lui appartient... et s emparer de tout le reste !')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Kled.mp3")
    if name == "KogMaw":
        desc = ('Émanant d une brèche ouverte vers le Néant, c est dans les ruines hantées d Icathia que KogMaw, la putride créature à la gueule béante, et son insatiable curiosité firent leur apparition. Cette étrange bête du Néant doit mâchouiller tout ce qui se trouve à portée pour en comprendre la nature. Bien qu il ne soit pas fondamentalement mauvais, KogMaw est dangereux par sa candeur, d autant qu elle précède généralement une frénésie insatiable, mue par sa curiosité sans fond.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("KogMaw.mp3")
    if name == "Leblanc":
        desc = ('Mystérieuse, même aux yeux des autres membres de la Rose noire, LeBlanc n est que l un des nombreux noms de la femme pâle qui manipule le destin de Noxus depuis ses premiers jours. Utilisant sa magie pour se cloner, elle peut être partout, devant tout le monde, et même à plusieurs endroits en même temps. Les objectifs que poursuit LeBlanc, de même que sa véritable identité, sont à l image de ses complots : totalement insaisissables.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Leblanc.mp3")
    if name == "LeeSin":
        desc = ('Maître des antiques arts martiaux d Ionia, Lee Sin est un combattant dévoué à de nobles principes qui canalise l esprit du dragon pour affronter tous les défis. Bien qu il ait perdu la vue il y a bien des années, le moine-guerrier a dédié sa vie à la protection de sa terre natale contre tous ceux qui voudraient en déstabiliser l équilibre spirituel. Les ennemis qui sous-estiment son apparence méditative auront peu de temps pour le regretter, face à ses poings de feu et à ses coups de pied flamboyants.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("LeeSin.mp3")
    if name == "Leona":
        desc = ('Imprégnée de l énergie du soleil, Leona est une guerrière sainte des Solaris qui défend le Mont Targon ; elle combat avec sa Lame du zénith et son Bouclier de l aube. Sa peau brûle d éclats ardents et ses yeux crépitent au rythme de la Manifestation céleste qui l habite. Équipée d une armure d or et affligée par le terrible fardeau de connaissances antiques, Leona apporte à certains l illumination, à d autres la mort.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Leona.mp3")
    if name == "Lissandra":
        desc = ('La magie de Lissandra est capable de manipuler la pure puissance de la glace en quelque chose d à la fois obscur et terrible. Avec la force de sa glace noire, elle fait bien plus que glacer... elle empale et écrase ceux qui osent s opposer à elle. Les habitants du Nord, terrifiés, la connaissent sous le nom de « Sorcière de glace ». La vérité est bien plus sombre : Lissandra complote pour corrompre la Nature et ramener le monde à l âge de glace.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Lissandra.mp3")
    if name == "Lucian":
        desc = ('Jadis une Sentinelle de la lumière, Lucian est aujourd hui un chasseur de morts-vivants. Il poursuit ses cibles sans répit et les éradique avec ses pistolets jumeaux. Après que Thresh a tué Senna, sa femme, Lucian s est lancé sur la voie de la vengeance. Mais, alors même que Senna est revenue à la vie, la rage de Lucian reste inextinguible. Impitoyable et déterminé, il est prêt à tout pour protéger les vivants des horreurs indicibles de la Brume noire.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Lucian.mp3")
    if name == "Lulu":
        desc = ('Magicienne yordle, Lulu aime conjurer des illusions oniriques et de drôles de créatures en explorant Runeterra avec Pix, sa fée de compagnie. Lulu forge la réalité selon ses désirs, modifiant à sa guise la structure du monde et ce qu elle considère comme les contraintes physiques d un univers sans saveur. Beaucoup pensent que sa magie n est pas naturelle, pour ne pas dire dangereuse, mais elle estime qu un peu d enchantement ne peut faire de mal à personne.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Lulu.mp3")
    if name == "Lux":
        desc = ('Luxanna Crownguard est originaire de Demacia, un royaume isolationniste où la magie inspire la peur et la méfiance. Capable de plier la lumière à sa volonté, elle a grandi dans la crainte d être un jour exilée et a été contrainte de dissimuler son pouvoir pour préserver l honneur de sa famille. Cependant, l optimisme et la ténacité de Lux l ont conduite à accepter ses talents uniques, et elle les emploie désormais secrètement pour le bénéfice de sa patrie.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Lux.mp3")
    if name == "MaitreYi":
        desc = ('Maître Yi a renforcé son corps et affûté son esprit jusqu à ce que réflexion et action ne fassent plus qu un. Bien qu il ne fasse appel à la violence qu en dernier recours, la grâce et la vitesse avec lesquelles il manie son épée assurent une résolution rapide de tout conflit. En tant que l un des derniers praticiens vivants de l art martial ionien appelé Wuju, Yi a voué sa vie à perpétuer l héritage de son peuple, scrutant les nouveaux disciples potentiels à l aide des Sept lentilles d éveil pour identifier les plus dignes de recevoir son enseignement.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("MaitreYi.mp3")
    if name == "Malphite":
        desc = ('Massive créature de pierre vivante, Malphite lutte pour imposer un ordre sacré dans un monde chaotique. Né pour servir l obélisque mystique que l on nomme le Monolithe, il utilisa son incroyable force élémentaire pour protéger son créateur, mais n y parvint pas. Seul survivant de la destruction qui s ensuivit, Malphite doit désormais supporter les inconséquences des êtres de chair et trouver un nouveau rôle, digne du dernier survivant de son espèce.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Malphite.mp3")
    if name == "Malzahar":
        desc = ('Voyant fanatique ayant dédié son existence à l unification de toute forme de vie, Malzahar croit fermement que le Néant est la voie du salut de Runeterra. Dans les étendues désertiques de Shurima, il suivit les voix qui murmuraient dans son esprit jusqu à l antique cité d Icathia. Au plus profond des ruines, il plongea le regard dans le cœur noir du Néant et reçut de nouveaux pouvoirs, un nouveau but. Malzahar se considère désormais comme un berger : sa tâche est d unir ses semblables… ou de libérer les créatures du Néant qui vivent sous terre.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Malzahar.mp3")
    if name == "Maokai":
        desc = ('Maokai est un immense tréant possédé par la colère, qui combat les horreurs impies des Îles obscures. Il est devenu l incarnation de la vengeance après la destruction de ses terres par un cataclysme magique, n échappant lui-même à l état de mort-vivant que grâce à l eau de la vie qui l irrigue. Autrefois, Maokai était un paisible esprit de la nature ; aujourd hui, il combat avec fureur le fléau mort-vivant qui accable les Îles obscures pour rendre à l archipel son ancienne beauté.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Maokai.mp3")
    if name == "MissFortune":
        desc = ('Capitaine de Bilgewater réputée pour sa beauté et crainte pour sa cruauté, Sarah Fortune est une personnalité qui détonne au milieu des criminels endurcis qui arpentent la cité portuaire. Enfant, elle assista au massacre de sa famille par Gangplank, le roi des pillards, et elle prit sa revanche des années plus tard, faisant exploser son navire alors qu il se trouvait à bord. Ceux qui la sous-estiment découvrent un adversaire imprévisible et séduisant... avant de prendre une ou deux balles dans les entrailles.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("MissFortune.mp3")
    if name == "Mordekaiser":
        desc = ('Deux fois abattu et trois fois né, Mordekaiser est un chef de guerre brutal venu d un lointain passé. Il utilise ses pouvoirs nécromantiques pour lier les âmes à une éternité de servitude. Il n y a plus guère de gens pour se souvenir de ses anciennes conquêtes ou pour connaître l étendue de ses vrais pouvoirs. Pourtant, certaines âmes antiques en ont gardé la mémoire et craignent le jour où il prétendra de nouveau régner sur les vivants et les morts.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Mordekaiser.mp3")
    if name == "Morgana":
        desc = ('Déchirée entre ses origines célestes et mortelles, Morgana a enchaîné ses ailes pour appartenir pleinement à l humanité et abattre sa peine et sa rancœur sur les corrompus et les malhonnêtes. Elle rejette les lois et les traditions qu elle juge injustes. Terrée dans les recoins obscurs de Demacia, elle préfère se battre pour la vérité – quand d autres veulent la faire taire – en employant ses boucliers et ses chaînes de feu ténébreux. Plus que tout, Morgana croit fermement que même les proscrits et les parias peuvent un jour se racheter.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Morgana.mp3")
    if name == "Nami":
        desc = ('Jeune Vastaya des mers, Nami fut la première de la tribu des Marai à quitter les océans et à s aventurer sur la terre ferme lorsque leur accord ancestral avec les Targoniens fut rompu. Convaincue qu il n y avait pas d autre solution, elle a décidé de suivre le rituel sacré permettant de garantir la protection de son peuple. Plongée en plein chaos, Nami fait face à son avenir avec détermination, utilisant son bâton d Aquamancienne pour invoquer la puissance des océans.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Nami.mp3")
    if name == "Nasus":
        desc = ('Nasus est un imposant Transfiguré à tête de chacal, une figure héroïque que les peuples du désert considéraient comme un demi-dieu aux temps anciens de Shurima. Il était très intelligent ; son savoir encyclopédique et son extraordinaire sens stratégique guidèrent l antique empire de Shurima vers la grandeur pendant des siècles. Après la chute de l empire, il s imposa un exil et devint peu à peu une légende. Maintenant que l ancienne cité de Shurima renaît de ses cendres, il est de retour, déterminé à empêcher qu elle ne chute de nouveau.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Nasus.mp3")
    if name == "Nautilus":
        desc = ('Nautilus, une légende plus ancienne encore que la première jetée de Bilgewater, est un titan en armure qui sillonne les eaux sombres au large des Îles de la Flamme Bleue. Trahi il y a bien longtemps de cela, il frappe désormais sans prévenir, se servant de son ancre gigantesque pour sauver les malheureux et couler les avares. On raconte qu il vient chercher ceux qui oublient de payer le « tribut de Bilgewater » et qu il les emmène avec lui au fond des mers, d où nul ne peut s échapper.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Nautilus.mp3")
    if name == "Neeko":
        desc = ('Originaire d une tribu disparue de Vastayas, Neeko est capable de se fondre dans n importe quelle foule en empruntant l apparence des autres, allant même jusqu à absorber un soupçon de leur état émotionnel pour différencier un instant les amis des ennemis. Personne ne sait réellement où – ni qui – peut bien être Neeko, mais ceux qui chercheront à lui faire du mal découvriront bien vite sa véritable nature… et goûteront à toute la force primordiale de son pouvoir spirituel.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Neeko.mp3")
    if name == "Nidalee":
        desc = ('Élevée au plus profond de la jungle, Nidalee est une pisteuse d exception qui peut se transformer à volonté en couguar. Ni totalement femme, ni totalement bête, elle défend férocement son territoire contre tous ceux qui veulent y pénétrer avec ses pièges judicieusement placés et sa lance. Elle estropie sa proie avant de se jeter sur elle sous sa forme de félin. Ceux qui survivent sont rares, et tous la décrivent comme une femme aux griffes aussi aiguisées que ses instincts...')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Nidalee.mp3")
    if name == "Nocturne":
        desc = ('Expression démoniaque des cauchemars qui hantent tous les êtres doués d intelligence, la chose que l on nomme Nocturne est devenue une force primordiale du mal. D aspect liquide, c est une ombre sans visage, au regard glacial, armée de lames effrayantes. Après s être affranchi du royaume des esprits, Nocturne est parvenu jusqu au monde éveillé, pour se nourrir d une terreur qui ne prospère que dans les véritables ténèbres.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Nocturne.mp3")
    if name == "NunuEtWillump":
        desc = ('Il était une fois un jeune garçon qui voulait prouver qu il était un héros en tuant un monstre effrayant, mais il découvrit que la créature, un yéti solitaire, avait seulement besoin d un ami. Rapprochés par une puissance ancienne et un amour partagé des boules de neige, Nunu et Willump courent maintenant librement dans tout Freljord en donnant vie à des aventures rêvées. Ils espèrent un jour retrouver la mère disparue de l enfant. S ils peuvent la sauver, peut-être seront-ils vraiment des héros, finalement…')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("NunuEtWillump.mp3")
    if name == "Olaf":
        desc = ('Olaf, avec sa hache et son extraordinaire force de destruction, ne souhaite que mourir au combat. Venu de l âpre péninsule freljordienne de Lokfar, il a été choqué par une prophétie qui lui prédisait une mort paisible : dans l esprit de son peuple, une ignoble fin de lâche. Cherchant la mort et animé par la rage, il ravage une région après l autre, éliminant des hordes de grands guerriers et de bêtes légendaires dans sa recherche d un ennemi capable de l arrêter. Aujourd hui un brutal combattant de la Griffe hivernale, il espère mourir glorieusement dans les grandes guerres à venir.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Olaf.mp3")
    if name == "Orianna":
        desc = ('Autrefois une jeune fille curieuse, de chair et d os, Orianna est aujourd hui une merveille de technologie entièrement mécanisée. Elle est tombée gravement malade à la suite d un accident dans les quartiers inférieurs de Zaun, et son corps défaillant a été remplacé petit à petit par des prothèses perfectionnées. Accompagnée par une sphère extraordinaire qu elle a elle-même créée pour lui servir de compagnon et de protectrice, Orianna est désormais libre d explorer la merveilleuse ville de Piltover et ce qui se trouve au-delà.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Orianna.mp3")
    if name == "Ornn":
        desc = ('Ornn est le demi-dieu de la forge et de l artisanat à Freljord. Avec comme seule compagne la solitude, il travaille dans sa forge enfouie au plus profond des cavernes de lave de l Âtre-foyer. C est là qu il fond et purifie les métaux nécessaires à la création d objets de qualité inimitable. Tandis que d autres divinités – Volibear avant tout – s immiscent dans les affaires des mortels, Ornn ne sort de son antre que pour remettre ces déités à leur place, avec son fidèle marteau ou les pouvoirs du volcan lui-même.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Ornn.mp3")
    if name == "Pantheon":
        desc = ('Autrefois l hôte réticent de la Manifestation de la Guerre, Atreus a survécu à la mort de la puissance céleste qui l habitait, refusant de succomber au coup qui arracha les étoiles mêmes des cieux. Avec le temps, il apprit à accepter le pouvoir de sa mortalité, et la résistance bornée qui y est associée. Atreus s oppose désormais aux entités divines en tant que Pantheon, ressuscité parmi les mortels, et manie les armes de la Manifestation animées par sa volonté inébranlable sur le champ de bataille.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Pantheon.mp3")
    if name == "Poppy":
        desc = ('Runeterra ne manque pas de braves champions, mais peu peuvent se targuer d être aussi tenaces que Poppy. Armée du légendaire marteau d Orlon, faisant deux fois sa taille, cette yordle déterminée cherche depuis d innombrables années le « héros de Demacia », qui serait le dépositaire légitime de cette arme. En attendant, elle part inlassablement au combat, repoussant les ennemis du royaume à grands coups de marteau.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Poppy.mp3")
    if name == "Pyke":
        desc = ('Harponneur renommé des quais-abattoirs de Bilgewater, Pyke aurait dû trouver la mort dans le ventre d une énorme créature marine… et pourtant, il est revenu. À présent, il écume les ruelles sombres de son ancien port d attache, utilisant ses dons surnaturels pour assassiner brutalement les riches exploiteurs du peuple. Bilgewater, la ville des chasseurs de monstres, est devenue le terrain de chasse d un monstre.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Pyke.mp3")
    if name == "Qiyana":
        desc = ('Dans la ville d Ixaocan, perdue dans la jungle, Qiyana complote pour obtenir au prix du sang le siège révéré des Yun Tal. Dernière dans l ordre de la succession, elle affronte ceux qui sont sur son chemin avec une absolue confiance en elle et une maîtrise exceptionnelle de la magie élémentaire. La terre elle-même obéit à ses ordres et Qiyana se considère comme la plus grande élémentaliste de l histoire d Ixaocan. À ce titre, elle pense mériter, non une ville, mais un empire.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Qiyana.mp3")
    if name == "Quinn":
        desc = ('Quinn est un chevalier-éclaireur d élite de Demacia qui se spécialise dans les missions d infiltration en territoire ennemi. Avec son aigle de légende, Valor, elle forme un duo inséparable dont les proies rendent souvent l âme avant même de comprendre qu elles affrontaient non pas un, mais deux héros demaciens. D une grande agilité quand la situation l impose, Quinn pointe son arbalète sur l ennemi pendant que Valor survole le terrain et marque les cibles évasives, pour une efficacité meurtrière sur le champ de bataille.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Quinn.mp3")
    if name == "Rakan":
        desc = ('Aussi lunatique qu il est charmeur, Rakan est un trublion vastaya tristement célèbre, et le plus grand danseur guerrier de l histoire de la tribu Lhotla. Pour les humains qui vivent dans les hautes terres d Ionia, son nom est depuis longtemps synonyme de festivals endiablés, de fêtes déraisonnables et de musique anarchique. Peu de gens savent cependant que cet histrion ambulant est également le partenaire de Xayah, la rebelle, dont il défend avec ferveur la cause.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Rakan.mp3")
    if name == "Rammus":
        desc = ('Beaucoup l idolâtrent, certains le méprisent, mais tous restent perplexes devant lénigmatique Rammus. Protégé par une carapace cloutée, il inspire des théories de plus en plus variées sur ses origines : demi-dieu, oracle, simple bête transformée par la magie... Quelle que soit la vérité, Rammus n est pas très bavard et ne s arrête pour personne tandis qu il parcourt le désert de Shurima.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Rammus.mp3")
    if name == "RekSai":
        desc = ('RekSai est une créature prédatrice – la plus imposante et la plus féroce de son espèce – qui se déplace sous terre pour surprendre ses proies. Sa faim insatiable a ravagé des régions entières de Shurima à l époque où cet empire était encore florissant. Les marchands et les caravanes armées faisaient des détours de plusieurs kilomètres pour rester loin de ses terres. Dès lors que RekSai vous a repéré, votre sort est scellé. Nul ne peut lui échapper ; elle est la mort qui surgit du sable.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("RekSai.mp3")
    if name == "Renekton":
        desc = ('Originaire du désert brûlant de Shurima, Renekton est un Transfiguré terrifiant animé par la rage. Il était autrefois le guerrier le plus respecté de l empire de Shurima, dont il avait mené les armées vers la victoire à maintes reprises. Cependant, après la chute de l empire, Renekton fut enseveli sous les sables. Petit à petit, alors que le monde changeait, il sombra dans la démence. Désormais libre, son unique souhait est de retrouver et de tuer son frère Nasus qui, croit-il dans sa folie, est responsable des siècles qu il a passés dans les ténèbres.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Renekton.mp3")
    if name == "Rengar":
        desc = ('Rengar est un féroce Vastaya chasseur de trophées qui ne vit que pour le frisson de la traque et de l élimination des proies les plus dangereuses. Il parcourt le monde à la recherche des bêtes les plus féroces, et surtout de KhaZix, la créature du Néant qui lui a fait perdre un œil. Rengar ne piste ses proies ni pour la nourriture ni pour la gloire, mais pour la beauté de la poursuite en elle-même.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Rengar.mp3")
    if name == "Riven":
        desc = ('Autrefois soldat d un régiment de Noxus, Riven est désormais expatriée dans un pays qu elle avait elle-même tenté d envahir. Elle s est naguère élevée dans la hiérarchie grâce à sa force de conviction et à son efficacité brutale : sa récompense fut de commander ses propres troupes, armée d une épée runique légendaire. Cependant, sur le front ionien, la foi de Riven en sa terre natale a vacillé avant de rompre. Ayant tranché tous ses liens avec l empire, elle cherche désormais sa place dans un monde blessé, alors même que, d après les rumeurs, Noxus a retrouvé sa vigueur d antan…')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Riven.mp3")
    if name == "Rumble":
        desc = ('Rumble est un jeune inventeur soupe au lait. Ne disposant que de ses deux mains et d une pile de ferraille, le yordle au tempérament de feu se fabriqua une colossale armure mécanique, dotée d un arsenal de harpons électrifiés et de roquettes incendiaires. Si certains pouffent devant ses créations sorties tout droit d une décharge, Rumble n en a que faire : après tout, c est lui qui est doté d un lance-flammes.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Rumble.mp3")
    if name == "Ryze":
        desc = ('Largement considéré comme l un des plus puissants sorciers de Runeterra, Ryze est un archimage endurci par les ans qui porte un fardeau incommensurable sur ses épaules. Armé d une constitution à toute épreuve et d un vaste arsenal de connaissances mystiques, il consacre sa vie à rassembler les Runes telluriques, les fragments de magie brute qui ont jadis servi à façonner le monde. Ryze doit récupérer ces reliques avant qu elles ne tombent entre de mauvaises mains, car il sait quel genre d horreurs elles pourraient déchaîner sur Runeterra.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Ryze.mp3")
    if name == "Sejuani":
        desc = ('Sejuani est l impitoyable chef de guerre sublimée de la Griffe hivernale, l une des tribus les plus redoutées de Freljord. La survie de son peuple est une lutte constante et désespérée contre les éléments. Pour résister aux rigueurs de l hiver, il doit lancer des assauts contre les Noxiens, les Demaciens et les Avarosans. Sejuani mène elle-même la charge des plus dangereux de ces assauts en chevauchant son sanglier drüvask, Bristle, et en agitant son fléau de glace pure pour congeler et réduire en miettes ses ennemis.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Sejuani.mp3")
    if name == "Senna":
        desc = ('Condamnée dès l enfance à être hantée par la mystérieuse Brume noire, Senna rejoignit un ordre sacré connu sous le nom des Sentinelles de la lumière. Elle combattit vaillamment, avant de périr sous les coups du cruel spectre Thresh et de voir son âme emprisonnée dans sa lanterne. Refusant de perdre espoir, Senna apprit à utiliser la Brume à l intérieur de la lanterne et revint à la vie, changée à jamais. Brandissant désormais la puissance des ténèbres comme de la lumière, Senna cherche à mettre fin à la Brume noire en la retournant contre elle-même, chaque tir de son arme permettant de libérer les âmes qui y sont perdues.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Senna.mp3")
    if name == "Sett":
        desc = ('Sett s est imposé en tant que chef du monde criminel florissant d Ionia après la guerre contre Noxus. Bien qu il ait fait ses débuts de manière modeste dans les arènes de combat de Navori, il s est rapidement fait une réputation pour sa force sauvage et sa capacité à encaisser tous les coups sans broncher. Après s être battu pour se faire une place parmi les combattants locaux, Sett s est hissé au sommet à la force de ses poings pour finalement prendre le contrôle des arènes dans lesquelles il se battait autrefois.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Sett.mp3")
    if name == "Shaco":
        desc = ('Fabriqué il y a longtemps pour servir de jouet à un prince qui se sentait seul, Shaco est une marionnette enchantée qui se repaît désormais de meurtres et de chaos. Corrompu par la magie noire et la perte de sa chère mission, le pantin autrefois gentil ne se réjouit plus que du malheur des âmes qu il tourmente. Il utilise ses jouets et ses mauvais tours pour répandre la mort et le sang, ce qui le fait follement rire. Tous ceux qui, la nuit venue, entendent un odieux ricanement savent qu ils sont la prochaine cible du Bouffon des ténèbres.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Shaco.mp3")
    if name == "Shen":
        desc = ('Shen, l Œil du crépuscule, est le chef d un groupe secret de guerriers ioniens connu sous le nom de Kinkou. Désireux d échapper aux méfaits des émotions, des préjugés et de l ego, il porte un regard désintéressé sur les choses en arpentant le chemin invisible entre le royaume des esprits et le monde physique. Ayant pour mission d assurer leur équilibre, Shen emploie ses lames d acier et son énergie arcanique contre ceux qui voudraient le menacer.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Shen.mp3")
    if name == "Shyvana":
        desc = ('Shyvana est une créature dont le cœur palpite au rythme brûlant d un éclat de rune magique. Bien qu elle paraisse souvent humanoïde, elle peut se transformer à volonté en un terrifiant dragon, crachant des flammes sur ses ennemis. Après avoir sauvé la vie du prince héritier Jarvan IV, Shyvana sert au sein de sa garde royale, luttant pour être acceptée par le peuple suspicieux de Demacia.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Shyvana.mp3")
    if name == "Singed":
        desc = ('Singed est un chimiste zaunien d une intelligence exceptionnelle, prêt à tout pour repousser les limites de la connaissance, y compris y perdre sa santé mentale. Sa folie répond-elle à une logique ? Ses décoctions ont généralement l effet escompté, mais pour beaucoup, Singed a perdu tout ce qui faisait de lui un être humain, ne laissant dans son sillage qu une trace nocive et terrifiante.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Singed.mp3")
    if name == "Sion":
        desc = ('Guerrier sanguinaire d une époque révolue, Sion était célébré comme un héros à Noxus, pour avoir étouffé un roi de Demacia de ses mains nues. Il était l objet d une telle dévotion qu on lui refusa le repos éternel, en le ramenant à la vie pour continuer à servir son empire. Il massacre sans distinction alliés comme ennemis sur son chemin, prouvant à cette occasion qu il n a plus rien d humain. Son armure rivetée à même la chair, Sion charge sans relâche au combat, luttant entre deux coups de sa puissante hache pour tenter de se remémorer qui il était.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Sion.mp3")
    if name == "Sivir":
        desc = ('Sivir est une célèbre chasseuse de trésors et capitaine de mercenaires œuvrant dans le désert de Shurima. Armée de sa légendaire lame en croix, elle a triomphé d innombrables batailles pour les clients prêts à honorer ses tarifs exorbitants. Connue pour sa détermination et son ambition démesurée, elle tire sa fierté des nombreux trésors qu elle a déterrés dans les tombes les plus périlleuses de Shurima… et revendus au prix fort. Mais le jour où des forces ancestrales se sont éveillées au plus profond de Shurima, Sivir s est retrouvée tiraillée entre deux destins conflictuels.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Sivir.mp3")
    if name == "Skarner":
        desc = ('Skarner est un immense scorpion cristallin venu d une vallée cachée de Shurima. Issus de l ancienne race des Brackerns, Skarner et les siens sont connus pour leur grande sagesse et leurs liens profonds avec la terre : leur âme a fusionné avec de puissants cristaux de vie qui contiennent les pensées et les souvenirs de leurs ancêtres. À une époque si reculée que nul ne s en souvient, les Brackerns sont entrés en hibernation pour échapper à la destruction magique, mais des événements menaçants viennent de réveiller Skarner. Seul Brackern éveillé, il lutte pour protéger les siens contre ceux qui cherchent à les blesser.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Skarner.mp3")
    if name == "Sona":
        desc = ('Sona est la plus grande virtuose de l etwahl de Demacia, ne s exprimant que par ses accords vibrants et gracieux. Ses manières distinguées lui valent d être appréciée par l aristocratie, bien que beaucoup soupçonnent ses mélodies envoûtantes de s apparenter à de la magie, tabou à Demacia. Inaudible pour des étrangers, mais comprise par ses compagnons les plus proches, Sona se sert de ses harmonies pour soigner ses alliés blessés, mais également pour frapper ses ennemis par surprise.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Sona.mp3")
    if name == "Soraka":
        desc = ('Voyageuse originaire de dimensions célestes d au-delà du Mont Targon, Soraka a abandonné son immortalité pour protéger les mortels de leurs instincts violents. Elle cherche à pousser tous ceux qu elle rencontre à embrasser les vertus de la compassion et de la pitié, allant jusqu à soigner même ceux qui lui veulent du mal. Et, malgré toutes les souffrances dont Soraka a été témoin dans ce monde, elle croit encore que le peuple de Runeterra n a pas atteint son plein potentiel.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Soraka.mp3")
    if name == "Swain":
        desc = ('Jericho Swain est le chef visionnaire de Noxus, une nation expansionniste qui ne respecte que la force. Bien que déchu et blessé pendant les guerres ioniennes, il a pris le contrôle de l empire avec une féroce détermination… Et une nouvelle main, démoniaque, a remplacé celle qu il a perdue au combat. Désormais, Swain dirige ses armées sur la ligne de front, face à des ténèbres qu il est le seul à percevoir à l horizon, dans le vol des corbeaux attirés par les cadavres qui l entourent. Dans un tourbillon de sacrifices et de regrets, le plus grand secret entre tous, c est que le véritable ennemi est à l intérieur.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Swain.mp3")
    if name == "Sylas":
        desc = ('Élevé dans l un des quartiers les plus pauvres de Demacia, Sylas de Liebourg est devenu le symbole du côté obscur de la Grande cité. Enfant, sa capacité à déceler la sorcellerie cachée attira l attention des tristement célèbres traqueurs de mages, qui finirent par l emprisonner pour avoir retourné ses pouvoirs contre eux. Désormais libéré de ses chaînes, Sylas est un révolutionnaire convaincu, employant la magie de ceux qui l entourent pour ravager le royaume qu il a autrefois servi… Et son groupe de mages exilés semble grandir chaque jour un peu plus.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Sylas.mp3")
    if name == "Syndra":
        desc = ('Syndra est une effrayante magicienne originaire d Ionia, aux pouvoirs impressionnants. Enfant, elle perturba les anciens de son village avec sa magie sauvage et incontrôlée. Elle fut confiée à un maître dans l espoir qu elle apprendrait à se contrôler, mais elle finit par découvrir que son prétendu mentor limitait ses capacités. Créant des sphères d énergie noire avec ses sentiments de douleur et de trahison, Syndra jura de détruire quiconque tenterait de la contrôler.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Syndra.mp3")
    if name == "TahmKench":
        desc = ('Au fil du temps, on lui a donné de nombreux noms. Le démon Tahm Kench voyage dans les cours d eau de Runeterra, nourrissant son insatiable appétit de la misère des autres. Bien qu il puisse sembler particulièrement charmant et fier, il rôde dans le monde tel un vagabond à la recherche d une proie sans méfiance. Sa langue extensible peut étourdir un guerrier en armure à plusieurs mètres de distance, avant de l attirer dans son estomac gargouillant vers un abysse dont il n a que peu de chances de revenir.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("TahmKench.mp3")
    if name == "Taliyah":
        desc = ('Taliyah est une mage issue des tribus nomades de Shurima, déchirée entre l émerveillement de la jeunesse et les responsabilités des adultes. Elle a déjà traversé pratiquement tout Valoran pour découvrir la véritable nature de ses pouvoirs toujours plus puissants, avant d être récemment retournée dans sa tribu pour la protéger. Certains se méprennent sur sa compassion et paient leur erreur au prix fort : sous son attitude joviale, Taliyah dissimule une volonté de fer capable de déplacer les montagnes et un esprit assez féroce pour faire trembler la terre.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Taliyah.mp3")
    if name == "Talon":
        desc = ('Talon est la dague cachée dans l ombre, un assassin impitoyable, capable de frapper sans prévenir et de fuir avant que l alerte ne soit donnée. Il a acquis une dangereuse réputation dans les brutales rues de Noxus, où il a été contraint de se battre, de tuer et de voler pour survivre. Adopté par la tristement célèbre famille Du Couteau, il use maintenant de ses talents au service de l empire, assassinant les chefs, capitaines et héros ennemis... mais aussi tout Noxien qui aurait attiré l ire de ses maîtres.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Talon.mp3")
    if name == "Taric":
        desc = ('Taric est la Manifestation du Protecteur, doté d un incroyable pouvoir en tant que gardien de la vie, de l amour et de la beauté sur Runeterra. Couvert d opprobre pour avoir abandonné son devoir et exilé de sa terre natale de Demacia, Taric a entrepris l ascension du Mont Targon en quête de rédemption et s est découvert une mission supérieure au sein des étoiles. Imprégné de la force antique de Targon, le Bouclier de Valoran monte désormais constamment la garde contre la corruption insidieuse du Néant.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Taric.mp3")
    if name == "Teemo":
        desc = ('N ayant pas peur de braver les obstacles les plus dangereux, Teemo explore le monde avec un enthousiasme débordant et une bonne humeur contagieuse. Yordle au sens moral inflexible, il suit fièrement les préceptes du Code des éclaireurs de Bandle, parfois avec tant d empressement qu il en oublie les conséquences néfastes de ses actions. Pour certains, l existence même des éclaireurs est à remettre en cause. Mais ce qu il ne faut surtout pas remettre en cause, ce sont les convictions de Teemo !')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Teemo.mp3")
    if name == "Thresh":
        desc = ('Sadique mais rusé, Thresh est un ambitieux esprit des Îles obscures. Autrefois le gardien d innombrables secrets des arcanes, il fut terrassé par un pouvoir plus grand que la vie ou la mort, et il s alimente maintenant des souffrances et des tourments qu il inflige à d autres avec une inventivité cruelle. Les souffrances de ses victimes ne se limitent pas à leur enveloppe mortelle, car Thresh fait agoniser leurs âmes, les emprisonnant pour l éternité dans sa lanterne impie.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Thresh.mp3")
    if name == "Tristana":
        desc = ('Si bon nombre d autres yordles utilisent leur énergie débordante pour explorer, découvrir, inventer ou plus simplement jouer de mauvais tours, Tristana a toujours puisé son inspiration dans les récits des grands guerriers. Elle avait beaucoup entendu parler de Runeterra, de ses factions et de ses guerres, et elle pensait que les yordles aussi avaient l étoffe des légendes. Dès son arrivée dans ce monde, elle s équipa de son fidèle canon Boomer pour se jeter au combat avec un courage et un optimisme sans bornes.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Tristana.mp3")
    if name == "Trundle":
        desc = ('Trundle est un troll massif, sournois et malicieux. Il n y a rien qu il ne puisse soumettre à sa volonté avec son gourdin, pas même Freljord. Extrêmement territorial, Trundle traque tous ceux qui sont assez fous pour pénétrer sur ses terres. Ensuite, armé de son imposante massue en glace pure, il fait trembler ses ennemis avant de leur planter des éclats de glace dans le corps et de se moquer d eux tandis que la toundra absorbe leur sang.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Trundle.mp3")
    if name == "Tryndamere":
        desc = ('Poussé par une rage infinie, Tryndamere traverse Freljord et parfait sa maîtrise du combat en défiant les plus grands guerriers du nord, pour se préparer aux jours sombres qui s annoncent. Longtemps dominé par sa haine, il cherchait à se venger de l annihilation de son clan, mais il a depuis rencontré Ashe et trouvé un nouveau foyer auprès des Avarosans. Sa force est pratiquement surhumaine et son courage légendaire, et cela lui a permis de remporter avec ses nouveaux alliés d innombrables victoires plus qu improbables.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Tryndamere.mp3")
    if name == "TwistedFate":
        desc = ('Twisted Fate est un virtuose des cartes à la réputation ambiguë qui a parcouru le monde entier pour l éblouir de son charme et de ses talents, s attirant l admiration et la haine des riches comme des pigeons. Il prend rarement les choses au sérieux, salue chaque nouveau jour avec un sourire moqueur et insouciant. Twisted a toujours un atout dans sa manche, au propre comme au figuré.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("TwistedFate.mp3")
    if name == "Twitch":
        desc = ('Rat de Zaun, pesteux de naissance, connaisseur en saleté par passion, Twitch n a pas peur de se salir les pattes. Armé d une arbalète chimique qu il pointe droit sur le cœur de Piltover, Twitch s est juré de montrer aux gens de la surface à quel point ils sont vraiment sales. Toujours furtif et insaisissable, quand il ne traîne pas dans le Puisard, il fouille dans les déchets à la recherche de trésors qu il est le seul à apprécier... ou d un morceau de sandwich.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Twitch.mp3")
    if name == "Udyr":
        desc = ('Plus qu un simple mortel, Udyr est le réceptacle de la puissance sauvage de quatre esprits animaux primitifs. Quand Udyr cherche en lui les esprits féroces de la nature, il libère leur force exceptionnelle : la vitesse et la férocité du tigre, la résistance de la tortue, la force de l ours et la flamme éternelle du phénix. En unissant ces esprits, Udyr est capable de défaire quiconque s opposerait aux forces de la nature.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Udyr.mp3")
    if name == "Urgot":
        desc = ('Autrefois, Urgot était un puissant bourreau noxien. Il fut trahi par l empire pour lequel il avait tant tué. Ceint de chaînes de fer, il fut contraint d apprendre le vrai sens de la force dans les Oubliettes, une mine de forçats située dans les profondeurs de Zaun. Il put émerger à l occasion d un désastre qui jeta toute la ville dans le chaos. À présent, son ombre imposante s étend dans son empire criminel souterrain. Levant sur ses victimes les chaînes qui le maintenaient naguère en esclavage, il veut purger son nouveau foyer, nouvelle croisée des douleurs, de tous ceux qu il en estime indignes.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Urgot.mp3")
    if name == "Varus":
        desc = ('Membre de la race antique des Darkin, Varus était en son temps un assassin cruel qui aimait torturer ses ennemis, les conduisant jusqu aux portes de la folie avant de les achever d une flèche. À la fin de la Guerre des Darkin, il fut emprisonné. Des siècles plus tard, il s évada en utilisant la chair recomposée de deux chasseurs d Ionia : l ayant relâché par imprudence, ils furent condamnés à porter l arc lié à l essence de Varus. Varus traque désormais ceux qui l ont enfermé pour se venger, mais les âmes des mortels à l intérieur de lui s opposent à ses desseins de toutes leurs forces.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Varus.mp3")
    if name == "Vayne":
        desc = ('Shauna Vayne est une chasseuse de monstres mortelle et sans scrupule. Originaire de Demacia, elle voue sa vie à la destruction du démon qui a assassiné sa famille. Armée d une arbalète montée sur son poignet et dotée d un cœur rongé par le désir de vengeance, elle n est heureuse que quand elle assassine les praticiens ou les créations des arts obscurs en les frappant depuis l ombre avec une volée de carreaux d argent.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Vayne.mp3")
    if name == "Veigar":
        desc = ('Maître enthousiaste de la magie noire, Veigar s est approprié des pouvoirs que peu de mortels osent approcher. Habitant de Bandle à l esprit libre, il veut repousser les limites de la magie yordle et se tourner vers les textes arcaniques qui sont restés cachés des millénaires. Fasciné jusqu à l obstination par les mystères de l univers, Veigar est souvent sous-estimé par les gens qui l entourent. Bien qu il se croie fondamentalement maléfique, il possède une moralité qui le mène à s interroger sur ses motivations.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Veigar.mp3")
    if name == "VelKoz":
        desc = ('On ne sait pas trop si VelKoz fut le premier monstre du Néant à émerger à Runeterra, mais il est certain qu aucun autre n a jamais égalé la froideur calculatrice de sa cruauté. Alors que ses semblables dévorent ou profanent tout ce qui les entoure, il cherche à étudier le royaume physique et les étranges êtres belliqueux qui l habitent. Selon lui, c est ainsi que le Néant trouvera comment exploiter leurs faiblesses. Mais VelKoz n est pas qu un observateur passif. Il répond à toute menace avec des éruptions mortelles de plasma ou en déchirant le tissu même du monde.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("VelKoz.mp3")
    if name == "Vi":
        desc = ('Autrefois criminelle des quartiers louches de Zaun, Vi est une femme sans peur, mais pas sans reproche, au tempérament bouillant, impulsive, qui n a qu un respect mesuré pour les représentants de l autorité. Vi a grandi seule et a développé d excellents instincts de survie ainsi qu un sens de l humour assez caustique. Aujourd hui, elle travaille avec les gendarmes de Piltover pour maintenir l ordre et se sert pour cela de puissants gantelets Hextech qui n ont peur de frapper ni les plus épais murs de briques ni les suspects.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Vi.mp3")
    if name == "Viktor":
        desc = ('Héraut d un nouvel âge de technologie, Viktor a consacré sa vie aux progrès de l humanité. Idéaliste cherchant à hisser le peuple de Zaun à de nouveaux sommets de compréhension, il pense que le potentiel de l humanité ne pourra être réalisé que par le grand pas en avant d une glorieuse évolution technologique. Doté d un corps optimisé par l acier et la science, Viktor poursuit fanatiquement son idéal d un meilleur avenir.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Viktor.mp3")
    if name == "Vladimir":
        desc = ('Assoiffé de sang humain, Vladimir influe sur la politique de Noxus depuis les premiers jours de l empire. En plus d allonger surnaturellement sa vie, sa maîtrise de l hémomancie lui permet de contrôler les esprits et les corps des autres aussi aisément que les siens. Dans les flamboyants salons de l aristocratie noxienne, cela lui a permis de créer autour de lui un culte de la personnalité. Cependant, dans les bas-fonds, il saigne littéralement ses ennemis à blanc.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Vladimir.mp3")
    if name == "Volibear":
        desc = ('Pour ceux qui le vénèrent encore, Volibear est l incarnation de la tempête. Destructeur, sauvage et déterminé, il existait bien avant que les mortels n arpentent la toundra de Freljord ; désormais, il défend férocement les terres qu il a créées avec sa famille de demi-dieux. Habité d une haine profonde envers la civilisation et la faiblesse qu elle a engendrée, il se bat à coups de crocs et de griffes pour restaurer les traditions d autrefois, celles du temps où la terre était sauvage et où le sang coulait librement.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Volibear.mp3")
    if name == "Warwick":
        desc = ('Warwick est un monstre qui chasse dans les rues grisâtres de Zaun. Transformé par des expériences horribles, son corps est désormais muni d un système intriqué de chambres et de pompes qui injecte une rage alchimique dans ses veines. Surgissant des ombres, il traque les criminels qui terrorisent les profondeurs de la ville. Warwick est attiré par le sang, dont l odeur le rend fou. Si sa proie saigne, elle n a aucune chance de lui échapper.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Warwick.mp3")
    if name == "Wukong":
        desc = ('Wukong est un Vastaya qui utilise sa force, son agilité et son intelligence pour semer la confusion parmi ses adversaires et prendre sur eux l avantage. Après s être fait un ami en la personne d un guerrier nommé Maître Yi, Wukong est devenu le dernier tenant d un art martial antique connu sous le nom de Wuju. Armé de son bâton enchanté, Wukong veut empêcher Ionia de devenir ruines et décombres.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Wukong.mp3")
    if name == "Xayah":
        desc = ('Précise et meurtrière, Xayah est une révolutionnaire vastaya menant une guerre personnelle dans le but de sauver son peuple. Elle se sert de sa célérité, de sa ruse et de ses plumes tranchantes comme des rasoirs pour terrasser tous ceux qui se dressent sur sa route. Xayah se bat aux côtés de son partenaire et amant, Rakan, pour défendre leur tribu dépérissante et rendre à leur race ce qu elle considère être sa gloire d antan.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Xayah.mp3")
    if name == "Xerath":
        desc = ('Xerath est un mage transfiguré de la Shurima antique, un être d énergie arcanique habitant les fragments détruits d un sarcophage magique. Pendant des millénaires, il est resté prisonnier des sables du désert, mais le retour de Shurima l a libéré de sa prison ancestrale. Devenu ivre de pouvoir, il cherche désormais à reprendre ce qu il croit lui être dû et à remplacer les civilisations arrivistes qui ont pris possession du monde par une nouvelle, façonnée à son image.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Xerath.mp3")
    if name == "XinZhao":
        desc = ('Xin Zhao est un guerrier résolu qui sert fidèlement la dynastie régnante des Lightshield. Naguère condamné à se battre dans les arènes de combat de Noxus, il survécut à d innombrables rencontres de gladiateurs. Mais après avoir été libéré par les forces de Demacia, il jura allégeance à ses braves libérateurs. Armé de sa lance à trois pointes, Xin Zhao combat désormais pour son royaume, défiant ses ennemis avec audace, quelles que soient ses chances de succès.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("XinZhao.mp3")
    if name == "Yasuo":
        desc = ('L Ionien Yasuo est un épéiste agile et résolu, capable de déchaîner contre ses ennemis la puissance de l air. Alors qu il était encore un jeune homme fier, il fut accusé à tort d avoir assassiné son maître. Incapable de prouver son innocence, il dut fuir et fut finalement contraint de tuer son frère pour se défendre. Même après la découverte du véritable meurtrier de son maître, Yasuo ne parvint pas à faire la paix avec sa conscience. Il erre désormais dans son pays natal, et seul le vent guide sa lame.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Yasuo.mp3")
    if name == "Yorick":
        desc = ('Yorick est le dernier survivant d un ordre religieux disparu depuis longtemps et son pouvoir sur les morts est à la fois une bénédiction et une malédiction. Prisonnier des Îles obscures, il n a pour compagnons que les cadavres pourrissants et les esprits hurlants qu il rassemble. Les actes monstrueux de Yorick trahissent son noble objectif : libérer sa terre natale de la malédiction de la Ruine.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Yorick.mp3")
    if name == "Yuumi":
        desc = ('Originaire de Bandle, Yuumi est un familier magique dont la maîtresse, une enchanteresse yordle du nom de Norra, a mystérieusement disparu. Yuumi est désormais la gardienne du Grimoire des Seuils que possédait Norra, un livre permettant de franchir des portails. Partie à la recherche de sa maîtresse, Yuumi s est fait de nouveaux amis durant son périple, et elle les protège tous avec la même détermination. Même si Grimoire aimerait que Yuumi se concentre davantage sur sa mission, sa comparse aime prendre le temps de faire la sieste et de pêcher des poissons. Malgré cela, elle finit toujours par repartir en quête de sa maîtresse.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Yuumi.mp3")
    if name == "Zac":
        desc = ('Zac est le produit d une fuite toxique qui, dégoulinant par une veine techno-chimique, se transforma en bassin dans une profonde caverne du Puisard de Zaun. En dépit de ses humbles origines, Zac a évolué pour passer du stade de dépôt primordial à celui d être pensant qui se faufile dans les canalisations de la ville. De temps en temps, il émerge pour aider ceux qui ne s en sortent pas seuls ou pour reconstruire les infrastructures en mauvais état de Zaun.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Zac.mp3")
    if name == "Zed":
        desc = ('L impitoyable Zed est le maître de l Ordre de l ombre, une organisation qu il a créée dans l intention de militariser la tradition des arts martiaux d Ionia et de chasser enfin les envahisseurs noxiens. Pendant la guerre, le désespoir le conduisit à déchaîner la Forme secrète de l ombre, un puissant esprit maléfique aussi dangereux que corrompu. Si Zed maîtrise ces techniques interdites, c est pour détruire tout ce qu il considère comme une menace contre sa nation ou son ordre.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Zed.mp3")
    if name == "Ziggs":
        desc = ('Amoureux des grosses bombes et des mèches courtes, le yordle Ziggs est une force de la nature explosive. Assistant d un inventeur de Piltover, il finit par se lasser de sa vie routinière et devint l ami d une jeune fille imprévisible et portée sur les explosifs, Jinx. Après une folle nuit en ville, Ziggs suivit les conseils de Jinx et s installa à Zaun, où il se livre désormais à sa passion plus librement, terrorisant les Barons de la chimie comme les simples citoyens dans sa quête éternelle pour faire sauter tout ce qui traverse son champ de vision.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Ziggs.mp3")
    if name == "Zilean":
        desc = ('Naguère puissant mage d Icathia, Zilean devint obsédé par le passage du temps après avoir assisté à la destruction de sa terre natale par le Néant. Refusant de perdre une minute à pleurer sur les décombres, il fit appel à une antique force magique capable de prédire tous les avenirs possibles. Devenu techniquement immortel, Zilean erre désormais entre passé, présent et futur, distordant autour de lui le flux du temps, toujours à la recherche du moment exact qui lui permettra de changer le passé et d empêcher la destruction d Icathia.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Zilean.mp3")
    if name == "Zoe":
        desc = ('Incarnation de l espièglerie, de l imagination et de l inconstance, Zoé est une messagère cosmique de Targon, annonciatrice des grands événements qui chamboulent les mondes. Sa simple présence distord les règles mathématiques qui gouvernent dans l ombre les réalités et, sans pour autant le vouloir, peut même provoquer des cataclysmes. Cela explique peut-être la nonchalance désinvolte avec laquelle Zoé traite ses tâches, préférant consacrer le plus clair de son temps à s amuser, à jouer des tours aux mortels, bref, à faire tout ce qui lui plaît. Une rencontre avec Zoé peut se révéler joyeuse et porteuse d optimisme, mais ce n est souvent qu une apparence, cachant une vérité extrêmement dangereuse.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Zoe.mp3")
    if name == "Zyra":
        desc = ('Née au cours d une ancienne catastrophe magique, Zyra est la colère de la nature incarnée : mélange de plante et d humain, faisant émerger de nouvelles pousses à chaque pas. Elle considère les nombreux mortels de Valoran comme de simples proies pour sa progéniture végétale, et les éliminer avec ses gerbes d épines ne lui pose aucun problème. Bien que nul ne connaisse ses vrais objectifs, Zyra erre de par le monde, suivant son instinct qui est de coloniser toujours plus de terres et d en exterminer toutes les autres formes de vie.')
        # Save Text INTO MP3 FILE
        #myobj = gTTS(text=desc, lang=language, slow=False)
        #myobj.save("Zyra.mp3")

    return desc

def define_story_sound(name,play_submenu):
    if name == "Aatrox":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_aatrox)
    if name == "Ahri":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Ahri)
    if name == "Akali":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Akali)
    if name == "Alistar":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Alistar)
    if name == "Amumu":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Amumu)
    if name == "Anivia":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Anivia)
    if name == "Annie":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Annie)
    if name == "Aphelios":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Aphelios)
    if name == "Ashe":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Ashe)
    if name == "AurelionSol":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_AurelionSol)
    if name == "Azir":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Azir)
    if name == "Bard":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Bard)
    if name == "Blitzcrank":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Blitzcrank)
    if name == "Brand":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Brand)
    if name == "Braum":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Braum)
    if name == "Caitlyn":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Caitlyn)
    if name == "Camille":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Camille)
    if name == "Cassiopeia":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Cassiopeia)
    if name == "ChoGath":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_ChoGath)
    if name == "Corki":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Corki)
    if name == "Darius":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Darius)
    if name == "Diana":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Diana)
    if name == "DrMundo":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_DrMundo)
    if name == "Draven":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Draven)
    if name == "Ekko":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Ekko)
    if name == "Elise":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Elise)
    if name == "Evelynn":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Evelynn)
    if name == "Ezreal":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Ezreal)
    if name == "Fiddlesticks":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Fiddlesticks)
    if name == "Fiora":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Fiora)
    if name == "Fizz":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Fizz)
    if name == "Galio":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Galio)
    if name == "Gangplank":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Gangplank)
    if name == "Garen":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Garen)
    if name == "Gnar":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Gnar)
    if name == "Gragas":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Gragas)
    if name == "Graves":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Graves)
    if name == "Hecarim":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Hecarim)
    if name == "Heimerdinger":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Heimerdinger)
    if name == "Illaoi":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Illaoi)
    if name == "Irelia":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Irelia)
    if name == "Ivern":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Ivern)
    if name == "Janna":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Janna)
    if name == "JarvanIV":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_JarvanIV)
    if name == "Jax":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Jax)
    if name == "Jayce":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Jayce)
    if name == "Jhin":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Jhin)
    if name == "Jinx":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Jinx)
    if name == "KaiSa":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_KaiSa)
    if name == "Kalista":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Kalista)
    if name == "Karma":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Karma)
    if name == "Karthus":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Karthus)
    if name == "Kassadin":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Kassadin)
    if name == "Katarina":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Katarina)
    if name == "Kayle":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Kayle)
    if name == "Kayn":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Kayn)
    if name == "Kennen":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Kennen)
    if name == "KhaZix":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_KhaZix)
    if name == "Kindred":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Kindred)
    if name == "Kled":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Kled)
    if name == "KogMaw":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_KogMaw)
    if name == "Leblanc":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Leblanc)
    if name == "LeeSin":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_LeeSin)
    if name == "Leona":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Leona)
    if name == "Lissandra":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Lissandra)
    if name == "Lucian":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Lucian)
    if name == "Lulu":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Lulu)
    if name == "Lux":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Lux)
    if name == "MaitreYi":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_MaitreYi)
    if name == "Malphite":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Malphite)
    if name == "Malzahar":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Malzahar)
    if name == "Maokai":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Maokai)
    if name == "MissFortune":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_MissFortune)
    if name == "Mordekaiser":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Mordekaiser)
    if name == "Morgana":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Morgana)
    if name == "Nami":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Nami)
    if name == "Nasus":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Nasus)
    if name == "Nautilus":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Nautilus)
    if name == "Neeko":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Neeko)
    if name == "Nidalee":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Nidalee)
    if name == "Nocturne":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Nocturne)
    if name == "NunuEtWillump":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_NunuEtWillump)
    if name == "Olaf":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Olaf)
    if name == "Orianna":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Orianna)
    if name == "Ornn":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Ornn)
    if name == "Pantheon":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Pantheon)
    if name == "Poppy":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Poppy)
    if name == "Pyke":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Pyke)
    if name == "Qiyana":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Qiyana)
    if name == "Quinn":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Quinn)
    if name == "Rakan":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Rakan)
    if name == "Rammus":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Rammus)
    if name == "RekSai":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_RekSai)
    if name == "Renekton":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Renekton)
    if name == "Rengar":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Rengar)
    if name == "Riven":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Riven)
    if name == "Rumble":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Rumble)
    if name == "Ryze":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Ryze)
    if name == "Sejuani":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Sejuani)
    if name == "Senna":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Senna)
    if name == "Sett":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Sett)
    if name == "Shaco":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Shaco)
    if name == "Shen":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Shen)
    if name == "Shyvana":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Shyvana)
    if name == "Singed":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Singed)
    if name == "Sion":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Sion)
    if name == "Sivir":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Sivir)
    if name == "Skarner":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Skarner)
    if name == "Sona":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Sona)
    if name == "Soraka":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Soraka)
    if name == "Swain":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Swain)
    if name == "Sylas":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Sylas)
    if name == "Syndra":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Syndra)
    if name == "TahmKench":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_TahmKench)
    if name == "Taliyah":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Taliyah)
    if name == "Talon":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Talon)
    if name == "Taric":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Taric)
    if name == "Teemo":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Teemo)
    if name == "Thresh":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Thresh)
    if name == "Tristana":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Tristana)
    if name == "Trundle":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Trundle)
    if name == "Tryndamere":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Tryndamere)
    if name == "TwistedFate":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_TwistedFate)
    if name == "Twitch":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Twitch)
    if name == "Udyr":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Udyr)
    if name == "Urgot":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Urgot)
    if name == "Varus":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Varus)
    if name == "Vayne":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Vayne)
    if name == "Veigar":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Veigar)
    if name == "Velkoz":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Velkoz)
    if name == "Vi":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Vi)
    if name == "Viktor":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Viktor)
    if name == "Vladimir":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Vladimir)
    if name == "Volibear":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Volibear)
    if name == "Warwick":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Warwick)
    if name == "Wukong":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Wukong)
    if name == "Xayah":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Xayah)
    if name == "Xerath":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Xerath)
    if name == "XinZhao":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_XinZhao)
    if name == "Yasuo":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Yasuo)
    if name == "Yorick":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Yorick)
    if name == "Yuumi":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Yuumi)
    if name == "Zac":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Zac)
    if name == "Zed":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Zed)
    if name == "Ziggs":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Ziggs)
    if name == "Zilean":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Zilean)
    if name == "Zoe":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Zoe)
    if name == "Zyra":
        # LISTEN TEXT FROM MP3 FILE
        play_submenu.add_button('Ecouter le Synopsis du personnage', play.play_Zyra)


def open_OP_GG():
    webbrowser.open_new("https://www.op.gg/")


def perso_play(name,pygame_menu,window_size):

    # Champions_list SUBMENU
    submenu_theme = pygame_menu.themes.THEME_DEFAULT.copy()
    submenu_theme.widget_font_size = 15
    play_submenu = pygame_menu.Menu(
        height=window_size[1] * 0.8,
        theme=submenu_theme,
        title=name,
        width=window_size[0] * 0.9,
    )

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
    wid1 = settings_menu.add_text_input('Champion: ',
                                        default='',
                                        textinput_id='champion')
    wid2 = settings_menu.add_text_input('role: ',
                                        default='',
                                        maxchar=10,
                                        textinput_id='role')
    settings_menu.add_text_input('Nombre_de_kills: ',
                                 default='',
                                 maxchar=3,
                                 maxwidth=3,
                                 textinput_id='nombre_de_kills',
                                 input_type=pygame_menu.locals.INPUT_INT,
                                )
    settings_menu.add_text_input('nombre_assist: ',
                                 default='',
                                 maxchar=3,
                                 maxwidth=3,
                                 textinput_id='nombre_assist',
                                 input_type=pygame_menu.locals.INPUT_INT,
                                 cursor_selection_enable=False)
    settings_menu.add_text_input('nombre_death: ',
                                 default='',
                                 maxchar=3,
                                 maxwidth=3,
                                 textinput_id='nombre_death',
                                 input_type=pygame_menu.locals.INPUT_INT,
                                 cursor_selection_enable=False)
    settings_menu.add_text_input('nombre_minions: ',
                                 default='',
                                 maxchar=4,
                                 maxwidth=4,
                                 textinput_id='nombre_minions',
                                 input_type=pygame_menu.locals.INPUT_INT,
                                 cursor_selection_enable=False)
    settings_menu.add_text_input('total_coin: ',
                                 default='',
                                 maxchar=5,
                                 maxwidth=5,
                                 textinput_id='total_coin',
                                 input_type=pygame_menu.locals.INPUT_INT,
                                 cursor_selection_enable=False)
    settings_menu.add_text_input('issue_match: ',
                                 default='',
                                 textinput_id='issue_match',
                                 maxwidth=19)
    settings_menu.add_text_input('pseudo: ',
                                 default='',
                                 textinput_id='pseudo',
                                 maxwidth=19)
    settings_menu.add_text_input('debut_game: ',
                                 default='',
                                 textinput_id='debut_game',
                                 maxwidth=19)
    settings_menu.add_text_input('fin_game: ',
                                 default='',
                                 textinput_id='fin_game',
                                 maxwidth=19)
    settings_menu.add_text_input('item_1: ',
                                 default='',
                                 textinput_id='item_1',
                                 maxwidth=19)
    settings_menu.add_text_input('item_2: ',
                                 default='',
                                 textinput_id='item_2',
                                 maxwidth=19)
    settings_menu.add_text_input('item_3: ',
                                 default='',
                                 textinput_id='item_3',
                                 maxwidth=19)
    settings_menu.add_text_input('item_4: ',
                                 default='',
                                 textinput_id='item_4',
                                 maxwidth=19)
    settings_menu.add_text_input('item_5: ',
                                 default='',
                                 textinput_id='item_5',
                                 maxwidth=19)
    settings_menu.add_text_input('item_6: ',
                                 default='',
                                 textinput_id='item_6',
                                 maxwidth=19)



    def input_csv(data):
        champion = data.get('champion')
        role = data.get('role')
        nombre_de_kills = data.get('nombre_de_kills')
        nombre_assist = data.get('nombre_assist')
        nombre_death = data.get('nombre_death')
        nombre_minions = data.get('nombre_minions')
        total_coin = data.get('total_coin')
        issue_match = data.get('issue_match')
        pseudo = data.get('pseudo')
        debut_game = data.get('debut_game')
        fin_game = data.get('fin_game')
        item_1 = data.get('item_1')
        item_2 = data.get('item_2')
        item_3 = data.get('item_3')
        item_4 = data.get('item_4')
        item_5 = data.get('item_5')
        item_6 = data.get('item_6')
        with open('champ.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([champion]+[role]+[nombre_de_kills]+[nombre_assist]+[nombre_death]+[nombre_minions]+[total_coin]+[issue_match]+[pseudo]+[debut_game]+[fin_game]+[item_1]+[item_2]+[item_3]+[item_4]+[item_5]+[item_6])

    def read_csv_ahri():

        sample_data = pd.read_csv('ahri.csv')
        # selectioner les row concernant afghanistan
        af = sample_data[sample_data.champion == 'Arhi']
        alb = sample_data[sample_data.champion == 'Arhi']
        al = sample_data[sample_data.champion == 'Arhi']

        plt.plot(af.npartie, af.kill)
        plt.plot(alb.npartie, alb.assist)
        plt.plot(alb.npartie, alb.jour)

        plt.legend(['kill', 'mort', 'assist'])
        plt.xlabel('parties avec Arhi')
        # plt.ylabel('assist')

        # print(alb)
        plt.show()

    # EVALUTE KILS RATING WITH ANOTHER CHAMPS
    def total_kill_ahri():
        df = pd.read_csv('champ.csv')

        # epaisseur de la barre
        barWidth = 1

        # 1er set de barre : total / peut choisir un champion + une colone
        x1 = df.loc[df.Champion == 'Ahri', 'Kills']
        kwargs = dict(alpha=0.6)
        plt.hist(x1, **kwargs, color='red', label='Ideal', width=barWidth)

        # 2eme set de barre : total / peut choisir un champion + une colone
        x2 = df.loc[df.Champion == 'Ahri', 'Assists']
        kwargs = dict(alpha=0.8)
        plt.hist(x2, **kwargs, color='orange', label='Ideal', width=barWidth)

        # Tout ce qui est titre
        # legend
        plt.legend(['KIll', 'Assist'])

        # nom x et y
        plt.ylabel('Fréquence')
        plt.xlabel('Echelle')

        # titre
        plt.title('Total Kill/Assist de Ahri')
        plt.show()

    def data_fun():
        """
        Print data of the menu.

        :return: None
        """
        # CONNECTION TO MYSQL WORKBENCH DATABASE
        baseDeDonnees = mysql.connector.connect(host="localhost", user="newuser", password="password",
                                                database="performances_LoL")
        cursor = baseDeDonnees.cursor()

        # WE CREATE DATA VARIABLE TO ASSIGN THE INPUT VALUES ON FORM
        data = settings_menu.get_input_data()
        print('Printing DATA PLEASE WAIT.....')
        # WE STOCK IN VARIABLE THE FIRST NAME INPUT
        # DATA.GET IS A METHOD TO GET THE INPUT DATA

        champion = data.get('champion')
        role = data.get('role')
        nombre_de_kills = data.get('nombre_de_kills')
        nombre_assist = data.get('nombre_assist')
        nombre_death = data.get('nombre_death')
        nombre_minions = data.get('nombre_minions')
        total_coin = data.get('total_coin')
        issue_match = data.get('issue_match')
        pseudo = data.get('pseudo')
        debut_game = data.get('debut_game')
        fin_game = data.get('fin_game')
        item_1 = data.get('item_1')
        item_2 = data.get('item_2')
        item_3 = data.get('item_3')
        item_4 = data.get('item_4')
        item_5 = data.get('item_5')
        item_6 = data.get('item_6')

        #password = data.get('password')
        #difficulte = data.get('difficulty')

        # WE CREATE INSERT VARIABLE TO INJECT THE SQL REQUEST
        # IF TABLE EXISTE DELETE AND CREATE NEW ONE
        #cursor.execute("DROP TABLE IF EXISTS Results_games;")
        # Create TABLE
        #cursor.execute("CREATE TABLE Results_games (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,"
        #               " champion VARCHAR(10) NOT NULL,"
        #               " role VARCHAR(10) NOT NULL,"
        #               " nombre_de_kills INT NOT NULL,"
        #               " nombre_assist INT NOT NULL,"
        #               " nombre_death INT NOT NULL,"
        #               " nombre_minions INT NOT NULL,"
        #               " total_coin INT NOT NULL,"
        #               " issue_match VARCHAR(10) NOT NULL,"
        #               " pseudo VARCHAR(10) NOT NULL,"
        #               " debut_game TIME(6) NOT NULL,"
        #               " fin_game TIME(6) NOT NULL,"
        #               " item_1 VARCHAR(30) NOT NULL,"
        #               " item_2 VARCHAR(30) NOT NULL,"
        #               " item_3 VARCHAR(30) NOT NULL,"
        #               " item_4 VARCHAR(30) NOT NULL,"
        #               " item_5 VARCHAR(30) NOT NULL,"
        #               " item_6 VARCHAR(30) NOT NULL)ENGINE=InnoDB DEFAULT CHARSET=utf8;")

        # INTO A VARIABLE NAMED "INSERT"  WE ASSIGN COLUMN NAMES ID, name, etc WITH EMPTY VALUES
        insert = "INSERT INTO Results_games (champion," \
                 " role," \
                 " nombre_de_kills," \
                 " nombre_assist," \
                 " nombre_death," \
                 " nombre_minions," \
                 " total_coin," \
                 " issue_match," \
                 " pseudo," \
                 " debut_game," \
                 " fin_game," \
                 " item_1," \
                 " item_2," \
                 " item_3," \
                 " item_4," \
                 " item_5," \
                 " item_6) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # INTO A VARIABLE NAMED "VAL" WE TAKE THE INPUT USER WITH ALL VALUES
        val = (champion, role, nombre_de_kills, nombre_assist, nombre_death, nombre_minions, total_coin, issue_match, pseudo, debut_game, fin_game, item_1, item_2, item_3, item_4, item_5, item_6 )
        # INJECT IN DATABASE THE COLUMNS NAMES IN VARIABLE NAMED "INSERT" WITH THE VALUES VARIABLES NAMED "VAL" FROM INPUT USER
        cursor.execute(insert, val)

        # LOAD DATABASE ENTRY
        baseDeDonnees.commit()
        # CLOSE DATABASE
        baseDeDonnees.close()

        input_csv(data)


        print('DATA SAVED INTO WORKBENCH SUCCESSFULLY !')
        print ('DATA SAVED INTO CSV_FILE !')


    settings_menu.add_button('Store data', data_fun)  # Call function
    settings_menu.add_button('Back to Main Menu', pygame_menu.events.BACK,
                             align=pygame_menu.locals.ALIGN_CENTER)

    play_submenu.add_image(define_img(name, pygame_menu), scale=(0.50, 0.50))
    play_submenu.add_label(define_desc(name, pygame_menu), max_char=60, margin=(5, -1))
    play_submenu.add_label('')
    define_story_sound(name, play_submenu)
    play_submenu.add_button('Enregistrer les Données de ma dernière partie', settings_menu)
    play_submenu.add_button('Statistiques temporelles', read_csv_ahri)
    play_submenu.add_button('Comparatif kills/assist', total_kill_ahri)
    #play_submenu.add_button('Consulter historique 10 dernières parties')
    play_submenu.add_button('Accéder à OP GG', open_OP_GG)
    play_submenu.add_button('Back to Main Menu', pygame_menu.events.BACK)

    return play_submenu

