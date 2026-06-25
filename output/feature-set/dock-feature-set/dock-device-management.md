---
source: https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/dock-device-management.html
path: feature-set/dock-feature-set/dock-device-management
---

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/dock-device-management.html#%E5%8A%9F%E8%83%BD%E6%A6%82%E8%BF%B0) 功能概述
设备管理功能支持设备向云端上报拓扑信息、推送设备属性、以及云端对设备的属性进行设置。让用户可以在云端查看以及调整设备状态，更为方便地展开工作。
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/dock-device-management.html#%E4%BA%A4%E4%BA%92%E6%97%B6%E5%BA%8F%E5%9B%BE) 交互时序图
AircraftDJI DockCloud Server设备上线loop[osd属性 0.5HZ 定频推送]opt[state属性 事件性上报]设备下线设备与网关通信连接，设备上线设备拓扑更新 Topic: sys/product/{gateway_sn}/statusMethod: update_topo飞行器属性推送设备（飞行器）属性推送 Topic: thing/product/{device_sn}/osd设备（机场）属性推送 Topic: thing/product/{device_sn}/osd飞行器属性推送设备（飞行器）属性推送 Topic: thing/product/{device_sn}/state设备（机场）属性推送 Topic: thing/product/{device_sn}/state设备属性设置 Topic: thing/product/{gateway_sn}/property/set变更命令下发设备属性变更飞行器响应设备端响应 Topic: thing/product/{gateway_sn}/property/set_reply设备与网关设备通信断开，设备下线设备拓扑更新 Topic: sys/product/{gateway_sn}/statusMethod: update_topoAircraftDJI DockCloud Server
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/dock-device-management.html#%E6%8E%A5%E5%8F%A3%E8%AF%A6%E7%BB%86%E5%AE%9E%E7%8E%B0) 接口详细实现
  * [飞行器设备属性open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/aircraft/properties.html)
  * [机场设备属性open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/properties.html)
  * [设备管理（MQTT）open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/device.html)
    * 设备拓扑更新  
网关设备感知到与子设备通信的连接与断开，会向云端上报子设备的上下线状态。协议中`type`与`sub_type`的值请参照[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)章节找到对照。
    * 设备属性推送  
设备属性划分为定频数据（osd）与状态数据（state），osd 属性会以 0.5 HZ定频上报，state属性会在属性变化时上报。不同的设备属性我们提供了不同的处理策略，使用不同的topic上报。设备属性分别介绍在：[飞行器设备属性open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/aircraft/properties.html)、[机场设备属性open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/properties.html)与[遥控器设备属性open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/aircraft/properties.html)章节。
    * 设备属性设置  
      * 当前设备属性的设置没有实现全面覆盖，我们将在后续逐渐实现。
      * 在设备属性章节中通过“accessMode”标识属性的读写状态，标识为“rw”表示属性可以被设置。
      * 设备属性设置只支持单个属性字段的设置。譬如`飞机限远状态（distance_limit_status）`属性包括`是否开启限远（state）`和`限远距离（distance-limit）`两个字段。在做飞机限远状态的属性设置时，设置指令需要发送两次。