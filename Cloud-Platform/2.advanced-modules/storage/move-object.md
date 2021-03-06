# 오브젝트 이동

지금까지의 과정에서 버킷에 오브젝트를 추가하고 이를 확인하는 기능을 확인했습니다. 이제, 오브젝트를 다른 버킷이나 폴더로 이동하는 기능을 확인하겠습니다.

## 오브젝트 이동

1. 버킷 간 오브젝트 이동을 위하여 임시 버킷을 생성하십시오. (버킷 이름 : 기존생성버킷명-temp)
빠른 구성을 위하여 Block all public access 체크 박스를 해제 하십시오.

![](../images/gid-s3-25.png)

2. 아래의 알림 창에 체크하시고, Create bucket를 선택하십시오.

![](../images/gid-s3-26.png)

3. Amazon S3 Console에서 오브젝트가 있는 버킷(처음 생성한 버킷)을 선택하고 이동하고자 하는 오브젝트의 체크박스를 클릭하십시오. 상단의 Actions 메뉴를 선택하면 해당 오브젝트에 대하여 수행할 수 있는 다양한 기능들을 확인할 수 있습니다. 나열된 기능들 중 Move 을 선택합니다.

![](../images/gid-s3-27.png)

4. 아래와 같이 목적지를 버킷으로 선택한 후, Browse S3 버튼을 클릭합니다.

![](../images/gid-s3-28.png)

5. 팝업 창에서 버킷 이름을 클릭한 후, 대상(도착) 버킷을 선택합니다. Choose destination 버튼을 클릭합니다.

![](../images/gid-s3-29.png)

![](../images/gid-s3-29-1.png)

6. 대상 버킷에서 오브젝트가 이동한 것을 확인하세요.

![](../images/gid-s3-30.png)

오브젝트를 이동시키더라도 기존에 설정된 권한은 그대로 유지됩니다.

[Previous](./static-web-hosting.md) | [Next](./enable-versioning.md)