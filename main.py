from bs4 import BeautifulSoup
import json
import requests
from collections import OrderedDict

input_json='data/course_codes_to_links.json'
output_file='output.md'

course_codes_to_links = json.load(open(input_json), object_pairs_hook=OrderedDict)['course_codes_to_links']

with open(output_file,'w+') as output_fp:
	for i, (course_code, course_link) in enumerate(course_codes_to_links.items()):
		print(f'[INFO] Course #{i+1} with code "{course_code}" is being written to "{output_file}"..')

		html_text = requests.post(course_link, data={'_lang':'en_us'}).text
		soup = BeautifulSoup(html_text, 'html.parser')

		parsed_course_code=soup.find('tr', id='courseshortinfo').findChildren()[2].text.strip()
		course_title=soup.find('tr', id='courseshortinfo').find(id='title').text.strip()
		course_objectives=str(soup.find('tr', class_="textcontent odd"))[58:-10].strip()
		course_content=str(soup.find('tr', class_='textcontent even'))[56:-10].strip()

		course_learning_outcomes_list=[]
		for i,list_item in enumerate(soup.find('div', id='learningoutcomes').findChildren()[1].find_all('li')):
			course_learning_outcomes_list.append(f"{i+1}. {list_item.text.strip()}")
		course_learning_outcomes = '\n'.join(course_learning_outcomes_list)
		
		output_fp.write((f'**Course Code:** "{parsed_course_code}"\n\n'))
		output_fp.write((f'**Course Title:** "{course_title}"\n\n'))
		output_fp.write((f'**Course Objectives:**\n{course_objectives}\n\n'))
		output_fp.write((f'**Course Content:**\n{course_content}\n\n'))
		output_fp.write((f'**Course Learning Outcomes:**\n{course_learning_outcomes}\n\n'))
		output_fp.write(('-'*40 + '\n\n'))
