# swagger_client.EmpServerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_change_app_state**](EmpServerApi.md#application_change_app_state) | **PATCH** /app/{app_id} | Changes an application state
[**application_delete_app**](EmpServerApi.md#application_delete_app) | **DELETE** /app/{app_id} | Removes an application from the platform
[**application_deploy_app**](EmpServerApi.md#application_deploy_app) | **POST** /app | Deploys an application in the platform
[**application_get_all_apps**](EmpServerApi.md#application_get_all_apps) | **GET** /app | Gets general information about all applications
[**application_get_app**](EmpServerApi.md#application_get_app) | **GET** /app/{app_id} | Gets all information about a specific application
[**application_get_app_tracing**](EmpServerApi.md#application_get_app_tracing) | **GET** /app/tracing/{app_id} | Gets information about tracing of a specific application
[**application_hello_world**](EmpServerApi.md#application_hello_world) | **GET** / | EMP Working!


# **application_change_app_state**
> AppInfo application_change_app_state(app_id, state)

Changes an application state

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmpServerApi()
app_id = 789 # int | ID of the application to change its state
state = swagger_client.AppState() # AppState | Parameters that will change the state of the application

try:
    # Changes an application state
    api_response = api_instance.application_change_app_state(app_id, state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmpServerApi->application_change_app_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**| ID of the application to change its state | 
 **state** | [**AppState**](AppState.md)| Parameters that will change the state of the application | 

### Return type

[**AppInfo**](AppInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_delete_app**
> AppInfo application_delete_app(app_id)

Removes an application from the platform

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmpServerApi()
app_id = 789 # int | ID of the application to remove

try:
    # Removes an application from the platform
    api_response = api_instance.application_delete_app(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmpServerApi->application_delete_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**| ID of the application to remove | 

### Return type

[**AppInfo**](AppInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_deploy_app**
> AppTotalInfo application_deploy_app(deploy)

Deploys an application in the platform

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmpServerApi()
deploy = swagger_client.AppDeploy() # AppDeploy | Application object to be deployed

try:
    # Deploys an application in the platform
    api_response = api_instance.application_deploy_app(deploy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmpServerApi->application_deploy_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deploy** | [**AppDeploy**](AppDeploy.md)| Application object to be deployed | 

### Return type

[**AppTotalInfo**](AppTotalInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_get_all_apps**
> ArrayOfApps application_get_all_apps()

Gets general information about all applications

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmpServerApi()

try:
    # Gets general information about all applications
    api_response = api_instance.application_get_all_apps()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmpServerApi->application_get_all_apps: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ArrayOfApps**](ArrayOfApps.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_get_app**
> AppTotalInfo application_get_app(app_id)

Gets all information about a specific application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmpServerApi()
app_id = 789 # int | ID of the application to get information

try:
    # Gets all information about a specific application
    api_response = api_instance.application_get_app(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmpServerApi->application_get_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**| ID of the application to get information | 

### Return type

[**AppTotalInfo**](AppTotalInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_get_app_tracing**
> str application_get_app_tracing(app_id)

Gets information about tracing of a specific application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmpServerApi()
app_id = 789 # int | ID of the application

try:
    # Gets information about tracing of a specific application
    api_response = api_instance.application_get_app_tracing(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmpServerApi->application_get_app_tracing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**| ID of the application | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_hello_world**
> application_hello_world()

EMP Working!

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmpServerApi()

try:
    # EMP Working!
    api_instance.application_hello_world()
except ApiException as e:
    print("Exception when calling EmpServerApi->application_hello_world: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

