# 🔍 FinScope · 글로벌 재무제표 분석기

한국 DART · 미국 SEC EDGAR 기반 기업 재무제표 검색 · 비교 · 시각화 도구

## 🌐 라이브 데모

👉 **[FinScope 사용하기](https://YOUR_USERNAME.github.io/REPO_NAME/)**

> 위 링크의 `YOUR_USERNAME`과 `REPO_NAME`을 본인 정보로 변경하세요.

## ✨ 주요 기능

### 🇰🇷 한국 기업 분석 (DART)
- 11만+개 한국 기업 검색 (상장사, 기타법인 포함)
- 단일 기업 N년 재무제표 분석 (사업/반기/분기 보고서)
- 두 기업 비교 분석
- 자동 재무비율 계산 (ROE, ROA, 부채비율 등 7개)
- 공시 이력 조회 (사업보고서/감사보고서)

### 🇺🇸 미국 기업 분석 (SEC EDGAR)
- 13,000+개 미국 상장기업 검색
- 단일/비교 분석 (10-K, 10-Q)
- US-GAAP 기준 재무 데이터
- XBRL 태그 + 한국어 번역 동시 표시

### 📊 풍부한 시각화
- 재무상태표/손익계산서 막대 차트
- **재무비율 레이더 차트** (7개 비율 한눈에)
- **수익성 구조 차트** (매출→총이익→영업이익→순이익)
- **다년 추세 라인 차트** (연도별 변화)
- **주가 차트** (캔들/라인/영역, 이동평균선, 거래량)

### 💾 추가 기능
- API 키 브라우저 저장 (localStorage)
- Word 파일 내보내기 (.docx)
- 영문(한글) 동시 표기

## 🔑 사용 준비

### 한국 DART 사용 시
1. [Open DART](https://opendart.fss.or.kr/) 회원가입
2. **[인증키 신청/관리]** 메뉴에서 API 키 발급 (40자리)
3. 발급받은 키를 페이지 상단에 입력 → [✓ 확인]

### 미국 SEC 사용 시
- 인증키 불필요. 미국 탭으로 전환만 하면 됩니다.

## 🛡️ CORS 우회 (권장)

브라우저는 보안 정책상 외부 API 직접 접근이 제한됩니다. 가장 안정적인 방법은 로컬 프록시를 띄우는 것입니다.

```bash
python dart_proxy.py
```

페이지에서 [📖 로컬 프록시 안내] 버튼을 누르면 자세한 가이드와 함께 프록시 스크립트를 다운로드할 수 있습니다.

## 🛠 기술 스택

- **순수 HTML/CSS/JavaScript** (빌드 도구 불필요)
- Chart.js 4.4 (재무 차트)
- TradingView lightweight-charts (주가 차트)
- docx.js (Word 다운로드)
- DART API + SEC EDGAR API
- Yahoo Finance + Stooq.com (주가 데이터)

## 📋 데이터 출처

- 한국: [Open DART](https://opendart.fss.or.kr/)
- 미국: [SEC EDGAR](https://www.sec.gov/edgar)
- 주가: [Yahoo Finance](https://finance.yahoo.com/) · [Stooq](https://stooq.com/)

## ⚖️ 라이선스 / 면책

- 본 도구는 교육 및 개인 분석 용도로 제작되었습니다.
- 표시되는 모든 재무 데이터는 공시 자료에서 가져온 것으로, 실제 투자 결정에는 원본 공시 자료를 직접 확인하시기 바랍니다.
- 주가 데이터는 실시간이 아니며 (Yahoo 약 15분 지연, Stooq 1일 지연), 투자 의사결정의 근거로 사용해서는 안 됩니다.
