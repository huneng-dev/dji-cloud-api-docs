<!-- source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/waypoint-management/waypointfile-upload-result-report.html -->
<!-- path: api-reference/pilot-to-cloud/https/waypoint-management/waypointfile-upload-result-report -->

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/waypoint-management/waypointfile-upload-result-report.html#%E4%B8%8A%E6%8A%A5%E8%88%AA%E7%BA%BF%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E7%BB%93%E6%9E%9C) 上报航线文件上传结果
`POST /wayline/api/v1/workspaces/{workspace_id}/upload-callback`
### Parameters  
| Name  | In  | Type  | Required  | Description  |  
| --- | --- | --- | --- | --- |  
| workspace_id  | path  | string  | true  | 工作空间id  |  
| x-auth-token  | header  | string  | true  | 访问令牌  |  
| body  | body  | [wayline.UploadCallbackInput](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/waypoint-management/waypointfile-upload-result-report.html#schemawayline.uploadcallbackinput)  | true  | body 参数  |  
### Responses  
| Status  | Meaning  | Description  | Schema  |  
| --- | --- | --- | --- |  
| 200  | [OKopen in new window](https://tools.ietf.org/html/rfc7231#section-6.3.1)  | OK  | [wayline.BaseResponse](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/waypoint-management/waypointfile-upload-result-report.html#schemawayline.baseresponse)  |  
> Example responses
```
{
	"code":0
   	"data": {},
    "message": "success"
}
```
#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/waypoint-management/waypointfile-upload-result-report.html#schemas) Schemas
## wayline.UploadCallbackInput
```
{
  "metadata": {
    "drone_model_key": "string",
    "payload_model_keys": [
      "string"
    ],
    "template_types": [
      0
    ]
  },
  "name": "string",
  "object_key": "string",
}
```
_Properties_  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| metadata  | [wayline.Metadata](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/waypoint-management/waypointfile-upload-result-report.html#schemawayline.metadata)  | false  | none  | 航线文件元数据  |  
| name  | string  | false  | none  | 文件名称  |  
| object_key  | string  | true  | none  | 文件在对象存储桶的key  |  
## wayline.Metadata
```
{
  "drone_model_key": "string",
  "payload_model_keys": [
    "string"
  ],
  "template_types": [
    0
  ]
}
```
_Properties_  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| drone_model_key  | string  | false  | none  | 飞机产品枚举值  |  
| payload_model_keys  | [string]  | false  | none  | 负载产品枚举值  |  
| template_types  | [integer]  | false  | none  | 航线模版类型集合  |