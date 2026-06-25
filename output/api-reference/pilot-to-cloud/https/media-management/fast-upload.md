---
source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/fast-upload.html
path: api-reference/pilot-to-cloud/https/media-management/fast-upload
---

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/fast-upload.html#%E6%96%87%E4%BB%B6%E5%BF%AB%E4%BC%A0) 文件快传
`POST /media/api/v1/workspaces/{workspace_id}/fast-upload`
### Parameters  
| Name  | In  | Type  | Required  | Description  |  
| --- | --- | --- | --- | --- |  
| workspace_id  | path  | string  | true  | 工作空间id  |  
| x-auth-token  | header  | string  | true  | 访问令牌  |  
| body  | body  | [media.FastUploadInput](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/fast-upload.html#schemamedia.fastuploadinput)  | true  | body  |  
### Responses  
| Status  | Meaning  | Description  | Schema  |  
| --- | --- | --- | --- |  
| 200  | [OKopen in new window](https://tools.ietf.org/html/rfc7231#section-6.3.1)  | OK  | [media.FastUploadOutput](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/fast-upload.html#tocS_media.FastUploadOutput)  |  
> Example responses
```
{
	"code":0,
    "message":"success",
   	"data":{}
}
```
#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/fast-upload.html#schemas) Schemas
## media.FastUploadInput
```
{
  "ext": {
    "drone_model_key": "string",
    "is_original": true,
    "payload_model_key": "string",
    "tinny_fingerprint": "string",
    "sn": "string"
  },
  "fingerprint": "string",
  "name": "string",
  "path": "string"
}
```
###  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/fast-upload.html#properties) Properties  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| ext  | [media.MediaFile](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/fast-upload.html#schemamedia.mediafile)  | false  | none  | 文件关联的扩展属性  |  
| fingerprint  | string  | true  | none  | 文件指纹  |  
| name  | string  | false  | none  | 文件的名称  |  
| path  | string  | false  | none  | 文件的业务路径  |  
## media.MediaFile
```
{
  "drone_model_key": "string",
  "is_original": true,
  "payload_model_key": "string",
  "tinny_fingerprint": "string",
  "sn": "string"
}
```
###  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/fast-upload.html#properties-1) Properties  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| drone_model_key  | string  | false  | none  | 飞机产品枚举值  |  
| is_original  | boolean  | false  | none  | 是否为原图  |  
| payload_model_key  | string  | false  | none  | 负载产品枚举值  |  
| tinny_fingerprint  | string  | false  | none  | 精简指纹  |  
| sn  | string  | false  | none  | 设备序列号  |  
## media.FastUploadOutput
```
{
    "code":0,
    "message":"success",
    "data":{}
}
```
###  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/fast-upload.html#properties-2) Properties  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| code  | string  | false  | none  | 错误码  |  
| message  | string  | false  | none  | 描述  |  
| data  | string  | false  | none  | 返回内容  |