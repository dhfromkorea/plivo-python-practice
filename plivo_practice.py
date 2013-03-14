import plivo
import settings

p = plivo.RestAPI(auth_id, auth_token)

# make an outbound call 
# and speak according to plivo_speak.xml 

params = {
'to': '',
'from': '',
'answer_url': ''
}
response = p.make_call(params)

