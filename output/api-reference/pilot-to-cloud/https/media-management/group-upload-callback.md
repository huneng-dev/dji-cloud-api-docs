---
source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/group-upload-callback.html
path: api-reference/pilot-to-cloud/https/media-management/group-upload-callback
---

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/group-upload-callback.html#%E6%96%87%E4%BB%B6%E7%BB%84%E4%B8%8A%E4%BC%A0%E5%AE%8C%E6%88%90%E5%90%8E%E5%9B%9E%E8%B0%83) 文件组上传完成后回调
`POST /media/api/v1/workspaces/{workspace_id}/group-upload-callback`
### Parameters  
| Name  | In  | Type  | Required  | Description  |  
| --- | --- | --- | --- | --- |  
| workspace_id  | path  | string  | true  | 工作空间 ID  |  
| x-auth-token  | header  | string  | true  | 访问令牌  |  
| body  | body  | [storage.FolderUploadCallbackInput](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/group-upload-callback.html#schemastorage.folderuploadcallbackinput)  | true  | body参数  |  
### Responses  
| Status  | Meaning  | Description  | Schema  |  
| --- | --- | --- | --- |  
| 200  | [OKopen in new window](https://tools.ietf.org/html/rfc7231#section-6.3.1)  | OK  | [storage.FolderUploadCallbackOutput](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/group-upload-callback.html#schema_storage.FolderUploadCallbackOutput)  |  
> Example responses
```
{
	"code":0,
   	"data":{},
    "message": "success"
}
```
#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/group-upload-callback.html#schemas) Schemas
## storage.MissionFinishCallBackInput
```
{
  "file_group_id": "xxx",
  "file_count": 0,
  "file_uploaded_count": 0
}
```
_Properties_  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| file_group_id  | string  | false  | none  | 文件组id，在一次航线任务中产生的媒体文件组 ID 相同  |  
| file_count  | int  | true  | none  | 指定文件组的媒体文件总数  |  
| file_uploaded_count  | int  | true  | none  | 文件组中已经成功上传的媒体文件总数  |  
## storage.FolderUploadCallbackOutput
```
{
  "code": 0,
  "data": {},
  "message": "string"
}
```
_Properties_  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| code  | integer  | false  | none  | 错误码  |  
| data  | [storage.CreateFavoriteInput](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/group-upload-callback.html#schemastorage.folderuploadcallbackinput)  | false  | none  | none  |  
| message  | string  | false  | none  | 错误描述  |