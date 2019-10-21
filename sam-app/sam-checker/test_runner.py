import os
import json


def store_content(shownCode, editedCode):
    # app.py            - shownCode
    # template.yaml     - editedCode
    os.popen("mkdir -p /tmp/myProject").read()
    with open('/tmp/myProject/template.yaml', 'w') as outFile:
        outFile.write(editedCode)
    with open('/tmp/myProject/app.py', 'w') as outFile:
        outFile.write(shownCode)


def execute():

    # Get text feedback of unit test results
    runUnitTest = 'cd /tmp/myProject; python3 -m unittest -v app.py 2>&1'
    unitTestResults = os.popen(runUnitTest).read()

    # Get html feedback of unit test results
    command = "cd /tmp/myProject; python3 -m unittest -v app.py 2>&1 | \
                /var/task/ansi2html.sh > /tmp/myProject/unitTestResults.html"
    os.popen(command).read()
    htmlOutput = "<h2>Python unittest results</h2><br/>"
    htmlOutput += os.popen("cat /tmp/myProject/unitTestResults.html").read()

    # Get JSON feedback of unit test results
    command = "python3 -m pytest --json-report -v /tmp/myProject/app.py \
            --json-report-summary --json-report-file /tmp/myProject/unitTestResults.json"
    os.popen(command).read()
    jsonOutput = json.loads(
        os.popen("cat /tmp/myProject/unitTestResults.json").read())

    # Get isComplete
    if ("summary" in jsonOutput):
        if("failed" in jsonOutput["summary"]):
            isComplete = False
        elif(jsonOutput["summary"].get("total", 0) == jsonOutput["summary"].get("passed", 1)):
            isComplete = True
        else:
            isComplete = False
    else:
        isComplete = False

    # Form the response
    results = {
        "isComplete": isComplete,
        "htmlFeedback": htmlOutput,
        "jsonFeedback": jsonOutput,
        "textFeedback": unitTestResults
    }

    return json.dumps(results)
