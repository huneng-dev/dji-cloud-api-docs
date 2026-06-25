<!-- source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/obtain-exited-tiny-fingerprint.html -->
<!-- path: api-reference/pilot-to-cloud/https/media-management/obtain-exited-tiny-fingerprint -->

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/obtain-exited-tiny-fingerprint.html#%E8%8E%B7%E5%8F%96%E5%B7%B2%E7%BB%8F%E5%AD%98%E5%9C%A8%E7%9A%84%E6%96%87%E4%BB%B6%E5%A4%B9%E7%B2%BE%E7%AE%80%E6%8C%87%E7%BA%B9) 获取已经存在的文件夹精简指纹
`POST /media/api/v1/workspaces/{workspace_id}/files/tiny-fingerprints`
### Parameters  
| Name  | In  | Type  | Required  | Description  |  
| --- | --- | --- | --- | --- |  
| tiny_fingerprints  | body  | array[string]  | true  | 精简指纹数组  |  
| workspace_id  | path  | string  | true  | 工作空间id  |  
| x-auth-token  | header  | string  | true  | 访问令牌  |  
### Responses  
| Status  | Meaning  | Description  | Schema  |  
| --- | --- | --- | --- |  
| 200  | [OKopen in new window](https://tools.ietf.org/html/rfc7231#section-6.3.1)  | OK  | [media.GetTinyFingerprintsOutput](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/obtain-exited-tiny-fingerprint.html#schemamedia.gettinyfingerprintsoutput)  |  
> Example responses
```
{
    "code":0,
    "message":"success",
    "data":{
        "tiny_fingerprints":[
            "5aec4c6e78052bf38fab901bcd1a2319_2021_12_8_22_13_10" //已经存在的精简文件指纹
        ]
    }
}
```
#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/media-management/obtain-exited-tiny-fingerprint.html#schemas) Schemas
## media.GetTinyFingerprintsOutput
```
{
    "code":0,
    "message":"success",
    "data":{
        "tiny_fingerprints":[
            "string"
        ]
    }
}
```
_Properties_  
| Name  | Type  | Required  | Restrictions  | Description  |  
| --- | --- | --- | --- | --- |  
| code  | string  | false  | none  | 错误码  |  
| message  | string  | false  | none  | 描述  |  
| data  | string  | false  | none  | 返回内容  |  
| » tiny_fingerprints  | [string]  | false  | none  | 已经存在的精简指纹数组  |