---
source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html
path: api-reference/dock-to-cloud/mqtt/dock/dock1/cmd
---

#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#event) Event
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E5%BC%BA%E5%88%B6%E5%85%B3%E8%88%B1%E7%9B%96%E8%BF%9B%E5%BA%A6) 强制关舱盖进度
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** cover_force_close
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
| »progress  | 进度  | struct  |   |   |  
| »»percent  | 进度百分比  | int  | {"max":"100","min":"0","step":"1","unit_name":"百分比 / %"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"output": {
			"progress": {
				"percent": 6
			},
			"status": "in_progress"
		},
		"result": 0
	},
	"method": "cover_force_close",
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E9%A3%9E%E8%A1%8C%E5%99%A8%E5%BC%80%E6%9C%BA%E8%BF%9B%E5%BA%A6) 飞行器开机进度
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** drone_open
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"output": {
			"status": "in_progress"
		},
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "drone_open"
}
```
**Topic:** thing/product/_{gateway_sn}_ /events_reply
**Direction:** down
**Method:** drone_open
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"method": "drone_open",
	"tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
	"bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
	"timestamp": "1234567890123",
	"data": {
		"result": 0
	}
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E9%A3%9E%E8%A1%8C%E5%99%A8%E5%85%B3%E6%9C%BA%E8%BF%9B%E5%BA%A6) 飞行器关机进度
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** drone_close
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
| »progress  | 进度  | struct  |   |   |  
| »»percent  | 进度百分比  | int  | {"max":"100","min":"0","step":"1","unit_name":"百分比 / %"}  |   |  
| »»step_key  | 当前步骤  | enum_string  | {"get_bid":"获取bid","check_ac_input_state":"检查市电供电状态","upgrading_prevent_reboot":"检查工作模式是否在升级","check_work_mode":"检查工作模式是否远程调试","check_task_state":"检查调试模式任务互斥状态","check_scram_state":"检查急停开关状态","close_drone":"关闭飞机"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"output": {
			"progress": {
				"percent": 20,
				"step_key": "check_work_mode"
			},
			"status": "in_progress"
		},
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "drone_close"
}
```
**Topic:** thing/product/_{gateway_sn}_ /events_reply
**Direction:** down
**Method:** drone_close
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"method": "drone_close",
	"tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
	"bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
	"timestamp": "1234567890123",
	"data": {
		"result": 0
	}
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E6%9C%BA%E5%9C%BA%E9%87%8D%E5%90%AF%E8%BF%9B%E5%BA%A6) 机场重启进度
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** device_reboot
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
| »progress  | 进度  | struct  |   |   |  
| »»percent  | 进度百分比  | int  | {"max":"100","min":"0","step":"1","unit_name":"百分比 / %"}  |   |  
| »»step_key  | 当前步骤  | enum_string  | {"get_bid":"获取bid","check_ac_input_state":"检查市电供电状态","upgrading_prevent_reboot":"检查工作模式是否在升级","check_work_mode":"检查工作模式是否远程调试","check_task_state":"检查调试模式任务互斥状态","write_reboot_param_file":"写入重启标志位"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"output": {
			"progress": {
				"percent": 20,
				"step_key": "write_reboot_param_file"
			},
			"status": "in_progress"
		},
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "device_reboot"
}
```
**Topic:** thing/product/_{gateway_sn}_ /events_reply
**Direction:** down
**Method:** device_reboot
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"method": "device_reboot",
	"tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
	"bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
	"timestamp": "1234567890123",
	"data": {
		"result": 0
	}
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E5%85%B3%E9%97%AD%E8%88%B1%E7%9B%96%E8%BF%9B%E5%BA%A6) 关闭舱盖进度
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** cover_close
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
| »progress  | 进度  | struct  |   |   |  
| »»percent  | 进度百分比  | int  | {"max":"100","min":"0","step":"1","unit_name":"百分比 / %"}  |   |  
| »»step_key  | 当前步骤  | enum_string  | {"get_bid":"获取bid","check_work_mode":"检查工作模式是否远程调试","check_task_state":"检查调试模式任务互斥状态","check_scram_state":"检查急停开关状态","turn_on_drone":"打开飞机","drone_paddle_forward":"飞机正慢转桨","close_cover":"关闭舱盖","drone_paddle_reverse":"飞机反慢转桨","drone_paddle_stop":"飞机停桨"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"output": {
			"progress": {
				"percent": 58,
				"step_key": "drone_paddle_reverse"
			},
			"status": "in_progress"
		},
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "cover_close"
}
```
**Topic:** thing/product/_{gateway_sn}_ /events_reply
**Direction:** down
**Method:** cover_close
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"method": "cover_close",
	"tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
	"bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
	"timestamp": "1234567890123",
	"data": {
		"result": 0
	}
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E6%89%93%E5%BC%80%E8%88%B1%E7%9B%96%E8%BF%9B%E5%BA%A6) 打开舱盖进度
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** cover_open
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
| »progress  | 进度  | struct  |   |   |  
| »»percent  | 进度百分比  | int  | {"max":"100","min":"0","step":"1","unit_name":"百分比 / %"}  |   |  
| »»step_key  | 当前步骤  | enum_string  | {"get_bid":"获取bid","check_work_mode":"检查工作模式是否远程调试","check_task_state":"检查调试模式任务互斥状态","check_scram_state":"检查急停开关状态","open_cover":"打开舱盖"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"output": {
			"progress": {
				"percent": 70,
				"step_key": "open_cover"
			},
			"status": "in_progress"
		},
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "cover_open"
}
```
**Topic:** thing/product/_{gateway_sn}_ /events_reply
**Direction:** down
**Method:** cover_open
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"method": "cover_open",
	"tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
	"bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
	"timestamp": "1234567890123",
	"data": {
		"result": 0
	}
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E6%89%93%E5%BC%80%E5%85%85%E7%94%B5%E8%BF%9B%E5%BA%A6) 打开充电进度
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** charge_open
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
| »progress  | 进度  | struct  |   |   |  
| »»percent  | 进度百分比  | int  | {"max":"100","min":"0","step":"1","unit_name":"百分比 / %"}  |   |  
| »»step_key  | 当前步骤  | enum_string  | {"get_bid":"获取bid","check_work_mode":"检查工作模式是否远程调试","check_task_state":"检查调试模式任务互斥状态","check_scram_state":"检查急停开关状态","check_cover":"检查舱盖状态","start_charge":"开启充电"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"output": {
			"progress": {
				"percent": 45,
				"step_key": "start_charge"
			},
			"status": "in_progress"
		},
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "charge_open"
}
```
**Topic:** thing/product/_{gateway_sn}_ /events_reply
**Direction:** down
**Method:** charge_open
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"method": "charge_open",
	"tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
	"bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
	"timestamp": "1234567890123",
	"data": {
		"result": 0
	}
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E5%85%B3%E9%97%AD%E5%85%85%E7%94%B5%E8%BF%9B%E5%BA%A6) 关闭充电进度
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** charge_close
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
| »progress  | 进度  | struct  |   |   |  
| »»percent  | 进度百分比  | int  | {"max":"100","min":"0","step":"1","unit_name":"百分比 / %"}  |   |  
| »»step_key  | 当前步骤  | enum_string  | {"get_bid":"获取bid","check_work_mode":"检查工作模式是否远程调试","check_task_state":"检查调试模式任务互斥状态","stop_charge":"停止充电"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"output": {
			"progress": {
				"percent": 80,
				"step_key": "stop_charge"
			},
			"status": "in_progress"
		},
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "charge_close"
}
```
**Topic:** thing/product/_{gateway_sn}_ /events_reply
**Direction:** down
**Method:** charge_close
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"method": "charge_close",
	"tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
	"bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
	"timestamp": "1234567890123",
	"data": {
		"result": 0
	}
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E9%A3%9E%E8%A1%8C%E5%99%A8%E6%95%B0%E6%8D%AE%E6%A0%BC%E5%BC%8F%E5%8C%96%E8%BF%9B%E5%BA%A6) 飞行器数据格式化进度
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** drone_format
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
| »progress  | 进度  | struct  |   |   |  
| »»percent  | 进度百分比  | int  | {"max":"100","min":"0","step":"1","unit_name":"百分比 / %"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"output": {
			"progress": {
				"percent": 80,
				"step_key": "xxx"
			},
			"status": "in_progress"
		},
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "drone_format"
}
```
**Topic:** thing/product/_{gateway_sn}_ /events_reply
**Direction:** down
**Method:** drone_format
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"method": "drone_format",
	"tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
	"bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
	"timestamp": "1234567890123",
	"data": {
		"result": 0
	}
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E6%9C%BA%E5%9C%BA%E6%95%B0%E6%8D%AE%E6%A0%BC%E5%BC%8F%E5%8C%96%E8%BF%9B%E5%BA%A6) 机场数据格式化进度
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** device_format
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
| »progress  | 进度  | struct  |   |   |  
| »»percent  | 进度百分比  | int  | {"max":"100","min":"0","step":"1","unit_name":"百分比 / %"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"output": {
			"progress": {
				"percent": 80,
				"step_key": "xxx"
			},
			"status": "in_progress"
		},
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "device_format"
}
```
**Topic:** thing/product/_{gateway_sn}_ /events_reply
**Direction:** down
**Method:** device_format
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"method": "device_format",
	"tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
	"bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
	"timestamp": "1234567890123",
	"data": {
		"result": 0
	}
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E6%8E%A8%E6%9D%86%E9%97%AD%E5%90%88%E8%BF%9B%E5%BA%A6) 推杆闭合进度
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** putter_close
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   |   |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
| »progress  | 进度  | struct  |   |   |  
| »»percent  | 进度百分比  | int  | {"max":"100","min":"0","step":"1","unit_name":"百分比 / %"}  |   |  
| »»step_key  | 当前步骤  | enum_string  | {"get_bid":"获取bid","check_work_mode":"检查工作模式是否远程调试","check_task_state":"检查调试模式任务互斥状态","check_scram_state":"检查急停开关状态","close_putter":"闭合推杆"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"output": {
			"progress": {
				"percent": 30,
				"step_key": "check_work_mode"
			},
			"status": "in_progress"
		},
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "putter_close"
}
```
**Topic:** thing/product/_{gateway_sn}_ /events_reply
**Direction:** down
**Method:** putter_close
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"method": "putter_close",
	"tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
	"bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
	"timestamp": "1234567890123",
	"data": {
		"result": 0
	}
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E6%8E%A8%E6%9D%86%E5%B1%95%E5%BC%80%E8%BF%9B%E5%BA%A6) 推杆展开进度
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** putter_open
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   |   |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
| »progress  | 进度  | struct  |   |   |  
| »»percent  | 进度百分比  | int  | {"max":"100","min":"0","step":"1","unit_name":"百分比 / %"}  |   |  
| »»step_key  | 当前步骤  | enum_string  | {"get_bid":"获取bid","check_work_mode":"检查工作模式是否远程调试","check_task_state":"检查调试模式任务互斥状态","check_scram_state":"检查急停开关状态","free_putter":"释放推杆"}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"output": {
			"progress": {
				"percent": 80,
				"step_key": "free_putter"
			},
			"status": "in_progress"
		},
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"method": "putter_open"
}
```
**Topic:** thing/product/_{gateway_sn}_ /events_reply
**Direction:** down
**Method:** putter_open
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
**Example:**
```
{
	"method": "putter_open",
	"tid": "6a7bfe89-c386-4043-b600-b518e10096cc",
	"bid": "42a19f36-5117-4520-bd13-fd61d818d52e",
	"timestamp": "1234567890123",
	"data": {
		"result": 0
	}
}
```
#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#service) Service
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E5%BC%BA%E5%88%B6%E5%85%B3%E8%88%B1%E7%9B%96) 强制关舱盖
机场“设备属性”推送的 `drone_in_dock` 字段值为 0 时，且通过机场摄像头观看确认飞行器不在舱内后，可调用该指令强制关闭舱盖。否则可能导致桨叶被夹。
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** cover_force_close
**Data:** null
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** cover_force_close
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E8%B0%83%E8%AF%95%E6%A8%A1%E5%BC%8F%E5%BC%80%E5%90%AF) 调试模式开启
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** debug_mode_open
**Data:** null
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** debug_mode_open
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E8%B0%83%E8%AF%95%E6%A8%A1%E5%BC%8F%E5%85%B3%E9%97%AD) 调试模式关闭
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** debug_mode_close
**Data:** null
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** debug_mode_close
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E6%89%93%E5%BC%80%E8%A1%A5%E5%85%89%E7%81%AF) 打开补光灯
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** supplement_light_open
**Data:** null
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** supplement_light_open
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E5%85%B3%E9%97%AD%E8%A1%A5%E5%85%89%E7%81%AF) 关闭补光灯
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** supplement_light_close
**Data:** null
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** supplement_light_close
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E7%94%B5%E6%B1%A0%E4%BF%9D%E5%85%BB%E7%8A%B6%E6%80%81%E5%88%87%E6%8D%A2) 电池保养状态切换
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** battery_maintenance_switch
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| action  | 操作  | enum_int  | {"0":"关闭","1":"开启"}  |   |  
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** battery_maintenance_switch
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E6%9C%BA%E5%9C%BA%E7%A9%BA%E8%B0%83%E5%B7%A5%E4%BD%9C%E6%A8%A1%E5%BC%8F%E5%88%87%E6%8D%A2) 机场空调工作模式切换
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** air_conditioner_mode_switch
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| action  | 操作  | enum_int  | {"0":"使机场空调进入空闲模式(关闭制冷、制热或除湿)","1":"使机场空调进入制冷模式","2":"使机场空调进入制热模式","3":"使机场空调进入除湿模式(除湿包含制冷除湿及制热除湿，由设备端根据自身所处情况自动化处理，无需用户介入)"}  |   |  
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** air_conditioner_mode_switch
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E6%9C%BA%E5%9C%BA%E5%A3%B0%E5%85%89%E6%8A%A5%E8%AD%A6%E5%BC%80%E5%85%B3) 机场声光报警开关
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** alarm_state_switch
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| action  | 操作  | enum_int  | {"0":"关闭","1":"开启"}  |   |  
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** alarm_state_switch
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E7%94%B5%E6%B1%A0%E8%BF%90%E8%A1%8C%E6%A8%A1%E5%BC%8F%E5%88%87%E6%8D%A2) 电池运行模式切换
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** battery_store_mode_switch
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| action  | 操作  | enum_int  | {"1":"计划模式","2":"待命模式"}  |   |  
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** battery_store_mode_switch
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E6%9C%BA%E5%9C%BA%E9%87%8D%E5%90%AF) 机场重启
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** device_reboot
**Data:** null
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** device_reboot
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E9%A3%9E%E8%A1%8C%E5%99%A8%E5%BC%80%E6%9C%BA) 飞行器开机
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** drone_open
**Data:** null
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** drone_open
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E9%A3%9E%E8%A1%8C%E5%99%A8%E5%85%B3%E6%9C%BA) 飞行器关机
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** drone_close
**Data:** null
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** drone_close
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E6%9C%BA%E5%9C%BA%E6%95%B0%E6%8D%AE%E6%A0%BC%E5%BC%8F%E5%8C%96) 机场数据格式化
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** device_format
**Data:** null
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** device_format
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E9%A3%9E%E8%A1%8C%E5%99%A8%E6%95%B0%E6%8D%AE%E6%A0%BC%E5%BC%8F%E5%8C%96) 飞行器数据格式化
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** drone_format
**Data:** null
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** drone_format
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E6%89%93%E5%BC%80%E8%88%B1%E7%9B%96) 打开舱盖
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** cover_open
**Data:** null
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** cover_open
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E5%85%B3%E9%97%AD%E8%88%B1%E7%9B%96) 关闭舱盖
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** cover_close
**Data:** null
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** cover_close
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E6%89%93%E5%BC%80%E5%85%85%E7%94%B5) 打开充电
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** charge_open
**Data:** null
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** charge_open
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E5%85%B3%E9%97%AD%E5%85%85%E7%94%B5) 关闭充电
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** charge_close
**Data:** null
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** charge_close
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E5%A2%9E%E5%BC%BA%E5%9B%BE%E4%BC%A0%E5%BC%80%E5%85%B3) 增强图传开关
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** sdr_workmode_switch
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| link_workmode  | 图传模式  | enum_int  | {"0":"仅使用 SDR","1":"4G 增强模式"}  | 在 4G 增强模式下，SDR 与 4G 会同时使用  |  
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** sdr_workmode_switch
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E6%8E%A8%E6%9D%86%E5%B1%95%E5%BC%80) 推杆展开
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** putter_open
**Data:** null
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** putter_open
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   |   |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html#%E6%8E%A8%E6%9D%86%E9%97%AD%E5%90%88) 推杆闭合
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** putter_close
**Data:** null
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** putter_close
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   |   |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |