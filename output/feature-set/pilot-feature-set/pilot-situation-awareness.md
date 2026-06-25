<!-- source: https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-situation-awareness.html -->
<!-- path: feature-set/pilot-feature-set/pilot-situation-awareness -->

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-situation-awareness.html#%E5%8A%9F%E8%83%BD%E6%A6%82%E8%BF%B0) 功能概述
态势感知功能主要是服务端可以推送设备（飞机/遥控器）坐标信息给到 Pilot 端， Pilot 会把推送过来的信息显示在地图中。这样就可以实现把同一个工作空间下的所有设备之间信息形成一张网，不止web端可以看到，飞手端也可以看到，从而有效的促进所有设备间的态势信息分享与沟通。
如下图所示，Pilot A 、Pilot B、 DOCK A、DOCK B通过上云API接口推送自身的设备拓扑和设备经纬度坐标给服务端，同时服务端也接收其他人员和设备的GPS信息，并把这些信息汇集到同一个工作空间，然后通过websocket把信息推送给Pilot， 这样Pilot A、Pilot B就可以在地图中看到整个工作空间下的所有人员和设备位置信息。
![](https://terra-1-g.djicdn.com/84f990b0bbd145e6a3930de0c55d3b2b/admin/doc/a6edba65-5f9b-457f-85dc-465d8829c461.png)   
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-situation-awareness.html#pilot-%E4%BA%A4%E4%BA%92%E6%97%B6%E5%BA%8F%E5%9B%BE) Pilot 交互时序图
Pilot WebviewDJI Pilot 2Cloud ServerOthers需先设置workspaceId, 加载api,ws,tsa模块opt[设备上线/下线]loop[状态推送]登录第三方云平台JSBridge:platformLoadComponent  加载 API 模块、WS 模块、TSA模块Websocket连接连接Pilot 首次上线，请求设备列表拓扑应答推送设备遥感信息定频推送设备遥测信息其他设备拓扑更新通过websocket推送device_online信息处理websocket信息请求设备列表拓扑Pilot WebviewDJI Pilot 2Cloud ServerOthers
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/pilot-feature-set/pilot-situation-awareness.html#%E6%8E%A5%E5%8F%A3%E8%AF%A6%E7%BB%86%E5%AE%9E%E7%8E%B0) 接口详细实现
  * [JSBridgeopen in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/jsbridge.html)  
加载态势感知模块  
在使用态势感知功能之前，需要预先在H5页面中通过JSBridge设置好工作空间信息（workspaceId），配置好ws模块、api模块，然后加载Pilot2的tsa模块。开发者可以考虑在上下线登录阶段直接添加加载tsa模块的接口。
  * [态势感知（HTTPS）open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/https/situation-awareness/obtain-device-topology-list.html)  
获取设备拓扑列表  
    * Pilot 在首次上线后，会发送http请求去获取同一个工作空间下的所有设备列表及其拓扑，服务端需要把整个设备列表发给Pilot2。同时，当接收到websocket指令通知设备online/offline/update的时候，也是需要调用该接口进行请求设备拓扑列表进行更新。
    * 自定义图标  
设备可以显示自定义图标，使用字段 icon_urls 来定义，如果有定义该字段，则优先按该字段的内容来显示。如果没有则按device_model来默认显示。
```
"icon_urls":{      
                "normal_icon_url":"resource://Pilot2/drawable/tsa_aircraft_others_normal",    // 正常状态下的图标
                "selected_icon_url":"resource://Pilot2/drawable/tsa_aircraft_others_pressed",   // 选中状态下的图标
            }
```
App内置了一些图标可供外部使用
```
url样式： resource://Pilot2/drawable/tsa_aircraft_others_normal
```
内置图标列表  
| 图标样式  | icon_url  | 备注  |  
| --- | --- | --- |  
| ![GTScreenshot_20220322_172153.png](https://terra-1-g.djicdn.com/84f990b0bbd145e6a3930de0c55d3b2b/admin/doc/33e69a29-a625-4196-8955-535fab5a1ef2.png)  | resource://Pilot2/drawable/tsa_car_select  |   |  
| ![GTScreenshot_20220322_172131.png](https://terra-1-g.djicdn.com/84f990b0bbd145e6a3930de0c55d3b2b/admin/doc/c458f256-4011-4205-9d6c-4c6e19d7d319.png)  | resource://Pilot2/drawable/tsa_car_normal  |   |  
| ![GTScreenshot_20220322_172207.png](https://terra-1-g.djicdn.com/84f990b0bbd145e6a3930de0c55d3b2b/admin/doc/19ee7c1b-fc10-468a-bfc5-bf00b1d62cdc.png)  | resource://Pilot2/drawable/tsa_person_select  |   |  
| ![GTScreenshot_20220322_172226.png](https://terra-1-g.djicdn.com/84f990b0bbd145e6a3930de0c55d3b2b/admin/doc/256035a6-4fb0-4a1d-8c67-0cbbd218d593.png)  | resource://Pilot2/drawable/tsa_person_normal  |   |  
| ![GTScreenshot_20220322_172239.png](https://terra-1-g.djicdn.com/84f990b0bbd145e6a3930de0c55d3b2b/admin/doc/5feb755a-a9fb-4388-be4a-6731edc4c848.png)  | resource://Pilot2/drawable/tsa_equipment_select  |   |  
| ![GTScreenshot_20220322_172248.png](https://terra-1-g.djicdn.com/84f990b0bbd145e6a3930de0c55d3b2b/admin/doc/811e604b-ed8a-49b0-aa02-48563e3833a4.png)  | resource://Pilot2/drawable/tsa_equipment_normal  |   |  
同时也可以定义网络上的图标，App内部下载缓存这些图标，并以固定大小(28dp)加载显示到地图上。
```
url样式：http://r56978dr7.hn-bkt.clouddn.com/tsa_equipment_normal.png
```
Pilot 地图中显示的图标如下图所示：
![](https://terra-1-g.djicdn.com/84f990b0bbd145e6a3930de0c55d3b2b/admin/doc/90d82dc5-dc7b-404a-8cec-208c4cf9d466.png)   
  * [态势感知（WebSocket）open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/websocket/situation-awareness/message-push.html) 与 [遥控器设备管理open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/mqtt/rc-plus/properties.html)  
    * 其他设备会推送遥感信息给到服务器端，同时服务端定频推送同一个工作空间下的所有设备遥感信息给 Pilot 端， Pilot 会根据接收到的数据实时更新地图中设备状态和位置。
    * 设备上线/下线推送  
当服务端接收到同一个工作空间下的任意设备拓扑更新的请求后，同时也通过websocket广播一条设备更新拓扑的推送给到 Pilot 端， Pilot 收到该推送后，会触发“获取设备拓扑列表”。