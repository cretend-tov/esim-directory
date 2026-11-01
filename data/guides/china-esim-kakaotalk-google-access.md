---
title: "중국에서 카카오톡·구글이 안 될 때 eSIM 점검법 (Airalo · Saily · Holafly)"
description: "중국에서 카카오톡·구글·인스타그램·왓츠앱이 막힐 때, Airalo·Saily·Holafly 공식 안내 기준으로 eSIM별 접속 방식(해외 경유·가상 위치·VPN 포함)과 점검 순서를 정리했습니다. 카카오톡은 공식 언급이 없어 미확인으로 표시. 2026-11-01 확인."
country: 중국
problem: "카카오톡·구글·인스타그램·왓츠앱 접속 안 됨 / 호텔 와이파이에서만 막힘 / 중국 앱(디디·바이두 지도)이 안 됨"
verified_on: "2026-11-01"
---
## 이런 경우에 해당합니다

- 중국에 도착했는데 **카카오톡 메시지가 전송 중에서 멈추거나** 구글 지도·지메일·인스타그램이 열리지 않는다.
- eSIM 데이터로는 되는데 **호텔·카페 와이파이에 붙으면 안 된다**.
- 반대로 구글·인스타그램은 되는데 **디디(DiDi)·바이두 지도 같은 중국 앱이 오류**를 낸다.

먼저 알아둘 점: Airalo 공식 도움말은 중국 현지망에서 구글(지메일·지도 포함)·인스타그램·페이스북·X·유튜브·왓츠앱이 일반적으로 접속되지 않는다고 안내합니다. 이 차단은 **연결 경로**에 걸리는 것이라, 같은 폰이라도 eSIM 데이터로 쓰느냐 와이파이로 쓰느냐에 따라 결과가 달라집니다.

## 3사 공식 안내 비교: 중국에서 막힌 앱이 되는가

| 제공사 | 공식 안내 요약 | 와이파이에서는 | 카카오톡 언급 | 출처 |
|---|---|---|---|---|
| Airalo | 중국 eSIM·아시아 지역·글로벌 eSIM 모두 **VPN이 필요 없다**고 안내. 데이터가 중국 본토 밖 게이트웨이로 나가는 국제 로밍 방식이라 구글·왓츠앱·SNS를 차단 없이 쓸 수 있다고 설명. 별도 VPN 기능은 없음 | 호텔 와이파이가 아니라 **eSIM 데이터를 쓸 때만** 해당된다고 명시 | 없음(미확인) | [도움말: 중국 VPN 필요 여부](https://www.airalo.com/help/using-managing-esims/ZSEEHBT5HW6F/stay-connected-in-china-your-guide-to-unfiltered-international-access-is-a-vpn-required/ZDZBNIKI4TFP) |
| Saily | Saily 앱 자체는 VPN 없이 쓸 수 있지만 **구글 계정으로 로그인은 안 됨**. 구글·인스타그램은 Saily 앱의 **가상 위치(Virtual location)** 기능으로 접속 가능(안 되면 캐시 삭제·서버 변경·앱 재설치). **왓츠앱은 VPN 필요** | 공식 페이지에 언급 없음(미확인) | 없음(미확인) | [중국 eSIM 페이지 FAQ](https://saily.com/esim-china/), [가상 위치 안내](https://saily.com/security-features/virtual-location/) |
| Holafly | 중국 eSIM에 **VPN이 추가 비용 없이 포함**돼 만리방화벽으로 막힌 앱·사이트에 접속할 수 있다고 안내. 왓츠앱 번호·대화는 그대로 유지 | 공식 페이지에 언급 없음(미확인) | 없음(미확인) | [중국 eSIM 페이지 FAQ](https://esim.holafly.com/esim-china/), [블로그: 중국 왓츠앱](https://esim.holafly.com/internet/does-whatsapp-work-in-china/) |

**카카오톡에 대해:** 세 곳 모두 공식 페이지에서 카카오톡을 따로 언급하지 않습니다. 공식 설명대로라면 데이터가 중국 밖으로 나가는 eSIM에서는 다른 해외 앱과 같은 조건일 것으로 보이지만, 카카오톡 접속 여부 자체는 **미확인**입니다. 출국 전에 판매처 고객센터에 "중국 본토에서 카카오톡이 되는지" 직접 물어보는 것이 가장 확실합니다.

## 안 될 때 점검 순서

1. **와이파이를 끄고** eSIM 데이터로 다시 시도합니다. Airalo는 우회 접속이 eSIM 데이터에만 해당하고 호텔 와이파이에는 적용되지 않는다고 명시합니다. 레딧에서도 "호텔을 7번 옮겼는데 와이파이에선 지메일·구글이 다 막힌다"는 글에 "중국의 모든 와이파이는 방화벽 뒤에 있으니 막힌 앱은 eSIM 데이터로 쓰라"는 답이 달렸습니다.
2. 폰 설정에서 **데이터 회선이 여행 eSIM으로** 잡혀 있는지, eSIM 회선의 **데이터 로밍이 켜져 있는지** 확인합니다(세 곳 모두 도착 후 데이터 로밍을 켜야 한다고 안내).
3. **Saily 사용자:** 앱에서 가상 위치를 켭니다. 그래도 구글·인스타그램이 안 되면 공식 안내대로 캐시 삭제 → 서버(위치) 변경 → 앱 재설치 순으로 해 봅니다. 왓츠앱은 가상 위치만으로는 안 되고 별도 VPN이 필요하다고 안내합니다.
4. **Holafly 사용자:** Holafly 블로그는 포함된 VPN에 문제가 있으면 고객지원에 연락하면 새 eSIM을 발급해 준다고 적고 있습니다. 앱 설치 정보는 Holafly 앱에서 다시 볼 수 있고, 고객지원은 24시간 채팅·왓츠앱으로 안내합니다.
5. 데이터 자체가 안 잡힌다면 접속 차단이 아니라 개통 문제입니다. [일본 eSIM 데이터가 안 될 때](../japan-esim-no-data/)의 APN·회선 점검 순서가 중국에서도 같은 방식으로 적용됩니다.

## 해외 앱은 되는데 중국 앱이 안 될 때 (레딧 경험담)

공식 정보가 아니라 **레딧 이용자들이 쓴 경험담**입니다. 참고만 하세요.

- **Airalo로 구글·인스타는 되는데 디디·바이두 지도가 안 됨:** 상하이 여행자가 Airalo eSIM으로 인스타그램·틱톡·구글·왓츠앱은 잘 됐지만, 디디는 'Network Exception' 오류, 바이두 지도는 로딩이 안 됐고 알리페이만 정상이었다고 썼습니다. 결국 다른 eSIM을 새로 샀다고 합니다. ([r/Airalo](https://www.reddit.com/r/Airalo/comments/1eog9g1/china_airalo_esim_unreliable/))
- **Airalo 속도 불만:** 같은 레딧 글타래(와이파이 문제 글)에서 Airalo는 VPN이 필요 없지만 일정 사용량 뒤 속도가 떨어지는 것 같다는 이용자 불만도 있었습니다(이용자 추정). ([r/chinatravel](https://www.reddit.com/r/chinatravel/comments/1se1nit/in_china_having_some_wifiinternet_issues/))
- **Holafly 연결 끊김:** 2026년 3월, Holafly 중국 eSIM이 개통 몇 시간 뒤 신호가 사라졌다거나, 18일 요금제가 15일째 끊겼다는 글이 있었습니다. 같은 글에는 한 달 동안 문제없이 썼다는 반대 경험도 있습니다. ([r/travelchina](https://www.reddit.com/r/travelchina/comments/1s57chf/holafly_esim_for_china/), [r/chinatravel](https://www.reddit.com/r/chinatravel/comments/1se1nit/in_china_having_some_wifiinternet_issues/))

정리하면, 해외 경유 eSIM은 **해외 앱용**으로는 공식 안내상 유리하지만, 중국 앱이 불안정했다는 경험담도 있으니 **중국 앱은 호텔 와이파이로, 막힌 해외 앱은 eSIM 데이터로** 나눠 쓰는 방법이 레딧에서 자주 권해집니다.

## 출국 전에 할 것

- eSIM은 **한국에서 미리 구매·설치**하세요. Saily는 중국 안에서 eSIM을 구매할 수 없다고 안내합니다.
- Saily 앱에 구글 계정으로 로그인한다면 **출국 전에 로그인**해 두세요(중국에서는 구글 로그인이 안 된다고 공식 FAQ에 적혀 있음).
- 왓츠앱이 꼭 필요하고 Saily를 쓴다면 출국 전에 VPN을 따로 준비해야 합니다(Saily 공식 안내).
- 가격·통신망·핫스팟 비교는 [중국 eSIM 비교](../../esim/china/)를 참고하세요.

## 확인하지 못한 정보

- 카카오톡이 각 사 중국 eSIM에서 되는지: 세 곳 모두 공식 언급이 없어 **미확인**입니다.
- Saily·Holafly eSIM을 와이파이로 쓸 때 우회가 적용되는지: 공식 페이지에 설명이 없어 **미확인**입니다(Airalo만 와이파이는 해당 없다고 명시).
- Holafly '포함 VPN'의 실제 동작 방식(별도 앱인지, 데이터 경로 자체인지): 공식 페이지에 설명이 없어 **미확인**입니다.
- Airalo의 중국 앱(디디·바이두 지도) 호환성: 공식 안내가 없고 레딧 경험담만 있어 **미확인**입니다.
- 실제 중국 현지 접속 테스트는 하지 않았습니다.

## 출처

- [Airalo 도움말: Stay Connected in China (Is a VPN Required?)](https://www.airalo.com/help/using-managing-esims/ZSEEHBT5HW6F/stay-connected-in-china-your-guide-to-unfiltered-international-access-is-a-vpn-required/ZDZBNIKI4TFP) — 2026-11-01 확인
- [Saily 중국 eSIM 공식 페이지 (FAQ: VPN·가상 위치)](https://saily.com/esim-china/) — 2026-11-01 확인
- [Saily 가상 위치 기능 안내](https://saily.com/security-features/virtual-location/) — 2026-11-01 확인
- [Holafly 중국 eSIM 공식 페이지 (FAQ: VPN 포함)](https://esim.holafly.com/esim-china/) — 2026-11-01 확인
- [Holafly 블로그: Does WhatsApp work in China?](https://esim.holafly.com/internet/does-whatsapp-work-in-china/) — 2026-11-01 확인
- 레딧 경험담: [r/Airalo](https://www.reddit.com/r/Airalo/comments/1eog9g1/china_airalo_esim_unreliable/), [r/chinatravel](https://www.reddit.com/r/chinatravel/comments/1se1nit/in_china_having_some_wifiinternet_issues/), [r/travelchina](https://www.reddit.com/r/travelchina/comments/1s57chf/holafly_esim_for_china/) — 2026-11-01 확인
