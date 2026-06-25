<!-- source: https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/remote-debug.html -->
<!-- path: feature-set/dock-feature-set/remote-debug -->

##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/remote-debug.html#%E5%8A%9F%E8%83%BD%E6%A6%82%E8%BF%B0) 功能概述
远程调试为在调试的作业流中实现无人值守，即让作业人员无需到现场，在云端就可以下发命令到设备端，进行设备的远程排障。远程调试命令可分为命令（cmd）和任务（job）。命令（cmd）一般指命令下发后，设备能即刻回复的行为，而任务（job）为任务下发后，设备需要持续动作的行为。
###  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/remote-debug.html#%E8%BF%9C%E7%A8%8B%E8%B0%83%E8%AF%95%E6%8C%87%E4%BB%A4) 远程调试指令
下发的指令经由云端跟设备之间传输的`下发控制命令`协议中“method”字段指定，详细的协议内容请根据本节中的`接口详细实现`在`云端API章节`中查看。  
| 命令（cmd）  | 任务（job）  |  
| --- | --- |  
| 调试模式开启/关闭  
补光灯开启/关闭  
4G图传功能开启/关闭  
一键返航  | 机场重启  
飞行器开机/关机  
一键排障（一键起飞自检）  
飞行器数据格式化  
机场数据格式化  
打开/关闭舱盖  
推杆展开/闭合  
充电打开/关闭  
 |  
###  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/remote-debug.html#%E4%BB%BB%E5%8A%A1-job-%E6%89%A7%E8%A1%8C%E6%B5%81%E7%A8%8B) 任务（job）执行流程
任务（job）下发后，设备将会返回执行状态。该状态定义在传输协议的“status”字段中。 状态列举如下：
  * 已下发
  * 执行中
  * 执行成功
  * 暂停
  * 拒绝
  * 失败
  * 取消或终止
  * 超时
执行流程如下：
![](https://terra-1-g.djicdn.com/71a7d383e71a4fb8887a310eb746b47f/cloudapi/V1.2.0/__________.png)
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/remote-debug.html#%E4%BA%A4%E4%BA%92%E6%97%B6%E5%BA%8F%E5%9B%BE) 交互时序图
DJI DockCloud Server下发命令（cmd）Topic: thing/product/{gateway_sn}/servicesMethod:{cmd_method}回复是否开始执行Topic: thing/product/{gateway_sn}/services_reply下发任务（job）Topic: thing/product/{gateway_sn}/servicesMethod:{cmd_method}回复是否开始执行Topic: thing/product/{gateway_sn}/services_reply上报任务进度Topic: thing/product/{gateway_sn}/eventsMethod:{cmd_method}DJI DockCloud Server
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/feature-set/dock-feature-set/remote-debug.html#%E6%8E%A5%E5%8F%A3%E8%AF%A6%E7%BB%86%E5%AE%9E%E7%8E%B0) 接口详细实现
[远程调试open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/dock-to-cloud/mqtt/dock/dock1/cmd.html)
  * 命令进度
  * 下发命令
  * 下发任务
  * ......