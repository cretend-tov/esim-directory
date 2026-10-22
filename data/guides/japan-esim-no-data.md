---
title: "일본에서 eSIM 데이터가 안 될 때 해결법 (로밍·APN 점검)"
description: "일본 도착 후 eSIM 신호는 뜨는데 인터넷이 안 될 때, Airalo·Saily·Holafly 공식 도움말 기준으로 데이터 로밍·데이터 회선·APN·수동 망 선택을 순서대로 점검하는 방법. 2026-10-22 확인."
country: 일본
problem: "데이터 안 됨 / 신호 없음(No Service)"
verified_on: "2026-10-22"
---
## 증상

- 일본에 도착했는데 eSIM 회선에 신호(LTE·4G·5G)는 보이지만 인터넷이 안 된다.
- 또는 "서비스 없음(No Service)", "SOS", "PDP 인증 실패(PDP Authentication Failure)" 같은 표시가 뜬다.

레딧 r/JapanTravelTips에도 "도착했는데 eSIM이 안 된다"는 글이 꾸준히 올라오며, 가장 많이 추천된 답은 **해당 eSIM 회선의 데이터 로밍을 켜라**, 그리고 **통신사 잠금(유심 락)된 폰은 안 될 수 있다**는 것이었습니다([레딧 글](https://www.reddit.com/r/JapanTravelTips/comments/1kjce1q/i_think_i_messed_up_the_esim/)). 아래 순서는 각 제공사 공식 도움말을 기준으로 정리했습니다.

## 먼저 확인할 것 (공식 출처 기반, 순서대로)

1. **eSIM을 지우지 마세요.** Holafly는 삭제한 eSIM은 다시 설치할 수 없고 보통 새로 사야 한다고 안내합니다. 아래 점검은 eSIM을 설치된 상태 그대로 두고 진행하세요.
2. **일본(커버리지 지역)에 도착했는지 확인.** Airalo·Holafly 모두 eSIM은 커버리지 지역 안에서만 망에 연결된다고 안내합니다.
3. **비행기 모드 끄기.** 이미 꺼져 있다면 켰다가 15초 뒤 끄기(Saily·Holafly 안내).
4. **와이파이 끄고 테스트.** Saily는 점검 전에 와이파이 연결을 끊으라고 안내합니다.
5. **eSIM 회선 켜기 + 모바일 데이터 회선으로 선택.** 아이폰은 설정 › 셀룰러(모바일 서비스) › 해당 eSIM › "이 회선 켜기", 그리고 셀룰러 데이터에서 그 eSIM 선택.
6. **해당 eSIM의 데이터 로밍 켜기.** Holafly는 로밍이 꺼져 있는 것이 개통 실패의 **가장 흔한 원인**이라고 안내합니다. 아이폰은 회선별로 로밍을 켤 수 있으니 한국 유심 쪽 로밍은 꺼 두면 한국 통신사 로밍 요금을 피할 수 있습니다(Airalo 안내). 단, Airalo는 일부 eSIM은 로밍을 꺼야 한다고도 하니 앱의 "How to connect" 안내를 따르세요.
7. **"셀룰러 데이터 전환 허용" 끄기.** Airalo·Saily·Holafly 모두 이 옵션을 끄라고 안내합니다(한국 회선으로 데이터가 넘어가는 것 방지).
8. **다른 SIM/eSIM 잠시 끄기.** 듀얼심일 때 다른 회선이 데이터를 막을 수 있다고 안내합니다.
9. **휴대폰 재시작.**
10. **5G 대신 LTE/4G로 바꿔 보기.** Saily는 5G를 끄고 LTE·4G를 고르라고 안내합니다.
11. **APN 확인** (아래 표의 제공사별 값). 신호는 있는데 인터넷만 안 될 때 확인할 항목입니다.
12. **망 수동 선택.** 설정 › 셀룰러 › eSIM › 네트워크 선택 › 자동 끄기 후 제공사가 안내한 망 선택. 참고로 일본 상품 페이지 기준 Airalo는 SoftBank(+1개 망), Saily는 KDDI·SoftBank, Holafly는 KDDI·SoftBank가 표시돼 있습니다([일본 eSIM 비교](../../esim/japan/) 참고).
13. **네트워크 설정 재설정.** 설정 › 일반 › 전송 또는 iPhone 재설정 › 재설정 › 네트워크 설정 재설정. 저장된 와이파이 비밀번호·블루투스 페어링이 지워지고, 로밍·APN 설정도 초기화되니 이후 5~11번을 다시 확인하세요.

## 제공사별 공식 해결 안내

| 제공사 | APN | 공식 안내 요약 | 출처 |
|---|---|---|---|
| Airalo | eSIM마다 다름. 앱 › My eSIMs › 해당 eSIM › View details › Connect to a network › How to connect 에 적힌 값을 **정확히** 입력(보통 소문자 한 단어). 안내에 APN이 없으면 수동 설정 불필요 | "PDP 인증 실패"는 주로 APN 오입력·누락, 또는 데이터 잔량 0 때문. 지원 망에 붙어 있는지 확인, 안 되면 네트워크 설정 재설정 후 재시작, 그래도 안 되면 앱/웹 채팅 문의 | [eSIM이 안 될 때](https://www.airalo.com/help/troubleshooting/0UEL63PDK5IJ/why-is-my-esim-not-working/X7ZYBK1S7GA8), [PDP 인증 실패](https://www.airalo.com/help/troubleshooting/0UEL63PDK5IJ/i-am-experiencing-pdp-authentication-failure/MTSK0S04Z6YN), [iOS 설치·연결](https://www.airalo.com/help/getting-started-with-airalo/E8DFWD88SHUX/how-do-i-install-an-airalo-esim-directly-on-my-ios-device/7Y77FP6UZXI8) |
| Saily | 공식 도움말 예시값 `wbdata` (이름·APN 모두 wbdata, 나머지 칸 비움. 아이폰은 "모바일 데이터"와 "LTE 설정" 두 칸 모두). 안드로이드는 APN이 없으면 Saily 앱을 최대 5분 열어 두면 자동 설정 | 와이파이 끄기 → 비행기 모드 15초 → 로밍 켜기 → 회선·데이터 선택 → 5G 끄기 → APN → 재시작 → 네트워크 재설정 → 망 수동 선택. 아이폰에서 APN이 없거나 연결이 안 되면 고객센터 문의 | [iOS 연결 문제](https://support.saily.com/hc/en-us/articles/13357933521436-How-to-fix-iOS-network-connection-issues), [Android 연결 문제](https://support.saily.com/hc/en-us/articles/13338388172828-How-to-fix-Android-no-net-issue), [개통 방법](https://support.saily.com/hc/en-us/articles/15751572038300-How-to-activate-my-Saily-eSIM) |
| Holafly | `Global` (아이폰은 APN 칸에만 입력. 삼성은 'Global' APN이 없으면 + 로 추가, 이름 Holafly / APN Global 후 저장·선택) | 대부분 APN은 미리 설정돼 있음. 신호(LTE·4G·5G)는 있는데 안 되면 APN, "서비스 없음"이면 접속 망을 확인하라고 구분. 망 수동 선택 시 목록의 통신사를 하나씩 30초씩 시도 | [APN 설정](https://esim.holafly.com/faq/esim-setup-guide/apn-setup-holafly-esims/), [설정·개통](https://esim.holafly.com/faq/esim-setup-guide/how-do-i-set-up-my-esim/), [iPhone 네트워크 사용 불가](https://esim.holafly.com/faq/connection-or-qr-issues/iphone-cellular-data-not-working/), [연결 안 될 때(일본어)](https://esim.holafly.com/ja/guides-esim/holafly-esim-not-working/) |

**팁:** Holafly 안내처럼 설정은 **한 번에 하나씩만** 바꾸고 와이파이를 끈 채 테스트하면 무엇이 원인이었는지 알 수 있습니다.

## 그래도 안 되면 (환불·고객센터)

- **Airalo:** 앱 또는 웹사이트의 채팅 말풍선으로 문의(공식 안내).
- **Saily:** 도움말 센터의 고객지원 버튼으로 문의. 어느 망을 수동 선택해야 할지 모르면 고객지원에 물어보라고 안내합니다.
- **Holafly:** 일본 상품 페이지 FAQ에 "연결 문제" 시 전액 또는 부분 환불을 요청할 수 있다고 안내돼 있습니다(승인 후 3~5영업일). 자세한 조건은 [일본 eSIM 비교](../../esim/japan/) 페이지와 Holafly 환불 정책 문서를 확인하세요.
- 문의할 때는 기종, 셀룰러 설정 화면, APN 화면, 신호 표시가 보이는 홈 화면 캡처를 준비해 두면 빠릅니다(와이파이는 끈 상태로).

## 확인하지 못한 정보

- **Saily의 일본 상품 전용 APN:** 도움말 문서의 예시값은 `wbdata`지만, 이것이 일본 eSIM에도 그대로 적용되는지는 일본 상품 페이지에서 확인하지 못했습니다(미확인). 설치 안내에 다른 값이 있으면 그 값을 우선하세요.
- **Airalo 일본 eSIM의 실제 APN 값과 로밍 켜기/끄기 여부:** 계정 앱 안에서만 보여 확인하지 못했습니다(미확인).
- **Airalo·Saily의 연결 문제 환불 조건:** 이번 확인 범위에 포함되지 않았습니다(미확인).
- 메뉴 이름은 iOS·안드로이드 버전, 제조사에 따라 조금씩 다를 수 있습니다. 실제 기기로 직접 테스트하지는 않았습니다.

## 출처

- [Airalo — Why is my eSIM not working?](https://www.airalo.com/help/troubleshooting/0UEL63PDK5IJ/why-is-my-esim-not-working/X7ZYBK1S7GA8) (2026-10-22 확인)
- [Airalo — PDP Authentication Failure](https://www.airalo.com/help/troubleshooting/0UEL63PDK5IJ/i-am-experiencing-pdp-authentication-failure/MTSK0S04Z6YN) (2026-10-22 확인)
- [Airalo — iOS 기기에 eSIM 설치·연결](https://www.airalo.com/help/getting-started-with-airalo/E8DFWD88SHUX/how-do-i-install-an-airalo-esim-directly-on-my-ios-device/7Y77FP6UZXI8) (2026-10-22 확인)
- [Saily — iOS 네트워크 연결 문제 해결](https://support.saily.com/hc/en-us/articles/13357933521436-How-to-fix-iOS-network-connection-issues) (2026-10-22 확인)
- [Saily — Android 인터넷 안 될 때](https://support.saily.com/hc/en-us/articles/13338388172828-How-to-fix-Android-no-net-issue) (2026-10-22 확인)
- [Saily — eSIM 개통 방법](https://support.saily.com/hc/en-us/articles/15751572038300-How-to-activate-my-Saily-eSIM) (2026-10-22 확인)
- [Holafly — APN 설정(iPhone·삼성)](https://esim.holafly.com/faq/esim-setup-guide/apn-setup-holafly-esims/) (2026-10-22 확인)
- [Holafly — eSIM 설정·개통](https://esim.holafly.com/faq/esim-setup-guide/how-do-i-set-up-my-esim/) (2026-10-22 확인)
- [Holafly — iPhone eSIM 네트워크 사용 불가](https://esim.holafly.com/faq/connection-or-qr-issues/iphone-cellular-data-not-working/) (2026-10-22 확인)
- [Holafly — 연결 안 될 때 원인과 대처(일본어)](https://esim.holafly.com/ja/guides-esim/holafly-esim-not-working/) (2026-10-22 확인)
- [Holafly 일본 eSIM 상품 페이지(환불 FAQ)](https://esim.holafly.com/esim-japan/) (2026-10-22 확인)
- [Reddit r/JapanTravelTips — I think I messed up the ESIM…](https://www.reddit.com/r/JapanTravelTips/comments/1kjce1q/i_think_i_messed_up_the_esim/) (여행자 경험담, 2026-10-22 확인)
