from plone import api
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema
from zope.interface import directlyProvides
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

message_colors = SimpleVocabulary([
    SimpleTerm(value=u'Blue', title=u'Blue'),
    SimpleTerm(value=u'Green', title=u'Green'),
    SimpleTerm(value=u'Orange', title=u'Orange'),
    SimpleTerm(value=u'Red', title=u'Red'),
])

class ISiteMessage(model.Schema):

    title = schema.TextLine(
            title=u"Message Title",
            required=True,
        )
        
    body = RichText(
            title=u"Message Information",
            default_mime_type='text/structured',
            required=False,
            default=u"",
        )
        
    message_color = schema.Choice(
            title=u"Message Color",
            source=message_colors,
            default=u"Orange",
            required=False,
        )   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        