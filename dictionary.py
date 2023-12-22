GREETING_RESPONSES = ["Hi,", "Hey,", "Hi there,", "Hello,", "I am glad! You are talking to me"]
RESPONSES_BLACKLIST = ["You are offending me", "Control your vocabulary", "Do not tell me that", "Try to be more educated"]

FALLBACKS = ["Sorry, what was that?","I haven't understood you.","Sorry, I didn't get that.","I don't understand you."]

QUESTIONS = ["what can you do","what can i ask","how can you help me", "what can we talk about", "what can i do"]

ENDS = ["nothing", "it's all", "i'm done", "it's finish"]

FINISH = ["i want to finish", "give me the breed", "show me my dog", "give me the race", "i want to see the result now", "ask me anymore"]

no_words = ['no', 'nope', 'nah', "n't", 'not', 'dont', 'doesnt']
yes_words = ['yes', 'yea', 'yeah', 'ok', 'okay', 'sure', 'fine', 'course']

tasks = {
    'temperament': ["temperament"],
    'weight': ["weight"], 
    'height': ["height"],
    'image': ["image"],
    'photo': ["image"],
    'size': ["weight", "height"],
    'picture': ["image"],
    'tall': ["height"],
    'long': ["weight"]
}

dog_for = {
    "company": ["companion","companionship","companionable","lapdog"],
    "guardian": ["guarding","guardian","guard","herding"],
    "protect": ["guarding","guardian","guard","herding"],
    "hunt" : ["hunting", "find", "kill", "hunt"],
    "disability": ["Golden Retriever", "Labrador Retriever", "Belgian Malinois", "Belgian Tervuren", "Alaskan Malamute"]
}

verbs = {
    "look": ["dog", "breed"],
    "choose": ["dog", "breed"],
    "find": ["dog", "breed"],
    "recommend": ["dog", "breed"],
    "know": ["dog", "breed"],
    "perfect": ["dog", "breed"],
}

verbs_ask = {
    "show": ["image", "pic", "photo"],
    "see": ["image", "pic", "photo"],
    "know": ["weight", "height", "size", "temperament"]
}


estado_animico = {
    "good": "I'm glad to hear that! :)",
    "bad": "Wow! Sorry to hear that :(",
    "great": "I'm glad to hear that! :)",
    "fatal": "Wow! Sorry to hear that :(",
    "regular": "Wow! There will be better days for sure.",
    "sad": "Wow! Sure there will be better days.",
    "happy": "I'm also able to talk to you!",
    "contented": "Me too to be able to talk to you!",
    "you": "Fine, thank you very much",
    "u": "Fine, thank you very much",
    "bored" : "I will try to cheer you up",
    "furious" : "Wow! Sorry to hear that :(",
    "scared" : "Wow! Sorry to hear that :(",
    "relaxed" : "I'm glad to hear that! :)",
    "angry" : "Wow! Sorry to hear that :(",
    "in love" : "I'm glad to hear that! :)",
    "fine" : "I'm glad to hear that! :)",
}

filtro = {
    "childrens": ["playful", 'bubbly', 'extroverted', 'diligent', 'opinionated', 'unflappable', 'boisterous', 'sturdy', 'merry', 'benevolent', 'respectful', 'people-oriented', 'sociable', 'familial', 'tolerant', 'companionable', 'easygoing', 'sensitive', 'adaptable', 'amiable', 'good-natured', 'reliable', 'sweet-tempered', 'kind', 'obedient', 'willed', "calm", "charming", "obedient", "affectionate", "friendly", "tolerant", 'fun-loving', 'happy', 'dutiful', 'outgoing', 'alert', 'courageous', 'docile', 'loving', 'protective', 'affectionate'],
    "disability": ["smart", 'clever', 'willful', 'thoughtful', 'unflappable', 'athletic', 'sturdy', 'trustworthy', 'merry', 'cooperative',  'cunning', 'vocal', 'people-oriented', 'tolerant', 'great-hearted', 'suspicious', 'powerful', 'keen', 'hard-working', 'trusting', 'agile', 'calm','companionable', 'steady', 'attentive', 'tenacious', 'kind', 'obedient', 'strong', "loyal", "trustworthy", "safe", "trainable", "faithful", 'clownish', 'happy', 'hardworking', 'dutiful', 'alert', 'confident', 'intelligent', 'courageous', 'docile', 'protective'],
    "pets": ["easygoing", 'bubbly', 'diligent', 'charming', 'extroverted', 'generous', 'unflappable', 'opinionated', 'boisterous', 'benevolent', 'respectful', 'merry', 'sociable', 'stable', 'gay', 'tolerant', 'bright', 'familial', 'lovable', 'sensitive', 'amiable', 'cheerful', 'joyful', 'determined', 'fierce', 'tempered', 'companionable', 'good-natured', 'self-assured', 'reliable', 'sweet-tempered', 'kind', "sociable", "cheerful", "friendly", 'playful', 'fun-loving', 'clownish', 'happy', 'confident', 'responsive', 'composed', 'loving'],
    "sports": ["athletic", 'clever', 'fast', 'athletic', 'unflappable', 'spunky', 'aggressive', 'cooperative', 'cunning', 'bossy', 'mischievous', 'patient', 'inquisitive', 'quick', 'powerful', 'rational', 'feisty', 'hardy','excitable', 'agile', 'adaptable', 'rugged', 'even', 'spirited', 'eager', 'lively', 'bold', 'tenacious', 'obedient', 'strong', "energetic", "active", 'stubborn', 'dominant', 'curious', 'playful', 'adventurous', 'active', 'fun-loving', 'wild', 'dutiful', 'intelligent', 'brave', 'docile', 'receptive', 'trainable', 'energetic'],
    "hours": ["independent", 'trustworthy', 'unflappable', 'vigilant', 'cat-like', 'respectful', 'self-important', 'patient', 'quiet', 'stable', 'rational', 'tolerant', 'territorial', 'trusting', 'hard-working', 'easygoing', 'adaptable', 'calm', 'watchful', 'good-tempered', 'refined', 'determined', 'tempered', 'self-confidence', 'cautious', 'self-assured', 'fearless','proud', 'steady', 'reserved', "docile",'assertive', "vigilant", "patient", "trustworthy", "calm", "tolerant", 'aloof', 'dignified', 'courageous', 'receptive', 'composed', 'responsible', 'devoted', 'gentle']
}

freq_advs =  {
    "always": True,
    "never": False,
    "frequently": True,
    "generally": True,
    "normally": True,
    "occasionally": False,
    "often": True,
    "regularly": True,
    "sometimes": True,
    "usually": True 
}

numbers = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven" : 11,
    "twelve" : 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nighteen": 19,
    "twenty": 20,
    "twenty-one": 21,
    "twenty-two": 22,
    "twenty-three": 23,
    "twenty-four": 24
}

blackList = ["fuck","dumb","crub","bastard","nigga","bitch","cunt","pussy","dick","asshole","stupid","badass","dickhead","idiot","cock","moderfucker","whore","jerk","dumbass"]