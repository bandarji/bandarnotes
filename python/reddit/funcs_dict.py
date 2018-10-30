def hi_texan():
  return 'howdy'

def greeting(language='unknown'):
  funcs = {
    'punjabi': lambda: 'saat sri akal',
    'hindi': lambda: 'kaise ho aap',
    'texan': hi_texan,
    'english': lambda: 'hello',
    'spanish': lambda: 'hola',
    'chinese': lambda: 'ni hao',
  }
  return funcs.get(language.lower(), lambda: '[JUST WAVE AND SMILE]')()

for language in ('Punjabi', 'Hindi', 'Chinese', 'Vietnamese', 'Texan'):
  print('Greet someone in {}: "{}"'.format(language, greeting(language)))

# $ python yaml_dd.py 
# Greet someone in Punjabi: "saat sri akal"
# Greet someone in Hindi: "kaise ho aap"
# Greet someone in Chinese: "ni hao"
# Greet someone in Vietnamese: "[JUST WAVE AND SMILE]"
# Greet someone in Texan: "howdy"
