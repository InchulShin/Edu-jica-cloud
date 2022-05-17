# Enviroment에서 사용하는 Amazon EBS 볼륨 크기 조정
크기를 조정할 Amazon EBS 볼륨에 대해 Amazon EC2 인스턴스와 연결된 환경을 엽니다.

AWS Cloud9 환경의 IDE에서 다음 내용의 파일을 만든 다음 해당 파일을 확장명으로 저장합니다..sh(예:resize.sh).

Note
이 스크립트는 Amazon Linux 2, Amazon Linux 또는 Ubuntu 서버를 실행하는 EC2 인스턴스에 연결된 Amazon EBS 볼륨에 적용됩니다.

또한 이 스크립트는 Nitro 기반 인스턴스에 NVMe 블록 디바이스로 표시된 Amazon EBS 볼륨의 크기를 조정합니다. Nitro 시스템을 기반으로 하는 인스턴스 목록은 단원을 참조하십시오.

```
#!/bin/bash

# Specify the desired volume size in GiB as a command line argument. If not specified, default to 20 GiB.
SIZE=${1:-20}

# Get the ID of the environment host Amazon EC2 instance.
INSTANCEID=$(curl http://169.254.169.254/latest/meta-data/instance-id)

# Get the ID of the Amazon EBS volume associated with the instance.
VOLUMEID=$(aws ec2 describe-instances \
  --instance-id $INSTANCEID \
  --query "Reservations[0].Instances[0].BlockDeviceMappings[0].Ebs.VolumeId" \
  --output text)

# Resize the EBS volume.
aws ec2 modify-volume --volume-id $VOLUMEID --size $SIZE

# Wait for the resize to finish.
while [ \
  "$(aws ec2 describe-volumes-modifications \
    --volume-id $VOLUMEID \
    --filters Name=modification-state,Values="optimizing","completed" \
    --query "length(VolumesModifications)"\
    --output text)" != "1" ]; do
sleep 1
done

#Check if we're on an NVMe filesystem
if [ $(readlink -f /dev/xvda) = "/dev/xvda" ]
then
  # Rewrite the partition table so that the partition takes up all the space that it can.
  sudo growpart /dev/xvda 1

  # Expand the size of the file system.
  # Check if we are on AL2
  STR=$(cat /etc/os-release)
  SUB="VERSION_ID=\"2\""
  if [[ "$STR" == *"$SUB"* ]]
  then
    sudo xfs_growfs -d /
  else
    sudo resize2fs /dev/xvda1
  fi

else
  # Rewrite the partition table so that the partition takes up all the space that it can.
  sudo growpart /dev/nvme0n1 1

  # Expand the size of the file system.
  # Check if we're on AL2
  STR=$(cat /etc/os-release)
  SUB="VERSION_ID=\"2\""
  if [[ "$STR" == *"$SUB"* ]]
  then
    sudo xfs_growfs -d /
  else
    sudo resize2fs /dev/nvme0n1p1
  fi
fi
```

IDE의 터미널 세션에서 포함된 디렉터리로 전환합니다.resize.sh파일을 복사합니다. 그런 다음 다음 명령 중 하나를 실행하여20를 Amazon EBS 볼륨의 크기를 다음과 같이 조정하려는 GiB 단위로 바꿉니다.

```
chmod +x resize.sh
```

```
bash resize.sh 100
```

```
./resize.sh 100
```