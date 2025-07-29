class Task:
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "✅ erledigt" if self.completed else "❌ offen"
        return f"[{self.id}] {self.title} - {status}\n   {self.description}"
