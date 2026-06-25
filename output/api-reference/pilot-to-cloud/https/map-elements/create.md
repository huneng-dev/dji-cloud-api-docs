---
source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/map-elements/create.html
path: api-reference/pilot-to-cloud/https/map-elements/create
---

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/map-elements/create.html#%E5%88%9B%E5%BB%BA%E5%85%83%E7%B4%A0) 创建元素
`POST /map/api/v1/workspaces/{workspace_id}/element-groups/{group_id}/elements`
### Parameters  
| Name  | In  | Type  | Required  | Description  |  
| --- | --- | --- | --- | --- |  
| group_id  | path  | string  | true  | 元素组id  |  
| workspace_id  | path  | string  | true  | 工作空间id  |  
| x-auth-token  | header  | string  | true  | 访问令牌  |  
| body param  | body  | [map.ElementCreateInput](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/map-elements/create.html#schemamap.elementcreateinput)  | true  | body参数  |  
### Responses  
| Status  | Meaning  | Description  | Schema  |  
| --- | --- | --- | --- |  
| 200  | [OKopen in new window](https://tools.ietf.org/html/rfc7231#section-6.3.1)  | OK  | [map.SwagUUIDResp](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/map-elements/create.html#schemamap.swaguuidresp)  |  
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
#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/map-elements/create.html#schemas) Schemas
## map.ElementCreateInput
```
{
  "id": "string",
  "name": "string",
  "resource": {
    "content": {
      "geometry": {
        "coordinates": [
          null
        ],
        "type": "text"
      },
      "properties": {
        "clampToGround": true,
        "color": "string"
      },
      "type": "text"
    },
    "type": 0
  }
}
```
_Properties_  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| id  | string  | true  | none  | 元素id  |  
| name  | string  | true  | none  | 元素名称  |  
| resource  | [map.ResourceItem](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/map-elements/create.html#schemamap.resourceitem)  | true  | none  | 资源对象  |  
## map.ResourceItem
```
{
  "content": {
    "geometry": {
      "coordinates": [
        null
      ],
      "type": "text"
    },
    "properties": {
      "clampToGround": true,
      "color": "string"
    },
    "type": "text"
  },
  "type": 0
}
```
_Properties_  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| content  | [map.Content](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/map-elements/create.html#schemamap.content)  | false  | none  | 资源内容对象  |  
| type  | integer  | false  | none  | 资源类型  
* 0 - pin点  
* 1 - 线  
* 2 - 面  |  
## map.Content
```
{
  "geometry": {
    "coordinates": [
      null
    ],
    "type": "text"
  },
  "properties": {
    "clampToGround": true,
    "is3d": false,
    "color": "string"
  },
  "type": "text"
}
```
_Properties_  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| geometry  | object  | false  | none  | geojson属性  |  
| » coordinates  | [any]  | false  | none  | geojson属性  |  
| » type  | string  | false  | none  | geojson属性  |  
| properties  | object  | false  | none  | geojson属性  |  
| » clampToGround  | boolean  | false  | none  | 是否贴地  |  
| » is3d  | boolean  | false  | none  | 是否为空间线面  |  
| » color  | string  | false  | none  | 支持的元素颜色  
* BLUE：0x2D8CF0  
* GREEN - 0x19BE6B  
* YELLOW - 0xFFBB00  
* ORANGE - 0xB620E0  
* RED - 0xE23C39  
* PURPLE - 0x212121  |  
| type  | string  | false  | none  | geojson属性  |  
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
| data  | [map.UUIDResp](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/map-elements/create.html#schemamap.uuidresp)  | true  | none  | none  |  
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