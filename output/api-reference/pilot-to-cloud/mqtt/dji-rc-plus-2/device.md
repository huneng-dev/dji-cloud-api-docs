<!-- source: https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/mqtt/dji-rc-plus-2/device.html -->
<!-- path: api-reference/pilot-to-cloud/mqtt/dji-rc-plus-2/device -->

#  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/mqtt/dji-rc-plus-2/device.html#event) Event
##  [#](https://developer.dji.com/doc/cloud-api-tutorial/cn/api-reference/pilot-to-cloud/mqtt/dji-rc-plus-2/device.html#%E8%AE%BE%E5%A4%87%E6%8B%93%E6%89%91%E6%9B%B4%E6%96%B0) 设备拓扑更新
**Topic:** thing/product/_{gateway_sn}_ /status
**Direction:** up
**Method:** update_topo
**Data:**  
| Column  | Name  | Type  | constraint  | Description  |  
| --- | --- | --- | --- | --- |  
| type  | 网关设备的产品类型  | int  |   | 参考：[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)  |  
| sub_type  | 网关子设备的产品子类型  | int  |   | 参考：[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)  |  
| device_secret  | 网关设备的密钥  | text  |   |   |  
| nonce  | nonce  | text  |   |   |  
| thing_version  | 网关设备的物模型版本  | text  |   |   |  
| sub_devices  | 子设备列表  | array  | {"size": 1, "item_type": struct}  |   |  
| »sn  | 子设备序列号（SN）  | text  |   |   |  
| »type  | 子设备的产品类型  | int  |   | 参考：[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)  |  
| »sub_type  | 子设备的产品子类型  | int  |   | 参考：[产品支持open in new window](https://developer.dji.com/doc/cloud-api-tutorial/cn/overview/product-support.html)  |  
| »device_secret  | 子设备的密钥  | text  |   |   |  
| »nonce  | nonce  | text  |   |   |  
| »thing_version  | 子设备的物模型版本  | text  |   |   |