import urllib.request, json
import trello_to_txt.config
import operator

def main():
	bytes = urllib.request.urlopen(trello_to_txt.config.board_url + '?key=' + trello_to_txt.config.dev_key + '&token=' + trello_to_txt.config.token + '&cards=open&lists=open').read()
	trello_data = json.loads(bytes.decode('utf-8'))
	output_text = ''

	for l in sorted(trello_data['lists'], key=operator.itemgetter('pos')):
		output_text += '# ' + l['name'] + '\n\n'
		for card in sorted((card for card in trello_data['cards'] if card['idList'] == l['id']), key=operator.itemgetter('pos')):
			output_text += '* {0} ({1})\n'.format(card['name'], ', '.join((label['name'] for label in card['labels'])))
		output_text += '\n'

	print(output_text)