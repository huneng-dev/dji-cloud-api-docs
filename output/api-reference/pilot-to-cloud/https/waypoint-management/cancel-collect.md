---
source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/waypoint-management/cancel-collect.html
path: api-reference/pilot-to-cloud/https/waypoint-management/cancel-collect
---

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/waypoint-management/cancel-collect.html#%E6%89%B9%E9%87%8F%E5%8F%96%E6%B6%88%E6%94%B6%E8%97%8F%E8%88%AA%E7%BA%BF%E6%96%87%E4%BB%B6) 批量取消收藏航线文件
`DELETE /wayline/api/v1/workspaces/{workspace_id}/favorites`
### Parameters  
| Name  | In  | Type  | Required  | Description  |  
| --- | --- | --- | --- | --- |  
| workspace_id  | path  | string  | true  | 工作空间id  |  
| id  | query  | array[string]  | false  | 航线文件id集合  |  
| x-auth-token  | header  | string  | true  | 访问令牌  |  
### Responses  
| Status  | Meaning  | Description  | Schema  |  
| --- | --- | --- | --- |  
| 200  | [OKopen in new window](https://tools.ietf.org/html/rfc7231#section-6.3.1)  | OK  | [wayline.BaseResponse](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/waypoint-management/cancel-collect.html#schemawayline.baseresponse)  |  
> Example responses
```
{
	"code":0
   	"data":{},
    "message": "success"
}
```
#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/waypoint-management/cancel-collect.html#schemas) Schemas
## wayline.BaseResponse
```
{
  "code": 0,
  "data": null,
  "message": "string"
}
```
_Properties_  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| code  | integer  | false  | none  | 错误码  |  
| data  | any  | false  | none  | none  |  
| message  | string  | false  | none  | 错误描述  |  
`DELETE /wayline/api/v1/workspaces/{workspace_id}/favorites`
### Parameters  
| Name  | In  | Type  | Required  | Description  |  
| --- | --- | --- | --- | --- |  
| workspace_id  | path  | string  | true  | 工作空间id  |  
| id  | query  | array[string]  | false  | 航线文件id集合  |  
| x-auth-token  | header  | string  | true  | 访问令牌  |  
### Responses  
| Status  | Meaning  | Description  | Schema  |  
| --- | --- | --- | --- |  
| 200  | [OKopen in new window](https://tools.ietf.org/html/rfc7231#section-6.3.1)  | OK  | [wayline.BaseResponse](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/waypoint-management/cancel-collect.html#schemawayline.baseresponse)  |  
> Example responses
```
{
	"code":0
   	"data":{},
    "message": "success"
}
```