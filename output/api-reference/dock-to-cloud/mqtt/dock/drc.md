<!-- source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html -->
<!-- path: api-reference/dock-to-cloud/mqtt/dock/drc -->

#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#event) Event
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#flyto-%E6%89%A7%E8%A1%8C%E7%BB%93%E6%9E%9C%E4%BA%8B%E4%BB%B6%E9%80%9A%E7%9F%A5) flyto 执行结果事件通知
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** fly_to_point_progress
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| fly_to_id  | 飞向目标点 ID  | text  |   |   |  
| status  | 状态  | enum_string  | {"wayline_cancel":"取消飞向目标点","wayline_failed":"执行失败","wayline_ok":"执行成功，已飞向目标点","wayline_progress":"执行中"}  |   |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| way_point_index  | 当前执行到第几个航点  | int  |   |   |  
| remaining_distance  | [新增]剩余任务距离  | float  | {"step":0.1,"unit":"米 / m"}  |   |  
| remaining_time  | [新增]剩余任务时间  | float  | {"step":0.1,"unit":"秒 / s"}  |   |  
| planned_path_points  | [新增]规划的轨迹点列表  | array  | {"size": -, "item_type": struct}  |   |  
| »latitude  | 轨迹点纬度(角度值)  | double  | {"max":90,"min":-90}  | 轨迹点纬度，角度值，南纬是负，北纬是正，精度到小数点后6位  |  
| »longitude  | 轨迹点经度(角度值)  | double  | {"max":180,"min":-180}  | 轨迹点经度，角度值，东经是正，西经是负，精度到小数点后6位  |  
| »height  | 轨迹点高度  | float  | {"step":0.1,"unit":"米 / m"}  | 轨迹点高度,椭球高  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"fly_to_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
		"planned_path_points": [
			{
				"height": 123.234,
				"latitude": 13.23,
				"longitude": 123.234
			}
		],
		"remaining_distance": 0,
		"remaining_time": 0,
		"result": 0,
		"status": "wayline_progress",
		"way_point_index": 0
	},
	"need_reply": 1,
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 16540709686556,
	"method": "fly_to_point_progress"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#%E4%B8%80%E9%94%AE%E8%B5%B7%E9%A3%9E%E7%BB%93%E6%9E%9C%E4%BA%8B%E4%BB%B6%E9%80%9A%E7%9F%A5) 一键起飞结果事件通知
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** takeoff_to_point_progress
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| status  | 任务状态  | enum_string  | {"task_finish":"一键起飞任务完成","task_ready":"准备起飞","wayline_cancel":"取消飞向目标点","wayline_failed":"执行失败","wayline_ok":"执行成功，已飞向目标点","wayline_progress":"执行中"}  |   |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| flight_id  | 一键起飞任务 UUID  | text  |   |   |  
| track_id  | 航迹 ID  | text  |   |   |  
| way_point_index  | 当前执行到第几个航点  | int  |   |   |  
| remaining_distance  | [新增]剩余任务距离  | float  | {"step":0.1,"unit":"米 / m"}  |   |  
| remaining_time  | [新增]剩余任务时间  | float  | {"step":0.1,"unit":"秒 / s"}  |   |  
| planned_path_points  | [新增]规划的轨迹点列表  | array  | {"size": -, "item_type": struct}  |   |  
| »latitude  | 轨迹点纬度(角度值)  | double  | {"max":90,"min":-90}  | 轨迹点纬度，角度值，南纬是负，北纬是正，精度到小数点后6位  |  
| »longitude  | 轨迹点经度(角度值)  | double  | {"max":180,"min":-180}  | 轨迹点经度，角度值，东经是正，西经是负，精度到小数点后6位  |  
| »height  | 轨迹点高度  | float  | {"step":0.1,"unit":"米 / m"}  | 轨迹点高度,椭球高  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"flight_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
		"planned_path_points": [
			{
				"height": 123.234,
				"latitude": 13.23,
				"longitude": 123.234
			}
		],
		"remaining_distance": 0,
		"remaining_time": 0,
		"result": 0,
		"status": "wayline_ok",
		"track_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
		"way_point_index": 1
	},
	"need_reply": 1,
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 16540709686556,
	"method": "takeoff_to_point_progress"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#drc-%E9%93%BE%E8%B7%AF%E7%8A%B6%E6%80%81%E9%80%9A%E7%9F%A5) DRC 链路状态通知
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** drc_status_notify
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| drc_state  | DRC 状态  | enum_int  | {"0":"未连接","1":"连接中","2":"已连接"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"drc_state": 2,
		"result": 0
	},
	"need_reply": 1,
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "drc_status_notify"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#joystick-%E6%8E%A7%E5%88%B6%E6%97%A0%E6%95%88%E5%8E%9F%E5%9B%A0%E9%80%9A%E7%9F%A5) Joystick 控制无效原因通知
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** joystick_invalid_notify
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| reason  | 任务状态  | int  | {"0":"遥控器失联","1":"低电量返航","2":"低电量降落","3":"靠近限飞区","4":"遥控器夺权（例如：触发了返航，B控夺权）"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"reason": 0
	},
	"need_reply": 1,
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "joystick_invalid_notify"
}
```
#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#service) Service
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#%E9%A3%9E%E8%A1%8C%E6%8E%A7%E5%88%B6%E6%9D%83%E6%8A%A2%E5%A4%BA) 飞行控制权抢夺
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** flight_authority_grab
**Data:** null
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "flight_authority_grab"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** flight_authority_grab
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "flight_authority_grab"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#%E8%B4%9F%E8%BD%BD%E6%8E%A7%E5%88%B6%E6%9D%83%E6%8A%A2%E5%A4%BA) 负载控制权抢夺
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** payload_authority_grab
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| payload_index  | 负载枚举值  | text  |   | 镜头负载与挂载位置枚举值。非标准的 device_mode_key，格式为 {type-subtype-gimbalindex}，可以参考[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"payload_index": "39-0-7"
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "payload_authority_grab"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** payload_authority_grab
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "payload_authority_grab"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#%E8%BF%9B%E5%85%A5%E6%8C%87%E4%BB%A4%E9%A3%9E%E8%A1%8C%E6%8E%A7%E5%88%B6%E6%A8%A1%E5%BC%8F) 进入指令飞行控制模式
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** drc_mode_enter
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| mqtt_broker  | Broker 连接信息  | struct  |   | 获取 MQTT 中继服务的地址与认证信息  |  
| »address  | 服务器连接地址  | text  |   | 服务器连接地址，例如：192.0.2.1:8883, mqtt.dji.com:8883  |  
| »client_id  | 客户端 ID  | text  |   | 可自定义的 MQTT 客户端 ID。建议使用设备的 SN 码，也可以与具有语义的前缀组合，例如，drc-4J4R101  |  
| »username  | 用户名  | text  |   | 建立连接时使用的用户名  |  
| »password  | 密码  | text  |   | 建立连接时认证所需要的密码  |  
| »expire_time  | 认证信息过期时间  | int  | {"unit":"秒 / s"}  | 在有效期内认证信息可以重复使用，另外认证信息过期后，并不会影响已建立连接的设备  |  
| »enable_tls  | 是否启用 TLS  | bool  |   | 启用 TLS 即对 MQTT 链路开启加密  |  
| osd_frequency  | OSD 频率  | int  | {"max":30,"min":1,"unit":"赫兹 / Hz"}  | 设置 OSD 上报频率  |  
| hsi_frequency  | HSI 频率  | int  | {"max":30,"min":1,"unit":"赫兹 / Hz"}  | 设置 HSI 上报频率  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"hsi_frequency": 1,
		"mqtt_broker": {
			"address": "mqtt.dji.com:8883",
			"client_id": "sn_a",
			"enable_tls": true,
			"expire_time": 1672744922,
			"password": "jwt_token",
			"username": "sn_a_username"
		},
		"osd_frequency": 10
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "drc_mode_enter"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** drc_mode_enter
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "drc_mode_enter"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#%E9%80%80%E5%87%BA%E6%8C%87%E4%BB%A4%E9%A3%9E%E8%A1%8C%E6%8E%A7%E5%88%B6%E6%A8%A1%E5%BC%8F) 退出指令飞行控制模式
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** drc_mode_exit
**Data:** null
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "drc_mode_exit"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** drc_mode_exit
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "drc_mode_exit"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#%E4%B8%80%E9%94%AE%E8%B5%B7%E9%A3%9E) 一键起飞
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** takeoff_to_point
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| target_latitude  | 目标点纬度(角度值)  | double  | {"max":90,"min":-90}  | 目标点纬度，角度值，南纬是负，北纬是正，精度到小数点后6位  |  
| target_longitude  | 目标点经度(角度值)  | double  | {"max":180,"min":-180}  | 目标点经度，角度值，东经是正，西经是负，精度到小数点后6位  |  
| target_height  | 目标点高度  | float  | {"max":1500,"min":2,"step":0.1,"unit":"米 / m"}  | 目标点高度（椭球高），使用 WGS84 模型，飞行器到点后默认行为：悬停  |  
| security_takeoff_height  | 安全起飞高度  | float  | {"max":1500,"min":2,"step":0.1,"unit":"米 / m"}  | 相对(机场)起飞点的高度（ALT），飞行器先升到特定的高度，然后再飞向目标点。  |  
| rth_mode  | 返航模式设置值  | enum_int  | {"0":"智能高度","1","设定高度"}  |   |  
| rth_altitude  | 返航高度  | int  | {"max":1500,"min":2,"step":1,"unit":"米 / m"}  | 相对(机场)起飞点的高度，相对高 ALT  |  
| rc_lost_action  | 遥控器失控动作  | enum_int  | {"0":"悬停","1":"着陆(降落)","2":"返航"}  | 遥控器失控动作  |  
| exit_wayline_when_rc_lost  | [废弃]航线失控动作  | enum_int  | {"0":"继续执行航线任务","1":"退出航线任务，执行遥控器失控动作"}  |   |  
| commander_mode_lost_action  | [新增]指点飞行失控动作  | enum_int  | {"0":"继续执行指点飞行任务","1":"退出指点飞行任务，执行普通失控行为"}  |   |  
| commander_flight_mode  | 指点飞行模式设置值  | enum_int  | {"0":"智能高度飞行","1","设定高度飞行"}  |   |  
| commander_flight_height  | [新增]指点飞行高度  | float  | {"max":3000,"min":2,"step":0.1,"unit":"米 / m"}  | 相对(机场)起飞点的高度，相对高 ALT  |  
| flight_id  | 一键起飞任务 UUID  | text  |   | 任务 UUID，全局唯一，用于染色，云端区分该值是普通计划任务还是一键起飞任务  |  
| max_speed  | 一键起飞的飞行过程中能达到的最大速度  | int  | {"max":15,"min":1,"unit":"米每秒 / m/s"}  |   |  
| simulate_mission  | [新增]是否在模拟器中执行任务  | struct  |   | 可选字段，用于在室内进行模拟任务调试。  |  
| »is_enable  | 是否开启模拟器任务  | enum_int  | {"0":"不开启","1":"开启"}  | 当次任务打开或关闭模拟器  |  
| »latitude  | 纬度  | double  | {"max":"90.0","min":"-90.0"}  |   |  
| »longitude  | 经度  | double  | {"max":"180.0","min":"-180.0"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"flight_id": "ABDEAC21DCADDA",
		"max_speed": 12,
		"out_of_control_action": 0,
		"rth_altitude": 100,
		"security_takeoff_height": 100,
		"target_height": 100,
		"target_latitude": 12.23,
		"target_longitude": 12.32
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "takeoff_to_point"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** takeoff_to_point
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "takeoff_to_point"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#flyto-%E9%A3%9E%E5%90%91%E7%9B%AE%E6%A0%87%E7%82%B9) flyto 飞向目标点
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** fly_to_point
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| fly_to_id  | 飞向目标点 ID  | text  |   |   |  
| max_speed  | flyto 的飞行过程中能达到的最大速度  | int  | {"max":15,"min":0,"unit":"米每秒 / m/s"}  |   |  
| points  | flyto 目标点列表  | array  | {"size": -, "item_type": struct}  | 仅支持 1 个目标点  |  
| »latitude  | 目标点纬度(角度值)  | double  | {"max":90,"min":-90}  | 目标点纬度，角度值，南纬是负，北纬是正，精度到小数点后6位  |  
| »longitude  | 目标点经度(角度值)  | double  | {"max":180,"min":-180}  | 目标点经度，角度值，东经是正，西经是负，精度到小数点后6位  |  
| »height  | 目标点高度  | float  | {"max":10000,"min":2,"step":0.1,"unit":"米 / m"}  | 目标点高度（椭球高），使用 WGS84 模型  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"fly_to_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
		"max_speed": 12,
		"points": [
			{
				"height": 100,
				"latitude": 12.23,
				"longitude": 12.23
			},
			{
				"height": 100,
				"latitude": 12.23,
				"longitude": 12.23
			}
		]
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "fly_to_point"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** fly_to_point
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "fly_to_point"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#%E7%BB%93%E6%9D%9F-flyto-%E9%A3%9E%E5%90%91%E7%9B%AE%E6%A0%87%E7%82%B9%E4%BB%BB%E5%8A%A1) 结束 flyto 飞向目标点任务
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** fly_to_point_stop
**Data:** null
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "fly_to_point_stop"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** fly_to_point_stop
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "fly_to_point_stop"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#%E8%B4%9F%E8%BD%BD%E6%8E%A7%E5%88%B6%E2%80%94%E5%88%87%E6%8D%A2%E7%9B%B8%E6%9C%BA%E6%A8%A1%E5%BC%8F) 负载控制—切换相机模式
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** camera_mode_switch
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| payload_index  | 相机枚举  | text  |   | 相机枚举值。非标准的 device_mode_key，格式为 {type-subtype-gimbalindex}，可以参考[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)  |  
| camera_mode  | 相机模式  | enum_int  | {"0":"拍照","1":"录像"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"camera_mode": 0,
		"payload_index": "39-0-7"
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "camera_mode_switch"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** camera_mode_switch
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "camera_mode_switch"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#%E8%B4%9F%E8%BD%BD%E6%8E%A7%E5%88%B6%E2%80%94%E5%8D%95%E6%8B%8D) 负载控制—单拍
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** camera_photo_take
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| payload_index  | 相机枚举  | text  |   | 相机枚举值。非标准的 device_mode_key，格式为 {type-subtype-gimbalindex}，可以参考[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"payload_index": "39-0-7"
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "camera_photo_take"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** camera_photo_take
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "camera_photo_take"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#%E8%B4%9F%E8%BD%BD%E6%8E%A7%E5%88%B6%E2%80%94%E5%BC%80%E5%A7%8B%E5%BD%95%E5%83%8F) 负载控制—开始录像
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** camera_recording_start
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| payload_index  | 相机枚举  | text  |   | 相机枚举值。非标准的 device_mode_key，格式为 {type-subtype-gimbalindex}，可以参考[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"payload_index": "39-0-7"
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "camera_recording_start"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** camera_recording_start
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "camera_recording_start"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#%E8%B4%9F%E8%BD%BD%E6%8E%A7%E5%88%B6%E2%80%94%E5%81%9C%E6%AD%A2%E5%BD%95%E5%83%8F) 负载控制—停止录像
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** camera_recording_stop
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| payload_index  | 相机枚举  | text  |   | 相机枚举值。非标准的 device_mode_key，格式为 {type-subtype-gimbalindex}，可以参考[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"payload_index": "39-0-7"
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "camera_recording_stop"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** camera_recording_stop
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "camera_recording_stop"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#%E8%B4%9F%E8%BD%BD%E6%8E%A7%E5%88%B6%E2%80%94%E7%94%BB%E9%9D%A2%E6%8B%96%E5%8A%A8%E6%8E%A7%E5%88%B6) 负载控制—画面拖动控制
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** camera_screen_drag
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| payload_index  | 相机枚举  | text  |   | 相机枚举值。非标准的 device_mode_key，格式为 {type-subtype-gimbalindex}，可以参考[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)  |  
| locked  | 机头和云台的相对关系是否锁定  | bool  | {"false":"仅云台转，机身不转","true":"锁定机头，云台和机身一起转"}  |   |  
| pitch_speed  | 云台 pitch 速度  | double  | {"unit":"弧度每秒 / rad/s"}  | 云台 pitch 速度  |  
| yaw_speed  | 云台 yaw 速度  | double  | {"unit":"弧度每秒 / rad/s"}  | 云台 yaw 速度，仅不锁机头时才生效  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"locked": true,
		"payload_index": "39-0-7",
		"pitch_speed": 0.1,
		"yaw_speed": 0.1
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "camera_screen_drag"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** camera_screen_drag
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "camera_screen_drag"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#%E8%B4%9F%E8%BD%BD%E6%8E%A7%E5%88%B6%E2%80%94%E5%8F%8C%E5%87%BB%E6%88%90%E4%B8%BA-aim) 负载控制—双击成为 AIM
双击 aim 功能为在相机镜头的视野范围内，双击镜头中的目标点，该目标点将成为镜头视野的中心
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** camera_aim
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| payload_index  | 相机枚举  | text  |   | 相机枚举值。非标准的 device_mode_key，格式为 {type-subtype-gimbalindex}，可以参考[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)  |  
| camera_type  | 相机类型  | enum_string  | {"ir":"红外","wide":"广角","zoom":"变焦"}  | 相机类型枚举  |  
| locked  | 机头和云台的相对关系是否锁定  | bool  | {"false":"仅云台转，机身不转","true":"锁定机头，云台和机身一起转"}  |   |  
| x  | 目标坐标 x  | double  | {"max":1,"min":0}  | 目标坐标 x，以镜头的左上角为坐标中心点，水平方向为 x  |  
| y  | 目标坐标 y  | double  | {"max":1,"min":0}  | 目标坐标 y，以镜头的左上角为坐标中心点，竖直方向为 y  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"camera_type": "zoom",
		"locked": true,
		"payload_index": "39-0-7",
		"x": 0.5,
		"y": 0.5
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "camera_aim"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** camera_aim
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "camera_aim"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#%E8%B4%9F%E8%BD%BD%E6%8E%A7%E5%88%B6%E2%80%94%E5%8F%98%E7%84%A6) 负载控制—变焦
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** camera_focal_length_set
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| payload_index  | 相机枚举  | text  |   | 相机枚举值。非标准的 device_mode_key，格式为 {type-subtype-gimbalindex}，可以参考[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)  |  
| camera_type  | 相机类型  | enum_string  | {"ir":"红外","wide":"广角","zoom":"变焦"}  | 相机类型枚举  |  
| zoom_factor  | 变焦倍数  | double  | {"max":200,"min":2}  | 变焦倍数，可见光是2-200，红外是2-20  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"camera_type": "zoom",
		"payload_index": "39-0-7",
		"zoom_factor": 5
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "camera_focal_length_set"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** camera_focal_length_set
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "camera_focal_length_set"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#%E8%B4%9F%E8%BD%BD%E6%8E%A7%E5%88%B6%E2%80%94%E9%87%8D%E7%BD%AE%E4%BA%91%E5%8F%B0) 负载控制—重置云台
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** gimbal_reset
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| payload_index  | 负载编号  | text  |   | 负载编号，相机枚举值。非标准的 device_mode_key，格式为 {type-subtype-gimbalindex}，可以参考[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)  |  
| reset_mode  | 重置模式类型  | enum_int  | {"0":"回中","1":"向下","2":"偏航回中","3":"俯仰向下"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"payload_index": "39-0-7",
		"reset_mode": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "gimbal_reset"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** gimbal_reset
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "gimbal_reset"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#%E8%B4%9F%E8%BD%BD%E6%8E%A7%E5%88%B6%E2%80%94look-at) 负载控制—Look At
lookat 功能指飞行器将从当前朝向转向实际经纬高度指定的点，在 M30/M30T 机型上建议使用锁定机头的方式，仅云台转动场景下在抵达云台限位角后 lookat 功能将出现异常
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** camera_look_at
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| payload_index  | 相机枚举  | text  |   | 相机枚举值。非标准的 device_mode_key，格式为 {type-subtype-gimbalindex}，可以参考[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)  |  
| locked  | 机头和云台的相对关系是否锁定  | bool  | {"false":"仅云台转，机身不转","true":"锁定机头，云台和机身一起转"}  |   |  
| latitude  | 目标点纬度(角度值)  | double  | {"max":90,"min":-90}  | 角度值。南纬是负，北纬是正，精度到小数点后6位。  |  
| longitude  | 目标点经度(角度值)  | double  | {"max":180,"min":-180}  | 角度值。东经是正，西经是负，精度到小数点后6位。  |  
| height  | 目标点高度  | float  | {"max":10000,"min":2,"step":0.1,"unit":"米 / m"}  | 目标点高度（椭球高）  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"height": 100,
		"latitude": 12.23,
		"locked": true,
		"longitude": 12.23,
		"payload_index": "39-0-7"
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "camera_look_at"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** camera_look_at
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "camera_look_at"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#%E8%B4%9F%E8%BD%BD%E6%8E%A7%E5%88%B6%E2%80%94%E5%88%86%E5%B1%8F) 负载控制—分屏
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** camera_screen_split
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| payload_index  | 相机枚举  | text  |   | 相机枚举值。非标准的 device_mode_key，格式为 {type-subtype-gimbalindex}，可以参考[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)  |  
| enable  | 是否使能分屏  | bool  |   | 开启还是关闭分屏  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"enable": true,
		"payload_index": "39-0-7"
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "camera_screen_split"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** camera_screen_split
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "camera_screen_split"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#%E8%B4%9F%E8%BD%BD%E6%8E%A7%E5%88%B6%E2%80%94%E7%85%A7%E7%89%87%E5%AD%98%E5%82%A8%E8%AE%BE%E7%BD%AE) 负载控制—照片存储设置
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** photo_storage_set
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| payload_index  | 相机枚举  | text  |   | 相机枚举值。非标准的 device_mode_key，格式为 {type-subtype-gimbalindex}，可以参考[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)  |  
| photo_storage_settings  | 照片存储设置集合  | array  | {"size": -, "item_type": enum_string}  | 拍照存储类型{current, wide, zoom, ir}，可多选  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"payload_index": "39-0-7",
		"photo_storage_settings": [
			"current",
			"wide",
			"zoom",
			"ir"
		]
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "photo_storage_set"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** photo_storage_set
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "photo_storage_set"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#%E8%B4%9F%E8%BD%BD%E6%8E%A7%E5%88%B6%E2%80%94%E8%A7%86%E9%A2%91%E5%AD%98%E5%82%A8%E8%AE%BE%E7%BD%AE) 负载控制—视频存储设置
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** video_storage_set
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| payload_index  | 相机枚举  | text  |   | 相机枚举值。非标准的 device_mode_key，格式为 {type-subtype-gimbalindex}，可以参考[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)  |  
| video_storage_settings  | 视频存储设置集合  | array  | {"size": -, "item_type": enum_string}  | 视频存储类型{current, wide, zoom, ir}，可多选  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"payload_index": "39-0-7",
		"video_storage_settings": [
			"current",
			"wide",
			"zoom",
			"ir"
		]
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "video_storage_set"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** video_storage_set
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "video_storage_set"
}
```
#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#drc) DRC
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#drc-%E9%A3%9E%E8%A1%8C%E6%8E%A7%E5%88%B6) DRC-飞行控制
进入指令飞行模式后允许通过该指令控制飞行器航行方向与速度，发送的频率需要保持在**5-10hz** 以内让设备能够比较精准的控制速度变化与方向。
**Topic:** thing/product/_{gateway_sn}_ /drc/down
**Direction:** down
**Method:** drone_control
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| seq  | 命令序号  | int  |   | 递增的序号，保证指令顺序执行。若 x、y、h、w 参数发生变化，seq 需要从 0 开始增长。  |  
| x  | 前进后退方向的速度  | double  | {"max":17,"min":-17,"unit":"米每秒 / m/s"}  | 前进后退的最大速度，负值表示向后移动  |  
| y  | 左右方向的速度  | double  | {"max":17,"min":-17,"unit":"米每秒 / m/s"}  | 左右移动的最大速度，负值表示向左移动  |  
| h  | 上下方向的速度  | double  | {"max":5,"min":-4,"unit":"米每秒 / m/s"}  | 向上向下移动的最大速度，负值表示向下移动  |  
| w  | 机身角速度  | double  | {"max":90,"min":-90,"unit":"弧度每秒 / rad/s"}  | 顺时针与逆时针的最大角速度，负值表示逆时针转动  |  
**Example:**
```
{
	"data": {
		"h": 2.76,
		"seq": 1,
		"w": 2.86,
		"x": 2.34,
		"y": -2.45
	},
	"method": "drone_control"
}
```
**Topic:** thing/product/_{gateway_sn}_ /drc/up
**Direction:** up
**Method:** drone_control
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误，异常case：没有飞行控制权，没有虚拟摇杆权限，数据包序号不对  |  
| output  | 输出  | struct  |   |   |  
| »seq  | 命令序号  | int  |   | 递增的序号，保证指令顺序执行  |  
**Example:**
```
{
	"data": {
		"output": {
			"seq": 1
		},
		"result": 0
	},
	"method": "drone_control"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#drc-%E9%A3%9E%E8%A1%8C%E5%99%A8%E6%80%A5%E5%81%9C) DRC-飞行器急停
**Topic:** thing/product/_{gateway_sn}_ /drc/down
**Direction:** down
**Method:** drone_emergency_stop
**Data:** null
**Example:**
```
{
	"data": {},
	"method": "drone_emergency_stop"
}
```
**Topic:** thing/product/_{gateway_sn}_ /drc/up
**Direction:** up
**Method:** drone_emergency_stop
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"data": {
		"result": 0
	},
	"method": "drone_emergency_stop"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#drc-%E5%BF%83%E8%B7%B3) DRC-心跳
**Topic:** thing/product/_{gateway_sn}_ /drc/down
**Direction:** down
**Method:** heart_beat
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| seq  | 命令序号  | int  |   | 递增的序号，保证指令顺序执行  |  
| timestamp  | 心跳发送时间戳  | int  | {"unit":"毫秒 / ms"}  | 收到的心跳发送时的时间戳，非设备端的时间，便于云端根据收发的间隔做时延计算  |  
**Example:**
```
{
	"data": {
		"seq": 10,
		"timestamp": 1670415891013
	},
	"method": "heart_beat"
}
```
**Topic:** thing/product/_{gateway_sn}_ /drc/up
**Direction:** up
**Method:** heart_beat
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| seq  | 命令序号  | int  |   | 递增的序号，保证指令顺序执行  |  
| timestamp  | 心跳发送时间戳  | int  | {"unit":"毫秒 / ms"}  | 收到的心跳发送时的时间戳，非设备端的时间，便于云端根据收发的间隔做时延计算  |  
**Example:**
```
{
	"data": {
		"seq": 10,
		"timestamp": 1670415891013
	},
	"method": "heart_beat"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#drc-%E9%81%BF%E9%9A%9C%E4%BF%A1%E6%81%AF%E4%B8%8A%E6%8A%A5) DRC-避障信息上报
**Topic:** thing/product/_{gateway_sn}_ /drc/up
**Direction:** up
**Method:** hsi_info_push
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| up_distance  | 上方的障碍物距离  | int  | {"unit":"毫米 / mm"}  |   |  
| down_distance  | 下方的障碍物距离  | int  | {"unit":"毫米 / mm"}  |   |  
| up_enable  | 上视避障开关状态  | bool  |   |   |  
| up_work  | 上视避障工作状态  | bool  |   |   |  
| down_enable  | 下视避障开关状态  | bool  |   |   |  
| down_work  | 下视避障工作状态  | bool  |   |   |  
| left_enable  | 左视避障开关状态  | bool  |   |   |  
| left_work  | 左视避障工作状态  | bool  |   |   |  
| right_enable  | 右视避障开关状态  | bool  |   |   |  
| right_work  | 右视避障工作状态  | bool  |   |   |  
| front_enable  | 前视避障开关状态  | bool  |   |   |  
| front_work  | 前视避障工作状态  | bool  |   |   |  
| back_enable  | 后视避障开关状态  | bool  |   |   |  
| back_work  | 后视避障工作状态  | bool  |   |   |  
| vertical_enable  | 垂直避障开关状态  | bool  |   |   |  
| vertical_work  | 垂直避障工作状态  | bool  |   |   |  
| horizontal_enable  | 水平避障开关状态  | bool  |   |   |  
| horizontal_work  | 水平避障工作状态  | bool  |   |   |  
| around_distances  | 周边的障碍物距离  | array  | {"size": 360, "item_type": int}  | 水平方向观察点，分布在[0,360)的角度区间，0对应机头方向正前方，顺时针分布，例如0度为机头正前方，90度为飞行器正右方。每个数值表示该角度上障碍物与飞行器距离，60000 表示该角度没有障碍物。若上报空数组，意味任意角度都无障碍物。若上报 4 个数据的数组，意味该数据为 TOF 避障数据，在红外避障失效时上报，譬如夜晚场景。  |  
**Example:**
```
"{\n        \"method\": \"hsi_info_push\",\n        \"timestamp\": 1670415891013,\n        \"data\": {\n          \"up_distance\": 10,\n          \"down_distance\": 10,\n          \"around_distances\": [\n            10,\n            8,\n            9,\n            16,\n            2,\n            60000,\n            60000,\n            60000,\n            ...\n          ],\n          \"up_enable\": true,\n          \"up_work\": true,\n          \"down_enable\": true,\n          \"down_work\": true,\n          \"left_enable\": true,\n          \"left_work\": true,\n          \"right_enable\": true,\n          \"right_work\": true,\n          \"front_enable\": true,\n          \"front_work\": true,\n          \"back_enable\": true,\n          \"back_work\": true,\n          \"vertical_enable\": true,\n          \"vertical_work\": true,\n          \"horizontal_enable\": true,\n          \"horizontal_work\": true\n        }\n      }"
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#drc-%E5%9B%BE%E4%BC%A0%E9%93%BE%E8%B7%AF%E5%BB%B6%E6%97%B6%E4%BF%A1%E6%81%AF%E4%B8%8A%E6%8A%A5) DRC-图传链路延时信息上报
**Topic:** thing/product/_{gateway_sn}_ /drc/up
**Direction:** up
**Method:** delay_info_push
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| sdr_cmd_delay  | 图传协议命令链路延时  | int  | {"unit":"毫秒 / ms"}  | 图传协议命令链路延时  |  
| liveview_delay_list  | 图传视频码流延时  | array  | {"size": -, "item_type": struct}  | 图传视频码流延时，多路码流  |  
| »video_id  | 码流编号  | text  |   | 码流编号  |  
| »liveview_delay_time  | 码流延时  | int  | {"unit":"毫秒 / ms"}  | 码流延时  |  
**Example:**
```
{
	"data": {
		"liveview_delay_list": [
			{
				"liveview_delay_time": 60,
				"video_id": "1581BN210004555439234/52-0-0/normal-0"
			},
			{
				"liveview_delay_time": 80,
				"video_id": "1581BN210004555439234/53-0-0/normal-0"
			}
		],
		"sdr_cmd_delay": 10
	},
	"timestamp": 1670415891013,
	"method": "delay_info_push"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/drc.html#drc-%E9%AB%98%E9%A2%91-osd-%E4%BF%A1%E6%81%AF%E4%B8%8A%E6%8A%A5) DRC-高频 osd 信息上报
**Topic:** thing/product/_{gateway_sn}_ /drc/up
**Direction:** up
**Method:** osd_info_push
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| attitude_head  | 飞行器姿态 head 角  | double  | {"unit":"度 / °"}  | 飞行器姿态 head 角  |  
| latitude  | 飞行器纬度  | double  | {"unit":"度 / °"}  |   |  
| longitude  | 飞行器经度  | double  | {"unit":"度 / °"}  |   |  
| height  | 飞行器高度  | double  | {"unit":"度 / °"}  | 飞行器海拔高度  |  
| speed_x  | 当前飞行器 x 坐标方向的速度  | double  | {"unit":"米每秒 / m/s"}  | 当前飞行器 x 坐标方向的速度  |  
| speed_y  | 当前飞行器 y 坐标方向的速度  | double  | {"unit":"米每秒 / m/s"}  | 当前飞行器 y 坐标方向的速度  |  
| speed_z  | 当前飞行器 z 坐标方向的速度  | double  | {"unit":"米每秒 / m/s"}  |   |  
| gimbal_pitch  | 云台 pitch 角  | double  | {"unit":"度 / °"}  |   |  
| gimbal_roll  | 云台 roll 角  | double  | {"unit":"度 / °"}  |   |  
| gimbal_yaw  | 云台 yaw 角  | double  | {"unit":"度 / °"}  |   |  
**Example:**
```
{
	"data": {
		"attitude_head": 60,
		"gimbal_pitch": 60,
		"gimbal_roll": 60,
		"gimbal_yaw": 60,
		"height": 10,
		"latitude": 10,
		"longitude": 10,
		"speed_x": 10,
		"speed_y": 10,
		"speed_z": 10
	},
	"timestamp": 1670415891013,
	"method": "osd_info_push"
}
```