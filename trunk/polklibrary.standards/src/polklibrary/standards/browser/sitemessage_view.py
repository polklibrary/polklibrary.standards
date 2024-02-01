from plone import api
from plone.dexterity.browser import add
from plone.memoize import ram
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

import datetime, time, json, uuid

CACHED_TIME = 60

class SiteMessageView(BrowserView):

    template = ViewPageTemplateFile("sitemessage_view.pt")
   
    def __call__(self):
        return self.template()

    @property
    def portal(self):
        return api.portal.get()
        
        
        
class SiteMessageJS(BrowserView):

    template = ViewPageTemplateFile("sitemessage_js.pt")
    
    def __call__(self):
        self.request.response.setHeader('Content-Type', 'application/javascript')
        self.request.response.setHeader('Access-Control-Allow-Origin', '*')
        self.jdata = self.process()
        self.js_thread_name = 'smthread_' + self.request.form.get('name','nonameassigned');
        return self.template()
        
        
    @ram.cache(lambda *args: time.time() // (CACHED_TIME))
    def process(self):
        data = {
            'cached': str(datetime.datetime.now()),
            'cached_seconds': CACHED_TIME,
            'messages': [],
        }
        brains = api.content.find(portal_type='polklibrary.standards.models.site_messages', review_state="published")
        for brain in brains:
            data['messages'].append({
                'title': brain.Title,
                'url': brain.getURL(),
                'color': brain.message_color.lower(),
            })
        return json.dumps(data)
        
        
    @property
    def portal(self):
        return api.portal.get()
        