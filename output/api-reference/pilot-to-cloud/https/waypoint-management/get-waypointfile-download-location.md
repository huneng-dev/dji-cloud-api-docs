---
source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/waypoint-management/get-waypointfile-download-location.html
path: api-reference/pilot-to-cloud/https/waypoint-management/get-waypointfile-download-location
---

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/waypoint-management/get-waypointfile-download-location.html#%E8%8E%B7%E5%8F%96%E8%88%AA%E7%BA%BF%E6%96%87%E4%BB%B6%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80) 获取航线文件下载地址
`GET /wayline/api/v1/workspaces/{workspace_id}/waylines/{id}/url`
### Parameters  
| Name  | In  | Type  | Required  | Description  |  
| --- | --- | --- | --- | --- |  
| workspace_id  | path  | string  | true  | 工作空间id  |  
| id  | path  | string  | true  | 航线文件id  |  
| x-auth-token  | header  | string  | true  | 访问令牌  |  
### Responses  
| Status  | Meaning  | Description  | Schema  |  
| --- | --- | --- | --- |  
| 200  | [OKopen in new window](https://tools.ietf.org/html/rfc7231#section-6.3.1)  | OK  | /  |