# 버킷 버저닝 활성화

동일한 버킷 내에 기존 파일을 최신 버전으로 갱신하지만, 기존 버전도 유지하고 싶은 경우 버킷 버저닝(Bucket Versioning) 을 사용 할 수 있습니다.

## 버저닝 활성화

1. Amazon S3 Console에서 버저닝을 활성화하고자 하는 버킷을 선택하고 Properties 메뉴를 선택하십시오. Bucket Versioning의 Edit 버튼을 클릭합니다.

![](../images/gid-s3-31.png)

- Bucket Versioning 기능 활성화 라디오 버튼을 클릭한 뒤, Save changes를 클릭합니다.

![](../images/gid-s3-32.png)

2. 편집 가능한 파일을 선택하여 버저닝 기능이 활성화된 원본 파일을 일부 수정하여 저장 하고, 수정된 파일을 다시 버킷에 업로드하십시오. 본 실습에서는 index.html 파일을 수정한 뒤, 같은 이름으로 재업로드합니다.

3. 변경된 파일의 업로드가 완료되면, S3 Console에서 해당 오브젝트를 클릭합니다. 오브젝트 상세 정보가 기재된 페이지에서 Versions 탭을 클릭하면, current version 정보를 확인할 수 있습니다.

![](../images/gid-s3-33.png)

[Previous](./move-object.md) | [Next](./delete-bucket.md)