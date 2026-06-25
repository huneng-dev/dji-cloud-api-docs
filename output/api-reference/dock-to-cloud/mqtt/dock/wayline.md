---
source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/wayline.html
path: api-reference/dock-to-cloud/mqtt/dock/wayline
---

#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/wayline.html#event) Event
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/wayline.html#%E8%AE%BE%E5%A4%87%E8%BF%94%E8%88%AA%E9%80%80%E5%87%BA%E7%8A%B6%E6%80%81%E9%80%9A%E7%9F%A5) 设备返航退出状态通知
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** device_exit_homing_notify
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| action  | 退出返航通知消息类型  | enum_int  | {"0":"退出”返航退出状态“","1":"进入”返航退出状态“"}  | 进入“返航退出状态”，指当机场处于返航模式时，由于 `reason` 字段中展示的原因，退出了返航过程。相似的，退出“返航退出状态”，指机场停止了退出返航这一过程。  |  
| reason  | 退出返航原因  | enum_int  | {"0":"操纵杆油门添加","1":"操纵杆间距添加","2":"行为树初始化失败","3":"被障碍物包围","4":"触发限飞限制","5":"障碍物距离太近","6":"无 GPS 信号","7":"GPS 和 VIO 位置输出标志为 false","8":"GPS 和 VIO 融合位置误差太大","9":"短距离回溯","10":"近距离触发返航"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"action": 1,
		"reason": "0",
		"sn": "机场 SN"
	},
	"need_reply": 1,
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp:": 1654070968655,
	"method": "device_exit_homing_notify"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/wayline.html#%E4%B8%8A%E6%8A%A5%E8%88%AA%E7%BA%BF%E4%BB%BB%E5%8A%A1%E8%BF%9B%E5%BA%A6) 上报航线任务进度
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** flighttask_progress
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| ext  | 扩展内容  | struct  |   |   |  
| »current_waypoint_index  | 当前执行到的航点数  | int  |   |   |  
| »wayline_mission_state  | 航线任务状态  | enum_int  | {"0":"断连","1":"不支持该航点","2":"航线准备状态,可上传文件,可执行已有文件","3":"航线文件上传中","4":"触发开始命令，飞行器触发读航线等逻辑，还未开始任务，处于准备状态","5":"进入航线,到第一个航点","6":"航线执行","7":"航线中断，触发条件：1.用户主动暂停 2.飞控异常","8":"航线恢复","9":"航线结束"}  |   |  
| »media_count  | 本次航线任务执行产生的媒体文件数量  | int  |   |   |  
| »track_id  | 航迹 ID  | text  |   |   |  
| »flight_id  | 任务 ID  | text  |   |   |  
| »break_point  | 航线断点信息  | struct  |   | 可选字段，用于告知云端本次航线任务断点信息  |  
| »»index  | 断点序号  | int  |   |   |  
| »»state  | 断点状态  | enum_int  | {"0":"在航段上","1":"在航点上"}  |   |  
| »»progress  | 当前航段进度  | float  | {"max":"1.0","min":"0"}  |   |  
| »»wayline_id  | 航线 ID  | int  |   |   |  
| »»break_reason  | 中断原因  | enum_int  | {}  |   |  
| »»latitude  | 断点纬度  | float  | {"max":"90","min":"-90","unit":"度 / °"}  |   |  
| »»longitude  | 断点经度  | float  | {"max":"180","min":"-180","unit":"度 / °"}  |   |  
| »»height  | 断点相对地球椭球面高度  | float  | {"unit":"米 / m"}  |   |  
| »»attitude_head  | 断点偏航轴角度  | float  |   | 偏航轴角度与真北角（经线）的角度，0到6点钟方向为正值，6到12点钟方向为负值  |  
| »wayline_id  | 当前在作业的航线ID  | int  |   | 包括进入航线的过渡阶段，例如0代表飞行器正在进入或者已经在执行第一条航线  |  
| status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","partially_done":"部分完成","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
| progress  | 进度  | struct  |   |   |  
| »current_step  | 执行步骤  | enum_int  | {"0":"初始状态","1":"启动前检查，飞行器是否在执行航线中","2":"启动前检查，机场是否退出工作模式","3":"启动前检查，航线执行中","4":"启动前检查，返航中","5":"航线执行进入准备状态，开始等待任务下发","6":"机场进入工作状态","7":"进入开机检查准备工作和开盖准备工作","8":"等待飞行系统准备就绪，推送连接建立","9":"等待 RTK 源监听有值上报","10":"检查 RTK 源是否是机场源，如果不是要重新设置","11":"等待飞行控制权通知","12":"机场无控制权，抢飞行器控制权抢夺","13":"获取最新 KMZ URL","14":"下载 KMZ","15":"KMZ 上传中","16":"染色配置","17":"飞行器起飞参数设置，备降点设置，起飞高度设置，染色设置","18":"飞行器 flyto 起飞参数设置","19":"Home 点设置","20":"触发执行航线","21":"航线执行中","22":"进入返航的检查准备工作","23":"飞行器降落机场","24":"降落以后的关盖","25":"机场退出工作模式","26":"机场异常恢复","27":"机场上传飞行系统日志","28":"相机录像状态检查","29":"获取媒体文件数量","30":"机场起飞开盖的异常恢复","31":"通知任务结果","32":"任务执行完成，通过配置文件配置，是否进行主动 log 拉取","33":"日志列表拉取 - 飞行器列表","34":"日志列表拉取 - 拉取机场列表","35":"日志列表拉取 - 上传日志列表结果","36":"日志拉取-拉取飞行器日志","37":"日志拉取-拉取机场日志","38":"日志拉取-压缩飞行器日志","39":"日志拉取-压缩机场日志","40":"日志拉取-上传飞行器日志","41":"日志拉取-上传机场日志","42":"日志拉取-通知结果","0xFFFD":"结束后等待服务回包","0xFFFE":"无具体状态","0xFFFFF":"UNKNOWN"}  |   |  
| »percent  | 进度值  | int  | {"max":"100","min":"0","step":"1"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"output": {
			"ext": {
				"break_point": {
					"attitude_head": 30,
					"break_reason": 1,
					"height": 100.23,
					"index": 1,
					"latitude": 23.4,
					"longitude": 113.99,
					"progress": 0.34,
					"state": 0,
					"wayline_id": 0
				},
				"current_waypoint_index": 3,
				"flight_id": "flight_id",
				"media_count": 6,
				"track_id": "track_id",
				"wayline_id": 0,
				"wayline_mission_state": 9
			},
			"progress": {
				"current_step": 19,
				"percent": 100
			},
			"status": "ok"
		},
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "flighttask_progress"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/wayline.html#%E4%BB%BB%E5%8A%A1%E5%B0%B1%E7%BB%AA%E9%80%9A%E7%9F%A5) 任务就绪通知
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** flighttask_ready
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| flight_ids  | 计划 ID  | array  | {"size": -, "item_type": text}  | 当前满足任务就绪条件的任务 ID 集合  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"flight_ids": [
			"aaaaaaa",
			"bbbbbbb"
		]
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "flighttask_ready"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/wayline.html#%E8%BF%94%E8%88%AA%E4%BF%A1%E6%81%AF) 返航信息
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** return_home_info
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| planned_path_points  | 规划的轨迹点列表  | array  | {"size": -, "item_type": struct}  | 飞行器实时规划的返航路线，数组中为一条完整的返航路线，每次推送为全量更新  |  
| »latitude  | 轨迹点纬度(角度值)  | double  | {"max":90,"min":-90}  | 轨迹点纬度，角度值，南纬是负，北纬是正，精度到小数点后6位  |  
| »longitude  | 轨迹点经度(角度值)  | double  | {"max":180,"min":-180}  | 轨迹点经度，角度值，东经是正，西经是负，精度到小数点后6位  |  
| »height  | 轨迹点高度  | float  | {"step":0.1,"unit":"米 / m"}  | 轨迹点高度,椭球高  |  
| last_point_type  | 返航路径最后一个点的类型  | enum_int  | {"0":"轨迹最后一个点在返航点的上空","1":"轨迹最后一个点不在返航点上空"}  | 轨迹planned_path_points最后一个点的类型。可用此字段，决定轨迹最后一个点的显示方式。0：轨迹最后一个点在返航点的地面上空。终端可以显示轨迹最后一个点到返航点的连线；1：轨迹最后一个点不是返航点。终端不应显示轨迹最后一个点到返航点的连线。无法到达返航点的原因：返航点在禁飞区或障碍物内  |  
| flight_id  | 任务 ID  | text  |   | 当前正在执行的航线任务id  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"flight_id": "abc",
		"last_point_type": 0,
		"planned_path_points": [
			{
				"height": 123.234,
				"latitude": 13.23,
				"longitude": 123.234
			}
		]
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "return_home_info"
}
```
#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/wayline.html#service) Service
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/wayline.html#%E5%88%9B%E5%BB%BA%E8%88%AA%E7%BA%BF%E4%BB%BB%E5%8A%A1-%E5%BA%9F%E5%BC%83) 创建航线任务（废弃）
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** flighttask_create
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| flight_id  | 计划 ID  | text  |   |   |  
| type  | 任务类型  | text  |   |   |  
| file  | 航线文件对象  | struct  |   |   |  
| »url  | 文件 URL  | text  |   |   |  
| »sign  | MD5 签名  | text  |   |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"file": {
			"sign": "xxxx",
			"url": "https://xxx.com/xxxx"
		},
		"flight_id": "xxxxxxx",
		"type": "wayline"
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp:": 1654070968655,
	"method": "flighttask_create"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** flighttask_create
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
	"timestamp:": 1654070968655,
	"method": "flighttask_create"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/wayline.html#%E4%B8%8B%E5%8F%91%E4%BB%BB%E5%8A%A1) 下发任务
若用户的云服务无法访问外网，需实现 [配置更新open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/config.html) 功能，下发可被云服务访问的 NTP 服务的 URL，以实现时钟同步，否则航线任务将无法正常执行。
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** flighttask_prepare
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| flight_id  | 计划 ID  | text  |   |   |  
| execute_time  | 开始执行时间  | int  | {"length":13}  | 任务开始执行时间毫秒时间戳。可选字段。当 `task_type` 为 0 或 1 时必填，为 2 时非必填。  |  
| task_type  | 任务类型  | enum_int  | {"0":"立即任务","1":"定时任务","2":"条件任务"}  | 立即任务和定时任务均由execute_time指定执行时间；条件任务支持ready_conditions字段指定任务就绪条件，设备可在指定时间段内满足就绪条件后即可执行；立即任务媒体上传优先级最高，定时任务和条件任务媒体上传优先级相同  |  
| wayline_type  | 航线类型  | enum_int  | {"0":"普通航点航线"}  |   |  
| file  | 航线文件对象  | struct  |   |   |  
| »url  | 文件 URL  | text  |   |   |  
| »fingerprint  | 文件签名  | text  |   | 文件内容 MD5 签名  |  
| ready_conditions  | 任务就绪条件  | struct  |   | 可选字段。条件任务（即 `task_type` 为2）时必填，其他类型任务会忽略该字段。下发条件任务后，设备会定频检查 `ready_conditions` 是否全部满足，若全部满足则会有 `flighttask_ready` 事件通知。且设备端接收 `flighttask_execute` 指令时，也会检查任务的 `ready_conditions` 是否已全部满足。  |  
| »battery_capacity  | 电池容量  | int  |   | 可执行任务的飞行器电池电量百分比阈值，任务开始执行时的飞行器电量必须大于 `battery_capacity`。  |  
| »begin_time  | 任务可执行时段的开始时间  | int  | {"length":13}  | 任务可执行时段起始时间毫秒时间戳，任务开始执行的时间必须大于 `begin_time`。  |  
| »end_time  | 任务可执行时段的结束时间  | int  | {"length":13}  | 任务可执行时段截止时间毫秒时间戳，任务开始执行的时间必须小于 `end_time`。  |  
| executable_conditions  | 任务执行条件  | struct  |   | 可选字段，用于在设备端增加任务执行的前置检查条件，存在任一条件不满足时会执行失败  |  
| »storage_capacity  | 存储容量  | int  |   | 可执行任务的机场或飞行器最低存储容量，机场或飞行器存储容量不满足 `storage_capacity` 时，任务执行失败。  |  
| break_point  | 航线断点信息  | struct  |   | 可选字段，用于断点续飞，若指定该字段，航线任务会从字段指定的断点位置开始执行。  |  
| »index  | 断点序号  | int  |   |   |  
| »state  | 断点状态  | enum_int  | {"0":"在航段上","1":"在航点上"}  |   |  
| »progress  | 当前航段进度  | float  | {"max":"1.0","min":"0"}  |   |  
| »wayline_id  | 航线 ID  | int  |   |   |  
| rth_altitude  | 返航高度  | int  | {"max":1500,"min":20,"unit":"米 / m"}  |   |  
| rth_mode  | 返航高度模式  | enum_int  | {"0":"智能高度","1":"设定高度"}  | 智能返航模式下，飞行器将自动规划最佳返航高度。大疆机场当前不支持设置返航高度模式，只能选择'设定高度'模式。当环境，光线不满足视觉系统要求时（譬如傍晚阳光直射、夜间弱光无光），飞行器将使用您设定的返航高度进行直线返航  |  
| out_of_control_action  | 遥控器失控动作  | enum_int  | {"0":"返航","1":"悬停","2":"降落"}  | 失控动作，当前固定传的值是 0，即返航。注意该枚举值定义跟飞控跟机场定义的不一致，机场端会进行转换。  |  
| exit_wayline_when_rc_lost  | 航线失控动作  | enum_int  | {"0":"继续执行航线任务","1":"退出航线任务，执行遥控器失控动作"}  | 保持跟 KMZ 文件一致  |  
| simulate_mission  | 是否在模拟器中执行任务  | struct  |   | 可选字段，用于在室内进行模拟任务调试。  |  
| »is_enable  | 是否开启模拟器任务  | enum_int  | {"0":"不开启","1":"开启"}  | 当次任务打开或关闭模拟器  |  
| »latitude  | 纬度  | double  | {"max":"90.0","min":"-90.0"}  |   |  
| »longitude  | 经度  | double  | {"max":"180.0","min":"-180.0"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"break_point": {
			"index": 1,
			"progress": 0.34,
			"state": 0,
			"wayline_id": 0
		},
		"executable_conditions": {
			"storage_capacity": 1000
		},
		"execute_time": 1234567890123,
		"exit_wayline_when_rc_lost": 0,
		"file": {
			"fingerprint": "xxxx",
			"url": "https://xxx.com/xxxx"
		},
		"flight_id": "xxxxxxx",
		"out_of_control_action": 0,
		"ready_conditions": {
			"battery_capacity": 90,
			"begin_time": 1234567890123,
			"end_time": 1234567890123
		},
		"rth_altitude": 100,
		"simulate_mission": {
			"is_enable": 1,
			"latitude": 22.1223,
			"longitude": 113.2222
		},
		"task_type": 2,
		"wayline_type": 1
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1234567890123,
	"method": "flighttask_prepare"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** flighttask_prepare
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
	"timestamp": 1234567890123,
	"method": "flighttask_prepare"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/wayline.html#%E6%89%A7%E8%A1%8C%E4%BB%BB%E5%8A%A1) 执行任务
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** flighttask_execute
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| flight_id  | 计划 ID  | text  |   |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"flight_id": "xxxxxxx"
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1234567890123,
	"method": "flighttask_execute"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** flighttask_execute
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
	"timestamp": 1234567890123,
	"method": "flighttask_execute"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/wayline.html#%E5%8F%96%E6%B6%88%E4%BB%BB%E5%8A%A1) 取消任务
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** flighttask_undo
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| flight_ids  | 计划 ID  | array  | {"size": -, "item_type": text}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"flight_ids": [
			"aaaaaaa",
			"bbbbbbb"
		]
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1234567890123,
	"method": "flighttask_undo"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** flighttask_undo
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
	"timestamp": 1234567890123,
	"method": "flighttask_undo"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/wayline.html#%E8%88%AA%E7%BA%BF%E6%9A%82%E5%81%9C) 航线暂停
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** flighttask_pause
**Data:** null
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "flighttask_pause"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** flighttask_pause
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
	"need_reply": 1,
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "flighttask_pause"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/wayline.html#%E8%88%AA%E7%BA%BF%E6%81%A2%E5%A4%8D) 航线恢复
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** flighttask_recovery
**Data:** null
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "flighttask_recovery"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** flighttask_recovery
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
	"need_reply": 1,
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "flighttask_recovery"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/wayline.html#%E4%B8%80%E9%94%AE%E8%BF%94%E8%88%AA) 一键返航
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** return_home
**Data:** null
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** return_home
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/wayline.html#%E5%8F%96%E6%B6%88%E8%BF%94%E8%88%AA) 取消返航
返航后，飞行器会退出航线模式，此时取消返航，飞行器会悬停
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** return_home_cancel
**Data:** null
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "return_home_cancel"
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** return_home_cancel
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
	"need_reply": 1,
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "return_home_cancel"
}
```
#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/wayline.html#requests) Requests
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/wayline.html#%E4%BB%BB%E5%8A%A1%E8%B5%84%E6%BA%90%E8%8E%B7%E5%8F%96) 任务资源获取
**Topic:** thing/product/_{gateway_sn}_ /requests
**Direction:** up
**Method:** flighttask_resource_get
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| flight_id  | 计划 ID  | text  |   |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"flight_id": "xxxxxxx"
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1234567890123,
	"method": "flighttask_resource_get"
}
```
**Topic:** thing/product/_{gateway_sn}_ /requests_reply
**Direction:** down
**Method:** flighttask_resource_get
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »file  | 航线文件对象  | struct  |   |   |  
| »»url  | 文件 URL  | text  |   |   |  
| »»fingerprint  | 文件签名  | text  |   | 文件 MD5 签名  |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"output": {
			"file": {
				"fingerprint": "signxxxx",
				"url": "https://xx.oss-cn-hangzhou.aliyuncs.com/xx.kmz?Expires=xx&OSSAccessKeyId=xxx&Signature=xxx"
			}
		},
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1234567890123,
	"method": "flighttask_resource_get"
}
```