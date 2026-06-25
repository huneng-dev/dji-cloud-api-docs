<!-- source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/waypoint-management/get-duplicated-waypointfile-name.html -->
<!-- path: api-reference/pilot-to-cloud/https/waypoint-management/get-duplicated-waypointfile-name -->

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/waypoint-management/get-duplicated-waypointfile-name.html#%E8%8E%B7%E5%8F%96%E9%87%8D%E5%A4%8D%E7%9A%84%E8%88%AA%E7%BA%BF%E6%96%87%E4%BB%B6%E5%90%8D%E7%A7%B0) 获取重复的航线文件名称
`GET /wayline/api/v1/workspaces/:workspace_id/waylines/duplicate-names`
### Parameters  
| Name  | In  | Type  | Required  | Description  |  
| --- | --- | --- | --- | --- |  
| workspace_id  | path  | string  | true  | 工作空间id  |  
| name  | query  | array[string]  | true  | 文件名称集合  |  
| x-auth-token  | header  | string  | true  | 访问令牌  |  
### Responses  
| Status  | Meaning  | Description  | Schema  |  
| --- | --- | --- | --- |  
| 200  | [OKopen in new window](https://tools.ietf.org/html/rfc7231#section-6.3.1)  | OK  | [wayline.GetDuplicateNamesOutput](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/waypoint-management/get-duplicated-waypointfile-name.html#schemawayline.getduplicatenamesoutput)  |  
> Example
```
{
    "code": 0,
    "message": "string",
    "data": ["name1", "name2"]
}
```
#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/waypoint-management/get-duplicated-waypointfile-name.html#schemas) Schemas
## wayline.GetDuplicateNamesOutput
```
{
  "code": 0,
  "data": [
    "string"
  ],
  "message": "string"
}
```
_Properties_  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| code  | integer  | false  | none  | 错误码  |  
| data  | array[string]  | false  | none  | 重复的文件名数组  |  
| message  | string  | false  | none  | 错误描述  |