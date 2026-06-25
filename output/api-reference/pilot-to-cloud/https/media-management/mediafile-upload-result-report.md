<!-- source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/mediafile-upload-result-report.html -->
<!-- path: api-reference/pilot-to-cloud/https/media-management/mediafile-upload-result-report -->

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/mediafile-upload-result-report.html#%E4%B8%8A%E6%8A%A5%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E7%BB%93%E6%9E%9C) 上报文件上传结果
`POST /media/api/v1/workspaces/{workspace_id}/upload-callback`
### Parameters  
| Name  | In  | Type  | Required  | Description  |  
| --- | --- | --- | --- | --- |  
| workspace_id  | path  | string  | true  | 工作空间id  |  
| x-auth-token  | header  | string  | true  | 访问令牌  |  
| -  | body  | [media.UploadCallbackInput](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/mediafile-upload-result-report.html#schemamedia.uploadcallbackinput)  | true  |   |  
### Responses  
| Status  | Meaning  | Description  | Schema  |  
| --- | --- | --- | --- |  
| 200  | [OKopen in new window](https://tools.ietf.org/html/rfc7231#section-6.3.1)  | OK  | [media.UploadCallbackOutput](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/mediafile-upload-result-report.html#schemamedia.uploadcallbackoutput)  |  
> Example responses
```
{
  "code":0,
  "message":"success",
  "data":{
    "object_key":"5asjwu24-2a18-4b4b-86f9-3a678da0bf4d/example.jpg"
  }
}
```
#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/mediafile-upload-result-report.html#schemas) Schemas
## media.UploadCallbackInput
```
{
  "result": 0,
  "ext": {
    "file_group_id": "string",
    "drone_model_key": "string",
    "is_original": true,
    "payload_model_key": "string",
    "tinny_fingerprint": "string",
    "sn": "string"
  },
  "fingerprint": "string",
  "metadata": {
    "absolute_altitude": 0,
    "created_time": "string",
    "gimbal_yaw_degree": 0,
    "relative_altitude": 0,
    "shoot_position": {
      "lat": 0,
      "lng": 0
    }
  },
  "name": "string",
  "object_key": "string",
  "path": "string",
  "sub_file_type": 0
}
```
_Properties_  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | int  | true  | none  | 文件上传到存储桶是否成功，非0代表失败  |  
| ext  | [media.MediaFile](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/mediafile-upload-result-report.html#schemamedia.mediafile)  | false  | none  | 文件关联的扩展字段  |  
| fingerprint  | string  | false  | none  | 文件指纹  |  
| metadata  | [media.MetaData](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/mediafile-upload-result-report.html#schemamedia.metadata)  | false  | none  | 媒体元数据  |  
| name  | string  | true  | none  | 文件的名称  |  
| object_key  | string  | true  | none  | 文件在对象存储桶的key  |  
| path  | string  | true  | none  | 文件的业务路径  |  
| sub_file_type  | integer  | false  | none  | 当文件为图片的时候生效  
* 0 - 普通图片  
* 1 - 全景图  |  
## media.MediaFile
```
{
  "file_group_id": "string",
  "drone_model_key": "string",
  "is_original": true,
  "payload_model_key": "string",
  "tinny_fingerprint": "string",
  "sn": "string"
}
```
_Properties_  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| file_group_id  | string  | false  | none  | 文件分组id  |  
| drone_model_key  | string  | false  | none  | 飞机产品枚举值  |  
| is_original  | boolean  | false  | none  | 是否为原图  |  
| payload_model_key  | string  | false  | none  | 负载产品枚举值  |  
| tinny_fingerprint  | string  | false  | none  | 精简指纹  |  
| sn  | string  | false  | none  | 设备序列号  |  
## media.MetaData
```
{
  "absolute_altitude": 0,
  "created_time": "string",
  "gimbal_yaw_degree": 0,
  "relative_altitude": 0,
  "shoot_position": {
    "lat": 0,
    "lng": 0
  }
}
```
_Properties_  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| absolute_altitude  | float  | false  | none  | 拍摄绝对高度(m)  |  
| created_time  | string  | false  | none  | 媒体拍摄时间(iso 8601)  |  
| gimbal_yaw_degree  | float  | false  | none  | 云台偏航角  |  
| relative_altitude  | float  | false  | none  | 拍摄相对高度(m)  |  
| shoot_position  | object  | false  | none  | 拍摄位置  |  
| » lat  | float  | false  | none  | 拍摄位置纬度  |  
| » lng  | float  | false  | none  | 拍摄位置经度  |  
## media.UploadCallbackOutput
```
{
  "code": 0,
  "data": {
    "object_key": "string"
  },
  "message": "string"
}
```
_Properties_  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| code  | integer  | false  | none  | 错误码  |  
| data  | [media.UploadCallbackOutputData](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/mediafile-upload-result-report.html#schemamedia.uploadcallbackoutputdata)  | false  | none  | none  |  
| message  | string  | false  | none  | 错误描述  |  
## media.UploadCallbackOutputData
```
{
  "object_key": "string"
}
```
_Properties_  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| object_key  | string  | false  | none  | 文件在对象存储桶的key  |