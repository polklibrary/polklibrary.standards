from plone import api
from plone.dexterity.browser import add
from plone.memoize import ram
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

import datetime, time, json, uuid

class UserCheckView(BrowserView):

   
    def __call__(self):
        output = ""
        output += "Checking Input: " + self.request.get('netid','abcdefg').lower()
        users = api.user.get_users()
        user = api.user.get(username=self.request.get('netid','abcdefg').lower().replace('@uwosh.edu',''))

        try:
            output += "\n    User NetID: " + str(user.getProperty('login'))
        except:
            pass
        try:
            output += "\n    User Name: " + str(user.getProperty('displayname'))
        except:
            pass
        try:
            output += "\n    User Card Number: " + str(user.getProperty('uwoshkoshlibraryid'))
        except:
            output += "\n    User Card Number: missing"


        return output

        
        
    @property
    def portal(self):
        return api.portal.get()
        
