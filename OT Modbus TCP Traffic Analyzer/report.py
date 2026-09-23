REPORT = None

def set_report(file):
    global REPORT
    REPORT = file

def write(text=""):              
    if REPORT:
       REPORT.write(text + "\n")
