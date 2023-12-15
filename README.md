# 2023 1-2 오픈소스 기초설계 repo
## Members
- 권나현
- 문재민
- 류승희
  
## 컴쟁이들을 위한 자세 잔소리 프로그램

## **About Project**
이 프로그램은 사용자의 자세를 분석하여 잠수를 매기고 잘못된 자세가 일정 시간 이상 지속되면 경고를 하여 사용자가 스스로 자세를 고칠 수 있게 한다. 사용자는 현재 자신이 앉아 있는 자세를 직접 확인할 수 있고 잘못된 자세를 프로그램의 도움으로 인지할 있다. 

## _Technology_
- python
- tensorflow
- opencv
- openpose

## _How to_
src 폴더의 test_code 폴더 안에 있는 파일들은 이미지를 넣어 돌릴 수 있는 코드입니다.
src 폴더의 code 폴더 안에 있는 파일들을 영상을 넣어 돌릴 수 있는 코드입니다.
src 폴더의 model 폴더에는 COCO 기반의 openpose 모델이 들어있습니다. 코드를 돌리려면 model의 경로를 수정해주세요.