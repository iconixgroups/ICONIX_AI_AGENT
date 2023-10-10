class AgentTemplate:
    def __init__(self, name, description, tasks):
        self.name = name
        self.description = description
        self.tasks = tasks

agent_templates = [
    AgentTemplate("Customer Service", "Handles customer queries and issues", ["Respond to queries", "Resolve issues"]),
    AgentTemplate("FAQ", "Answers frequently asked questions", ["Answer questions"]),
    AgentTemplate("Lead Generation", "Generates and qualifies leads", ["Generate leads", "Qualify leads"]),
    AgentTemplate("Scheduling Assistance", "Helps schedule appointments and meetings", ["Schedule appointments", "Schedule meetings"]),
    AgentTemplate("Research Assistance", "Assists in conducting research", ["Conduct research"]),
    AgentTemplate("Advice", "Provides advice based on user input", ["Provide advice"]),
    AgentTemplate("Data Collection", "Collects and organizes data", ["Collect data", "Organize data"]),
    AgentTemplate("Personalized Recommendations", "Provides personalized recommendations", ["Provide recommendations"]),
    AgentTemplate("Write Code", "Writes code based on user input", ["Write code"]),
    AgentTemplate("Design UX", "Designs user experiences", ["Design user experiences"]),
    AgentTemplate("Design UI", "Designs user interfaces", ["Design user interfaces"])
]

def browse_template():
    for template in agent_templates:
        print(f"Name: {template.name}\nDescription: {template.description}\nTasks: {', '.join(template.tasks)}\n")

def select_template(template_name):
    for template in agent_templates:
        if template.name == template_name:
            return template
    return None