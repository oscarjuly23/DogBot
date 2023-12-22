import logging
from os import name
from re import T

from requests.api import get
from dictionary import *
from filemanager import *
from persona import *
from hogar import *
from calculate import *
from dog import *
import random
import nltk
from spellchecker import SpellChecker
from nltk.corpus import stopwords
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, user
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

intentos = 1
intentos2 = 2
quinaTask = ""
persona = Persona()
hogar = Hogar()
spell = SpellChecker()
dog = None


#Yes/no synonyms
yesSyns = getSynonyms("yes")
noSyns = getSynonyms("no")
#Size synonyms
synsS = getSynonyms("small")
synsM = getSynonyms("medium")
synsL = getSynonyms("large")
numAbuses = 0

def checkBlacklist(text, update: Update) -> int:
    global numAbuses
    for word in blackList:
        if word in text:
            numAbuses += 1
            if numAbuses == 3:
                update.message.reply_text("I don't have to put up with this. When you are more relaxed I will talk to you.")
                return ConversationHandler.END
            else: 
                update.message.reply_text(random.choice(RESPONSES_BLACKLIST))
                break

def clean_text(text):
    tokens = nltk.word_tokenize(text)
    # Remove the punctuations
    tokens = [word for word in tokens if any(chr.isalnum() for chr in word)]
    # Lower the tokens
    tokens = [word.lower() for word in tokens]
    # Remove stopword
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('no')
    all_stopwords.remove('not')
    all_stopwords.remove('you')
    all_stopwords.remove('all')
    tokens = [word for word in tokens if not word in all_stopwords]
    # Lemmatize
    lemma = nltk.WordNetLemmatizer()
    tokens = [lemma.lemmatize(word, pos = "v") for word in tokens]
    tokens = [lemma.lemmatize(word, pos = "n") for word in tokens]
    #Spell correction
    tokens = [spell.correction(word) for word in tokens]
    return tokens

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

STATUS, TASK, DATO, BREED, FINALIDAD, CUIDADOS, NIÑOS, MASCOTAS, TAMAÑO, PREFERENCIA, HORARIO, DEPORTE, DISCAPACIDAD, VIVIENDA, ESPACIO, CARACTER = range(16)

def start(update: Update, _: CallbackContext) -> int:
    update.message.reply_text(
        random.choice(GREETING_RESPONSES) + " " + f"{update.effective_user.first_name}!")
    update.message.reply_text("My name is DogBot, how are you?")
    return STATUS

bucle = False

def status(update: Update, _: CallbackContext) -> int:
    wordExists = False
    text = clean_text(update.message.text)
    if checkBlacklist(update.message.text, update) == -1: return ConversationHandler.END
    for word in text:
        if word in estado_animico:
            wordExists = True
            update.message.reply_text(estado_animico[word])
    if not wordExists:
        update.message.reply_text(random.choice(FALLBACKS))
    logger.info("%s: %s", update.message.from_user.first_name, update.message.text)
    update.message.reply_text('What can I do for you?')

    return TASK

def task(update: Update, _: CallbackContext) -> int:
    for question in QUESTIONS:
        if question in  update.message.text.lower():
            update.message.reply_text('I can help you to find the ideal dog breed for you and provide information on a wide variety of breeds.')
            return TASK
    global quinaTask
    global dog
    hhTask = False
    dog = breedExists(update.message.text)
    text = clean_text(update.message.text)
    if checkBlacklist(update.message.text, update) == -1: return ConversationHandler.END
    logger.info("%s: %s", update.message.from_user.first_name, update.message.text)
    for end in ENDS:
        if end in update.message.text.lower():
            update.message.reply_text('Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove())
            return ConversationHandler.END
    for word in text:
        if word in verbs:
            for verb in verbs[word]:
                if verb in text:
                    update.message.reply_text('What do you want a dog for (companion, guardian...)?')
                    return FINALIDAD
        elif word in tasks:
            quinaTask = word
            hhTask = True
    if hhTask:
        if dog == None:
            update.message.reply_text('Can you tell me the breed of the dog?')
            return BREED
        else:
            info(update)
            update.message.reply_text("What else can I do for you?")
            return TASK
    else:
        if dog == None:
            update.message.reply_text("I can't do that! Try to ask me something else?")
            return TASK
        else:
            update.message.reply_text('What do you want to know about ' + dog.name + "?")
            return DATO

def breed(update: Update, _: CallbackContext) -> int:
    global dog
    global quinaTask
    global intentos2
    dog = breedExists(update.message.text)
    if checkBlacklist(update.message.text, update) == -1: return ConversationHandler.END
    logger.info("%s: %s", update.message.from_user.first_name, update.message.text)
    if dog == None:
        if intentos2 > 0:
            intentos2 -= 1
            update.message.reply_text(random.choice(FALLBACKS) + 'Can you tell me the breed of the dog? (Complete name)')
            return BREED
        else: 
            update.message.reply_text("I have not found this breed. Let's start again.")
            update.message.reply_text("What can I do for you?")
            intentos2 = 2
            quinaTask = ''
            return TASK
    else:
        update.message.reply_text('Collecting information about ' + dog.name + "...")
        info(update)
        update.message.reply_text("What else can I do for you?")
        return TASK

def dato(update: Update, _: CallbackContext) -> int:
    global intentos2
    global dog
    global quinaTask
    hhTask = False
    text = clean_text(update.message.text)
    if checkBlacklist(update.message.text, update) == -1: return ConversationHandler.END
    logger.info("%s: %s", update.message.from_user.first_name, update.message.text)
    for word in text:
        if word in verbs:
            for verb in verbs[word]:
                if verb in text:
                    update.message.reply_text('What do you want a dog for (companion, guardian...)?')
                    return FINALIDAD
        elif word in tasks:
            quinaTask = word
            hhTask = True
        elif word == "all" or word == "everything":
            update.message.reply_text("This is everything I have found about " + dog.name + ":")
            update.message.reply_text("Bred for: " + dog.bredFor)
            update.message.reply_text("Height: " + str(dog.height) + " cm")
            update.message.reply_text("Weight: " + str(dog.weight) + " kg")
            update.message.reply_text("Temperament: " + ' '.join(dog.temperament))
            update.message.reply_text(dog.image)
            update.message.reply_text("What else can I do for you?")
            dog = None
            return TASK
    if hhTask:
        info(update)
        update.message.reply_text("What else can I do for you?")
        return TASK
    else: 
        if intentos2 > 0:
            intentos2 -= 1
            update.message.reply_text(random.choice(FALLBACKS) + 'What do you want to know about ' + dog.name +  ' (image, weight, temperament...)')
            return DATO
        else: 
            update.message.reply_text("I don't understand you. This is everything I have found about " + dog.name + ":")
            update.message.reply_text("Bred for: " + dog.bredFor)
            update.message.reply_text("Height: " + str(dog.height) + " cm")
            update.message.reply_text("Weight: " + str(dog.weight) + " kg")
            update.message.reply_text("Temperament: " + ' '.join(dog.temperament))
            update.message.reply_text(dog.image)
            update.message.reply_text("What else can I do for you?")
            intentos2 = 2
            dog = None
            return TASK

def info(update: Update):
    global dog
    global quinaTask
    for i in tasks[quinaTask]:
        if i == "temperament":
            update.message.reply_text(dog.name + " are " + ' '.join(getattr(dog,i)))
        elif i == "weight":
            update.message.reply_text("The " + i + " of " + dog.name + ": " + str(getattr(dog,i)) + " kg")
        elif i == "height":
            update.message.reply_text("The " + i + " of " + dog.name + ": " + str(getattr(dog,i)) + " cm")
        else:
            update.message.reply_text("The " + i + " of " + dog.name + ": " + str(getattr(dog,i)))
        

def finalidad(update: Update, _: CallbackContext) -> int:
    global intentos
    wordExists = False
    finalidad = ''
    text = clean_text(update.message.text)
    if checkBlacklist(update.message.text, update) == -1: return ConversationHandler.END
    synsCompanion = getSynonyms('company')
    synsGuardian = getSynonyms('guardian')
    synsHunt = getSynonyms('hunt')
    synsDisability = getSynonyms('disability')
    while not bucle:
        for word in text:
            if word in synsCompanion:
                finalidad = 'company'
                wordExists = True
            elif word in synsGuardian:
                finalidad = 'guardian'
                wordExists = True
            elif word in synsHunt:
                finalidad = 'hunt'
                wordExists = True
            elif word in synsDisability:
                wordExists = True
                finalidad = 'disability'
            if word in dog_for:
                wordExists = True
                finalidad = word
        logger.info("%s: %s", update.message.from_user.first_name, update.message.text)
        if finalidad == 'disability':
            persona.set_discapacidad(True)
        if wordExists:
            intentos = 1
            break
        if intentos > 0:
            intentos -= 1
            update.message.reply_text(random.choice(FALLBACKS) + " What do you want a dog for?")
            return FINALIDAD
        else:
            intentos = 1
            update.message.reply_text("Sorry I still don't understand you, I will apply a filter by default.")
            break
    persona.set_finalidad(finalidad)
    update.message.reply_text('Do you care about the dog care time?')

    return CUIDADOS

def cuidados(update: Update, _: CallbackContext) -> int:
    if finishedQuestions(update) == -1:
        printDades(update)
        update.message.reply_text("What else can I do for you?")
        return TASK 
    cuidados = update.message.text
    update.message.reply_text('Are you looking for a dog that gets along with children?')

    return NIÑOS

def niños(update: Update, _: CallbackContext) -> int:
    if finishedQuestions(update) == -1:
        printDades(update)
        update.message.reply_text("What else can I do for you?")
        return TASK 
    global intentos
    wordExists = False
    niñosOk = False
    text = clean_text(update.message.text)
    if checkBlacklist(update.message.text, update) == -1: return ConversationHandler.END
    while not bucle:
        for word in text:
            if word in yesSyns or word in yes_words:
                niñosOk = True
                wordExists = True
            if word in noSyns or word in no_words:
                niñosOk = False
                wordExists = True
        logger.info("%s: %s", update.message.from_user.first_name, update.message.text)
        if wordExists:
            intentos = 1
            break
        if intentos > 0:
            intentos -= 1
            update.message.reply_text(random.choice(FALLBACKS) + " Do you want to get along with children?")
            return NIÑOS
        else:
            intentos = 1
            update.message.reply_text("Sorry I still don't understand you, I will apply a filter by default.")
            break
    persona.set_niños(niñosOk)
    update.message.reply_text('Do you want your dog to get along with other pets?')

    return MASCOTAS

def mascotas(update: Update, _: CallbackContext) -> int:
    if finishedQuestions(update) == -1:
        printDades(update)
        update.message.reply_text("What else can I do for you?")
        return TASK 
    global intentos
    wordExists = False
    mascotasOk = False
    text = clean_text(update.message.text)
    if checkBlacklist(update.message.text, update) == -1: return ConversationHandler.END
    while not bucle:
        for word in text:
            if word in yesSyns or word in yes_words:
                mascotasOk = True
                wordExists = True
                break
            if word in noSyns or word in no_words:
                mascotasOk = False
                wordExists = True
                break
        logger.info("%s: %s", update.message.from_user.first_name, update.message.text)
        if wordExists:
            intentos = 1
            break
        if intentos > 0:
            intentos -= 1
            update.message.reply_text(random.choice(FALLBACKS) + " Do you want to get along with pets?")
            return MASCOTAS
        else:
            intentos = 1
            update.message.reply_text("Sorry I still don't understand you, I will apply a filter by default.")
            break
    persona.set_mascotas(mascotasOk)
    update.message.reply_text('Do you have a size preference?')

    return TAMAÑO

def tamaño(update: Update, _: CallbackContext) -> int:
    if finishedQuestions(update) == -1:
        printDades(update)
        update.message.reply_text("What else can I do for you?")
        return TASK 
    preferencia = False
    tamaño = ""
    wordExists = False
    tamañoOk = False
    global intentos
    text = clean_text(update.message.text)
    if checkBlacklist(update.message.text, update) == -1: return ConversationHandler.END
    while not bucle:
        for word in text:
            if word in synsS:
                wordExists = True
                tamañoOk = True
                tamaño = "S"
                break
            elif word in synsM:
                wordExists = True
                tamañoOk = True
                tamaño = "M"
                break
            elif word in synsL:
                wordExists = True
                tamañoOk = True
                tamaño = "L"
                break
            if word in yesSyns or word in yes_words:
                preferencia = True
                wordExists = True
            if word in noSyns or word in no_words:
                preferencia = False
                wordExists = True
        logger.info("%s: %s", update.message.from_user.first_name, update.message.text)
        if wordExists:
            intentos = 1
            break
        if intentos > 0:
            intentos -= 1
            update.message.reply_text(random.choice(FALLBACKS) + " Do you have a size preference?")
            return TAMAÑO
        else:
            intentos = 1
            update.message.reply_text("Sorry I still don't understand you, I will apply a filter by default.")
            break
    if tamañoOk:
        persona.set_tamaño(tamaño)
        update.message.reply_text('How many hours do you spend away from home a day?')
        return HORARIO
    else:
        if preferencia:
            update.message.reply_text('What size would you like (small, large, medium)?')
            return PREFERENCIA
        else:
            update.message.reply_text('How many hours do you spend away from home a day?')
            return HORARIO

def preferencia(update: Update, _: CallbackContext) -> int:
    if finishedQuestions(update) == -1:
        printDades(update)
        update.message.reply_text("What else can I do for you?")
        return TASK 
    wordExists = False
    tamaño = ""
    global intentos
    text = clean_text(update.message.text)
    if checkBlacklist(update.message.text, update) == -1: return ConversationHandler.END
    while not bucle:
        for word in text:
            if word in synsS:
                wordExists = True
                tamaño = "S"
                break
            elif word in synsM:
                wordExists = True
                tamaño = "M"
                break
            elif word in synsL:
                wordExists = True
                tamaño = "L"
                break
        logger.info("%s: %s", update.message.from_user.first_name, update.message.text)
        if wordExists:
            intentos = 1
            break
        if intentos > 0:
            intentos -= 1
            update.message.reply_text(random.choice(FALLBACKS) + " What's your size preference?")
            return PREFERENCIA
        else:
            intentos = 1
            update.message.reply_text("Sorry I still don't understand you, I will apply a filter by default.")
            break
    persona.set_tamaño(tamaño)
    update.message.reply_text('How many hours do you spend away from home a day?')

    return HORARIO

def horario(update: Update, _: CallbackContext) -> int:
    if finishedQuestions(update) == -1:
        printDades(update)
        update.message.reply_text("What else can I do for you?")
        return TASK 
    wordExists = False
    global intentos
    horas = 0
    text = clean_text(update.message.text)
    if checkBlacklist(update.message.text, update) == -1: return ConversationHandler.END
    while not bucle:
        for word in text:
            if word.isnumeric():
                wordExists = True
                horas = word
                if int(word) < 0 or int(word) > 24:
                    wordExists = False
            else:
                if word in numbers:
                    horas = numbers[word]
                    wordExists = True
        logger.info("%s: %s", update.message.from_user.first_name, update.message.text)
        if wordExists:
            intentos = 1
            if int(horas) > 12:
                update.message.reply_text("GUAU! Sorry, it's many hours away from home.")
            break
        if intentos > 0:
            intentos -= 1
            update.message.reply_text(random.choice(FALLBACKS) + " How many hours do you spend away from home a day?")
            return HORARIO
        else:
            intentos = 1
            update.message.reply_text("Sorry I still don't understand you, I will apply a filter by default.")
            break
    persona.set_horas(horas)
    update.message.reply_text('Would you like to do sport with your dog?')

    return DEPORTE


def deporte(update: Update, _: CallbackContext) -> int:
    if finishedQuestions(update) == -1:
        printDades(update)
        update.message.reply_text("What else can I do for you?")
        return TASK 
    esDeportista = False
    wordExists = False
    global intentos
    text = clean_text(update.message.text)
    if checkBlacklist(update.message.text, update) == -1: return ConversationHandler.END
    while not bucle:
        for word in text:
            if word in yesSyns or word in yes_words:
                esDeportista = True
                wordExists = True
                break
            if word in noSyns or word in no_words:
                esDeportista = False
                wordExists = True
                break
            if word in freq_advs:
                esDeportista = freq_advs[word]
                wordExists = True
        logger.info("%s: %s", update.message.from_user.first_name, update.message.text)
        if wordExists:
            intentos = 1
            break
        if intentos > 0:
            intentos -= 1
            update.message.reply_text(random.choice(FALLBACKS) + " Would you like to do sport with your dog?")
            return DEPORTE
        else:
            intentos = 1
            update.message.reply_text("Sorry I still don't understand you, I will apply a filter by default.")
            break
    persona.set_deporte(esDeportista)
    if persona.get_discapacidad():
        update.message.reply_text("Do you live in a house or an apartment?")
        return VIVIENDA
    else: 
        update.message.reply_text('Do you suffer from any disability?')
        return DISCAPACIDAD


def discapacidad(update: Update, _: CallbackContext) -> int:
    if finishedQuestions(update) == -1:
        printDades(update)
        update.message.reply_text("What else can I do for you?")
        return TASK 
    wordExists = False
    esDiscapacitado = False
    global intentos
    text = clean_text(update.message.text)
    if checkBlacklist(update.message.text, update) == -1: return ConversationHandler.END
    while not bucle:
        for word in text:
            if word in yesSyns or word in yes_words:
                esDiscapacitado = True
                wordExists = True
                break
            if word in noSyns or word in no_words:
                esDiscapacitado = False
                wordExists = True
                break
        logger.info("%s: %s", update.message.from_user.first_name, update.message.text)
        if wordExists:
            intentos = 1
            break
        if intentos > 0:
            intentos -= 1
            update.message.reply_text(random.choice(FALLBACKS) + " Do you suffer from any disability?")
            return DISCAPACIDAD
        else:
            intentos = 1
            update.message.reply_text("Sorry I still don't understand you, I will apply a filter by default.")
            break
    persona.set_discapacidad(esDiscapacitado)   
    update.message.reply_text("Do you live in a house or an apartment?")
    return VIVIENDA

def vivienda(update: Update, _: CallbackContext) -> int:
    if finishedQuestions(update) == -1:
        printDades(update)
        update.message.reply_text("What else can I do for you?")
        return TASK 
    wordExists = False
    global intentos
    tipoHogar = ""
    text = clean_text(update.message.text)
    if checkBlacklist(update.message.text, update) == -1: return ConversationHandler.END
    synsHouse = getSynonyms("house")
    synsApartment = getSynonyms("apartment")
    while not bucle:
        for word in text:
            if word in synsHouse:
                tipoHogar = "house"
                wordExists = True
            elif word in synsApartment:
                tipoHogar = "apartment"
                wordExists = True
        logger.info("%s: %s", update.message.from_user.first_name, update.message.text)
        if wordExists:
            intentos = 1
            break
        if intentos > 0:
            intentos -= 1
            update.message.reply_text(random.choice(FALLBACKS) + " Do you live in a house or an apartment?")
            return VIVIENDA
        else:
            intentos = 1
            update.message.reply_text("Sorry I still don't understand you, I will apply a filter by default.")
            break    
    hogar.set_tipo(tipoHogar)
    persona.set_hogar(hogar)
    if "house" == hogar.get_tipo():
        update.message.reply_text("Do you have a garden in your house?")
    else:
        update.message.reply_text("Do you have a terrace on your apartment?")
    return ESPACIO
    
def espacio(update: Update, _: CallbackContext) -> int:
    if finishedQuestions(update) == -1:
        printDades(update)
        update.message.reply_text("What else can I do for you?")
        return TASK 
    wordExists = False
    jardin = False
    terraza = False
    global intentos
    if "house" == hogar.get_tipo():
        text = clean_text(update.message.text)
        if checkBlacklist(update.message.text, update) == -1: return ConversationHandler.END
        while not bucle:
            for word in text:
                if word in yesSyns or word in yes_words:
                    jardin = True
                    wordExists = True
                    break
                if word in noSyns or word in no_words:
                    jardin = False
                    wordExists = True
                    break
            logger.info("%s: %s", update.message.from_user.first_name, update.message.text)
            if wordExists:
                intentos = 1
                break
            if intentos > 0:
                intentos -= 1
                update.message.reply_text(random.choice(FALLBACKS) + " Do you have a garden in your house?")
                return ESPACIO
            else:
                intentos = 1
                update.message.reply_text("Sorry I still don't understand you, I will apply a filter by default.")
    else :
        text = clean_text(update.message.text)
        if checkBlacklist(update.message.text, update) == -1: return ConversationHandler.END
        while not bucle:
            for word in text:
                if word in yesSyns or word in yes_words:
                    terraza = True
                    wordExists = True
                    break
                if word in noSyns or word in no_words:
                    terraza = False
                    wordExists = True
                    break
            logger.info("%s: %s", update.message.from_user.first_name, update.message.text)
            if wordExists:
                intentos = 1
                break
            if intentos > 0:
                intentos -= 1
                update.message.reply_text(random.choice(FALLBACKS) + " Do you have a terrace on your flat?")
                return ESPACIO
            else:
                intentos = 1
                update.message.reply_text("Sorry I still don't understand you, I will apply a filter by default.")
    hogar.set_terraza(terraza)
    hogar.set_jardin(jardin)
    persona.set_hogar(hogar)
    update.message.reply_text("With what character would you define yourself?")
    return CARACTER

def caracter(update: Update, _: CallbackContext) -> int:
    if finishedQuestions(update) == -1:
        printDades(update)
        update.message.reply_text("What else can I do for you?")
        return TASK
    logger.info("%s: %s", update.message.from_user.first_name, update.message.text) 
    text = clean_text(update.message.text)
    if checkBlacklist(update.message.text, update) == -1: return ConversationHandler.END
    persona.set_caracter(text)
    print(persona)
    update.message.reply_text("Finding the ideal dog for you...")
    printDades(update)
    update.message.reply_text("What else can I do for you?")
    return TASK

def cancel(update: Update, _: CallbackContext) -> int:
    update.message.reply_text('Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def printDades(update: Update):
    global persona
    global hogar
    dog = recomendedDog(persona)
    persona = Persona()
    hogar = Hogar()
    update.message.reply_text(dog.name)
    update.message.reply_text("Height: " + str(dog.height) + " cm")
    update.message.reply_text("Weight: " + str(dog.weight) + " kg")
    update.message.reply_text("Temperament: " + ' '.join(dog.temperament))    
    update.message.reply_text(dog.image)

def finishedQuestions(update: Update) -> int:
    for terminate in FINISH:
        if terminate in update.message.text.lower():
            return -1


def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater('1755906349:AAH0dc_yEq3jlvwL7e9qiVLHmu-eJdpwDns')

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            STATUS: [MessageHandler(Filters.text & ~Filters.command, status)],
            TASK: [MessageHandler(Filters.text & ~Filters.command, task)],
            BREED: [MessageHandler(Filters.text & ~Filters.command, breed)],
            DATO: [MessageHandler(Filters.text & ~Filters.command, dato)],
            FINALIDAD: [MessageHandler(Filters.text & ~Filters.command, finalidad)],
            CUIDADOS: [MessageHandler(Filters.text & ~Filters.command, cuidados)],
            NIÑOS: [MessageHandler(Filters.text & ~Filters.command, niños)],
            MASCOTAS: [MessageHandler(Filters.text & ~Filters.command, mascotas)],
            TAMAÑO: [MessageHandler(Filters.text & ~Filters.command, tamaño)],
            PREFERENCIA: [MessageHandler(Filters.text & ~Filters.command, preferencia)],
            HORARIO: [MessageHandler(Filters.text & ~Filters.command, horario)],
            DEPORTE: [MessageHandler(Filters.text & ~Filters.command, deporte)],
            DISCAPACIDAD: [MessageHandler(Filters.text & ~Filters.command, discapacidad)],
            VIVIENDA: [MessageHandler(Filters.text & ~Filters.command, vivienda)],
            ESPACIO: [MessageHandler(Filters.text & ~Filters.command, espacio)],
            CARACTER: [MessageHandler(Filters.text & ~Filters.command, caracter)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()