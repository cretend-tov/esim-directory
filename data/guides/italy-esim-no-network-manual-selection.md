---
title: "이탈리아 도착했는데 eSIM이 안 되고 통신망이 안 잡힐 때 (수동 선택)"
description: "로마·밀라노·나폴리 공항에 내렸는데 여행 eSIM이 'No Service'·SOS이거나 신호는 뜨는데 인터넷이 안 될 때, 데이터 로밍 점검부터 WINDTRE·Vodafone 등 통신망 수동 선택까지 Airalo·Saily·Holafly·Apple·Google 공식 안내와 실제 후기로 정리했습니다. 2026-11-19 확인."
country: 이탈리아
problem: "도착 후 개통 안 됨 / No Service·SOS / 신호는 있는데 데이터 안 됨"
verified_on: "2026-11-19"
---
## 증상

- 로마 피우미치노·밀라노 말펜사·나폴리 공항에 내렸는데 여행 eSIM이 **'서비스 없음(No Service)'이나 'SOS'**로만 뜬다.
- 신호 막대는 꽉 찼는데 **인터넷(사파리·구글 지도)이 안 열린다.** 왓츠앱만 되는 경우도 있다.
- 한국에서 미리 설치하고 출국했는데, 이탈리아 도착 후 개통이 안 된 것 같다.

## 먼저 알아둘 것: 이탈리아에서 내 eSIM이 쓰는 통신망

여행 eSIM은 이탈리아 현지 통신망을 빌려 씁니다. 휴대폰이 **내 eSIM이 지원하지 않는 망**에 자동으로 붙으려 하면 신호는 보여도 연결이 안 될 수 있고, 이때 **수동 선택**이 해결책이 됩니다. 각 제공사 공식 페이지에 적힌 이탈리아 통신망은 다음과 같습니다 (2026-11-19 KST 확인).

| 제공사 | 이탈리아 통신망 (공식 표기) | 지원 망 목록을 보는 곳 | 출처 |
|---|---|---|---|
| Airalo | **Wind Tre**(주 통신망) + '+1 other'(이름은 페이지에 표시 안 됨) | 새 앱: 패키지 상세(Package Details) / 기존 앱: My eSIMs › View Details(ICCID 옆) | [이탈리아 페이지](https://www.airalo.com/italy-esim), [도움말](https://www.airalo.com/help/troubleshooting/0UEL63PDK5IJ/why-is-my-esim-connecting-to-the-wrong-network/9NGFLMM9D4I2) |
| Saily | **미확인** — "이탈리아 최고의 통신망(Italy's best networks)"이라고만 표기, 통신사 이름 없음. 속도는 "현지 통신사에 따라 3G/4G/LTE/5G" | 공식 도움말: 어느 망인지 모르면 고객센터에 문의 | [이탈리아 페이지](https://saily.com/esim-italy/), [iOS 도움말](https://support.saily.com/hc/en-us/articles/13357933521436-How-to-fix-iOS-network-connection-issues) |
| Holafly | **Vodafone Italy / WINDTRE** (가능 지역 5G, 4G/LTE) | 홀라플라이 웹사이트의 국가 페이지 Coverage·Networks 항목 | [이탈리아 페이지](https://esim.holafly.com/esim-italy/), [아이폰 FAQ](https://esim.holafly.com/faq/connection-or-qr-issues/iphone-cellular-data-not-working/) |

> TIM·iliad는 위 세 곳 공식 이탈리아 페이지에 **표시되어 있지 않습니다.** 레딧 후기에는 Airalo로 TIM·iliad에 붙었다는 경험담이 있지만(아래 참고), 공식 확인은 안 된 내용입니다(**미확인**). 반드시 **내 앱의 지원 망 목록**을 기준으로 고르세요.

## 도착 직후 점검 순서 (공식 안내 기준)

1. **날짜·시간 자동 설정 확인.** Apple은 해외 도착 후 날짜·시간이 틀리면 설정 › 일반 › 날짜 및 시간에서 '자동으로 설정'을 켜라고 안내합니다. ([Apple](https://support.apple.com/en-us/109037), 2026-11-19 확인)
2. **비행기 모드 켰다 끄기.** Apple은 약 30초, Saily·Holafly는 15초 기다렸다 끄라고 안내합니다. 비행기에서 내린 직후 현지 망을 다시 찾게 하는 가장 기본적인 방법입니다. ([Apple](https://support.apple.com/en-us/109037), [Saily](https://support.saily.com/hc/en-us/articles/13357933521436-How-to-fix-iOS-network-connection-issues), [Holafly](https://esim.holafly.com/faq/connection-or-qr-issues/iphone-cellular-data-not-working/), 2026-11-19 확인)
3. **eSIM 회선 켜기 + 셀룰러(모바일) 데이터 회선으로 선택.**
    - 아이폰: 설정 › 셀룰러(모바일 서비스) › 여행 eSIM › '이 회선 켜기' → 뒤로 가서 '셀룰러 데이터'에서 여행 eSIM 선택. Holafly는 '셀룰러 데이터 전환 허용'을 꺼서 한국 유심으로 넘어가지 않게 하라고 안내합니다.
    - 갤럭시: 설정 › 연결 › SIM 관리자 › eSIM 켜기 → '모바일 데이터'에서 여행 eSIM 선택 (Saily·Holafly 안드로이드 도움말)
    - 픽셀: 설정 › 네트워크 및 인터넷 › SIM › '모바일 데이터'에서 기본 데이터 SIM 선택. Google은 데이터 기본 SIM은 하나만 지정할 수 있다고 안내합니다. ([Google](https://support.google.com/pixelphone/answer/2926415?hl=en), 2026-11-19 확인)
4. **여행 eSIM의 데이터 로밍 켜기.** 세 제공사 모두 이탈리아 도착 후 데이터 로밍을 켜야 연결된다고 안내합니다. Holafly는 eSIM이 제대로 설치돼 있으면 로밍을 켜도 추가 요금이 없다고 안내하고, 한국 유심은 꺼 두라고 권합니다. Apple도 'No Service'·'SOS'만 보이면 데이터 로밍이 켜져 있는지 확인하라고 안내합니다. ([Holafly 이탈리아](https://esim.holafly.com/esim-italy/), [Saily 이탈리아](https://saily.com/esim-italy/), [Apple](https://support.apple.com/en-us/109037), 2026-11-19 확인)
    - 갤럭시: 설정 › 연결 › 모바일 네트워크 › 데이터 로밍 / 픽셀: 설정 › 네트워크 및 인터넷 › SIM › 로밍
5. **와이파이 끄고 테스트.** Saily는 공항 와이파이에 붙은 상태를 끄고 확인하라고 안내합니다.
6. **그래도 'No Service'·SOS이거나 신호만 있고 인터넷이 안 되면 → 통신망 수동 선택** (아래).

## 통신망 수동 선택 방법

자동 선택이 지원하지 않는 망이나 문제가 있는 망에 붙어 있을 때 **직접 망을 고르는 방법**입니다. Airalo·Saily·Holafly 모두 공식 해결책으로 안내합니다.

**아이폰** (Airalo·Saily·Holafly 공식 도움말)

1. 설정 › 셀룰러(모바일 서비스) › 여행 eSIM 선택
2. '네트워크 선택' › '자동' 끄기
3. 사용 가능한 망 목록이 뜰 때까지 기다리기 (Holafly: 몇 분 걸릴 수 있음)
4. 지원 망 목록에 있는 망 선택

**갤럭시** (Airalo·Saily·Holafly 공식 도움말)

1. 설정 › 연결 › 모바일 네트워크 › 네트워크 사업자
2. '자동 선택' 끄기(수동 선택) → 목록이 뜰 때까지 기다리기
3. 지원 망 선택

**픽셀** — Google은 설정 › 네트워크 및 인터넷 › SIM에서 '네트워크(Network)' 항목으로 사용 가능한 망 중 사업자를 고를 수 있다고 안내합니다([Google](https://support.google.com/pixelphone/answer/2926415?hl=en)). Airalo 도움말은 설정 › 네트워크 및 인터넷 › eSIM 선택 › 고급 › 이동통신사 › '자동 선택' 끄기로 안내합니다. 메뉴 이름은 안드로이드 버전마다 조금 다릅니다.

**어느 망을 고를까**

- **Airalo:** 앱의 지원 망 목록(위 표 참고)에 나온 망을 고르라고 안내합니다. 공식 이탈리아 페이지 기준 주 통신망은 Wind Tre입니다.
- **Holafly:** 목록의 사업자를 **하나씩 골라 각각 30초씩 기다린 뒤** 신호가 가장 센 곳을 고르라고 안내합니다. 이탈리아 공식 표기 망은 Vodafone Italy / WINDTRE입니다.
- **Saily:** "Saily가 제공한 사업자"를 고르고, 모르면 고객센터에 문의하라고 안내합니다. 이탈리아 통신사명은 공식 페이지에 없어 **미확인**입니다.
- 지원 목록에 없는 망은 골라도 연결되지 않습니다. 연결된 뒤 다른 지역으로 크게 이동할 때는 다시 '자동'으로 돌려 두는 편이 안전합니다(공식 안내가 아닌 일반적인 주의사항).

## 수동 선택으로도 안 되면

1. **5G 끄고 LTE/4G로.** Saily는 아이폰 '음성 및 데이터'에서 LTE·4G·3G를, 안드로이드 '선호 네트워크 유형'에서 4G·3G를 고르라고 안내합니다.
2. **APN 확인.** Saily 도움말은 APN에 `wbdata`를 넣고 나머지는 비워 두라고 안내합니다(아이폰: 모바일 데이터 네트워크의 '모바일 데이터'·'LTE 설정' APN 칸 / 안드로이드: 액세스 포인트 이름 › 추가). 다른 제공사는 설치 안내에 APN이 표시된 경우에만 입력하세요.
3. **재시작 → 네트워크 설정 재설정.** 재설정은 eSIM을 지우지 않지만 와이파이 비밀번호·로밍·APN 설정이 초기화되므로 끝나면 3·4번을 다시 확인하세요. Holafly는 **eSIM을 삭제하지 말라**고 강조합니다(삭제 후 재설치 불가할 수 있음).
4. **고객센터 문의.** Airalo·Saily·Holafly 모두 24시간 채팅 상담을 안내합니다. Holafly 이탈리아 FAQ는 연결 문제가 있으면 전액 또는 부분 환불을 요청할 수 있고, 승인 후 3~5영업일 걸린다고 안내합니다. 환불 일반 안내는 [여행 중 eSIM이 갑자기 끊겼을 때](../esim-stopped-working-mid-trip-refund-replacement/) 가이드를 참고하세요.

## 실제 여행자 경험담 (레딧, 개인 경험)

아래는 공식 정보가 아니라 **레딧 이용자들이 직접 쓴 경험담**입니다. 시기·기기·요금제에 따라 다를 수 있어 참고만 하세요.

- **나폴리 도착 후 신호는 꽉 찼는데 데이터 불통 → TIM으로 수동 선택해 해결:** Airalo 유럽 eSIM이 이탈리아에서 'windtre'로 표시되며 신호는 꽉 찼지만 인터넷이 안 됐다는 글에, 나폴리에서 자동으로 'vodafone IT'에 붙었다가 Airalo 상담 후 'I TIM'으로 수동 변경해 해결했다는 댓글이 있습니다. 같은 글에 "자동으로 잡힌 것과 같은 망이라도 수동으로 다시 고르니 데이터가 됐다"는 댓글도 있습니다. ([r/eSIMs](https://www.reddit.com/r/eSIMs/comments/1kqmi48/both_a_eurolink_from_airalo_and_an_o2_esim_not/))
- **토스카나에서 WINDTRE 수동 선택:** 이탈리아 도착 후 eSIM이 안 된다는 글(2026년 6월)의 댓글에서, 재시작이 크게 도움이 됐고 WINDTRE로 수동 설정하니 토스카나에서 가장 잘 됐다는 후기가 있습니다. 같은 글에는 당일 유럽 지역에서 Airalo 장애가 있었다는 이용자 댓글도 있어, 설정 문제가 아닐 수도 있다는 점을 보여 줍니다. ([r/Airalo](https://www.reddit.com/r/Airalo/comments/1u2va2e/just_landed_in_italy_and_none_of_my_esims_are/))
- **망마다 체감이 다름:** Airalo로 WINDTRE·TIM·Vodafone 중 고를 수 있었고 WINDTRE가 시골까지 무난, TIM은 일부 지역에서 더 빨랐다는 후기, 연결이 별로면 '자동'을 끄고 목록 맨 위에 뜨는 망을 고르라는 후기가 있습니다(2023년). ([r/Airalo](https://www.reddit.com/r/Airalo/comments/15sx0m9/travelling_to_italy/))
- **표기된 망과 실제 잡히는 망이 다를 수 있음:** Airalo 이탈리아 eSIM이 상품 설명과 달리 WINDTRE·iliad에만 붙고 Vodafone·TIM은 수동으로 골라도 안 됐다는 후기(2024년 1월)와, 이후 4개 망(WINDTRE, Vodafone IT, I TIM, iliad) 모두 됐다는 댓글이 함께 있습니다. iliad는 대도시에서만 보였다는 의견도 있습니다. ([r/Airalo](https://www.reddit.com/r/Airalo/comments/19dwxox/italy_mammamia_networks/))

→ 공통점: **신호가 있는데 데이터가 안 되면 '다른 망'으로 수동 선택해 보는 것**이 실제로 자주 통했습니다. 다만 어느 망이 되는지는 시기·상품마다 달라 앱의 지원 망 목록을 먼저 보세요.

## 출발 전에 해 둘 것

- **한국에서 eSIM 설치까지 끝내기.** Airalo는 커버리지 밖에서도 미리 설치·연결해 두면 도착 즉시 쓸 수 있다고 안내합니다. Saily는 도착하면 자동 개통, Holafly는 지원 망에 연결되는 순간 개통된다고 안내합니다.
- **앱에서 내 상품의 이탈리아 지원 망 이름을 캡처해 두기.** 공항에서 와이파이 없이 수동 선택할 때 바로 고를 수 있습니다.
- **오프라인 지도 받아 두기.** Holafly는 돌로미티 일부 지점 등 산간·국립공원·외곽 도로에서는 신호가 약하거나 불안정할 수 있다고 안내합니다.
- 상품별 가격·통신망 비교는 [이탈리아 eSIM 비교](../../esim/italy/), 신호는 있는데 데이터만 안 되는 경우는 [듀얼심 데이터 전환 점검](../dual-sim-data-switching-travel-esim-not-working/)과 [일본 eSIM 데이터가 안 될 때](../japan-esim-no-data/)의 점검 순서도 그대로 적용됩니다.

## 확인하지 못한 정보

- **Saily의 이탈리아 통신사 이름:** 공식 이탈리아 페이지에 없어 **미확인**입니다(2026-11-19 확인).
- **Airalo 이탈리아 eSIM의 두 번째 통신망('+1 other') 이름:** 공식 페이지에 이름이 표시되지 않아 **미확인**입니다. 레딧에는 TIM·Vodafone·iliad 경험담이 있지만 공식 확인은 아닙니다.
- **TIM·iliad 지원 여부:** 세 제공사 공식 이탈리아 페이지에 TIM·iliad 표기가 없어 **미확인**입니다(레딧 경험담만 있음).
- **휴대폰 망 목록에 뜨는 표시 이름('I TIM', 'Vodafone IT', 'WINDTRE', 'iliad'):** 레딧 이용자 표현이며 공식 출처로 확인하지 못했습니다(**미확인**). 기기·OS에 따라 다르게 보일 수 있습니다.
- **Apple의 아이폰 '네트워크 선택' 수동 선택 절차:** Apple 공식 지원 페이지에서 해당 절차 문서를 찾지 못해, 절차는 Airalo·Saily·Holafly 공식 도움말 기준으로 적었습니다(Apple 문서는 날짜·시간, 비행기 모드, 데이터 로밍 부분만 인용).
- **Saily `wbdata` APN이 이탈리아 상품에 그대로 맞는지:** 공식 도움말이 기기별 일반 안내로만 되어 있어 **미확인**입니다. 앱의 설치 정보 값을 우선하세요.
- **Airalo·Saily 환불 조건:** 이탈리아 상품 페이지에 없어 **미확인**입니다.
- **X(트위터) 불만글:** 2026-11-19 검색에서 이 주제와 직접 관련된 글을 찾지 못해 레딧 경험담만 인용했습니다.
- 실제 현지 개통·수동 선택 테스트는 하지 않았습니다(모두 공식 페이지·후기 기재 내용).

## 출처

- [Airalo 이탈리아 eSIM 공식 페이지](https://www.airalo.com/italy-esim) — 2026-11-19 확인
- [Airalo 도움말: Why is my eSIM connecting to the wrong network?](https://www.airalo.com/help/troubleshooting/0UEL63PDK5IJ/why-is-my-esim-connecting-to-the-wrong-network/9NGFLMM9D4I2) — 2026-11-19 확인
- [Saily 이탈리아 eSIM 공식 페이지 (기술 정보)](https://saily.com/esim-italy/) — 2026-11-19 확인
- [Saily 도움말: How to fix iOS network connection issues?](https://support.saily.com/hc/en-us/articles/13357933521436-How-to-fix-iOS-network-connection-issues) — 2026-11-19 확인
- [Saily 도움말: How to fix Android no net issue?](https://support.saily.com/hc/en-us/articles/13338388172828-How-to-fix-Android-no-net-issue) — 2026-11-19 확인
- [Holafly 이탈리아 eSIM 공식 페이지 (통신망·FAQ)](https://esim.holafly.com/esim-italy/) — 2026-11-19 확인
- [Holafly FAQ: iPhone eSIM Network not available](https://esim.holafly.com/faq/connection-or-qr-issues/iphone-cellular-data-not-working/) — 2026-11-19 확인
- [Holafly FAQ: Mobile data not working on Android](https://esim.holafly.com/faq/connection-or-qr-issues/why-data-not-working-android/) — 2026-11-19 확인
- [Apple: About cellular data roaming options for your iPhone and iPad](https://support.apple.com/en-us/109037) — 2026-11-19 확인
- [Google Pixel 도움말: Connect to mobile networks on a Pixel phone](https://support.google.com/pixelphone/answer/2926415?hl=en) — 2026-11-19 확인
- 레딧 경험담: [r/eSIMs](https://www.reddit.com/r/eSIMs/comments/1kqmi48/both_a_eurolink_from_airalo_and_an_o2_esim_not/), [r/Airalo 1](https://www.reddit.com/r/Airalo/comments/1u2va2e/just_landed_in_italy_and_none_of_my_esims_are/), [r/Airalo 2](https://www.reddit.com/r/Airalo/comments/15sx0m9/travelling_to_italy/), [r/Airalo 3](https://www.reddit.com/r/Airalo/comments/19dwxox/italy_mammamia_networks/) — 2026-11-19 확인
