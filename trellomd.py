import urllib.request, json
import configparser
import operator

config = configparser.ConfigParser()
config.read_file(open('trellomd.cfg'))

bytes = urllib.request.urlopen(config['config']['board_url'] + '?key=' + config['config']['dev_key'] + '&token=' + config['config']['token'] + '&cards=open&lists=open').read()
trello_data = json.loads(bytes.decode('utf-8'))
output_text = ''

for l in sorted(trello_data['lists'], key=operator.itemgetter('pos')):
	output_text += '# ' + l['name'] + '\n\n'
	for card in sorted((card for card in trello_data['cards'] if card['idList'] == l['id']), key=operator.itemgetter('pos')):
		if not card['labels']:
			output_text += '* {0}\n'.format(card['name'])
		else:
			output_text += '* {0} ({1})\n'.format(card['name'], ', '.join((label['name'] for label in card['labels'])))
	output_text += '\n'

print(output_text)