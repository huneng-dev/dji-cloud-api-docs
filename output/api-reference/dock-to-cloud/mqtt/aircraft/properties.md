---
source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/aircraft/properties.html
path: api-reference/dock-to-cloud/mqtt/aircraft/properties
---

#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/aircraft/properties.html#property) Property
  * pushMode：
    * 0：设备推送定频数据，设备将以 0.5HZ 的频率定时上报
    * 1：设备推送状态数据，设备在状态变化时上报
  * accessMode：
    * r：属性只读
    * rw：属性可读写
| Column  | Name  | Type  | accessMode  | pushMode  | constraint  | Description  |  
| --- | --- | --- | --- | --- | --- | --- |  
| payloads  | 负载状态  | array  | r  | 1  | {}  |   |  
| »[array_item]  | Elements in array  | struct  | r  | 1  | {}  | {"size": ""}  |  
| »»control_source  | 负载控制权  | text  |   |   |   |   |  
| »»payload_index  | 负载编号  | text  |   |   |   | 负载索引，格式为 _{type-subtype-gimbalindex}_  |  
| »»firmware_version  | 固件版本  | text  |   |   |   |   |  
| »»sn  | 负载序列号（SN）  | text  |   |   |   |   |  
| mode_code  | 飞行器状态  | enum_int  | r  | 0  | {"0":"待机","1":"起飞准备","2":"起飞准备完毕","3":"手动飞行","4":"自动起飞","5":"航线飞行","6":"全景拍照","7":"智能跟随","8":"ADS-B 躲避","9":"自动返航","10":"自动降落","11":"强制降落","12":"三桨叶降落","13":"升级中","14":"未连接","15":"APAS","16":"虚拟摇杆状态","17":"指令飞行"}  |   |  
| distance_limit_status  | 飞行器限远状态  | struct  | rw  | 0  |   |   |  
| »state  | 是否开启限远  | enum_int  |   |   | {"0":"未设置","1":"已设置"}  |   |  
| »distance_limit  | 限远距离  | int  |   |   | {"max":"8000","min":"15","step":"1","unit":"米 / m"}  |   |  
| »is_near_distance_limit  | 是否接近设定的限制距离  | enum_int  | r  |   | {"0":"未达到设定的限制距离","1":"接近设定的限制距离"}  |   |  
| wpmz_version  | 飞行器的航线解析库版本号  | text  | r  | 1  |   | 若飞行器的固件版本过低，查询会报异常，机场将向云端推送 1.0.2 版本的 WPMZ  |  
| rth_altitude  | 返航高度  | int  | rw  | 0  | {"max":500,"min":20,"unit":"米 / m"}  | 返航高度  |  
| rc_lost_action  | 遥控器失控动作  | enum_int  | rw  | 0  | {"0":"悬停","1":"着陆(降落)","2":"返航"}  | 遥控器失控动作  |  
| exit_wayline_when_rc_lost  | [废弃]航线失控动作  | enum_int  | rw  | 0  | {"0":"继续执行航线任务","1":"退出航线任务，执行遥控器失控动作"}  | 执行航线时失控了，选择继续执行完航线，还是执行遥控器失控动作  |  
| cameras  | 飞行器相机信息  | array  | r  | 0  | {}  |   |  
| »[array_item]  | Elements in array  | struct  | r  | 0  | {}  | {"size": ""}  |  
| »»remain_photo_num  | 剩余拍照张数  | int  |   |   |   | 剩余拍照张数  |  
| »»remain_record_duration  | 剩余录像时间  | int  |   |   | {"unit":"秒 / s"}  | 剩余录像时间  |  
| »»record_time  | 视频录制时长  | int  |   |   | {"unit":"秒 / s"}  | 视频录制时长  |  
| »»payload_index  | 负载编号  | text  |   |   |   | 负载编号，相机枚举值。非标准的 device_mode_key，格式为 {type-subtype-gimbalindex}，可以参考[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)  |  
| »»camera_mode  | 相机模式  | enum_int  |   |   | {"0":"拍照","1":"录像"}  | 相机模式  |  
| »»photo_state  | 拍照状态  | enum_int  |   |   | {"0":"空闲","1":"拍照中"}  | 拍照状态  |  
| »»screen_split_enable  | 分屏是否使能  | bool  |   |   | {"true":"分屏使能开启","false":"分屏使能关闭"}  |   |  
| »»recording_state  | 录像状态  | enum_int  |   |   | {"0":"空闲","1":"录像中"}  | 录像状态  |  
| »»zoom_factor  | 变焦倍数  | float  |   |   | {"max":200,"min":2}  |   |  
| »»ir_zoom_factor  | 红外变焦倍数  | float  |   |   | {"max":20,"min":2}  | 红外变焦倍数  |  
| »»liveview_world_region  | 视场角（FOV）在 liveview 中的区域  | struct  |   |   | [{"accessMode":"r","dataType":{"max":1,"min":0,"type":"float"},"desc":"左上角的 x 轴起始点","identifier":"left","name":"左上角的 x 轴起始点","pushMode":0,"required":false},{"accessMode":"r","dataType":{"max":1,"min":0,"type":"float"},"desc":"左上角的 y 轴起始点","identifier":"top","name":"左上角的 y 轴起始点","pushMode":0,"required":false},{"accessMode":"r","dataType":{"max":1,"min":0,"type":"float"},"desc":"右下角的 x 轴起始点","identifier":"right","name":"右下角的 x 轴起始点","pushMode":0,"required":false},{"accessMode":"r","dataType":{"max":1,"min":0,"type":"float"},"desc":"右下角的 y 轴起始点","identifier":"bottom","name":"右下角的 y 轴起始点","pushMode":0,"required":false}]  | 变焦相机的视场角相对于广角相机或者红外相机的视场角，在 liveview 中会有所不同。坐标原点为镜头左上角。  |  
| _{type-subtype-gimbalindex}_  | {_{type-subtype-gimbalindex}_ _AEncSWZTyQ}  | struct  | r  | 0  |   | {_{type-subtype-gimbalindex}_ _XeIeqFlRLP}  |  
| »thermal_current_palette_style  | 调色盘样式  | enum_int  | rw  |   | {"0":"白热","1":"黑热","2":"描红","3":"医疗","5":"彩虹 1","6":"铁红","8":"北极","11":"熔岩","12":"热铁","13":"彩虹 2"}  | 红外相机提供多种调色样式，用户可根据不同的场景选择不同的色彩，便于更加清晰地查看目标  |  
| »thermal_supported_palette_styles  | 设备支持的调色盘样式集合  | array  |   |   | {"item":{"specs":{"0":"白热","1":"黑热","2":"描红","3":"医疗","5":"彩虹 1","6":"铁红","8":"北极","11":"熔岩","12":"热铁","13":"彩虹 2"},"type":"enum_int"}}  | 不同设备所支持的样式能力有所不同  |  
| »thermal_gain_mode  | 增益模式  | enum_int  | rw  |   | {"0":"自动","1":"低增益, 测温范围0°C-500°C","2":"高增益, 测温范围-20°C-150°C"}  | 低增益提供更大的测温范围，高增益拥有更高的测温精度  |  
| »thermal_isotherm_state  | 是否开启等温线  | enum_int  | rw  |   | {"0":"关闭","1":"开启"}  | 等温线允许用户观测自己感兴趣的温度区间的内容，让兴趣温度区间的物体能更加凸显  |  
| »thermal_isotherm_upper_limit  | 测温区间上限  | int  | rw  |   | {"unit":"摄氏度 / °C"}  | 仅启用等温线功能后有效  |  
| »thermal_isotherm_lower_limit  | 测温区间下限  | int  | rw  |   | {"unit":"摄氏度 / °C"}  | 仅启用等温线功能后有效  |  
| »thermal_global_temperature_min  | 全局画面中测量的最低温度  | float  | r  |   | {"unit":"摄氏度 / °C"}  |   |  
| »thermal_global_temperature_max  | 全局画面中测量的最高温度  | float  | r  |   | {"unit":"摄氏度 / °C"}  |   |  
| country  | 国家区域码  | text  | r  | 0  |   |   |  
| rid_state  | RID 工作状态  | bool  | r  | 0  | {"true":"正常","false":"异常"}  |   |  
| commander_mode_lost_action  | [新增]指点飞行失控动作  | enum_int  | rw  | 1  | {"0":"继续执行指点飞行任务","1":"退出指点飞行任务，执行普通失控行为"}  | 执行指点飞行时失控了，选择继续执行完，还是执行普通失控行为  |  
| current_commander_flight_mode  | [新增]指点飞行模式当前值  | enum  | r  | 1  | {"0":"智能高度飞行","1":"设定高度飞行"}  | 指点飞行模式当前值  |  
| commander_flight_height  | [新增]指点飞行高度  | float  | rw  | 1  | {"unit":"米 / m","min":2,"max":3000,"step":0.1}  | 相对(机场)起飞点的高度，相对高 ALT  |  
| mode_code_reason  | 飞行器进入当前状态的原因  | enum_int  | r  | 1  | {"0":"无意义","1":"电池电量不足（返航、降落）","2":"电池电压不足（返航、降落）","3":"电压严重过低（返航、降落）","4":"遥控器按键请求（起飞、返航、降落）","5":"App 请求（起飞、返航、降落）","6":"遥控信号丢失（返航、降落、悬停）","7":"导航、SDK 等外部设备触发（起飞、返航、降落）","8":"进入机场限飞区（降落）","9":"虽然触发了返航但是因为距离 Home 点距离太近（降落）","10":"虽然触发了返航但是因为距离 Home 点距离太远（降落）","11":"执行航点任务时请求（起飞）","12":"返航阶段到达 Home 点上方后请求（降落）","13":"飞行器高度下降，距地面 0.7m（二段降落限低）时，继续下降导致（降落）","14":"App、SDK 等设备强制突破限低保护进行（降落）","15":"因为周围有航班经过而请求（返航、降落）","16":"因为高度控制失败请求（返航、降落）","17":"智能低电量返航后进入（降落）","18":"AP 控制飞行模式（手动飞行）","19":"硬件异常（返航、降落）","20":"防触地保护结束（降落）","21":"返航取消 (悬停)","22":"返航时遇到障碍物（降落）","23":"机场场景下大风触发（返航）"}  |   |  
| gear  | 档位  | enum_int  | r  | 0  | {"0":"A","1":"P","2":"NAV","3":"FPV","4":"FARM","5":"S","6":"F","7":"M","8":"G","9":"T"}  |   |  
| firmware_version  | 固件版本  | text  | r  | 1  | {"length":"64"}  |   |  
| compatible_status  | 固件一致性  | enum_int  | r  | 1  | {"0":"不需要一致性升级","1":"需要一致性升级"}  | 一致性升级：指飞行器某些模块的固件版本与系统匹配版本不一致，需要进行升级。常见的情况例如：飞行器与遥控器已经升级至最新版本，但替换电池时发现电池未升级，此时一致性升级将被提示。普通升级：开发者将飞行器所有模块升级至指定固件版本。  |  
| firmware_upgrade_status  | 固件升级状态  | enum_int  | r  | 1  | {"0":"未升级","1":"升级中"}  |   |  
| horizontal_speed  | 水平速度  | float  | r  | 0  | {"unit":"米每秒 / m/s"}  |   |  
| vertical_speed  | 垂直速度  | float  | r  | 0  | {"unit":"米每秒 / m/s"}  |   |  
| longitude  | 当前位置经度  | float  | r  | 0  |   |   |  
| latitude  | 当前位置纬度  | float  | r  | 0  |   |   |  
| height  | 绝对高度  | float  | r  | 0  |   | 相对地球椭球面高度, 计算：相对起飞点的高度 + 起飞点的椭球高  |  
| elevation  | 相对起飞点高度  | float  | r  | 0  |   |   |  
| attitude_pitch  | 俯仰轴角度  | float  | r  | 0  |   |   |  
| attitude_roll  | 横滚轴角度  | float  | r  | 0  |   |   |  
| attitude_head  | 偏航轴角度  | int  | r  | 0  |   | 偏航轴角度与真北角（经线）的角度，0到6点钟方向为正值，6到12点钟方向为负值  |  
| home_longitude  | Home 点经度  | float  | r  | 1  |   |   |  
| home_latitude  | Home 点纬度  | float  | r  | 1  |   |   |  
| home_distance  | 距离 Home 点的距离  | float  | r  | 0  |   |   |  
| wind_speed  | 风速  | float  | r  | 0  |   | 风速估计，该风速是通过飞行器姿态推测出的，有一定的误差，仅供参考，不能作为气象数据使用  |  
| wind_direction  | 当前风向  | enum_int  | r  | 0  | {"1":"正北","2":"东北","3":"东","4":"东南","5":"南","6":"西南","7":"西","8":"西北"}  |   |  
| control_source  | 当前控制源  | text  | r  | 1  |   | 可以为设备，也可以为某个浏览器。设备使用 A/B 表示 A 控，B 控，浏览器以自生成的 uuid 作为标识符  |  
| low_battery_warning_threshold  | 低电量告警  | int  | r  | 1  |   | 用户设置的电池低电量告警百分比  |  
| serious_low_battery_warning_threshold  | 严重低电量告警  | int  | r  | 1  |   | 用户设置的电池严重低电量告警百分比  |  
| total_flight_time  | 飞行器累计飞行航时  | int  | r  | 0  | {"unit":"秒 / s"}  |   |  
| total_flight_distance  | 飞行器累计飞行总里程  | float  | r  | 0  | {"unit":"米 / m"}  |   |  
| battery  | 飞行器电池信息  | struct  | r  | 0  |   |   |  
| »capacity_percent  | 电池的总剩余电量  | int  |   |   | {"max":100,"min":0}  |   |  
| »remain_flight_time  | 剩余飞行时间  | int  |   |   | {"unit":"秒 / s"}  |   |  
| »return_home_power  | 返航所需电量百分比  | int  |   |   | {"max":100,"min":0}  |   |  
| »landing_power  | 强制降落电量百分比  | int  |   |   | {"max":100,"min":0}  |   |  
| »batteries  | 电池详细信息  | array  |   |   | {}  |   |  
| »»[array_item]  | Elements in array  | struct  |   |   | {}  | {"size": ""}  |  
| »»»capacity_percent  | 电池剩余电量  | int  |   |   | {"max":100,"min":0}  |   |  
| »»»index  | 电池序号  | int  |   |   | {"min":"0"}  |   |  
| »»»sn  | 电池序列号（SN）  | text  |   |   |   |   |  
| »»»type  | 电池类型  | enum_int  |   |   | {}  |   |  
| »»»sub_type  | 电池子类型  | enum_int  |   |   | {}  |   |  
| »»»firmware_version  | 固件版本  | text  |   |   |   |   |  
| »»»loop_times  | 电池循环次数  | int  |   |   |   |   |  
| »»»voltage  | 电压  | int  |   |   | {"unit":"毫伏 / mV"}  |   |  
| »»»temperature  | 温度  | float  |   |   | {"unit":"摄氏度 / °C"}  | 保留小数点后一位  |  
| »»»high_voltage_storage_days  | 高电压存储天数  | int  |   |   | {"unit":"日 / day"}  |   |  
| storage  | 存储容量  | struct  | r  | 0  |   | kb  |  
| »total  | 总容量  | int  |   |   | {"unit":"千字节 / KB"}  |   |  
| »used  | 已使用容量  | int  |   |   | {"unit":"千字节 / KB"}  |   |  
| position_state  | 搜星状态  | struct  | r  | 0  |   |   |  
| »is_fixed  | 是否收敛  | enum_int  |   |   | {"0":"未开始","1":"收敛中","2":"收敛成功","3":"收敛失败"}  |   |  
| »quality  | 搜星档位  | enum_int  |   |   | {"1":"1档","2":"2档","3":"3档","4":"4档","5":"5档"}  |   |  
| »gps_number  | GPS 搜星数量  | int  |   |   |   |   |  
| »rtk_number  | RTK 搜星数量  | int  |   |   |   |   |  
| track_id  | 航迹 ID  | text  | r  | 0  | {"length":"64"}  |   |  
| _{type-subtype-gimbalindex}_  | {_{type-subtype-gimbalindex}_ _XXGoBhzNpQ}  | struct  | r  | 0  |   | {_{type-subtype-gimbalindex}_ _jwYOqxlOgI}  |  
| »gimbal_pitch  | 云台俯仰轴角度  | double  | r  |   | {"max":"180","min":"-180","step":0.1,"unit":"度 / °"}  |   |  
| »gimbal_roll  | 云台横滚轴角度  | double  | r  |   | {"max":"180","min":"-180","step":0.1,"unit":"度 / °"}  |   |  
| »gimbal_yaw  | 云台偏航轴角度  | double  | r  |   | {"max":"180","min":"-180","step":0.1,"unit":"度 / °"}  |   |  
| »measure_target_longitude  | 激光测距目标经度  | double  | r  |   | {"max":"180","min":"-180","unit":"度 / °"}  |   |  
| »measure_target_latitude  | 激光测距目标纬度  | double  | r  |   | {"max":"90","min":"-90","unit":"度 / °"}  |   |  
| »measure_target_altitude  | 激光测距目标海拔  | double  | r  |   | {"unit":"米 / m"}  |   |  
| »measure_target_distance  | 激光测距距离  | double  | r  |   | {"unit":"米 / m"}  |   |  
| »measure_target_error_state  | 激光测距状态  | enum_int  | r  |   | {"0":"NORMAL","1":"TOO_CLOSE","2":"TOO_FAR","3":"NO_SIGNAL"}  |   |  
| »payload_index  | 负载索引，格式为 _{type-subtype-gimbalindex}_  | text  | r  |   |   |   |  
| »smart_track_point  | Smart Track 点信息  | array  | r  |   | {}  |   |  
| »»[array_item]  | Elements in array  | struct  |   |   | {}  | {"size": ""}  |  
| »»»track_target_mode  | Track 模式  | enum_int  |   |   | {"1":"正常跟踪","2":"正常跟踪，可信度低","3":"目标是 GPS 点，或目标丢失但有预测"}  |   |  
| »»»track_latitude  | 目标纬度  | double  |   |   | {"max":"90","min":"-90","unit":"度 / °"}  |   |  
| »»»track_longitude  | 目标经度  | double  |   |   | {"max":"180","min":"-180","unit":"度 / °"}  |   |  
| »»»track_altitude  | 跟踪目标海拔高度  | double  |   |   | {"unit":"米 / m"}  |   |  
| »zoom_factor  | 变焦倍数  | double  | r  |   |   |   |  
| total_flight_sorties  | 飞行器累计飞行总架次  | int  | r  | 0  |   |   |  
| maintain_status  | 保养信息  | struct  | r  | 0  |   |   |  
| »maintain_status_array  | 保养信息数组  | array  |   |   | {}  |   |  
| »»[array_item]  | Elements in array  | struct  |   |   | {}  | {"size": ""}  |  
| »»»state  | 保养状态  | enum_int  |   |   | {"0":"无保养","1":"有保养"}  |   |  
| »»»last_maintain_type  | 上一次保养类型  | enum_int  |   |   | {"1":"飞行器基础保养","2":"飞行器常规保养","3":"飞行器深度保养"}  |   |  
| »»»last_maintain_time  | 上一次保养时间  | date  |   |   | {"unit":"秒 / s"}  |   |  
| »»»last_maintain_flight_time  | 上一次保养时飞行航时  | int  |   |   | {"unit":"小时 / h"}  |   |  
| »»»last_maintain_flight_sorties  | 上一次保养时飞行架次  | int  |   |   | {"max":"2147483647","min":"0","step":"1"}  |   |  
| activation_time  | 飞行器激活时间(unix 时间戳)  | int  | r  | 0  | {"unit":"秒 / s"}  |   |  
| night_lights_state  | 飞行器夜航灯状态  | enum_int  | rw  | 0  | {"0":"关闭","1":"打开"}  |   |  
| height_limit  | 飞行器限高  | int  | rw  | 0  | {"max":"1500","min":"20","step":"1","unit":"米 / m"}  |   |  
| is_near_height_limit  | 是否接近设定的限制高度  | enum_int  | r  | 0  | {"0":"未达到设定的限制高度","1":"接近设定的限制高度"}  |   |  
| is_near_area_limit  | 是否接近限飞区  | enum_int  | r  | 0  | {"0":"未达到限飞区","1":"接近限飞区"}  |   |  
| obstacle_avoidance  | 飞行器避障状态  | struct  | rw  | 0  |   |   |  
| »horizon  | 水平避障状态  | enum_int  |   |   | {"0":"关闭","1":"开启"}  |   |  
| »upside  | 上视避障状态  | enum_int  |   |   | {"0":"关闭","1":"开启"}  |   |  
| »downside  | 下视避障状态  | enum_int  |   |   | {"0":"关闭","1":"开启"}  |   |  
| rth_mode  | 返航高度模式设置值  | enum_int  | r  | 1  | {"0":"智能高度","1":"设定高度"}  | 智能返航模式下，飞行器将自动规划最佳返航高度。大疆机场当前不支持设置返航高度模式，只能选择'设定高度'模式。当环境，光线不满足视觉系统要求时（譬如傍晚阳光直射、夜间弱光无光），飞行器将使用您设定的返航高度进行直线返航  |  
| current_rth_mode  | 返航高度模式当前值  | enum_int  | r  | 1  | {"0":"智能高度","1":"设定高度"}  | 大疆机场当前只会使用'设定高度'模式  |  
| psdk_ui_resource  | psdk ui 资源包  | array  | r  | 1  | {}  |   |  
| »[array_item]  | Elements in array  | struct  | r  | 1  | {}  | {"size": ""}  |  
| »»psdk_index  | psdk 负载设备索引  | int  |   |   | {"min":0}  |   |  
| »»psdk_ready  | psdk 就绪状态  | enum_int  |   |   | {"0":"未就绪","1":"已就绪"}  |   |  
| »»object_key  | oss 对象  | text  |   |   |   |   |  
| psdk_widget_values  | psdk 负载设备属性值  | array  | r  | 1  | {}  |   |  
| »[array_item]  | Elements in array  | struct  | r  | 1  | {}  | {"size": ""}  |  
| »»psdk_index  | psdk 负载设备索引  | int  |   |   | {"min":0}  |   |  
| »»psdk_name  | 设备名称  | text  |   |   |   |   |  
| »»psdk_sn  | 设备序号  | text  |   |   |   |   |  
| »»psdk_version  | 设备固件版本  | text  |   |   |   |   |  
| »»psdk_lib_version  | psdk lib 版本  | text  |   |   |   |   |  
| »»speaker  | 喊话器状态  | struct  |   |   | [{"identifier":"work_mode","name":"喊话器工作模式","pushMode":1,"accessMode":"r","dataType":{"type":"enum_int","specs":{"0":"TTS 负载模式","1":"录音喊话"}}},{"identifier":"play_mode","name":"喊话器播放模式","pushMode":1,"accessMode":"r","dataType":{"type":"enum_int","specs":{"0":"单次播放","1":"循环播放(单曲)"}}},{"identifier":"play_volume","name":"喊话器音量","pushMode":1,"accessMode":"r","dataType":{"type":"int","specs":{"min":0,"max":100,"step":1}}},{"identifier":"system_state","name":"喊话器状态","pushMode":1,"accessMode":"r","dataType":{"type":"enum_int","specs":{"0":"空闲中","1":"传输中(机场到飞行器)","2":"播放中","3":"异常中","4":"TTS 文本转换中","99":"下载中(机场从云端下载)"}}},{"identifier":"play_file_name","name":"喊话器最近一次播放的文件名称","pushMode":1,"accessMode":"r","dataType":{"type":"text","specs":{"length":128,"unit":"字节 / B"}}},{"identifier":"play_file_md5","name":"喊话器最近一次播放的文件md5校验和","pushMode":1,"accessMode":"r","dataType":{"type":"text"}}]  |   |