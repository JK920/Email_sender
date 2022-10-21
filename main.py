import contact
import content
import email_sender
sender = input('From: ')
password = input('Password: ')

names,emails,post = contact.contacts('jobs.csv')
for i in range(len(names)):
    email_sender.send(sender, password, emails[i], post[i], content.createContent(names[i], post[i]))
