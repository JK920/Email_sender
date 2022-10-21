import csv
def contacts(filename):
    with open(filename) as file:
        contact = list(csv.DictReader(file))
        names = []
        emails = []
        jobs = []
        for d in contact:
            names.append(d['Name'])
            emails.append(d['E-mail'])
            jobs.append(d['Job'])
        return names,emails,jobs