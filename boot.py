def ask_single_choice(question, options):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = int(input("Choose an option: ")) - 1
    return options[choice]

def ask_multiple_choice_with_follow_up(question, options, follow_up_questions):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choices = input("Choose options (separated by commas): ")
    selected_options = [options[int(choice) - 1] for choice in choices.split(',')]
    follow_up_answers = {}
    for option in selected_options:
        if option in follow_up_questions:
            follow_up_answers[option] = input(follow_up_questions[option] + " ")
    return follow_up_answers

def ask_open_input(question):
    return input(question + " ")

def main():
    project_name = ask_open_input("What is the name of your project?")
    project_purpose = ask_open_input("What is the purpose of your project?")

    code_status = ask_single_choice("This code is...", 
                                    ["Actively maintained", "Maintained", "Occasionally updated", "Not in active development"])

    contribution_status = ask_single_choice("We are _______ contributions at this time.", 
                                            ["Actively encouraging", "Currently accepting", "Not accepting"])

    if contribution_status == "Actively encouraging":
        contribution_from = ask_single_choice("From?", 
                                              ["Coders with experience", "The community in general", "Anyone interested in contributing"])
        skillset_needed = input("Are you looking for people with a particular skillset? (y/n) ")
        skillset = ask_open_input("We are particularly looking for contributors with experience in") if skillset_needed.lower() == 'y' else ""
    else:
        contribution_from = ""
        skillset = ""

    maintainers = ask_open_input("Who are the project's maintainers?")

    contact_methods_follow_up = {
        "Email": "What is their email address?",
        "Discord": "What is their Discord username?",
        "Twitter": "What is their Twitter handle?",
        "Facebook": "What is their Facebook profile?"
    }
    contact_methods = ask_multiple_choice_with_follow_up("How can they be contacted?", 
                                                         ["Email", "Through a pull request on Github", "Discord", "Twitter", "Facebook", "Other"],
                                                         contact_methods_follow_up)

    with open("contributing.md", "w") as file:
        file.write("Project Introduction:\n")
        file.write("---------------------\n")
        file.write(f"Project Name: {project_name}\n")
        file.write(f"Project Purpose: {project_purpose}\n")
        file.write(f"Code Status: {code_status}\n")
        file.write(f"Contribution Status: {contribution_status}\n")
        if contribution_status == "Actively encouraging":
            file.write(f"Seeking contributions from: {contribution_from}\n")
            if skillset:
                file.write(f"With skills in: {skillset}\n")
        file.write(f"Maintainers: {maintainers}\n")
        for method, detail in contact_methods.items():
            file.write(f"Contact Method: {method} - {detail}\n")

    print("contributing.md file has been created.")

if __name__ == "__main__":
    main()

