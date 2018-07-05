# AppDeploy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the application to be deployed | 
**docker_image** | **str** | Name of the docker image | 
**envs** | [**list[EnvironmentVariables]**](EnvironmentVariables.md) |  | 
**stateless** | **bool** | For stateless apps use true, stateful use false. | 
**port** | **int** | Port number of the application | 
**quality_metrics** | [**list[QualityMetrics]**](QualityMetrics.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


