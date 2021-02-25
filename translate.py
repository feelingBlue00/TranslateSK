from googletrans import Translator

translator = Translator()
translation = translator.translate('veritas lux mea', src='la')

print(translation.text)

