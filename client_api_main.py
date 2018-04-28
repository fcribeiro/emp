import swagger_client
from swagger_client.rest import ApiException

api = swagger_client.EmpServerApi()
api.api_client.configuration.host = "http://localhost:8080"

try:
    response = api.application_get_all_apps()
    print(response)
except ApiException as e:
    print("Exception: %s\n" % e)
