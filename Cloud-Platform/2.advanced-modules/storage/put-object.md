# 버킷에 오브젝트 추가하기

버킷이 정상적으로 생성 되었다면 오브젝트를 추가할 준비가 되었습니다. 오브젝트는 텍스트 파일, 이미지 파일 및 비디오 파일 등 모든 종류의 파일이 될 수 있습니다. Amazon S3에 파일을 추가할 때, 해당 파일에 대한 권한 및 접근 설정 등에 대한 정보를 메타데이터에 포함시킬 수 있습니다.

## 정적 웹 호스팅을 위한 오브젝트 추가
이번 실습은 S3를 통해, 정적 웹사이트를 호스팅합니다. 해당 정적 웹사이트는 특정 이미지를 클릭하면 VPC Lab에서 생성한 인스턴스로 리다이렉팅하는 역할을 합니다. 따라서 이미지 파일 1개, HTML 파일 1개, ALB DNS name을 준비합니다.

1. [aws.png](../images/aws.png) 이미지 파일을 다운로드하여 aws.png 로 저장 합니다.

2. 아래의 소스코드를 이용하여 index.html 을 작성합니다.

```
<html>
    <head>
        <meta charset="utf-8">
        <title> AWS General Immersion Day S3 HoL </title>
    </head>
    <body>
        <center>
        <br>
        <h2> Click image to be redirected to the EC2 instance that you created </h2>
        <img src="S3에 업로드될 이미지 접근 URL" onclick="window.location='DNS 이름'"/>
        </center>
    </body>
</html>
```

3. aws.png 파일을 S3로 업로드 합니다. 방금 생성한 S3 버킷 을 클릭 합니다.

![](../images/gid-s3-05.png)

4. Upload 버튼을 클릭하고 Add files 버튼을 클릭합니다. 파일 탐색기를 통해서 미리 다운로드 받아둔 aws.png 파일을 선택합니다. 또는 해당 파일을 화면으로 Drag & Drop 으로 가져다 놓습니다.

![](../images/gid-s3-06.png)

![](../images/gid-s3-07.png)

5. 업로드할 파일 정보 aws.png 파일을 확인한 후, 하단의 Upload 버튼을 클릭하여 업로드 합니다.

![](../images/gid-s3-08.png)

![](../images/gid-s3-08-1.png)

6. index.html에 이미지 URL을 기입하기 위해서 URL 정보를 확인합니다. 업로드 된 aws.png 파일을 선택한 후, 우측에 나오는 상세 정보에서 Object URL 정보를 복사합니다.

![](../images/gid-s3-09.png)

7. index.html에 이미지의 URL 부분에 복사해둔 Object URL 을 붙여 넣습니다. 그리고 이미지를 클릭하면 ALB로 이동하도록 2-2. 오토 스케일링 웹 서비스 배포에서 생성한 로드밸런서의 ALB DNS Name(http://ALB  DNS Name) 을 지정합니다.

![](../images/gid-s3-10.png)

8. 이미지 업로드한 방법과 같이 index.html 파일도 S3에 업로드 합니다.

![](../images/gid-s3-11.png)

9. 업로드한 이미지를 확인하면 다음과 같습니다.

![](../images/gid-s3-12.png)

[Previous](./create-bucket.md) | [Next](./view-object.md)