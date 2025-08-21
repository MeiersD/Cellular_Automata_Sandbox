class RulesBook:
    def __init__(self):
        self.rules = [[None for _ in range(4)] for _ in range(33)]

    def get_rules(self) -> list:
        print("Retrieving rules...")
        return self.rules
    
    def set_rules(self, new_rules: list):
        print("Setting new rules...")
        self.rules = new_rules