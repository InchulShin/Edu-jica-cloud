# 정적 웹 사이트 호스팅 사용

Amazon S3를 이용하여 정적 웹 사이트를 호스팅할 수 있습니다.

## 정적 웹 사이트 설정
정적 웹 사이트란, 웹 페이지에 정적 콘텐츠(HTML, 이미지, 비디오) 또는 클라이언트 측 스크립트(Javascript)만을 포함하는 웹 사이트를 가리킵니다. 이와는 대조적으로 동적 웹 사이트의 경우 PHP, JSP 또는 ASP.NET과 같은 서버 측 스크립트를 포함한 서버 측 처리를 필요로 합니다. Amazon S3에서는 서버 측 스크립팅을 지원하지 않습니다. 동적 웹 사이트를 호스팅하고자 하는 경우, AWS의 EC2와 같은 다른 서비스를 사용하면 됩니다.

1. S3 콘솔에서 방금 생성한 버킷을 선택하고, Properties 탭을 클릭합니다. 스크롤을 내려 Static website hosting 의 Edit 버튼을 클릭합니다.

![](../images/gid-s3-22.png)

![](../images/gid-s3-22-1.png)

2. 정적 웹사이트 호스팅 기능 활성화 및 호스팅 타입 선택 그리고 index document 값에 index.html 값을 입력한 후, save changes 버튼을 클릭합니다.

![](../images/gid-s3-23.png)

3. Static website hosting 항목에 생성된 Bucket website endpoint를 클릭하여 정적 웹 사이트로 접속합니다.

![](../images/gid-s3-23-1.png)

4. 접속이 잘 됩니다. 이렇게 Amazon S3를 이용하여 정적 웹 사이트를 호스팅할 수 있습니다.

![](../images/gid-s3-24.png)

[Previous](./view-object.md) | [Next](./move-object.md)