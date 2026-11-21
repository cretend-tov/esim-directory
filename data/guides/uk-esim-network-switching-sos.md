---
title: "영국에서 eSIM 통신망이 계속 바뀌거나 SOS만 뜰 때"
description: "런던·스코틀랜드에서 여행 eSIM이 EE·O2·Vodafone·Three 사이를 오가며 끊기거나 'SOS'·'서비스 없음'만 뜰 때, 데이터 로밍·회선 점검부터 통신망 수동 선택·자동 복귀까지 Airalo·Saily·Holafly·Apple·Google 공식 안내와 실제 후기로 정리했습니다. 2026-11-21 확인."
country: 영국
problem: "통신망이 계속 바뀜 / SOS·No Service / 신호는 있는데 데이터 끊김"
verified_on: "2026-11-21"
---
## 증상

- 영국(런던·맨체스터·에든버러 등)에서 여행 eSIM의 **통신사 표시가 EE ↔ O2 ↔ Vodafone ↔ Three 등으로 계속 바뀌고**, 바뀔 때마다 데이터가 잠깐씩 끊긴다.
- 상태 표시줄에 **'SOS'·'SOS만'·'서비스 없음(No Service)'·'검색 중'**이 뜨고 인터넷이 안 된다. 위성 아이콘이 함께 보이기도 한다.
- 신호 막대는 있는데 앱이 안 열리고, 몇 분 뒤 다시 되는 일이 반복된다.

## 먼저 알아둘 것: 'SOS'의 뜻과 영국에서 내 eSIM이 쓰는 통신망

**SOS의 뜻 (Apple 공식):** 'SOS' 또는 'SOS만'은 기기가 **내 셀룰러 망에 연결되지 않은 상태**이며, 다른 통신사 망으로 긴급 전화만 걸 수 있다는 뜻입니다. '서비스 없음'·'검색 중'은 셀룰러 망에 아예 연결되지 않은 상태입니다. 즉 **eSIM 자체가 고장났다는 뜻이 아니라 '지원되는 망에 등록이 안 됐다'는 신호**입니다. 다만 Apple 문서는 이 'SOS' 긴급전화 기능이 호주·캐나다·미국에서 제공된다고 적고 있어, 영국에서 어떤 문구로 표시되는지는 기기·설정마다 다를 수 있습니다(**미확인**). ([Apple](https://support.apple.com/en-us/120000), [Apple 상태 아이콘](https://support.apple.com/guide/iphone/learn-the-meaning-of-iphone-status-icons-iphef7bb57dc/ios), 2026-11-21 확인)

**영국 통신망 (각 제공사 공식 표기, 2026-11-21 KST 확인)**

| 제공사 | 영국 통신망 (공식 표기) | 지원 망 목록을 보는 곳 | 출처 |
|---|---|---|---|
| Airalo | **EE**(주 통신망) + '+2 others'(이름은 페이지에 표시 안 됨) | 새 앱: 패키지 상세(Package Details) / 기존 앱: My eSIMs › View Details(ICCID 옆) | [영국 페이지](https://www.airalo.com/united-kingdom-esim), [도움말](https://www.airalo.com/help/troubleshooting/0UEL63PDK5IJ/why-is-my-esim-connecting-to-the-wrong-network/9NGFLMM9D4I2) |
| Saily | **미확인** — "영국 최고의 통신망(the UK's best networks)"이라고만 표기, 통신사 이름 없음. "여러 망을 지원하면 다른 망으로 바꾸면 나아질 수 있다"고 안내 | 공식 도움말: 어느 망인지 모르면 고객센터에 문의 | [영국 페이지](https://saily.com/esim-united-kingdom/), [iOS 도움말](https://support.saily.com/hc/en-us/articles/13357933521436-How-to-fix-iOS-network-connection-issues) |
| Holafly | **Orange UK / T-Mobile UK / H3G UK / VirginMediaO2 UK / Vodafone UK** (가능 지역 5G, 4G/LTE) | 홀라플라이 웹사이트의 국가 페이지 Coverage·Networks 항목 | [영국 페이지](https://esim.holafly.com/esim-united-kingdom/), [아이폰 FAQ](https://esim.holafly.com/faq/connection-or-qr-issues/iphone-cellular-data-not-working/) |

> 여러 망을 지원하는 eSIM은 한 망 신호가 약해지면 다른 망으로 넘어가면서 **잠깐 끊김**이 생길 수 있습니다. 레딧 이용자들은 "eSIM은 가장 센 신호로 알아서 옮겨 다니지 않고, 정해진 순서대로 붙었다가 **신호를 완전히 잃어야** 다른 망으로 넘어간다"고 설명합니다(경험담, 공식 확인 아님 — 아래 참고).

## 점검 순서 (공식 안내 기준)

1. **여행 eSIM의 데이터 로밍 켜기.** Holafly는 아이폰이 **SOS·서비스 없음일 때 가장 효과적인 조치**가 데이터 로밍 켜기라고 안내하고, 제대로 설치돼 있으면 추가 요금이 없다고 합니다. Saily는 eSIM을 켜고 로밍을 켜 둬야 도착 시 자동 개통된다고 안내합니다. Apple도 해외에서 'SOS'·'서비스 없음'이면 데이터 로밍을 확인하라고 안내합니다. ([Holafly FAQ](https://esim.holafly.com/faq/connection-or-qr-issues/iphone-cellular-data-not-working/), [Holafly 영국](https://esim.holafly.com/esim-united-kingdom/), [Saily 영국](https://saily.com/esim-united-kingdom/), [Apple](https://support.apple.com/en-us/120000), 2026-11-21 확인)
    - 아이폰: 설정 › 셀룰러(모바일 서비스) › 여행 eSIM › 데이터 로밍
    - 갤럭시: 설정 › 연결 › 모바일 네트워크 › 데이터 로밍 / 픽셀: 설정 › 네트워크 및 인터넷 › SIM › 로밍
2. **eSIM 회선 켜기 + 셀룰러 데이터 회선으로 선택 + 한국 회선 정리.**
    - 아이폰: 설정 › 셀룰러 › 여행 eSIM › '이 회선 켜기' → 뒤로 가서 '셀룰러 데이터'에서 여행 eSIM 선택. Holafly는 **'셀룰러 데이터 전환 허용'을 끄고**, 다른 회선이 간섭해 '서비스 없음'이 생기지 않도록 **다른 회선을 꺼 두라**고 안내합니다.
    - 갤럭시: 설정 › 연결 › SIM 관리자 › eSIM 켜기 → '모바일 데이터'에서 여행 eSIM 선택 (Saily 안드로이드 도움말)
    - 픽셀: 설정 › 네트워크 및 인터넷 › SIM › '모바일 데이터'에서 기본 데이터 SIM 선택(데이터 기본 SIM은 하나만 지정 가능). ([Google](https://support.google.com/pixelphone/answer/2926415?hl=en), 2026-11-21 확인)
3. **비행기 모드 15초 켰다 끄기 → 재시작.** Apple·Saily·Holafly 모두 비행기 모드를 최소 15초 켰다 끈 뒤, 안 되면 재시작하라고 안내합니다. 망 등록을 새로 하게 만드는 기본 조치입니다.
4. **와이파이 끄고 테스트.** Saily는 와이파이를 끈 상태에서 확인하라고 안내합니다.
5. **아이폰: 이동통신사 설정 업데이트 확인.** Apple은 와이파이 연결 상태에서 설정 › 일반 › 정보로 들어가 업데이트가 있으면 설치하라고 안내합니다.
6. **그래도 망이 계속 바뀌거나 SOS가 남으면 → 통신망 수동 선택** (아래).

## 통신망 수동 선택으로 한 망에 고정하기

망이 계속 바뀌거나, 지원하지 않는 망에 붙어 SOS가 뜰 때 **직접 망을 골라 고정**하는 방법입니다. Airalo·Saily·Holafly 모두 공식 해결책으로 안내합니다.

**아이폰** (Airalo·Saily·Holafly 공식 도움말)

1. 설정 › 셀룰러(모바일 서비스) › 여행 eSIM 선택
2. '네트워크 선택' › '자동' 끄기
3. 망 목록이 뜰 때까지 기다리기 (Holafly: 몇 분 걸릴 수 있음)
4. 지원 망 목록에 있는 망 선택

**갤럭시** (Airalo·Saily 공식 도움말)

1. 설정 › 연결 › 모바일 네트워크 › 네트워크 사업자
2. '수동 선택' → 목록이 뜨면 지원 망 선택

**픽셀** — Airalo 도움말: 설정 › 네트워크 및 인터넷 › eSIM 선택 › 고급 › 이동통신사 › '자동 선택' 끄기 → 망 선택. Google은 같은 메뉴의 '네트워크' 항목에서 사용 가능한 사업자를 고를 수 있다고 안내합니다. 메뉴 이름은 안드로이드 버전마다 조금 다릅니다.

**어느 망을 고를까**

- **Airalo:** 앱의 지원 망 목록에 있는 망을 고르라고 안내합니다. 공식 영국 페이지 기준 주 통신망은 **EE**입니다.
- **Holafly:** 목록의 사업자를 **하나씩 골라 각각 30초씩 기다린 뒤** 신호가 가장 센 곳을 고르라고 안내합니다. 영국 공식 표기 망은 Orange UK / T-Mobile UK / H3G UK / VirginMediaO2 UK / Vodafone UK입니다.
- **Saily:** "Saily가 제공한 사업자"를 고르고, 모르면 고객센터에 문의하라고 안내합니다. 영국 통신사명은 공식 페이지에 없어 **미확인**입니다.
- 지원 목록에 없는 망은 골라도 연결되지 않습니다.

> ⚠️ **수동 선택의 단점:** 고정한 망의 신호가 없는 곳(시골·산간 등)에 가면 다른 망으로 넘어가지 않아 오히려 끊길 수 있습니다. 문제가 풀렸으면 이동 전이나 신호가 사라졌을 때 **다시 '자동'으로 돌려 두세요**. 귀국 후에도 '자동'으로 돌려 두는 것이 안전합니다(공식 안내가 아닌 일반적인 주의사항).

## 그래도 안 되면

1. **5G 끄고 LTE/4G로.** Saily는 아이폰 '음성 및 데이터'에서 LTE·4G·3G를, 안드로이드 '선호 네트워크 유형'에서 4G·3G를 고르라고 안내합니다. 5G↔4G 전환이 잦을 때도 시도해 볼 만합니다.
2. **APN 확인.** Saily 도움말은 APN에 `wbdata`를 넣고 나머지는 비워 두라고 안내합니다. 다른 제공사는 설치 안내에 APN이 표시된 경우에만 입력하세요.
3. **네트워크 설정 재설정.** eSIM은 지워지지 않지만 와이파이 비밀번호·로밍·APN 설정이 초기화되므로 끝나면 1·2번을 다시 확인하세요. Holafly는 **eSIM을 삭제하지 말라**고 강조합니다(영국 페이지 FAQ: 설치 후에는 이전·재설치 불가).
4. **제공사 장애일 수도 있음.** 위 조치를 다 해도 갑자기 여러 사람이 동시에 안 된다면 제공사 쪽 장애일 수 있습니다. Airalo는 2026년 6월 24일(현지) 협력사 업데이트 중 장애로 일부 이용자 데이터가 끊겼다고 레딧 공식 계정으로 공지하고, 복구 후 비행기 모드 10초·재시작·데이터 로밍 확인을 안내했습니다. ([r/Airalo 공식 공지](https://www.reddit.com/r/Airalo/comments/1ugc7z7/about_the_june_24_outage/))
5. **고객센터 문의·환불.** Airalo·Saily·Holafly 모두 24시간 상담을 안내합니다. Holafly 영국 FAQ는 연결 문제가 있으면 전액 또는 부분 환불을 받을 수 있고 승인 후 3~5영업일 걸린다고 안내합니다. 일반 환불 안내는 [여행 중 eSIM이 갑자기 끊겼을 때](../esim-stopped-working-mid-trip-refund-replacement/) 가이드를 참고하세요.

## 실제 여행자 경험담 (레딧, 개인 경험)

아래는 공식 정보가 아니라 **레딧 이용자들이 직접 쓴 경험담**입니다. 시기·기기·요금제에 따라 다를 수 있어 참고만 하세요.

- **영국에서 SOS·위성 표시와 망 순환이 반복:** Airalo 장애 공지 글(2026년 6월) 댓글에 "영국 여행 내내 SOS/위성 표시가 계속 뜨고, 데이터 제공 망이 계속 바뀌었으며, 로밍을 몇 번이고 다시 켜야 했다"는 불만이 있습니다. 같은 글에 EU·영국 무제한 eSIM이 2주 동안 여러 번 안 됐다는 댓글도 있습니다. ([r/Airalo](https://www.reddit.com/r/Airalo/comments/1ugc7z7/about_the_june_24_outage/))
- **"가장 센 망으로 자동 이동하지 않는다":** 영국 여행용 eSIM을 묻는 글(2025년 8월)에 "어떤 eSIM도 가장 센 신호로 자동 전환하지 않는다. 정해진 선호 순서로 붙고, 신호를 잃거나 수동으로 바꿀 때만 전환된다"는 댓글이 있습니다. ([r/eSIMs](https://www.reddit.com/r/eSIMs/comments/1mwmrqp/holiday_in_uk_need_sim_that_switches_around_to/))
- **아이폰은 신호를 완전히 잃어야 망을 바꾼다는 설명:** 영국 멀티망 SIM 이용자 글(2026년 7월)에 "아이폰은 현재 망 신호를 완전히 잃기 전에는 다른 망을 찾지 않는다"는 댓글과, 해당 SIM 회사 계정의 "설정 › 모바일 서비스 › 네트워크 선택에서 자동을 끄고 원하는 망을 고르라"는 답변이 있습니다(여행 eSIM 3사와는 다른 회사 사례). ([r/honestmobile](https://www.reddit.com/r/honestmobile/comments/1uyzx71/smart_sim_becoming_pointless_in_uk/))
- **망마다 지역별 체감 차이:** 영국 여행 eSIM 추천 글(2025년 3월)에 스코틀랜드 하이랜드에서는 EE가 가장 나았고 O2는 약했다는 후기, 하이랜드 외딴 지역은 어느 망도 안 터지니 오프라인 지도를 받아 두라는 조언이 있습니다. 같은 글에 런던에서 Airalo로 거의 서비스가 안 됐다는 불만 댓글도 있습니다. ([r/uktravel](https://www.reddit.com/r/uktravel/comments/1j4vydy/best_esim_for_uk_going_to_london_and_scotland_and/))
- **Vodafone 망은 시골·실내에서 약했다는 후기:** 2024년 6월 영국 남부 여행 후기에서 Vodafone 기반 eSIM이 런던 대형 건물 실내와 도시 밖에서 EDGE나 '서비스 없음'이 잦았고 EE가 훨씬 나았다는 내용이 있습니다(여행 eSIM 3사와는 다른 상품). ([r/eSIMs](https://www.reddit.com/r/eSIMs/comments/1di65gg/uk_vodafone_travel_from_esimnet_2024_trip/))

→ 공통점: **로밍·데이터 회선 설정을 먼저 확인하고, 망이 계속 바뀌면 지원 망 중 그 지역에서 잘 잡히는 망으로 수동 고정**하는 것이 현실적인 해결책입니다. 다만 어느 망이 좋은지는 지역마다 달라 정답은 없습니다.

## 출발 전에 해 둘 것

- **한국에서 eSIM 설치까지 끝내기.** Airalo는 커버리지 밖에서도 미리 설치·연결해 두면 도착 즉시 쓸 수 있다고 안내합니다. Saily는 도착하면 자동 개통, Holafly는 지원 망에 연결되는 순간 개통된다고 안내합니다.
- **앱에서 내 상품의 영국 지원 망 이름을 캡처해 두기.** 와이파이 없이 수동 선택할 때 바로 고를 수 있습니다.
- **스코틀랜드·외곽 이동 시 오프라인 지도 받기.** Holafly는 스코틀랜드 하이랜드 일부 지점 등 산간·섬·외곽 도로에서는 신호가 약하거나 불안정할 수 있다고 안내합니다.
- 상품별 가격·통신망 비교는 [영국 eSIM 비교](../../esim/united-kingdom/), 공항 도착 직후 개통 문제는 [이탈리아 통신망 수동 선택](../italy-esim-no-network-manual-selection/)과 [듀얼심 데이터 전환 점검](../dual-sim-data-switching-travel-esim-not-working/)의 점검 순서도 그대로 적용됩니다.

## 확인하지 못한 정보

- **Saily의 영국 통신사 이름:** 공식 영국 페이지에 없어 **미확인**입니다(2026-11-21 확인).
- **Airalo 영국 eSIM의 나머지 2개 통신망('+2 others') 이름:** 공식 페이지에 이름이 표시되지 않아 **미확인**입니다.
- **Holafly 표기 망(Orange UK / T-Mobile UK / H3G UK / VirginMediaO2 UK)이 휴대폰 망 목록에서 어떤 이름(EE·Three·O2 등)으로 보이는지:** 공식 출처로 확인하지 못했습니다(**미확인**).
- **영국에서 아이폰 상태 표시줄 문구:** Apple은 'SOS' 긴급전화 기능을 호주·캐나다·미국 기능으로 안내하고 있어, 영국에서 'SOS'로 뜰지 '서비스 없음'으로 뜰지는 **미확인**입니다(레딧에는 영국에서 SOS가 떴다는 경험담 있음).
- **각 eSIM이 망을 자동 전환하는 기준(신호 세기·선호 순서):** 3사 공식 페이지에 설명이 없어 **미확인**이며, 위 설명은 레딧 경험담입니다.
- **Saily `wbdata` APN이 영국 상품에 그대로 맞는지:** 공식 도움말이 기기별 일반 안내라 **미확인**입니다. 앱의 설치 정보 값을 우선하세요.
- **Airalo·Saily 환불 조건:** 영국 상품 페이지에 없어 **미확인**입니다.
- **X(트위터) 불만글:** 이번 조사에서는 레딧 경험담만 인용했습니다.
- 실제 현지 개통·수동 선택 테스트는 하지 않았습니다(모두 공식 페이지·후기 기재 내용).

## 출처

- [Airalo 영국 eSIM 공식 페이지](https://www.airalo.com/united-kingdom-esim) — 2026-11-21 확인
- [Airalo 도움말: Why is my eSIM connecting to the wrong network?](https://www.airalo.com/help/troubleshooting/0UEL63PDK5IJ/why-is-my-esim-connecting-to-the-wrong-network/9NGFLMM9D4I2) — 2026-11-21 확인
- [Saily 영국 eSIM 공식 페이지 (기술 정보·FAQ)](https://saily.com/esim-united-kingdom/) — 2026-11-21 확인
- [Saily 도움말: How to fix iOS network connection issues?](https://support.saily.com/hc/en-us/articles/13357933521436-How-to-fix-iOS-network-connection-issues) — 2026-11-21 확인
- [Saily 도움말: How to fix Android no net issue?](https://support.saily.com/hc/en-us/articles/13338388172828-How-to-fix-Android-no-net-issue) — 2026-11-21 확인
- [Holafly 영국 eSIM 공식 페이지 (통신망·FAQ·환불)](https://esim.holafly.com/esim-united-kingdom/) — 2026-11-21 확인
- [Holafly FAQ: How to fix iPhone eSIM Network not available error](https://esim.holafly.com/faq/connection-or-qr-issues/iphone-cellular-data-not-working/) — 2026-11-21 확인
- [Apple: If you see SOS, No Service, or Searching on your iPhone or iPad](https://support.apple.com/en-us/120000) — 2026-11-21 확인
- [Apple: Learn the meaning of iPhone status icons](https://support.apple.com/guide/iphone/learn-the-meaning-of-iphone-status-icons-iphef7bb57dc/ios) — 2026-11-21 확인
- [Google Pixel 도움말: Connect to mobile networks on a Pixel phone](https://support.google.com/pixelphone/answer/2926415?hl=en) — 2026-11-21 확인
- 레딧: [r/Airalo 장애 공지](https://www.reddit.com/r/Airalo/comments/1ugc7z7/about_the_june_24_outage/), [r/eSIMs 1](https://www.reddit.com/r/eSIMs/comments/1mwmrqp/holiday_in_uk_need_sim_that_switches_around_to/), [r/honestmobile](https://www.reddit.com/r/honestmobile/comments/1uyzx71/smart_sim_becoming_pointless_in_uk/), [r/uktravel](https://www.reddit.com/r/uktravel/comments/1j4vydy/best_esim_for_uk_going_to_london_and_scotland_and/), [r/eSIMs 2](https://www.reddit.com/r/eSIMs/comments/1di65gg/uk_vodafone_travel_from_esimnet_2024_trip/) — 2026-11-21 확인
