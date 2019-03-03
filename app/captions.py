import random

captions = {
    'the Golden Gate Bridge': [
        'I tried to catch some fog at the bridge.  I mist.<br>#sorrykarl #wittytourist',
        '"We build too many walls and not enough bridges.” -Sir Isaac Newton<br>#wellread #wittytourist',
        'I’ve mist you, GGB!<br>#goldengatebridge #wittytourist'
    ],
    'the Oakland Bay Bridge': [
        '“When the lights go down in the Cityyyy…And the sun shines on the bay…”<br>#lifeisaJOURNEY #wittytourist',
        'check out my bae<br>#wittytourist',
        '"All the boys say...hey bay bay, hey bay bay, hey" -Gwen Stefani👩‍🎤🎤🎵<br>#wittytourist',
        'saltbay🧂🔪🥩<br>#wittytourist',
        'I cannot Bay bothered adulting right now<br>#wittytourist'
    ],
    'a cable car': [
        'The cable car was moving too slow so Simba yelled, MUFASA!!🚋"<br>#wittytourist"'
    ],
    'Lombard Street': [
        '"I haven\'t lived my life on the straight and narrow...but people still LOVE me 🤷‍” -Lombard Street<br>#wittytourist',
        '"I haven\'t lived my life on the straight and narrow...and I\'m world famous. 🎤⬇️” -Lombard Street<br>#wittytourist',
        'time to get turnt ↩️↪️<br>#crookedstreet #wittytourist'
    ],
    'Alcatraz': [
        'This place ROCKS!<br>#alcatraz #wittytourist',
        'What do you think of this cellfie?<br>#alcatraz #wittytourist',
        'How did this picture end up on Alcatraz? It was framed!😂🚓<br>#sorrynotsorry #badpun #wittytourist"'
    ],
    'the Painted Ladies at Alamo Square': [
        '"Didn’t see the milkman, the paperboy, or evening tv..."<br>#fullhousehouse #yougotitdude #wittytourist',
        'CUT, IT, OUT<br>✂️👉🙅‍♂️<br>#fullhousehouse #unclejoey #yougotitdude #wittytourist',
    ],
    'the Palace of Fine Arts': [
        "Be thine own palace, or the world's thy jail.<br>#wittytourist",
        "The Palace of Fine ARTS always draws a crowd, it's a masterpiece<br>#wittytourist"
    ],
    'the sea lions at Pier 39': [
        'Does this get your seal of approval?<br>#wittytourist',
        'Signed, Sealed, Delivered 💌<br>#wittytourist',
    ],
    'the Transamerica Pyramid': [
        'If the Transamerica Pyramid had never been built, SF’s skyline would be pointless<br>#wittytourist',
        '🤷‍♂️ What\'s the point 🙃<br>#wittytourist',
    ],
    'Muir Woods': [
        '"If you don\'t like where you are, move...you are not a tree.”  -Probably John Muir<br>#natureporn #wittytourist',
        '"These redwoods! What a TREEt”<br>#natureporn #wittytourist',
        '"reTREEt from the real world!”<br>#natureporn #wittytourist',
        'Take it or leaf it, these redwoods are giant!"<br>#natureporn #wittytourist'
    ],
    'Ghirardelli Square': [
        'Choc it out!🍫🍦<br>#ghirardellisquare #wittytourist'
    ],
    'Coit Tower': [
        'I ❤️ SF!  It\'s so Coit!<br>#coittower #wittytourist',
        'I see you Bay!  Don\'t be Coit with me 🙈🌉<br>#coittower #wittytourist'
    ],
    'Fisherman\'s Wharf': [
        'Anyone got a good fishing pun? Let minnow...🐟🌉<br>#wittytourist',
        'Rope puns are knot for everyone...I literally can knot<br>#wittytourist'
    ]
}

intros = [
    "🔥 BOOM Shakalaka 🔥",
    "💯 Boo-yah! 💯",
    "☀️💪🏻 Sun's out, guns out ☀️💪🏻",
    "🎱 Outlook good 🎱",
    "🧞✨ Shazaaam! ✨🧞",
    "🍔 McLovin' it! 🍔",
    "📺 Schwingggg! 📺",
    "🍻 Dilly! Dilly! 🍻",
    "🍑 Time to Break the Internet 🍑",
    "✅ YAAAAS ✅"
]

def witty_finder(prediction: str) -> str:
    return random.choice(captions[str(prediction)])
    
def witty_intro():
    return random.choice(intros)