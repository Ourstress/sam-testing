import os
import yaml

def getIndexPage():

    # Read index.html
    with open("/var/task/index.html", encoding="utf8") as file:
        webpage = file.read()

    # Read problems.yaml
    with open("/var/task/problems.yaml") as stream:
        document = yaml.safe_load(stream)
    
    # Define template component to fill up with yaml contents
    templateComponent = """
    {
        name: "question $$INDEX$$", layoutItems: [
            { vModel: "$$SHOWN$$" },
            { vModel: "$$EDITABLE$$" },
            { vModel: "$$HIDDEN$$" },
            { vModel: "$$INTRODUCTION$$" }
        ], status: " 🔴"
    }
    """
    replacedContent = ("$$INDEX$$","$$SHOWN$$","$$EDITABLE$$","$$HIDDEN$$", "$$INTRODUCTION$$")

    # Methods to replace template component with yaml contents
    def escapeNewLine(string):
        return string.replace("\n", "\\n")
    
    def replaceWithYaml(document):
        component = ""
        for index,problem in enumerate(document["Problems"]):
            location = document["Problems"][problem] 
            replacementContent = (str(index + 1), escapeNewLine(location["Tests"]), escapeNewLine(location["Editable"]), escapeNewLine(location["Hidden"]), escapeNewLine(location["Introduction"]) )
            interimComponent = templateComponent
            for check, rep in zip(replacedContent, replacementContent):
                interimComponent = interimComponent.replace(check, rep)
            component += interimComponent + ","
        return(component)[:-1]
        
    # make the replacement on index.html
    webpage = webpage.replace('"$$TOBEREPLACEDBYYAML$$"', replaceWithYaml(document))
    
    return webpage