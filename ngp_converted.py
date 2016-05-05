import csv
import glob
from datetime import *

ngp_path = 'C:\Users/valued/Desktop/politech/ngp_converter/*.csv'
ngp_converted_file = 'C:\Users/valued/Desktop/politech/ngp_converter/ngp_converted_registration_import.csv'

converted_list = []

shift_id = 31415
created_by_user_id = 31415
form_number = ''
us_citizen = 't'
eligible_voting_age = 't'
signature = 't'
identification = 't'
created_at = str(datetime.now())
updated_at = str(datetime.now())
contacted_voter = 'f'

registration_forms = ['id',	
	'registration_type',
	'shift_id',
	'created_by_user_id',
	'form_number',	
	'first_name',
	'middle_name',
	'last_name',
	'name_suffix',
	'voting_street_address_one',
	'voting_street_address_two',
	'voting_city',
	'voting_state',	
	'voting_zipcode',
	'mailing_street_address_one',
	'mailing_street_address_two',
	'mailing_city',
	'mailing_zipcode',
	'county',	
	'precinct',
	'gender',
	'date_of_birth',
	'registration_date',
	'identification',
	'phone_number',
	'email_address',
	'us_citizen',
	'eligible_voting_age',
	'signature',
	'extras',
	'created_at',
	'updated_at',
	'contacted_voter',
	'score',
	'batch_id',
	'attempted',
	'party',
	'name_prefix',
	'ethnicity',
	'latitude',
	'longitude',
	'distance_from_location']

	
converted_list.append(registration_forms)

for files in glob.glob(ngp_path):
	with open(files, "rb") as ngpfile:
		sniffer = csv.reader(ngpfile,delimiter = ',')
		headers = sniffer.next()
		for line in sniffer:
			converted = ['','',shift_id,created_by_user_id,form_number,line[9],line[10],line[11],line[12],line[89],line[90],line[98],line[97],line[100],line[125],line[126],line[122],line[124],line[123],'',line[179],line[26],'',identification,line[37],line[27],us_citizen,eligible_voting_age,signature,'',created_at,updated_at,contacted_voter,'','','',line[18],line[18],line[21],'','','']
			converted_list.append(converted)
			print converted
			
with open(ngp_converted_file, "w+") as ngpconvertedfile:
	scribe = csv.writer(ngpconvertedfile, delimiter = ',', lineterminator = '\n')
	scribe.writerows(converted_list)
			
			
