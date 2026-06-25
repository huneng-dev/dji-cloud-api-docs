---
source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock2/psdk-transmit-custom-data.html
path: api-reference/dock-to-cloud/mqtt/dock/dock2/psdk-transmit-custom-data
---

#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock2/psdk-transmit-custom-data.html#event) Event
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock2/psdk-transmit-custom-data.html#%E8%87%AA%E5%AE%9A%E4%B9%89%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81-cloud) 自定义消息推送 Cloud
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** custom_data_transmission_from_psdk
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| value  | 数据内容  | text  | {"length":"小于 256"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
	"data": {
		"value": "hello world"
	},
	"gateway": "4TADKAQ000002J",
	"method": "custom_data_transmission_from_psdk",
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
	"timestamp": 1689911315621
}
```
#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock2/psdk-transmit-custom-data.html#service) Service
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock2/psdk-transmit-custom-data.html#cloud-%E8%87%AA%E5%AE%9A%E4%B9%89%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E5%88%B0-psdk) Cloud - 自定义消息推送到 PSDK
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** custom_data_transmission_to_psdk
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| value  | 数据内容  | text  | {"length":"小于 256"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
	"data": {
		"value": "hello world"
	},
	"method": "custom_data_transmission_to_psdk",
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
	"timestamp": 1689740550047
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** custom_data_transmission_to_psdk
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
	"data": {
		"result": 0
	},
	"method": "custom_data_transmission_to_psdk",
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
	"timestamp": 1689740550047
}
```