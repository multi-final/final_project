# <h1 align = "center"> 오늘의 간추린 뉴스 </h1>
<p align = "center"> 바쁜 현대인들을 위한 주요 뉴스 요약 서비스 </p>

<div align = "center">

<img width="30%" src="https://github.com/kihyun2/test/assets/103742790/2714364b-85c3-4050-a255-742e40f6553b">

</div>

</br>

## 📰 오간뉴 프로젝트 소개
&nbsp;&nbsp;오간뉴는 "오늘의 간추린 뉴스"라는 뜻의 약어입니다. 오간뉴는 매일 아침 주요 뉴스를 AI가 요약해서 제공해주는 서비스 입니다. 뉴스의 핵심을 파악하여 이를 위주로 기사를 간략하게 간추려 줌으로써, 바쁜 현대인들이 정보를 빠르고 효율적으로 습득할 수 있도록 지원하는 서비스입니다.</br>

&nbsp;&nbsp;오간뉴는 미디어의 생산 및 유통과정에 AI가 주도적으로 참여하게 되어, AI솔루션(Tranformer)을 활용하여 변형한 컨텐츠를 이용자가 선택한 성향에 맞춘 초 개인화 서비스와 함께 제공합니다.</br>

&nbsp;&nbsp;오간뉴는 AI를 통해 기사를 재생성함으로써 보다 객관적이고 직관적인 보도를 합니다. 또한 오간뉴에서는 개인의 성향에 따라 언론사, 섹션을 선택하여 취향대로 구독할 수 있습니다.</br>

</br>

개발 기간: 2023년 4월 25일 ~ 2023년 6월 9일</br>
개발 인원: 총 5명(AI 모델링 2명, 프론트엔드 2명, 백엔드 1명)

</br>

## 🐤 프로젝트 팀 소개
<br>

|[조민우](https://github.com/minu-97)|[고은영](https://github.com/iameun02)|[박기현](https://github.com/kihyun2)|[하정수](https://github.com/Eric4848)|[유재찬](https://github.com/DevRyu10)|
|:---:|:---:|:---:|:---:|:---:|
|`AI modeling`|`AI modeling`|`Front-end`|`Front-end`|`Back-end`|
<br>
<br>

## 💻 화면 구성
<br>

|메인| 기사 보기|
| :---: |  :---: |
|<img src="https://github.com/kihyun2/test/assets/103742790/cd9ffe12-6f9b-4504-aeea-b401e7eee844" width="100%" height="100%"/> |<img src="https://github.com/kihyun2/test/assets/103742790/027d9b30-4f49-420a-941c-1aefb4eb600d" width="100%" height="100%"/>|<img src="https://user-images.githubusercontent.com/78632299/210406605-3f3dbfef-21f0-4731-991e-2489aac4f19a.gif" width="100%" height="100%"/>|
|기사 키워드의 워드클라우드와 날씨를 확인할 수 있습니다.| 기사를 확인하고 분류, 검색, 스크랩할 수 있습니다.|

</br>
</br>

## 📖 프로젝트 기능 구성
### 주요 기능
1. 요약 기사 제공
   - 10개 언론사 및 5개 분야에서 크롤링한 기사 1000개를 각각 요약하여 제공합니다.
   - ajax를 이용해 페이지 갱신 없이 스크롤하여 기사를 한눈에 볼 수 있습니다.
   - 언론사, 분야를 선택하면 해당 언론사, 분야로 기사를 필터링하여 볼 수 있습니다.
   - 찾고 싶은 키워드를 입력하면 검색이 가능합니다.
2. 스크랩
   - 로그인된 유저가 Scrap 버튼 클릭시 스크랩할 수 있습니다.
   - Scrap된 기사 또한 관심있는 언론사, 분야로 필터링이 가능합니다.
### 추가 기능
1. 워드클라우드
   - 기사 요약문에서의 키워드 노출 빈도로 만든 워드클라우드를 제공합니다.
   - 워드클라우드에서 키워드를 클릭하면 해당 키워드가 나온 기사들을 볼 수 있습니다.
   - 분야별의 워드클라우드를 확인할 수 있습니다.
2. 날씨
   - 현재 온도와 날씨, 일주일간의 날씨를 함께 제공합니다.

</br>
</br>

## 🔍 데이터 수집

|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| 학습용 데이터 | 서비스 데이터 |
|:---:| :---: | :---: |
| 대상 | AI HUB, 레포트 생성 데이터, 네이버 뉴스(IT/과학) 요약 문장 태깅 데이터셋 |네이버 뉴스|
| 개수 |10,850개|1000개 / 일|
| 이유 |뉴스 원문 기사 요약 학습|매일 기사를 수집하여 요약 후 웹사이트를 통해 요약문 제공|
| 절차 |AI HUB, Github을 통해 다운로드| 10개 언론사 및 5개 섹션에서 크롤링, 자동화 구현을 위해 크론탭 사용|

</br>
</br>

## 🔨 데이터 전처리

| 수집 데이터 전처리 | Model Input 데이터 전처리 | Keyword extraction|
|:---:|:---:|:---:|
|결측치 제거| 개행 제거|정규표현식을 통해 숫자 제거|
|중복 내용 제거|원문 str 타입으로 변환|2글자 이상의 단어만 추출|
|데이터 파싱 | 입력 문자 길이 제한(max_length=512)|불용어 제거|
|DB 구조에 맞게 데이터 타입 변환(날짜,기자 정보)|토큰화 및 텐서화|

</br>
</br>

## 📌 인공지능 모델 선정
</br>
<div align = "center">

|모델 비교|
| :---: |
|<img width="80%" src="https://github.com/kihyun2/test/assets/103742790/f18ba713-843a-4bc7-b66c-414baba9ce19">|
|전이 학습 및 파인튜닝 과정을 거쳐 여러 모델을 비교 후, 최종적으로 KoBART-base-v2 모델을 서빙 모델로 선정|

</br>

| v2 모델을 사용한 요약 결과 |
| :---: |
|<img src="https://github.com/kihyun2/test/assets/103742790/f7ba3ed8-4c91-4146-afda-86c198fab119">|
|<img src="https://github.com/kihyun2/test/assets/103742790/dc8c402f-d7e4-44fe-bf9e-23f589d49800">|

</div>
</br>
</br>

## 📂 시스템 구조
<div align = "center">

<img src="https://github.com/kihyun2/test/assets/103742790/2a8890ca-bc89-4b83-873d-1e3803107018">

</div>
</br>
</br>

## 💡 Skills

### AI modeling
![colab](https://img.shields.io/badge/colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)
![pytorch](https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)


### Front-end
![javascript](https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

### Back-end
![django](https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white)
![mariadb](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white)

### Deploy
![aws](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![docker](https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
