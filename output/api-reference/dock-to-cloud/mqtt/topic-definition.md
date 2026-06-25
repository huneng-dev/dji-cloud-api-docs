---
source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html
path: api-reference/dock-to-cloud/mqtt/topic-definition
---

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#topic-%E6%80%BB%E8%A7%88) Topic 总览
为了方便设备云平台区分不同属性的处理策略，将设备上报物模型属性分为 osd 和 state 两类，分别用不同的 topic 上报。
  * osd：设备定频上报的属性，对应 pushmode = 0。
  * state：设备事件性上报的物模型属性，对应 pushmode=1。
> **说明：** 下表中的 _{gateway_sn}_ 表示网关设备的 SN， _{device_sn}_ 表示该物模型属性的所属设备的 SN 。  
| Topic Name  | 发送者 -> 订阅者  | Message  | 说明  |  
| --- | --- | --- | --- |  
| thing/product/_{device_sn}_ /osd  | 设备 > 云平台  | [osd message struct](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#osd-message-struct)  | 设备端定频向云平台推送的设备属性（properties），  
具体内容范围参见物模型内容  |  
| thing/product/_{device_sn}_ /state  | 设备 > 云平台  | [state message struct](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#state-message-struct)  | 设备端按需上报向云平台推送的设备属性（properties），  
具体内容范围参见物模型内容  |  
| thing/product/_{gateway_sn}_ /services  | 云平台 -> 设备  | [services message struct](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#services-message-struct)  | 云平台向设备发送的服务（具体service identifier 见物模型内容）。  |  
| thing/product/_{gateway_sn}_ /services_reply  | 设备 > 云平台  | [services_reply message struct](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#services_reply-message-struct)  | 设备对 service 的回复、处理结果  |  
| thing/product/_{gateway_sn}_ /events  | 设备 > 云平台  | [events message struct](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#events-message-struct)  | 设备端向云平台发送的，需要关注和处理的事件。  
比如SD满了，飞机解禁禁飞区等信息（事件范围参见物模型内容）  |  
| thing/product/_{gateway_sn}_ /events_reply  | 云平台 -> 设备  | [events_reply message struct](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#events_reply-message-struct)  | 云平台对设备事件的回复、处理结果  |  
| thing/product/_{gateway_sn}_ /requests  | 设备 > 云平台  | [requests message struct](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#requests-message-struct)  | 设备端向云平台发送请求，为了获取一些信息，比如上传的临时凭证  |  
| thing/product/_{gateway_sn}_ /requests_reply  | 云平台 -> 设备  | [requests_reply message struct](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#requests_reply-message-struct)  | 云平台对设备请求的回复  |  
| sys/product/_{gateway_sn}_ /status  | 设备 > 云平台  | [status message struct](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#status-message-struct)  | 设备上下线、更新拓扑  |  
| sys/product/_{gateway_sn}_ /status_reply  | 云平台 -> 设备  | [status_reply message struct](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#status_reply-message-struct)  | 平台响应  |  
| thing/product/_{gateway_sn}_ /property/set  | 云平台 -> 设备  | [property set message struct](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#property-set-message-struct)  | 设备属性设置。设备属性是否可以被修改，在设备属性章节通过“accessMode”标识符号判断，accessMode = rw 表示可被读写。  |  
| thing/product/_{gateway_sn}_ /property/set_reply  | 设备 > 云平台  | [property set_reply message struct](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#property-set-reply-message-struct)  | 设备属性设置的响应  |  
| thing/product/_{gateway_sn}_ /drc/up  | 设备 > 云平台  | [DRC message struct](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#drc-up-message-struct)  | DRC 协议上行  |  
| thing/product/_{gateway_sn}_ /drc/down  | 云平台 > 设备  | [DRC message struct](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#drc-down-message-struct)  | DRC 协议下行  |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#%E5%85%AC%E5%85%B1%E5%AD%97%E6%AE%B5%E8%A7%A3%E9%87%8A) 公共字段解释  
| Column  | Name  | Type  | Description  |  
| --- | --- | --- | --- |  
| tid  | 事务uuid  | text  | 事务（Transaction）的 UUID：表征一次简单的消息通信，如：增/删/改/查，云台控制等，可以是：  
1. 数据上报请求+数据上报响应  
2. 握手认证请求+响应+ack  
3.报警事件单向通知等，解决事务多并发和消息匹配的问题  |  
| bid  | 业务uuid  | text  | 业务（Business）的 UUID：有些功能不是一次通信就能完成的，包含持续一段时间内的所有交互。  
业务通常由多个原子事务组成，且持续时间较长;   
例如点播/下载/回放；解决业务多并发和重复请求的问题，便于所有模块的状态机管理。  |  
| timestamp  | 毫秒时间戳  | int  | 消息的发送时间  |  
| gateway  | 网关设备的序列号  | text  | 发送该消息的网关设备的序列号  |  
| data  | 消息内容  | object  | 消息内容  |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#osd-%E7%BB%93%E6%9E%84%E7%A4%BA%E4%BE%8B) osd 结构示例 
_topic_ : thing/product/_{device_sn}_ /osd
```
{
    "tid": "65717bf1-aee7-4abb-8ea3-9b1908548d74",
    "bid": "cf5ad2e6-2f32-4b59-980e-d5c9ee412805",
    "timestamp": 1667220873846,
    "data": {
        "job_number": 492,
        "acc_time": 1859010,
        "activation_time": 0,
        "maintain_status": {
            "maintain_status_array": [
                {
                    "state": 0,
                    "last_maintain_type": 17,
                    "last_maintain_time": 0,
                    "last_maintain_work_sorties": 0
                }
            ]
        },
        "electric_supply_voltage": 231,
        "working_voltage": 25440,
        "working_current": 1120,
        "backup_battery": {
            "voltage": 26631,
            "temperature": 27.9,
            "switch": 1
        },
        "drone_battery_maintenance_info": {
            "maintenance_state": 0,
            "maintenance_time_left": 0
        }
    },
    "gateway": "dock_sn"
} 
```
```
{
    "bid": "d6cfcea4-c6ca-439b-948f-b17d88fc308f",
    "data": {
        "flighttask_step_code": 255,
        "media_file_detail": {
            "remain_upload": 0
        },
        "wireless_link": {
            "4g_freq_band": 2.4,
            "4g_gnd_quality": 0,
            "4g_link_state": 0,
            "4g_quality": 0,
            "4g_uav_quality": 0,
            "dongle_number": 0,
            "link_workmode": 0,
            "sdr_freq_band": 2.4,
            "sdr_link_state": 0,
            "sdr_quality": 0
        }
    },
    "tid": "e4c15182-776b-4c13-9973-3fc76848ca15",
    "timestamp": 1667220881576,
    "gateway": "dock_sn"
}
```
```
{
    "tid": "43d2e632-1558-4c4e-83d2-eeb51b7a377a",
    "bid": "7578f2ac-1f12-4d47-9ab6-5de146ed7b8a",
    "timestamp": 1667220916697,
    "data": {
        "network_state": {
            "type": 2,
            "quality": 0,
            "rate": 5.0970001220703125
        },
        "drone_charge_state": {
            "state": 0,
            "capacity_percent": 100
        },
        "drone_in_dock": 1,
        "rainfall": 0,
        "wind_speed": 0,
        "environment_temperature": 24,
        "temperature": 24.9,
        "humidity": 62,
        "latitude": 22.907809968,
        "longitude": 113.703482143,
        "height": 34.174125671386719,
        "alternate_land_point": {
            "latitude": 22.907898319908661,
            "longitude": 113.70347329676635,
            "safe_land_height": 0,
            "is_configured": 1
        },
        "first_power_on": 1631945855969,
        "position_state": {
            "is_calibration": 1,
            "is_fixed": 2,
            "quality": 5,
            "gps_number": 6,
            "rtk_number": 25
        },
        "storage": {
            "total": 82045336,
            "used": 51772
        },
        "mode_code": 1,
        "cover_state": 0,
        "supplement_light_state": 0,
        "emergency_stop_state": 0,
        "air_conditioner_mode": 0,
        "battery_store_mode": 1,
        "alarm_state": 0,
        "putter_state": 0,
        "sub_device": {
            "device_sn": "1581F5BKD225D00BP891",
            "device_model_key": "0-67-0",
            "device_online_status": 0,
            "device_paired": 1
        }
    },
    "gateway": "dock_sn"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#state-%E7%BB%93%E6%9E%84%E7%A4%BA%E4%BE%8B) state 结构示例 
_topic_ : thing/product/_{device_sn}_ /state
```
{
    "tid":"6a7bfe89-c386-4043-b600-b518e10096cc",
    "bid":"42a19f36-5117-4520-bd13-fd61d818d52e",
    "timestamp": 1598411295123,
    "gateway":"sn",
    "data":{}
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#services-%E7%BB%93%E6%9E%84%E7%A4%BA%E4%BE%8B) services 结构示例 
_topic_ : thing/product/_{gateway_sn}_ /services
```
{
    "tid":"6a7bfe89-c386-4043-b600-b518e10096cc",
    "bid":"42a19f36-5117-4520-bd13-fd61d818d52e",
    "timestamp": 1598411295123,
    "gateway":"sn",
    "method": "some_method",
    "data": {}
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#services-reply-%E7%BB%93%E6%9E%84%E7%A4%BA%E4%BE%8B) services_reply 结构示例 
###  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#data%E4%B8%AD%E5%BF%85%E5%A1%AB%E5%AD%97%E6%AE%B5%E8%A7%A3%E9%87%8A) data中必填字段解释  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 设备响应的结果码  | int  |   | 非 0 代表错误  |  
| output  | 设备消息内容  | struct  |   | 设备响应服务端命令的消息内容  |  
```
{
    "tid":"6a7bfe89-c386-4043-b600-b518e10096cc",
    "bid":"42a19f36-5117-4520-bd13-fd61d818d52e",
    "timestamp": 1598411295123,
    "gateway":"sn",
    "method": "some_method",
    "data": {
        "result": 0, 
    	"output": {}
    }  
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#events-%E7%BB%93%E6%9E%84%E7%A4%BA%E4%BE%8B) events 结构示例 
_topic_ : thing/product/_{gateway_sn}_ /events  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| need_reply  | 服务端是否需要答复  | int  |   | 服务端收到设备的events事件上报消息后，跟进need_reply来判断是否给予收到答复;0代表不需要，1代表需要  |  
```
{
    "tid":"6a7bfe89-c386-4043-b600-b518e10096cc",
    "bid":"42a19f36-5117-4520-bd13-fd61d818d52e",
    "timestamp": 1598411295123,
    "need_reply": 0,
    "gateway":"sn",
    "method": "some_method",
    "data": {}
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#events-reply-%E7%BB%93%E6%9E%84%E7%A4%BA%E4%BE%8B) events_reply 结构示例 
_topic_ : thing/product/_{gateway_sn}_ /events_reply
###  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#data%E4%B8%AD%E5%BF%85%E5%A1%AB%E5%AD%97%E6%AE%B5%E8%A7%A3%E9%87%8A-1) data中必填字段解释  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 服务端响应的结果码  | int  |   | 非 0 代表错误  |  
```
{
    "tid":"6a7bfe89-c386-4043-b600-b518e10096cc",
    "bid":"42a19f36-5117-4520-bd13-fd61d818d52e",
    "timestamp": 1598411295123,
    "gateway":"sn",
    "method": "some_method",
    "data": {
        "result": 0
    }
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#requests-%E7%BB%93%E6%9E%84%E7%A4%BA%E4%BE%8B) requests 结构示例 
_topic_ : thing/product/_{gateway_sn}_ /requests
```
{
    "tid":"6a7bfe89-c386-4043-b600-b518e10096cc",
    "bid":"42a19f36-5117-4520-bd13-fd61d818d52e",
    "timestamp": 1598411295123,
    "gateway":"sn",
    "method": "some_method",
    "data": {}
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#requests-reply-%E7%BB%93%E6%9E%84%E7%A4%BA%E4%BE%8B) requests_reply 结构示例 
_topic_ : thing/product/_{gateway_sn}_ /requests_reply
###  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#data%E4%B8%AD%E5%BF%85%E5%A1%AB%E5%AD%97%E6%AE%B5%E8%A7%A3%E9%87%8A-2) data中必填字段解释  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 服务端响应的结果码  | int  |   | 非 0 代表错误  |  
| output  | 服务消息内容  | struct  |   | 服务端响应设备的消息内容  |  
```
{
    "tid":"6a7bfe89-c386-4043-b600-b518e10096cc",
    "bid":"42a19f36-5117-4520-bd13-fd61d818d52e",
    "timestamp": 1598411295123,
    "gateway":"sn",
    "method": "some_method",
    "data": {
        "result": 0,
        "output":{}
    }
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#status-%E7%BB%93%E6%9E%84%E7%A4%BA%E4%BE%8B) status 结构示例 
_topic_ : sys/product/_{gateway_sn}_ /status
```
## 网关设备+子设备上线
{
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"method": "update_topo",
	"timestamp": 1234567890123,
	"data": {
		"type": 98,
		"sub_type": 0,
		"device_secret": "secret",
		"nonce": "nonce",
		"version": 1,
		"sub_devices": [
			{
				"sn": "drone001",
				"type": 116,
				"sub_type": 0,
				"index": "A",
				"device_secret": "secret",
				"nonce": "nonce",
				"version": 1
			}
		]
	}
}
## 子设备下线
{
    "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
    "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
    "method": "update_topo",
    "timestamp": 1234567890123,
    "data": {
        "type": 98,
        "sub_type": 0,
        "device_secret":"secret",
        "nonce":"nonce",
        "version": 1,
        "sub_devices":[]
    }
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#status-reply-%E7%BB%93%E6%9E%84%E7%A4%BA%E4%BE%8B) status_reply 结构示例 
_topic_ : sys/product/_{gateway_sn}_ /status_reply
###  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#data%E4%B8%AD%E5%BF%85%E5%A1%AB%E5%AD%97%E6%AE%B5%E8%A7%A3%E9%87%8A-3) data中必填字段解释  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 结果码  | int  |   | 非0代表错误  |  
```
{
    "tid":"6a7bfe89-c386-4043-b600-b518e10096cc",
    "bid":"42a19f36-5117-4520-bd13-fd61d818d52e",
    "timestamp": 1598411295123,
    "method": "update_topo",
    "data": {
        "result": 0 
    }
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#property-set-%E7%BB%93%E6%9E%84%E7%A4%BA%E4%BE%8B) property set 结构示例 
_topic_ : thing/product/_{gateway_sn}_ /property/set  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| some_property  | 需要修改的属性key  | string  |   | 参考[设备管理-设备属性设置open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/device.html)  
设备属性是否可以被修改，在设备属性章节通过“accessMode”标识符号判断，accessMode = rw 表示可被读写。  |  
| some_value  | 需要修改的属性value  | string/int/float  |   | 参考对应的设备属性  |  
```
{
    "tid":"6a7bfe89-c386-4043-b600-b518e10096cc",
    "bid":"42a19f36-5117-4520-bd13-fd61d818d52e",
    "timestamp": 1598411295123,
    "data": {
      "some_property": some_value
    }
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#property-set-reply-%E7%BB%93%E6%9E%84%E7%A4%BA%E4%BE%8B) property set_reply 结构示例 
_topic_ : thing/product/_{gateway_sn}_ /property/set_reply
###  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#data%E4%B8%AD%E5%BF%85%E5%A1%AB%E5%AD%97%E6%AE%B5%E8%A7%A3%E9%87%8A-4) data中必填字段解释  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| some_property  | 需要修改的属性key  | string  |   | 参考[设备管理-设备属性设置open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/device.html)  
设备属性是否可以被修改，在设备属性章节通过“accessMode”标识符号判断，accessMode = rw 表示可被读写。  |  
| result  | 对应属性的设置结果  | int  |   | 0: 成功，1：失败，2：超时，其他参考错误码解释  |  
```
{
    "tid":"6a7bfe89-c386-4043-b600-b518e10096cc",
    "bid":"42a19f36-5117-4520-bd13-fd61d818d52e",
    "timestamp": 1598411295123,
    "data": {
        "some_property": {
           "result": 0  // 0: 成功，1：失败，2：超时，其他参考错误码解释
        }
    }
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#drc-up-%E7%BB%93%E6%9E%84%E7%A4%BA%E4%BE%8B) drc up 结构示例 
_topic_ : thing/product/_{gateway_sn}_ /drc/up
###  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#data%E4%B8%AD%E5%BF%85%E5%A1%AB%E5%AD%97%E6%AE%B5%E8%A7%A3%E9%87%8A-5) data中必填字段解释  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 服务端响应的结果码  | int  |   | 非 0 代表错误  |  
| output  | 服务消息内容  | struct  |   | 服务端响应设备的消息内容  |  
```
{
	"method": "drone_control",
	"data": {
		"result": 0,
		"output": {
			"seq": 1
		}
	}
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/topic-definition.html#drc-down-%E7%BB%93%E6%9E%84%E7%A4%BA%E4%BE%8B) drc down 结构示例 
_topic_ : thing/product/_{gateway_sn}_ /drc/down
```
{
	"method": "drone_control",
	"data": {
		"seq": 1,
		"x": 2.34,
		"y": -2.45,
		"h": 2.76,
		"w": 2.86
	}
}
```