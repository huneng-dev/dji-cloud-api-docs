<!-- source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/map-elements/delete.html -->
<!-- path: api-reference/pilot-to-cloud/https/map-elements/delete -->

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/map-elements/delete.html#%E5%88%A0%E9%99%A4%E5%85%83%E7%B4%A0) 删除元素
`DELETE /map/api/v1/workspaces/{workspace_id}/elements/{id}`
### Parameters  
| Name  | In  | Type  | Required  | Description  |  
| --- | --- | --- | --- | --- |  
| id  | path  | integer  | true  | 元素id  |  
| workspace_id  | path  | string  | true  | 工作空间id  |  
| x-auth-token  | header  | string  | true  | 访问令牌  |  
### Responses  
| Status  | Meaning  | Description  | Schema  |  
| --- | --- | --- | --- |  
| 200  | [OKopen in new window](https://tools.ietf.org/html/rfc7231#section-6.3.1)  | OK  | [map.SwagUUIDResp](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/map-elements/delete.html#schemamap.swaguuidresp)  |  
> Example responses
```
{
	"code":0
   	"data":{
    	"id":"94c51c50-f111-45e8-ac8c-4f96c93ced44"
    },
    "message": "success"
}
```
#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/map-elements/delete.html#schemas) Schemas
## map.SwagUUIDResp
```
{
  "code": 0,
  "data": {
    "id": "string"
  },
  "message": "string"
}
```
_Properties_  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| code  | integer  | true  | none  | 错误码  |  
| data  | [map.UUIDResp](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/map-elements/delete.html#schemamap.uuidresp)  | true  | none  | none  |  
| message  | string  | true  | none  | 错误描述  |  
## map.UUIDResp
```
{
  "id": "string"
}
```
_Properties_  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| id  | string  | true  | none  | 元素id  |