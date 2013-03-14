import plivo
import settings

p = plivo.RestAPI(settings.AUTH_ID, settings.AUTH_TOKEN)


# make an outbound call 
# and speak according to plivo_speak.xml 

params = {
'to': '',
'from': '',
'answer_url': ''
}
response = p.make_call(params)

