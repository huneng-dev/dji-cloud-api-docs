---
source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/properties.html
path: api-reference/dock-to-cloud/mqtt/dock/properties
---

#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/properties.html#property) Property
  * pushMode：
    * 0：设备推送定频数据，设备将以 0.5HZ 的频率定时上报
    * 1：设备推送状态数据，设备在状态变化时上报
  * accessMode：
    * r：属性只读
    * rw：属性可读写
| Column  | Name  | Type  | accessMode  | pushMode  | constraint  | Description  |  
| --- | --- | --- | --- | --- | --- | --- |  
| longitude  | 经度  | double  | r  | 0  | {"min":"0","max":"180","step":"0.01"}  | 网关设备的经度  |  
| latitude  | 纬度  | double  | r  | 0  | {"min":"0","max":"180","step":"0.01"}  | 网关设备的纬度  |  
| firmware_version  | 固件版本  | text  | r  | 1  | {"length":"64"}  | 网关设备的固件版本  |  
| firmware_upgrade_status  | 固件升级状态  | enum  | r  | 1  | {"0":"未升级","1":"升级中"}  |   |  
| mode_code  | 机场状态  | enum  | r  | 0  | {"0":"空闲中","1":"现场调试","2":"远程调试","3":"固件升级中","4":"作业中"}  |   |  
| flighttask_step_code  | 机场任务状态  | enum  | r  | 0  | {"0":"作业准备中","1":"飞行作业中","2":"作业后状态恢复","3":"自定义飞行区更新中","4":"地形障碍物更新中","5":"任务空闲","256":"未知状态"}  |   |  
| sub_device  | 子设备状态  | struct  | r  | 0  |   |   |  
| »device_sn  | 子设备sn  | text  |   |   |   |   |  
| »product_type  | 子设备枚举值  | text  |   |   |   | 格式为 _{domain-type-subtype}_  |  
| »device_online_status  | 机场停机坪上的飞行器开机状态  | enum  |   |   | {"0":"关机","1":"开机"}  |   |  
| »device_paired  | 机场停机坪上的飞行器是否与机场对频  | enum  |   |   | {"0":"未对频","1":"已对频"}  |   |  
| cover_state  | 舱盖状态  | enum  | r  | 0  | {"0":"关闭","1":"打开","2":"半开","3":"舱盖状态异常"}  |   |  
| putter_state  | 推杆状态  | enum  | r  | 0  | {"0":"关闭","1":"打开","2":"半开","3":"推杆状态异常"}  |   |  
| supplement_light_state  | 补光灯状态  | enum  | r  | 0  | {"0":"关闭","1":"打开"}  |   |  
| network_state  | 网络状态  | struct  | r  | 0  |   | KB/s  |  
| »type  | 网络类型  | enum  |   |   | {"1":"4G","2":"以太网"}  |   |  
| »quality  | 网络质量  | enum_int  |   |   | {"0":"无信号","1":"差","2":"较差","3":"一般","4":"较好","5":"好"}  |   |  
| »rate  | 网络速率  | int  |   |   | {}  | KB/s  |  
| drone_in_dock  | 飞机是否在舱  | enum  | r  | 0  | {"0":"舱外","1":"舱内"}  |   |  
| job_number  | 机场累计作业次数  | int  | r  | 0  | {"min":"0","max":"4294967295","unit":"t","unitName":"次","step":"1"}  |   |  
| media_file_detail  | 媒体文件上传细节  | struct  | r  | 0  |   |   |  
| »remain_upload  | 待上传数量  | int  |   |   | {}  |   |  
| wireless_link  | 图传链路  | struct  | r  | 0  |   |   |  
| »dongle_number  | 飞机上 Dongle 数量  | int  |   |   | {}  |   |  
| »4g_link_state  | 4G 链路连接状态  | enum  |   |   | {"0":"断开","1":"连接"}  |   |  
| »sdr_link_state  | SDR 链路连接状态  | enum  |   |   | {"0":"断开","1":"连接"}  |   |  
| »link_workmode  | 机场的图传链路模式  | enum  |   |   | {"0":"SDR 模式","1":"4G 融合模式"}  |   |  
| »sdr_quality  | SDR 信号质量  | int  |   |   | {"min":"0","max":"5","step":"1"}  |   |  
| »4g_quality  | 总体 4G 信号质量  | int  |   |   | {"min":"0","max":"5","step":"1"}  |   |  
| »4g_uav_quality  | 天端 4G 信号质量  | int  |   |   | {"min":"0","max":"5","step":"1"}  | 飞行器端与 4G 服务器之间的信号质量  |  
| »4g_gnd_quality  | 地端 4G 信号质量  | int  |   |   | {"min":"0","max":"5","step":"1"}  | 地面端（如遥控器、DJI Dock等）与 4G 服务器之间的信号质量  |  
| »sdr_freq_band  | SDR 频段  | float  |   |   | {}  |   |  
| »4g_freq_band  | 4G 频段  | float  |   |   | {}  |   |  
| live_status  | 网关当前整体直播状态推送  | array  | r  | 1  | {}  |   |  
| »[array_item]  | Elements in array  | struct  | r  | 1  | {}  | {"size": ""}  |  
| »»video_id  | 直播码流标识符  | text  |   |   |   | 格式为 _{sn}/{camera_index}/{video_index}_ 。其中 _{sn}_ 为视频源设备sn， _{camera_index}_ 为相机索引，使用 _{type-subtype-gimbalindex}_ 的格式， _{video_index}_ 为该相机级别的视频源可以选择的码流index  |  
| »»video_type  | 视频类型  | text  |   |   | {"length":"24"}  | 表明视频镜头的类型，如normal/wide/zoom/ir等  |  
| »»video_quality  | 直播质量  | enum  |   |   | {"0":"自适应","1":"流畅","2":"标清","3":"高清","4":"超清"}  | 不同清晰度的分辨率与码率分别为，流畅：960 * 540、512Kbps，标清：1280 * 720、1Mbps，高清：1280 * 720、1.5Mbps，超清：1920 * 1080、3Mbps  |  
| »»status  | 直播状态  | enum  |   |   | {"0":"未直播","1":"在直播"}  |   |  
| »»error_status  | 错误码  | int  |   |   | {"length":6}  |   |  
| live_capacity  | 网关直播能力  | struct  | r  | 1  |   | 上报该网关设备当前可直播的能力  |  
| »available_video_number  | 该网关当前可选择推流的码流数量  | int  |   |   |   |   |  
| »coexist_video_number_max  | 该网关当前可同时推流的最大码流数量  | int  |   |   |   |   |  
| »device_list  | 可选择的视频设备源（设备层，比如飞行器）  | array  |   |   | {}  |   |  
| »»[array_item]  | Elements in array  | struct  |   |   | {}  | {"size": ""}  |  
| »»»sn  | 飞机等视频源设备序列号（SN）  | text  |   |   |   |   |  
| »»»available_video_number  | 该序列号的设备源可以被选择推流的码流数  | int  |   |   |   |   |  
| »»»coexist_video_number_max  | 该序列号的设备源可以同时被推流的最大码流数  | int  |   |   |   |   |  
| »»»camera_list  | 该序列号的设备源上的相机列表  | array  |   |   | {"item":{"type":"struct","specs":[{"identifier":"camera_index","name":"相机索引，使用 _{type-subtype-gimbalindex}_ ","dataType":{"type":"text"}},{"identifier":"available_video_number","name":"该相机级别的视频源可以被选择推流的码流数","dataType":{"type":"int"}},{"identifier":"coexist_video_number_max","name":"该相机级别的视频源可以同时被推流的码流数","dataType":{"type":"int"}},{"identifier":"video_list","name":"该相机级别的视频源可以选择的码流列表","dataType":{"type":"array","specs":{"item":{"type":"struct","specs":[{"identifier":"video_index","name":"该相机级别的视频源可以选择的码流index","dataType":{"type":"text"}},{"identifier":"video_type","name":"该相机级别的视频源可以选择的码流类型","dataType":{"type":"text"}},{"identifier":"switchable_video_types","name":"该视频流支持切换的视频镜头类型列表：normal/wide/zoom/ir","dataType":{"type":"array","specs":{"type":"text","length":"24"}}}]}}}}]}}  |   |  
| rainfall  | 降雨量  | enum  | r  | 0  | {"0":"无雨","1":"小雨","2":"中雨","3":"大雨"}  |   |  
| wind_speed  | 风速  | float  | r  | 0  | {"min":"-1.4E-45","max":"3.4028235E38","unit":"m/s","unitName":"米每秒","step":"0.1"}  |   |  
| environment_temperature  | 环境温度  | float  | r  | 0  | {"min":"-1.4E-45","max":"3.4028235E38","unit":"°C","unitName":"摄氏度","step":"0.1"}  |   |  
| temperature  | 舱内温度  | float  | r  | 0  | {"min":"-1.4E-45","max":"3.4028235E38","unit":"°C","unitName":"摄氏度","step":"0.1"}  |   |  
| humidity  | 舱内湿度  | float  | r  | 0  | {"min":"0","max":"100","unit":"%RH","unitName":"相对湿度","step":"0.1"}  |   |  
| electric_supply_voltage  | 市电电压  | int  | r  | 0  | {"min":"-2147483648","max":"2147483647","unit":"V","unitName":"伏特","step":"1"}  |   |  
| working_voltage  | 工作电压  | int  | r  | 0  | {"min":"-2147483648","max":"2147483647","unit":"mV","unitName":"毫伏","step":"1"}  |   |  
| working_current  | 工作电流  | float  | r  | 0  | {"min":"-1.4E-45","max":"3.4028235E38","unit":"mA","unitName":"毫安","step":"0.1"}  |   |  
| storage  | 存储容量  | struct  | r  | 0  |   | kb  |  
| »total  | 总容量  | int  |   |   | {"min":"-2147483648","max":"2147483647","unit":"KB","unitName":"千字节","step":"1"}  |   |  
| »used  | 已使用容量  | int  |   |   | {"min":"-2147483648","max":"2147483647","unit":"KB","unitName":"千字节","step":"1"}  |   |  
| first_power_on  | 首次上电时间  | int  | r  | 0  | {"min":"-2147483648","max":"2147483647","unit":"ms","unitName":"毫秒","step":"1"}  |   |  
| acc_time  | 机场累计运行时长  | int  | r  | 1  | {"min":"-2147483648","max":"2147483647","unit":"s","unitName":"秒","step":"1"}  |   |  
| compatible_status  | 固件一致性  | enum  | r  | 1  | {"0":"不需要一致性升级","1":"需要一致性升级"}  |   |  
| alternate_land_point  | 备降点  | struct  | r  | 0  |   |   |  
| »longitude  | 经度  | float  |   |   | {"min":"-1.4E-45","max":"3.4028235E38","step":"0.1"}  |   |  
| »latitude  | 纬度  | float  |   |   | {"min":"-1.4E-45","max":"3.4028235E38","step":"0.1"}  |   |  
| »safe_land_height  | 安全高度(备降转移高)  | float  |   |   | {"min":"-1.4E-45","max":"3.4028235E38","step":"0.1"}  |   |  
| »is_configured  | 是否设置备降点  | enum  |   |   | {"0":"未设置","1":"已设置"}  |   |  
| height  | 椭球高度  | double  | r  | 0  | {"min":"-4.9E-324","max":"1.7976931348623157E308","unit":"m","unitName":"米","step":"0.01"}  |   |  
| activation_time  | 机场激活时间(unix 时间戳)  | int  | r  | 0  | {"min":"0","max":"2147483647","unit":"s","unitName":"秒","step":"1"}  |   |  
| air_conditioner  | 机场空调工作状态信息  | struct  | r  | 0  |   |   |  
| »air_conditioner_state  | 机场空调状态  | (int型)enum  |   |   | {"0":"空闲模式（无制冷、制热、除湿等）","1":"制冷模式","2":"制热模式","3":"除湿模式","4":"制冷退出模式","5":"制热退出模式","6":"除湿退出模式","7":"制冷准备模式","8":"制热准备模式","9":"除湿准备模式"}  | 机场空调工作状态信息，一个时刻仅存在一种工作模式，不能同时存在多个模式  |  
| »switch_time  | 剩余需要等待的可切换时间  | int  |   |   | {"unit":"秒"}  | 模式切换顺序为准备模式、工作（制冷、制热、除湿）模式、退出模式、空闲模式。本属性将上报，可以切换下一个模式指令还需要等待的时间。例如当前机场空调在进入制冷模式后，必须制冷5分钟后才可以退出制冷模式，本属性将上报还需要多久退出制冷模式，为0表示随时可退出  |  
| battery_store_mode  | 电池运行模式  | enum  | r  | 0  | {"1":"计划模式","2":"待命模式"}  | 计划模式适合规律作业场景，无任务时电池电量保持在55%~60%，电池寿命较长。待命模式适合应急作业场景，无任务时电池电量保持在90%~95%，电池寿命较短。  |  
| alarm_state  | 机场声光报警状态  | enum  | r  | 0  | {"0":"声光报警关闭","1":"声光报警开启"}  |   |  
| drone_battery_maintenance_info  | 飞行器电池保养信息  | struct  |   | 0  |   |   |  
| »maintenance_state  | 保养状态  | enum  |   |   | {"0":"无需保养","1":"待保养","2":"正在保养"}  |   |  
| »maintenance_time_left  | 电池保养剩余时间  | int  |   |   | {"unit":"小时"}  | 向下取整  |  
| »heat_state  | 电池加热保温状态  | (int型)enum  |   |   | {"0":"电池未开启加热或保温","1":"电池在加热中","2":"电池在保温中"}  | 当飞机舱内关机时由本物模型上报机场连接飞机的电池加热保温信息  |  
| »batteries  | 电池详细信息  | array  |   |   | {}  | 当飞机舱内关机时由本物模型上报机场连接飞机的电池信息，基本数据与飞机物模型中电池信息基本保持一致  |  
| »»[array_item]  | Elements in array  | struct  |   |   | {}  | {"size": ""}  |  
| »»»capacity_percent  | 电池剩余电量  | int  |   |   | {"min":0,"max":100}  | 保留小数点后一位，正常范围 0~100，设备端获取不到数据的异常值为 32767  |  
| »»»index  | 电池序号  | (int型)enum  |   |   | {"0":"左电池","1":"右电池"}  |   |  
| »»»voltage  | 电压  | int  |   |   | {"unit":"毫伏"}  | 正常范围0~28000mV，设备端获取不到数据的异常值为 32767  |  
| »»»temperature  | 温度  | float  |   |   | {"unit":"摄氏度"}  | 保留小数点后一位，正常范围-40~150摄氏度，设备端获取不到数据的异常值为 32767  |  
| backup_battery  | 机场备用电池信息  | struct  | r  | 0  |   |   |  
| »switch  | 备用电池开关  | enum  |   |   | {"0":"备用电池关闭","1":"备用电池开启"}  |   |  
| »voltage  | 备用电池电压  | int  |   |   | {"unit":"毫伏","min":"0","max":"30000","step":"1"}  | 备用电池关闭时电压为 0  |  
| »temperature  | 备用电池温度  | float  |   |   | {"unit":"摄氏度","step":"0.1"}  | 保留小数点后一位  |  
| drone_charge_state  | 飞机充电状态  | struct  | r  | 0  |   |   |  
| »capacity_percent  | 电量百分比  | int  |   |   | {"min":"0","max":"100"}  |   |  
| »state  | 充电状态  | enum  |   |   | {"0":"空闲","1":"充电中"}  |   |  
| emergency_stop_state  | 紧急停止按钮状态  | enum  | r  | 0  | {"0":"关闭","1":"开启"}  |   |  
| position_state  | 搜星状态  | struct  | r  | 0  |   |   |  
| »is_calibration  | 是否标定  | enum  |   |   | {"0":"未标定","1":"已标定"}  |   |  
| »is_fixed  | 是否收敛  | enum  |   |   | {"0":"非开始","1":"收敛中","2":"收敛成功","3":"收敛失败"}  |   |  
| »quality  | 搜星档位  | enum  |   |   | {"1":"1档","2":"2档","3":"3档","4":"4档","5":"5档"}  |   |  
| »gps_number  | GPS 搜星数量  | int  |   |   |   |   |  
| »rtk_number  | RTK 搜星数量  | int  |   |   |   |   |  
| maintain_status  | 保养信息  | struct  | r  | 0  |   |   |  
| »maintain_status_array  | 保养信息数组  | array  |   |   | {}  |   |  
| »»[array_item]  | Elements in array  | struct  |   |   | {}  | {"size": ""}  |  
| »»»state  | 保养状态  | enum  |   |   | {"0":"无保养","1":"保养中"}  |   |  
| »»»last_maintain_type  | 上一次保养类型  | enum_int  |   |   | {"0":"无保养","17":"机场常规保养","18":"机场深度保养"}  |   |  
| »»»last_maintain_time  | 上一次保养时间  | date  |   |   | {"unit":"utc秒时间戳"}  |   |  
| »»»last_maintain_work_sorties  | 上一次保养时工作架次  | int  |   |   | {"unit":"次","step":"1"}  |   |  
| wpmz_version  | 机场的航线解析库版本号  | text  | r  | 1  | {}  |   |  
| drc_state  |   | enum  | r  | 0  | {"0":"未连接","1":"连接中","2":"已连接"}  | DRC 链路的状态  |  
| user_experience_improvement  | 用户体验改善计划  | enum_int  | rw  | 1  | {"0":"初始状态","1":"拒绝加入用户体验改善计划","2":"同意加入用户体验改善计划"}  |   |