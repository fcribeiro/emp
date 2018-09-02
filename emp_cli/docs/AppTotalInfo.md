# AppTotalInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The application ID. | 
**name** | **str** | Name of the deployed application | 
**state** | **str** | Current state of the application | 
**docker_image** | **str** | Name of the docker image | 
**envs** | [**list[EnvironmentVariables]**](EnvironmentVariables.md) |  | 
**stateless** | **bool** | Stateless apps use true, stateful use false. | 
**quality_metrics** | [**list[QualityMetrics]**](QualityMetrics.md) |  | 
**port** | **int** | Port number of the application | 
**replicas** | **int** | Number of replicas of an application | 
**external_ip** | **str** | External IP of the application | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


