#obsluguje sigma rules
#wczytuje rule i nastepnie przekazuje je do skanera
#obsluga bledow ze sciezka itp
#REG.DET.1
#REG.DET.1.2

def read_rules_from_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def parse_rules(rules_string):
    return sigmac.parse(rules_string)

def execute_rules(parsed_rules, event_data):
    results = []
    for rule in parsed_rules:
        result = rule.execute(event=event_data)
        results.append(result)
    return results

def handle_rules(file_path, event_data):
    rules_string = read_rules_from_file(file_path)
    parsed_rules = parse_rules(rules_string)
    results = execute_rules(parsed_rules, event_data)
    return results
