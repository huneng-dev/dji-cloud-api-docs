<!-- source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/log.html -->
<!-- path: api-reference/dock-to-cloud/mqtt/dock/log -->

#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/log.html#event) Event
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/log.html#%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E8%BF%9B%E5%BA%A6%E9%80%9A%E7%9F%A5) 文件上传进度通知
**Topic:** thing/product/_{gateway_sn}_ /events
**Direction:** up
**Method:** fileupload_progress
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| ext  |   | struct  |   |   |  
| »files  |   | array  | {}  |   |  
| »»[array_item]  | Elements in array  | struct  | {}  | {"size": ""}  |  
| »»»module  | 所属设备类型  | enum  | {"0":"飞机","3":"机场"}  |   |  
| »»»size  | 文件大小  | int  |   | byte  |  
| »»»device_sn  | 设备序列号  | text  |   |   |  
| »»»key  | 对象存储桶key  | text  |   |   |  
| »»»fingerprint  | 文件指纹  | text  |   |   |  
| »»»progress  |   | struct  | [{"identifier":"prgress","dataType":{"type":"int"}},{"identifier":"finish_time","desc":"上传完成时间","dataType":{"type":"int"}},{"identifier":"upload_rate","desc":"上传速率","dataType":{"type":"int"}}]  |   |  
**Example:**
```
{
	"method": "fileupload_progress",
	"need_reply": 0,
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1655781395926,
	"gateway": "dock_sn",
	"data": {
		"output": {
			"ext": {
				"files": [
					{
						"module": "0",
						"size": 155232,
						"device_sn": "drone_sn",
						"key": "4bf0039f-6434-44a8-b891-8d7b6b7ff138/drone_sn/video_20220621_110830.log",
						"fingerprint": "4f65b891f3bc09bdb6d4c36a996b532d",
						"progress": {
							"current_step": 19,
							"prgress": 100,
							"finish_time": 1655781395926,
							"upload_rate": 0,
							"result": 0,
							"status": "ok"
						}
					},
					{
						"module": "3",
						"size": 155232,
						"device_sn": "dock_sn",
						"key": "4bf0039f-6434-44a8-b891-8d7b6b7ff138/dock_sn/video_20220621_110830.log",
						"fingerprint": "4f65b891f3bc09bdb6d4c36a996b532d",
						"progress": {
							"current_step": 19,
							"total_step": 30,
							"prgress": 100,
							"finish_time": 1655781395926,
							"upload_rate": 0,
							"result": 0,
							"status": "ok"
						}
					}
				]
			},
			"status": "ok"
		}
	}
}
```
#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/log.html#service) Service
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/log.html#%E8%8E%B7%E5%8F%96%E8%AE%BE%E5%A4%87%E5%8F%AF%E4%B8%8A%E4%BC%A0%E7%9A%84%E6%96%87%E4%BB%B6%E5%88%97%E8%A1%A8) 获取设备可上传的文件列表
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** fileupload_list
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| module_list  | 文件所属过滤列表  | array  |   |   |  
| »[array_item]  | Elements in array  | enum  | {"0":"飞机","3":"机场"}  |   |  
**Example:**
```
{
	"method": "fileupload_list",
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1654070968655,
	"data": {
		"module_list": [
			"0",
			"3"
		]
	}
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** fileupload_list
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| files  |   | array  | {}  |   |  
| »[array_item]  | Elements in array  | struct  | {}  | {"size": "2"}  |  
| »»device_sn  | 设备序列号  | text  |   |   |  
| »»result  | 结果码  | int  |   | 非 0 代表错误  |  
| »»module  | 所属设备类型  | enum  | {"0":"飞机","3":"机场"}  |   |  
| »»list  | 文件索引列表  | array  |   |   |  
**Example:**
```
{
	"timestamp": 1654070968655,
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"method": "fileupload_list",
	"gateway": "",
	"data": {
		"files": [
			{
				"device_sn": "xxxxxxxxx",
				"list": [
					{
						"boot_index": 1111,
						"end_time": 1659427398806,
						"size": 33789,
						"start_time": 1654070968655
					},
					{
						"boot_index": 22222,
						"end_ime": 1659427398806,
						"size": 33789,
						"start_time": 1659427398806
					}
				],
				"module": "0",
				"result": 0
			},
			{
				"device_sn": "device_sn",
				"list": [
					{
						"boot_index": 11111,
						"end_time": 1659427398806,
						"size": 36772,
						"start_time": 1659427398806
					},
					{
						"boot_index": 22222,
						"end_ime": 1659427398806,
						"size": 33789,
						"start_time": 1659427398806
					}
				],
				"module": "3",
				"result": 0
			}
		],
		"result": 0
	}
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/log.html#%E5%8F%91%E8%B5%B7%E6%97%A5%E5%BF%97%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0) 发起日志文件上传
设备端收到服务端下发的命令后，会直接返回执行结果状态
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** fileupload_start
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| bucket  | 对象存储桶名称  | text  | {}  |   |  
| region  | 数据中心所在的地域  | text  | {}  |   |  
| credentials  | 凭证信息  | struct  |   |   |  
| »access_key_id  | 访问密钥ID  | text  | {}  |   |  
| »access_key_secret  | 秘密访问密钥  | text  | {}  |   |  
| »expire  | 访问密钥过期时间  | int  | {"unit":"s","unitName":"秒","step":"1"}  |   |  
| »security_token  | 会话凭证  | text  | {}  |   |  
| endpoint  | 对外服务的访问域名  | text  | {}  |   |  
| provider  | 云厂商枚举值  | enum  | {"ali":"阿里云","aws":"亚马逊云","minio":"minio"}  |   |  
| params  |   | struct  |   |   |  
| »files  |   | array  | {}  |   |  
| »»[array_item]  | Elements in array  | struct  | {}  | {"size": ""}  |  
| »»»object_key  | 对象存储key  | text  |   |   |  
| »»»module  | 日志所属模块  | text  |   |   |  
| »»»list  | 文件索引列表  | array  | {"item":{"type":"struct","specs":[{"identifier":"boot_index","name":"文件索引","dataType":{"type":"int"}},{"identifier":"start_time","name":"日志开始时间(毫秒时间戳)","dataType":{"type":"int"}},{"identifier":"end_time","name":"日志结束时间(毫秒时间戳)","dataType":{"type":"int"}},{"identifier":"size","name":"日志文件大小","desc":"byte","dataType":{"type":"int"}}]}}  |   |  
**Example:**
```
{
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"timestamp": 1659429523120,
	"method": "fileupload_start",
	"data": {
		"bucket": "stg-dji-service-hz-ksd7",
		"region": "hz",
		"credentials": {
			"access_key_id": "STS.access_key_id",
			"access_key_secret": "access_key_secret",
			"expire": 1659432522000,
			"security_token": "security_token"
		},
		"endpoint": "https://oss-cn-hangzhou.aliyuncs.com",
		"params": {
			"files": [
				{
					"list": [
						{
							"boot_index": 1111,
							"end_time": 1659427398806,
							"size": 33789,
							"start_time": 1654070968655
						},
						{
							"boot_index": 22222,
							"end_ime": 1659427398806,
							"size": 33789,
							"start_time": 1659427398806
						}
					],
					"module": "3",
					"object_key": "object_key"
				}
			]
		},
		"provider": "ali"
	}
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** fileupload_start
**Data:** null
**Example:**
```
{
	"timestamp": 1655781392412,
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"method": "fileupload_start",
	"gateway": "",
	"data": {
		"result": 0
	}
}
```
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/log.html#%E4%B8%8A%E4%BC%A0%E7%8A%B6%E6%80%81%E6%9B%B4%E6%96%B0) 上传状态更新
设备端收到服务端下发的命令后，会直接返回执行结果状态
**Topic:** thing/product/_{gateway_sn}_ /services
**Direction:** down
**Method:** fileupload_update
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| status  | 上传状态  | enum  | {"cancel":"取消"}  |   |  
| module_list  | 日志所属模块列表  | array  | {"size": }  |   |  
| »[array_item]  | Elements in array  |   | {"type":"enum","specs":{"0":"飞机","3":"机场"}}  |   |  
**Example:**
```
{
	"method": "fileupload_update",
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"data": {
		"status": "cancel",
		"module_list": [
			"0",
			"3"
		]
	}
}
```
**Topic:** thing/product/_{gateway_sn}_ /services_reply
**Direction:** up
**Method:** fileupload_update
**Data:** null
**Example:**
```
{
	"timestamp": 1655781392412,
	"tid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"bid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx",
	"method": "fileupload_update",
	"gateway": "",
	"data": {
		"result": 0
	}
}
```