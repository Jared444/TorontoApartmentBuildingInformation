import json
from js import document

def search_address(*args):
    print("Search function called")
    user_input = document.getElementById("usersearch").value
    print(f"User input: {user_input}")
    with open("ApartmentRecords.json") as file:
        data = json.load(file)
        results = [item for item in data if user_input.lower() in item["SITE ADDRESS"].lower()]
        print(f"Results found: {results}")
        if results:
            display_results(results)
        else:
            display_results(["No results found."])

def display_results(results):
    result_container = document.getElementById("resultContainer")
    result_container.innerHTML = ""
    for result in results:
        result_container.innerHTML += f"<p>{result}</p>"
