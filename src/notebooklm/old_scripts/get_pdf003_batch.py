import json
data = json.load(open('02_LitRev_Sistematica/config/registry_parsed.json'))
for q in data['questions']:
    if q['question_id'].startswith('PDF003') and q['question_id'] <= 'PDF003_Q05':
        print(f"ID: {q['question_id']}")
        print(f"Text: {q['question_text']}")
        print(f"Tag: {q['tag']}")
        print("---")