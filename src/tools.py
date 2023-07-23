import googleanalytics as ga
import segment
import dialogflow_v2 as dialogflow
from zendesk import Zendesk

# Google Analytics
def useAnalyticsTool(user_id, event_name):
    account = ga.authenticate(user_id)
    property = account.properties[event_name]
    return property

# Segment
def integrateSegment(user_id, event_name):
    segment.identify(user_id=user_id, traits={'event': event_name})
    segment.track(user_id=user_id, event=event_name)

# Dialogflow
def integrateDialogflow(project_id, session_id, texts, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    for text in texts:
        text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        return response.query_result.fulfillment_text

# Zendesk
def integrateZendesk(user_id, event_name):
    zendesk = Zendesk(user_id, event_name)
    return zendesk
