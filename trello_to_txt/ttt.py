import urllib.request, json
import trello_to_txt.config

def main():
	bytes = urllib.request.urlopen(trello_to_txt.config.board_url + '?key=' + trello_to_txt.config.dev_key + '&token=' + trello_to_txt.config.token + '&cards=open&lists=open').read()
	trello_data = json.loads(bytes.decode('utf-8'))
	output_data = {}
	trello_list_names = {}
	trello_list_positions = {}
	trello_card_positions = {}
	output_text = ''

	for l in trello_data['lists']:
		output_data[l['name']] = []
		trello_list_names[l['id']] = l['name']
		trello_list_positions[l['name']] = int(l['pos'])

	for c in trello_data['cards']:
		output_data[trello_list_names[c['idList']]].append(c['name'])
		trello_card_positions[c['name']] = int(c['pos'])

	for list_name in sorted(output_data.keys(), key=trello_list_positions.get):
		output_text += '# ' + list_name + '\n\n'
		for card_name in sorted(output_data[list_name], key=trello_card_positions.get):
			output_text += '* ' + card_name + '\n'
		output_text += '\n'

	print(output_text)