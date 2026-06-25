---
source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/config.html
path: api-reference/dock-to-cloud/mqtt/dock/dock1/config
---

#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/config.html#requests) Requests
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/config.html#%E8%8E%B7%E5%8F%96%E9%85%8D%E7%BD%AE) 获取配置
**Topic:** thing/product/_{gateway_sn}_ /requests
**Direction:** up
**Method:** config
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| config_type  | 配置类型  | enum_string  | {"json":"json 格式"}  |   |  
| config_scope  | 配置范围  | enum_string  | {"product":"产品维度"}  |   |  
**Example:**
```
{
	"bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
	"data": {
		"config_scope": "product",
		"config_type": "json"
	},
	"gateway": "sn",
	"tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
	"timestamp": 1667803298000,
	"method": "config"
}
```
**Topic:** thing/product/_{gateway_sn}_ /requests_reply
**Direction:** down
**Method:** config
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| ntp_server_host  | NTP 服务 Host  | text  |   |   |  
| app_id  | 在 [开发者网站open in new window](https://developer.dji.com/user/apps/#all) 创建的 App 的 ID  | text  |   |   |  
| app_key  | 在 [开发者网站open in new window](https://developer.dji.com/user/apps/#all) 创建的 App 的 Key  | text  |   |   |  
| app_license  | 在 [开发者网站open in new window](https://developer.dji.com/user/apps/#all) 创建的 App 的 License  | text  |   |   |  
| ntp_server_port  | NTP 服务端口号  | int  |   | 若请求中没有本字段，NTP 默认端口号为 123  |  
**Example:**
```
{
	"bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
	"data": {
		"app_id": "123456",
		"app_key": "app_key",
		"app_license": "app_license",
		"ntp_server_host": "host_url",
		"ntp_server_port": 456
	},
	"gateway": "sn",
	"tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
	"timestamp": 1667803298000,
	"method": "config"
}
```