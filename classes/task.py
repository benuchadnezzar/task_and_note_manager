class Task:
    def __init__(self, name, start_date, due_date, priority, main_type, sub_type, responsible, hours):
        self.name = name
        self.start_date = start_date
        self.due_date = due_date
        self.priority = priority
        self.main_type = main_type
        self.responsible = responsible
        self.hours = hours
    
    def add_time(self, hours):
        pass

    def time_warning(self, hours):
        pass

    def priority_warning(self, priority):
        pass
    
    def add_to_tracker(self, name, start_date, due_date, priority, main_type, sub_type, responsible, hours):
        pass

    def add_to_asana(self, name, start_date, due_date, priority, main_type, sub_type, responsible, hours):
        pass

    def add_to_calendar(self, start_date, due_date, hours):
        pass
    
    def update_asana(self):
        pass

    def update_calendar(self):
        pass
    
    def cancel(self):
        pass