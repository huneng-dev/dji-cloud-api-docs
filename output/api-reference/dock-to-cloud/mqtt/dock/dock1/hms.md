---
source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/hms.html
path: api-reference/dock-to-cloud/mqtt/dock/dock1/hms
---

#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/hms.html#event) Event
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/hms.html#%E5%81%A5%E5%BA%B7%E5%91%8A%E8%AD%A6) 健康告警
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** hms
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| list  | 健康告警列表  | array  | {"size": 20, "item_type": struct}  |   |  
| »level  | 告警等级  | enum_int  | {"0":"通知","1":"提醒","2":"警告"}  |   |  
| »module  | 事件模块  | enum_int  | {"0":"飞行任务","1":"设备管理","2":"媒体","3":"hms"}  |   |  
| »in_the_sky  | 是否飞行  | enum_int  | {"0":"在地上","1":"在天上"}  |   |  
| »code  | 告警码  | text  | {"length":"10240"}  |   |  
| »device_type  | 设备类型  | text  |   | 格式为 _{domain-type-subtype}_ ，可以根据[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)查询  |  
| »imminent  | 是否为及时性的  | enum_int  | {"0":"否","1":"是"}  | 代表是否为及时性的告警码。比如风过大，会随着风力减小而自动消失。  |  
| »args  | 参数  | struct  |   |   |  
| »»component_index  | 文案变量  | int  | {"length":"10240"}  | 需要填充在 '告警文案查询json文件'，[hms.jsonopen in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/hms.html)'中的变量  |  
| »»sensor_index  | 文案变量  | int  | {"length":"10240"}  | 需要填充在 '告警文案查询json文件'，[hms.jsonopen in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/hms.html)'中的变量  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"list": [
			{
				"args": {
					"component_index": 0,
					"sensor_index": 0
				},
				"code": "0x16100083",
				"device_type": "0-67-0",
				"imminent": 1,
				"in_the_sky": 0,
				"level": 2,
				"module": 3
			}
		]
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "hms"
}
```