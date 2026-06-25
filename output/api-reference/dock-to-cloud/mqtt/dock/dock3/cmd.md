<!-- source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html -->
<!-- path: api-reference/dock-to-cloud/mqtt/dock/dock3/cmd -->

#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#event) Event
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#esim-%E7%9A%84%E8%BF%90%E8%90%A5%E5%95%86%E5%88%87%E6%8D%A2%E8%BF%9B%E5%BA%A6) eSIM 的运营商切换进度
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** esim_operator_switch
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   |   |  
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
				"percent": 0
			},
			"status": "in_progress"
		},
		"result": 0
	},
	"gateway": "dock_sn",
	"method": "esim_operator_switch",
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp:": 1654070968655
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#esim-%E6%BF%80%E6%B4%BB%E8%BF%9B%E5%BA%A6) eSIM 激活进度
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** esim_activate
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   |   |  
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
				"percent": 0
			},
			"status": "in_progress"
		},
		"result": 0
	},
	"gateway": "dock_sn",
	"method": "esim_activate",
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp:": 1654070968655
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E6%9C%BA%E5%9C%BA%E6%95%B0%E6%8D%AE%E6%A0%BC%E5%BC%8F%E5%8C%96%E8%BF%9B%E5%BA%A6) 机场数据格式化进度
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
	"timestamp:": 1654070968655,
	"method": "device_format"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E9%A3%9E%E8%A1%8C%E5%99%A8%E6%95%B0%E6%8D%AE%E6%A0%BC%E5%BC%8F%E5%8C%96%E8%BF%9B%E5%BA%A6) 飞行器数据格式化进度
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
	"timestamp:": 1654070968655,
	"method": "drone_format"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E5%85%B3%E9%97%AD%E5%85%85%E7%94%B5%E8%BF%9B%E5%BA%A6) 关闭充电进度
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
	"timestamp:": 1654070968655,
	"method": "charge_close"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E6%89%93%E5%BC%80%E5%85%85%E7%94%B5%E8%BF%9B%E5%BA%A6) 打开充电进度
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
				"step_key": "close_putter"
			},
			"status": "in_progress"
		},
		"result": 0
	},
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp:": 1654070968655,
	"method": "charge_open"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E6%89%93%E5%BC%80%E8%88%B1%E7%9B%96%E8%BF%9B%E5%BA%A6) 打开舱盖进度
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
	"timestamp:": 1654070968655,
	"method": "cover_open"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E5%85%B3%E9%97%AD%E8%88%B1%E7%9B%96%E8%BF%9B%E5%BA%A6) 关闭舱盖进度
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
	"timestamp:": 1654070968655,
	"method": "cover_close"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E6%9C%BA%E5%9C%BA%E9%87%8D%E5%90%AF%E8%BF%9B%E5%BA%A6) 机场重启进度
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
	"timestamp:": 1654070968655,
	"method": "device_reboot"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E5%BC%BA%E5%88%B6%E5%85%B3%E8%88%B1%E7%9B%96%E8%BF%9B%E5%BA%A6) 强制关舱盖进度
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
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E9%A3%9E%E8%A1%8C%E5%99%A8%E5%85%B3%E6%9C%BA%E8%BF%9B%E5%BA%A6) 飞行器关机进度
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
	"timestamp:": 1654070968655,
	"method": "drone_close"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E9%A3%9E%E8%A1%8C%E5%99%A8%E5%BC%80%E6%9C%BA%E8%BF%9B%E5%BA%A6) 飞行器开机进度
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
	"timestamp:": 1654070968655,
	"method": "drone_open"
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E4%B8%80%E9%94%AE%E6%A0%87%E5%AE%9A%E7%BB%93%E6%9E%9C) 一键标定结果
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** rtk_calibration
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| output  | 输出  | struct  |   | 标定执行输出信息  |  
| » ext  | 附加信息  | struct  |   | 附加信息  |  
| »» devices  | 标定设备集合  | array  |   | 标定设备结果列表  |  
| »»» sn  | 设备序列号  | string  |   | 设备序列号（SN）  |  
| »»» type  | 标定类型  | int  | {1: 手动标定}  | 标定类型  |  
| »»» module  | 模块  | string  | { "3": 机场, "6": 中继 }  | 设备所属模块  |  
| »»» result  | 结果码  | int  |   | 标定结果码（0 表示成功，非 0 表示错误）  |  
| »»» status  | 设备状态  | string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  | 设备标定状态（超时返回 "failed" 并提供错误码）  |  
| »» version  | 标定版本  | int  |   | 标定版本号  |  
| » progress  | 进度  | struct  |   | 标定整体进度，设备仅在有结果时推送  |  
| »» percent  | 进度百分比  | int  |   | 进度百分比，仅包含两个值，ok时为100，failed时为0）  |  
| »» current_step  | 当前步骤  | int  |   | 固定值 1  |  
| » status  | 任务状态  | enum_string  | {failed":"失败","ok":"执行成功"}  | 所有设备都标定成功时返回ok,任一设备失败返回failed  |  
| result  | 返回码  | int  |   | 固定为0，具体标定设备的错误码到标定结果列表中查看  |  
###  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E7%A4%BA%E4%BE%8B) 示例
```
{
  "method": "rtk_calibration",
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp": 1676948902792,
  "need_reply": 1,
  "data": {
    "output": {
      "ext": {
        "devices": [
          {
            "sn": "string",
            "type": 1,
            "module": "3",
            "result": 0,
            "status": "ok"
          },
          {
            "sn": "string",
            "type": 1,
            "module": "6",
            "result": 341010,
            "status": "failed"
          }
        ],
        "version": 1
      },
      "progress": {
        "percent": 0,
        "current_step": 1
      },
      "status": "failed"
    },
    "result": 0
  },
  "gateway": "sn"
}
```
#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#service) Service
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#esim-%E7%9A%84%E8%BF%90%E8%90%A5%E5%95%86%E5%88%87%E6%8D%A2) eSIM 的运营商切换
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** esim_operator_switch
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| imei  | dongle imei  | text  |   | 标识要操作的 Dongle  |  
| device_type  | 目标设备类型  | enum_string  | {"dock":"设置机场 Dongle","drone":"设置飞行器 Dongle"}  | 标识要操作的目标设备  |  
| esim_operator  | 切换的目标运营商  | enum_int  | {"1":"移动","2":"联通","3":"电信"}  |   |  
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** esim_operator_switch
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#esim-%E5%92%8C-sim-%E5%88%87%E6%8D%A2) eSIM 和 SIM 切换
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** sim_slot_switch
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| imei  | dongle imei  | text  |   | 标识要操作的 Dongle  |  
| device_type  | 目标设备类型  | enum_string  | {"dock":"设置机场 Dongle","drone":"设置飞行器 Dongle"}  | 标识要操作的目标设备  |  
| sim_slot  | 切换的目标卡槽  | enum_int  | {"1":"实体 SIM 卡","2":"eSIM"}  | 在使用实体 SIM 卡和使用 eSIM 之间切换  |  
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** sim_slot_switch
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#esim-%E6%BF%80%E6%B4%BB) eSIM 激活
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** esim_activate
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| imei  | dongle imei  | text  |   | 标识要操作的 Dongle  |  
| device_type  | 目标设备类型  | enum_string  | {"dock":"设置机场 Dongle","drone":"设置飞行器 Dongle"}  | 标识要操作的目标设备  |  
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** esim_activate
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   |   |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E5%A2%9E%E5%BC%BA%E5%9B%BE%E4%BC%A0%E5%BC%80%E5%85%B3) 增强图传开关
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
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E5%85%B3%E9%97%AD%E5%85%85%E7%94%B5) 关闭充电
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
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E6%89%93%E5%BC%80%E5%85%85%E7%94%B5) 打开充电
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
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E5%85%B3%E9%97%AD%E8%88%B1%E7%9B%96) 关闭舱盖
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
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E6%89%93%E5%BC%80%E8%88%B1%E7%9B%96) 打开舱盖
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
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E9%A3%9E%E8%A1%8C%E5%99%A8%E6%95%B0%E6%8D%AE%E6%A0%BC%E5%BC%8F%E5%8C%96) 飞行器数据格式化
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
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E6%9C%BA%E5%9C%BA%E6%95%B0%E6%8D%AE%E6%A0%BC%E5%BC%8F%E5%8C%96) 机场数据格式化
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
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E9%A3%9E%E8%A1%8C%E5%99%A8%E5%85%B3%E6%9C%BA) 飞行器关机
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
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E9%A3%9E%E8%A1%8C%E5%99%A8%E5%BC%80%E6%9C%BA) 飞行器开机
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
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E6%9C%BA%E5%9C%BA%E9%87%8D%E5%90%AF) 机场重启
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
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E7%94%B5%E6%B1%A0%E8%BF%90%E8%A1%8C%E6%A8%A1%E5%BC%8F%E5%88%87%E6%8D%A2) 电池运行模式切换
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
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E6%9C%BA%E5%9C%BA%E5%A3%B0%E5%85%89%E6%8A%A5%E8%AD%A6%E5%BC%80%E5%85%B3) 机场声光报警开关
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
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E6%9C%BA%E5%9C%BA%E7%A9%BA%E8%B0%83%E5%B7%A5%E4%BD%9C%E6%A8%A1%E5%BC%8F%E5%88%87%E6%8D%A2) 机场空调工作模式切换
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
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E7%94%B5%E6%B1%A0%E4%BF%9D%E5%85%BB%E7%8A%B6%E6%80%81%E5%88%87%E6%8D%A2) 电池保养状态切换
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
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E5%85%B3%E9%97%AD%E8%A1%A5%E5%85%89%E7%81%AF) 关闭补光灯
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
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E6%89%93%E5%BC%80%E8%A1%A5%E5%85%89%E7%81%AF) 打开补光灯
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
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E8%B0%83%E8%AF%95%E6%A8%A1%E5%BC%8F%E5%85%B3%E9%97%AD) 调试模式关闭
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
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E8%B0%83%E8%AF%95%E6%A8%A1%E5%BC%8F%E5%BC%80%E5%90%AF) 调试模式开启
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
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E4%B8%80%E9%94%AE%E6%A0%87%E5%AE%9A) 一键标定
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** rtk_calibration
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| devices  | 标定设备集合  | array  | {"size": "-", "item_type": "struct" }  |   |  
| » sn  | 设备序列号（SN）  | text  | {"length":"10240"}  |   |  
| » type  | 标定类型  | enum_int  | {"1": "手动标定"}  |   |  
| » module  | 模块枚举值  | enum_string  | {"3": "机场", "6": "中继" }  |   |  
| » data  | 标定数据  | struct  |   |   |  
| »» longitude  | 经度  | double  |   |   |  
| »» latitude  | 纬度  | double  |   |   |  
| »» height  | 高度  | double  |   |   |  
**Example:**
```
{
  "bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
  "timestamp:": 1654070968655,
  "method": "rtk_calibration",
  "data": {
    "devices": [
      {
        "sn": "string",
        "type": 1,
        "module": "3",
        "data": {
          "height": 60.285194396972656,
          "latitude": 22.755022128112614,
          "longitude": 114.89828051067889
        }
      }
    ]
  }
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** rtk_calibration
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| result  | 返回码  | int  |   | 非 0 代表错误  |  
| output  | 输出  | struct  |   |   |  
| »status  | 任务状态  | enum_string  | {"canceled":"取消或终止","failed":"失败","in_progress":"执行中","ok":"执行成功","paused":"暂停","rejected":"拒绝","sent":"已下发","timeout":"超时"}  |   |  
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock3/cmd.html#%E5%BC%BA%E5%88%B6%E5%85%B3%E8%88%B1%E7%9B%96) 强制关舱盖
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