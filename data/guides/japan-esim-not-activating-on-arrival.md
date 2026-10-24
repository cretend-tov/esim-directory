---
title: "일본 도착했는데 eSIM이 자동 개통 안 될 때 (요금제 시작 조건·점검 순서)"
description: "일본에 내렸는데 eSIM 요금제가 자동으로 시작되지 않을 때, Airalo·Saily·Holafly 공식 도움말 기준으로 요금제가 언제 시작되는지와 도착 직후 점검 순서를 정리했습니다. 2026-10-24 확인."
country: 일본
problem: "도착 후 자동 개통 안 됨 / 요금제 시작 안 됨"
verified_on: "2026-10-24"
---
## 증상

- 출국 전에 eSIM을 설치해 뒀는데, 일본에 내린 뒤에도 앱에 요금제가 "시작됨/사용 중"으로 바뀌지 않는다.
- 휴대폰 설정에서는 eSIM이 "켜짐"인데 신호나 데이터가 안 잡힌다.
- 또는 출국 전에 설치하지 못해서, 일본에 와서야 설치하려는데 개통이 안 된다.

레딧 r/JapanTravelTips에는 "도착했는데 eSIM이 개통되지 않는다"는 글이 반복해서 올라옵니다. 가장 많이 추천된 답은 **그 eSIM 회선의 데이터 로밍을 켜라**였고, **통신사 잠금(유심 락) 폰이면 안 될 수 있다**, **휴대폰을 껐다 켜니 됐다**는 경험담도 있었습니다([레딧 글 1](https://www.reddit.com/r/JapanTravelTips/comments/1kjce1q/i_think_i_messed_up_the_esim/)). 출국 하루 전 설치했을 때는 "개통 실패, 신호 없음"으로 보였지만 일본에 도착하니 정상 작동했다는 글도 있습니다([레딧 글 2](https://www.reddit.com/r/JapanTravelTips/comments/1cfspef/esim_not_activating_how_to_proceed/)). 아래 내용은 각 제공사 공식 도움말 기준입니다.

## 먼저 알아둘 것: "설치"와 "요금제 시작"은 다르다

- **Airalo:** 대부분의 패키지는 커버리지 지역(일본)에서 **지원 망에 처음 연결될 때** 유효기간이 시작됩니다. 단 **일부 패키지는 설치하는 순간 시작**되니, My eSIMs › DETAILS › SHOW MORE 의 "VALIDITY POLICY"를 꼭 확인하라고 안내합니다. 커버리지 밖에서 설치하면 절차를 다 따라 해도 일본에 도착하기 전에는 쓸 수 없습니다.
- **Saily:** 출국 전에 eSIM을 설치하고 **데이터 로밍을 켜 두면** 도착해서 지원 망에 연결될 때 요금제가 자동으로 시작됩니다. 구매 후 180일 안에 개통하지 않으면 180일이 지나면 자동 개통됩니다.
- **Holafly:** 설치만으로는 시작되지 않고, 도착 후 eSIM 회선을 켜고 데이터 회선으로 선택하고 데이터 로밍을 켠 상태에서 현지 망에 연결될 때 시작됩니다. 설치 직후 휴대폰에 "활성/켜짐"으로 보이는 것은 정상이며 요금제가 시작됐다는 뜻은 아니라고 안내합니다. 단 월·연 **구독형 요금제는 구매 시점부터** 기간이 시작됩니다.

즉, 도착 직후 "자동 개통이 안 됐다"는 것은 대부분 **휴대폰이 아직 일본 망에 붙지 못한 상태**입니다. 아래 순서로 점검하세요.

## 도착 직후 점검 순서 (공식 출처 기반)

1. **eSIM을 지우지 마세요.** Holafly는 대부분의 eSIM이 1회용이라 지우면 고객센터 없이 다시 받을 수 없다고 안내합니다.
2. **비행기 모드 끄기.** 기내에서 켜 둔 비행기 모드를 끄세요.
3. **eSIM 회선 켜기.** 아이폰은 설정 › 셀룰러(모바일 서비스) › 해당 eSIM › "이 회선 켜기". 출국 전에 꺼 두었다면 이때 켭니다(Holafly 안내).
4. **셀룰러 데이터 회선을 이 eSIM으로 선택.**
5. **이 eSIM의 데이터 로밍 켜기.** Holafly는 로밍이 꺼져 있는 것이 개통 실패의 가장 흔한 원인이라고 안내하고, Saily도 자동 개통 조건으로 데이터 로밍 켜기를 듭니다.
6. **한국 유심 쪽 데이터 로밍은 끄거나, 한국 회선을 잠시 끄기.** Saily는 듀얼심 폰이면 기본 회선의 데이터 로밍을 끄고, 듀얼심이 아니면 기본 회선을 아예 끄라고 안내합니다.
7. **"셀룰러 데이터 전환 허용" 끄기**(Holafly 안내).
8. **휴대폰 재시작.** 레딧 경험담에서도 재시작으로 해결된 사례가 있습니다.
9. **(안드로이드) APN 확인.** Saily는 Saily APN이 없으면 Saily 앱을 최대 5분 열어 두면 자동 설정된다고 안내합니다. APN 값과 신호는 있는데 데이터가 안 될 때의 상세 점검은 [일본 eSIM 데이터가 안 될 때](../japan-esim-no-data/) 가이드를 참고하세요.
10. **제공사 앱에서 상태 확인.** Holafly는 휴대폰 설정 대신 앱의 Purchases에서 "Installed – In use"인지 보라고 안내합니다.

### 아직 설치를 안 하고 일본에 왔다면

- **Airalo:** 커버리지 지역 안에 있으면 구매 직후 바로 설치·연결해 쓸 수 있다고 안내합니다. 설치에는 안정적인 인터넷이 필요하니 공항·호텔 와이파이를 이용하세요.
- **Saily·Holafly:** 출국 전 설치를 권장합니다(Holafly는 최소 하루 전). 도착 후 설치 가능 여부는 별도 문서를 이번에 확인하지 못했습니다(아래 "확인하지 못한 정보" 참고).

## 제공사별 공식 안내 요약

| 제공사 | 요금제 시작 시점 | 도착 후 안 될 때 공식 안내 | 출처 |
|---|---|---|---|
| Airalo | 대부분 일본 지원 망 첫 연결 시. 일부 패키지는 설치 즉시(패키지별 VALIDITY POLICY 확인) | eSIM이 켜져 있고 데이터 회선으로 선택돼 있어야 망에 연결. 커버리지 밖에서는 절차를 따라도 사용 불가. 지원팀 24시간 | [When can I use my eSIM?](https://www.airalo.com/help/getting-started-with-airalo/E8DFWD88SHUX/when-can-i-install-my-esim/EQOCBMXDPSB2), [유효기간 안내](https://www.airalo.com/help/using-managing-esims/ZSEEHBT5HW6F/hvordan-fungerer-datam%C3%A6ngder-og-gyldighedsperioder-for-esimpakker/8KC1GEAUTAL0) |
| Saily | 도착해 지원 망 연결 시 자동(출국 전 설치 + 로밍 켜기 조건). 구매 후 180일 지나면 자동 개통 | eSIM 켜기 → 로밍 켜기 → 기본 회선 로밍 끄기/회선 끄기 → (안드로이드) APN 확인 → 안 되면 고객지원 | [개통 여부 확인](https://support.saily.com/hc/en-us/articles/12823108536476-How-long-does-an-eSIM-take-to-activate), [요금제 관리](https://support.saily.com/hc/en-us/articles/21484628749084-Saily-data-plan-management) |
| Holafly | 일일 요금제: 도착 후 회선 켜기·데이터 선택·로밍 켜기 상태로 현지 망 연결 시. 구독형: 구매 시 | 도착 확인 → 회선 켜기·데이터 선택 → 로밍 켜기(가장 흔한 원인) → 다른 SIM 끄기 → eSIM 삭제 금지 | [언제 개통되나](https://esim.holafly.com/faq/esim-setup-guide/when-should-i-set-up-my-esim/), [설정·개통](https://esim.holafly.com/faq/esim-setup-guide/how-do-i-set-up-my-esim/) |

**주의:** Holafly는 한 번 시작되면 회선을 끄거나 다른 eSIM으로 바꿔도 날짜가 계속 차감된다고 안내합니다.

## 그래도 안 되면 (환불·고객센터)

- **Airalo:** 지원팀이 24시간 운영된다고 안내합니다. 앱·웹사이트에서 문의하세요.
- **Saily:** 위 점검 후에도 안 되면 고객지원에 문의하라고 안내합니다.
- **Holafly:** 지우지 말고 고객지원에 문의하세요. 일본 상품의 연결 문제 환불 안내는 [일본 eSIM 데이터가 안 될 때](../japan-esim-no-data/) 가이드에 정리해 두었습니다.
- 문의 전 기종, 셀룰러 설정 화면, 신호 표시가 보이는 홈 화면 캡처를 준비하면 빠릅니다.
- 레딧 경험담처럼 **통신사 잠금(유심 락)된 폰**이면 해외 eSIM이 작동하지 않을 수 있습니다. 출국 전에 통신사에서 잠금 여부를 확인하세요.

## 확인하지 못한 정보

- **Airalo 일본 패키지 각각의 VALIDITY POLICY:** 패키지 상세(계정·앱) 안에서만 보여 이번에 확인하지 못했습니다(미확인). 구매 전 상세에서 직접 확인하세요.
- **Saily·Holafly를 일본 도착 후에 처음 설치해도 되는지:** 공식 문서는 출국 전 설치를 권장할 뿐, 도착 후 설치 가능 여부를 명시한 문서를 이번에 찾지 못했습니다(미확인).
- **Saily 아이폰에서 자동 개통이 안 될 때의 추가 조치:** 공식 문서에는 고객지원 문의만 안내돼 있습니다.
- 메뉴 이름은 iOS·안드로이드 버전과 제조사에 따라 다를 수 있습니다. 실제 기기로 직접 테스트하지는 않았습니다.

## 출처

- [Airalo — When can I use my eSIM?](https://www.airalo.com/help/getting-started-with-airalo/E8DFWD88SHUX/when-can-i-install-my-esim/EQOCBMXDPSB2) (2026-10-24 확인)
- [Airalo — 데이터·유효기간 안내(When does my validity period start?)](https://www.airalo.com/help/using-managing-esims/ZSEEHBT5HW6F/hvordan-fungerer-datam%C3%A6ngder-og-gyldighedsperioder-for-esimpakker/8KC1GEAUTAL0) (2026-10-24 확인)
- [Saily — How to check if my Saily eSIM is activated?](https://support.saily.com/hc/en-us/articles/12823108536476-How-long-does-an-eSIM-take-to-activate) (2026-10-24 확인)
- [Saily — Saily data plan management](https://support.saily.com/hc/en-us/articles/21484628749084-Saily-data-plan-management) (2026-10-24 확인)
- [Holafly — When to activate your eSIM](https://esim.holafly.com/faq/esim-setup-guide/when-should-i-set-up-my-esim/) (2026-10-24 확인)
- [Holafly — How to set up and activate an eSIM](https://esim.holafly.com/faq/esim-setup-guide/how-do-i-set-up-my-esim/) (2026-10-24 확인)
- [Reddit r/JapanTravelTips — I think I messed up the ESIM…](https://www.reddit.com/r/JapanTravelTips/comments/1kjce1q/i_think_i_messed_up_the_esim/) (여행자 경험담, 2026-10-24 확인)
- [Reddit r/JapanTravelTips — ESim not activating. How to proceed??](https://www.reddit.com/r/JapanTravelTips/comments/1cfspef/esim_not_activating_how_to_proceed/) (여행자 경험담, 2026-10-24 확인)
