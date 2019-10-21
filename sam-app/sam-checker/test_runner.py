import os
import json
import yaml


def store_content(shownCode, editedCode):
    # app.py            - shownCode
    # template.yaml     - editedCode
    os.popen("mkdir -p /tmp/myProject").read()
    with open('/tmp/myProject/template.yaml', 'w') as outFile:
        outFile.write(editedCode)
    with open('/tmp/myProject/app.py', 'w') as outFile:
        outFile.write(shownCode)


def execute():
    result = "Empty"
    with open('/tmp/myProject/template.yaml', 'r') as inFile:
        data_loaded = yaml.safe_load(inFile)
        result = data_loaded

    # Form the response
    results = {
        "isComplete": True,
        "htmlFeedback": result,
        "jsonFeedback": result,
        "textFeedback": result
    }

    return json.dumps(results)
