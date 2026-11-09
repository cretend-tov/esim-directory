---
title: "내 폰이 eSIM 되는지 확인하는 법 (통신사 잠금·국내 갤럭시 포함)"
description: "여행 eSIM을 사기 전에 내 폰이 eSIM을 지원하는지, 통신사 잠금(캐리어락)은 없는지 확인하는 방법. Apple·삼성 공식 안내와 Airalo·Saily·Holafly 공식 도움말 기준으로 정리했습니다. 2026-11-09 확인."
country: 공통
problem: "eSIM 지원 여부 / 통신사 잠금(캐리어락) / 국내 출시 갤럭시"
verified_on: "2026-11-09"
---
## 한눈에 보기

여행 eSIM을 쓰려면 **두 가지가 모두** 맞아야 합니다. Airalo·Saily·Holafly 공식 도움말이 공통으로 안내하는 조건입니다.

1. **폰이 eSIM을 지원**할 것 (같은 모델이라도 출시 국가에 따라 다름)
2. **통신사 잠금(캐리어락)이 없을 것** — Holafly는 "eSIM 지원 ≠ 잠금 해제"라고 따로 강조합니다.

Airalo는 여기에 **탈옥(iOS)·루팅(Android)된 기기가 아닐 것**을 추가 조건으로 둡니다.

> eSIM은 대부분 **한 번 설치하면 다른 폰으로 옮길 수 없습니다**(Saily 기기 목록 FAQ). 그래서 **구매 전에** 아래 확인을 끝내는 게 중요합니다.

## 1단계: 30초 확인 — `*#06#`

전화(통화) 앱에서 `*#06#`을 누르면 기기 정보 화면이 뜹니다.

| 결과 | 의미 | 출처 |
|---|---|---|
| **EID**(32자리 숫자)가 보임 | eSIM 지원 | [Airalo](https://www.airalo.com/help/about-airalo/what-devices-support-esim), [Holafly](https://esim.holafly.com/faq/compatibility/phones-compatible-holafly-esims/) |
| IMEI만 보이고 EID 없음 | eSIM 미지원(물리 SIM만) | [Holafly](https://esim.holafly.com/faq/compatibility/phones-compatible-holafly-esims/) |

- 카카오톡·왓츠앱 같은 메신저가 아니라 **기본 전화 앱**에서 눌러야 합니다(Airalo).
- 통화가 걸리지 않고 마지막 `#`을 누르면 화면이 바로 뜹니다(Holafly).

## 2단계: 설정 메뉴에서 확인

| 기기 | 확인 경로 | "지원"으로 보는 기준 | 출처 |
|---|---|---|---|
| iPhone | 설정 → 셀룰러(모바일 서비스) | **eSIM 추가** 항목이 있음 | [Holafly](https://esim.holafly.com/faq/compatibility/phones-compatible-holafly-esims/) |
| iPhone (모델 확인) | 설정 → 일반 → 정보 → **모델 번호**를 탭해 `AXXXX` 형식으로 바꾸기 | 중국 본토·홍콩·마카오 모델 번호가 **아니면** 대체로 지원 | [Airalo iOS 확인법](https://www.airalo.com/help/getting-started-with-airalo/how-do-i-check-if-my-ios-device-supports-esim), [Apple 모델 번호 목록](https://support.apple.com/en-us/108044) |
| 갤럭시 | 설정 → 연결 → SIM 관리자 | **eSIM 추가** 항목이 있음 | [삼성전자 공식 안내](https://www.samsung.com/sec/support/newsalert/3184/), [Airalo Android 확인법](https://www.airalo.com/help/getting-started-with-airalo/how-do-i-check-if-my-android-device-supports-esim) |
| Google Pixel | 설정 → 네트워크 및 인터넷 → SIM 옆 **+** | "Download a SIM instead?(대신 SIM 다운로드)" 옵션이 보임 | [Airalo Android 확인법](https://www.airalo.com/help/getting-started-with-airalo/how-do-i-check-if-my-android-device-supports-esim) |
| 그 밖의 Android | `*#06#` | EID 표시 | 같은 출처 |

Airalo는 Android가 제조사·통신사별로 수정될 수 있어서 **목록에 있는 모델이어도 지역판에 따라 eSIM이 빠질 수 있다**고 안내합니다. 최종 확인은 제조사·판매처·가입 통신사에 하라는 것이 3사 공통 안내입니다.

## 3단계: 통신사 잠금(캐리어락) 확인

| 기기 | 확인 방법 | 잠금 없음 | 잠김 | 출처 |
|---|---|---|---|---|
| iPhone | 설정 → 일반 → 정보 → **이동통신사 잠금**(Carrier Lock, 이전 iOS는 Network Provider Lock) | **SIM 제한 없음**(No SIM restrictions) | 통신사 이름 또는 SIM Locked 표시 → 그 통신사에서만 사용 가능 | [Apple: 다른 통신사용 잠금 해제](https://support.apple.com/en-us/109316), [Holafly](https://esim.holafly.com/faq/compatibility/is-my-phone-unlocked-and-able-to-use-esims/) |
| Android (Holafly 방법) | 설정 → 연결 → 모바일 네트워크 → 네트워크 사업자 → **자동 선택 끄기** | 여러 사업자가 목록에 뜸 | 한 곳만 보이거나 자동 선택을 끌 수 없음 | [Holafly](https://esim.holafly.com/faq/compatibility/is-my-phone-unlocked-and-able-to-use-esims/) |
| Android (Airalo 방법) | 다른 통신사 SIM을 꽂고 전화 걸어 보기 | 통화 연결됨 | 연결 안 되거나 잠김 안내가 뜸 | [Airalo](https://www.airalo.com/help/getting-started-with-airalo/how-do-i-check-if-my-android-device-supports-esim) |

**잠겨 있으면:** Apple은 **현재 통신사만 잠금을 풀 수 있고 Apple은 풀 수 없다**고 안내합니다. 처리에 며칠 걸릴 수 있으니 출국 직전이 아니라 **미리** 요청하세요. Holafly는 할부·약정·회사 지급폰이 잠겨 있는 경우가 많고, 통신사가 IMEI로 잠금 상태를 확인해 줄 수 있다고 안내합니다.

## 국내 출시 갤럭시는 따로 확인하세요

해외판에서 eSIM을 지원하는 모델이라도 **한국에서 산 갤럭시는 다를 수 있습니다.** 공식 출처끼리도 표현이 조금씩 다릅니다.

| 출처 | 국내 출시 갤럭시에 대한 안내 |
|---|---|
| [삼성전자 공식 안내](https://www.samsung.com/sec/support/newsalert/3184/) | eSIM 지원 기기로 S20 이후·Z 폴드/플립 전 세대 등을 나열하면서 "**국가별로 다를 수 있으며, 일부 국가는 특정 모델 출시 이후부터 사용 가능**"하다고 단서를 둠. A36·A35는 유럽·북미·한국, A54는 유럽·북미·한국·일본만 해당이라고 명시 |
| [Holafly 한국어 지원 모델 목록](https://esim.holafly.com/ko/guides-esim/esim-phones/) | 국내판은 **Z 폴드4·Z 플립4·S23 시리즈 및 이후 기기**부터 지원, **국내판 S22 시리즈는 미지원** |
| [Holafly 영문 목록](https://esim.holafly.com/how-to/esim-phones/) · [Saily 기기 목록](https://saily.com/esim-supported-devices/) | 한국 구매 모델 중 **S20·S21·S22 시리즈, 노트20, 폴드·Z 폴드2·Z 폴드3, Z 플립·Z 플립 5G·Z 플립3**는 eSIM 미지원 |
| [Airalo 기기 목록](https://www.airalo.com/help/about-airalo/what-devices-support-esim) | 한국 구매 갤럭시는 대부분 미지원이며 예외는 S24·S23·Z 폴드5·폴드4·Z 플립5·플립4·A54라고 표기(이후 출시 모델은 이 문장에 없음 — 목록 갱신 여부 **미확인**) |

정리하면, **국내판 S22 이하·Z 폴드3/플립3 이하**는 eSIM이 안 될 가능성이 높다는 게 Holafly·Saily 공통 안내이고, 가장 확실한 방법은 위 2단계처럼 **SIM 관리자에 "eSIM 추가"가 있는지 직접 보는 것**입니다.

## iPhone에서 조심할 모델

| 경우 | 공식 안내 | 출처 |
|---|---|---|
| 중국 본토 판매 iPhone | eSIM 미지원 | [Airalo](https://www.airalo.com/help/about-airalo/what-devices-support-esim), [Saily](https://saily.com/esim-supported-devices/) |
| 홍콩·마카오 판매 iPhone | 일부 모델만 지원(Airalo: 13 mini·12 mini·SE 2020·XS만 예외적으로 지원) | 같은 출처 |
| iPhone Air | 전 세계 eSIM 전용, 중국판도 eSIM 지원 | [Saily](https://saily.com/esim-supported-devices/), [Apple 모델 목록](https://support.apple.com/en-us/108044) |
| iPhone XS·XS Max·XR | 3사 목록 모두 eSIM 지원 기기로 포함(가장 오래된 지원 모델) | [Airalo](https://www.airalo.com/help/about-airalo/what-devices-support-esim), [Saily](https://saily.com/esim-supported-devices/) |
| iPhone X 이하 | 3사 지원 목록에 없음 | 같은 출처 |

Saily는 **iPhone 13 이후 모델은 eSIM 2개를 동시에 활성화**할 수 있다고 안내합니다. 국내 통신사 eSIM을 이미 쓰고 있어도 여행 eSIM을 함께 켤 수 있는지 판단할 때 참고하세요.

## 그래도 애매하면

- 3사 모두 "목록은 완전하지 않으니 **제조사·판매처·가입 통신사**에 확인"하라고 안내합니다.
- Holafly는 eSIM을 **아직 설치하지 않았다면** 다른 호환 기기에 쓰거나 지인에게 넘기는 방법도 안내합니다. 설치 후에는 이전이 안 되니 주의하세요.
- 이미 설치했다가 지운 경우는 [eSIM QR 코드 삭제·분실 시 재설치 가능 여부](../esim-deleted-qr-lost-reinstall/)를, 구매 후 못 쓰게 된 경우는 [여행 취소 시 환불 규정 3사 비교](../esim-refund-trip-cancelled/)를 참고하세요.

## 확인하지 못한 정보

- 국내 통신 3사(SKT·KT·LG U+)와 알뜰폰의 **국내 출시폰 잠금 정책**은 이번에 각 통신사 공식 페이지로 확인하지 못했습니다(**미확인**).
- 삼성전자 공식 안내는 국가별 차이만 언급하고 **국내판 모델별 지원 여부를 따로 표로 밝히지 않아**, 국내판 지원 범위는 Holafly·Saily·Airalo 안내를 근거로 했습니다. 세 곳의 목록도 서로 완전히 일치하지 않습니다.
- Holafly의 Android 잠금 확인 메뉴 경로(연결 → 모바일 네트워크 → 네트워크 사업자)는 갤럭시 기준이며, 다른 제조사의 정확한 메뉴명은 **미확인**입니다.
- Saily FAQ의 "XS·XS Max·XR은 eSIM과 물리 SIM을 동시에 못 쓴다"는 문구는 Apple 공식 문서로 대조하지 못해 본문에서 뺐습니다.
- 실제 기기로 직접 테스트하지는 않았습니다.

## 출처

- [Apple: 다른 통신사에서 사용하도록 iPhone 잠금 해제하기](https://support.apple.com/en-us/109316) — 2026-11-09 확인
- [Apple: iPhone 모델 식별하기(모델 번호 목록)](https://support.apple.com/en-us/108044) — 2026-11-09 확인
- [삼성전자: 갤럭시 eSIM 서비스 지원 모델 및 전 세계 이동통신사 정보](https://www.samsung.com/sec/support/newsalert/3184/) — 2026-11-09 확인
- [Airalo: What devices support eSIM?](https://www.airalo.com/help/about-airalo/what-devices-support-esim) — 2026-11-09 확인
- [Airalo: How do I check if my iOS device supports eSIM?](https://www.airalo.com/help/getting-started-with-airalo/how-do-i-check-if-my-ios-device-supports-esim) — 2026-11-09 확인
- [Airalo: How do I check if my Android device supports eSIM?](https://www.airalo.com/help/getting-started-with-airalo/how-do-i-check-if-my-android-device-supports-esim) — 2026-11-09 확인
- [Saily: Devices that support eSIMs](https://saily.com/esim-supported-devices/) — 2026-11-09 확인
- [Holafly FAQ: How to check eSIM compatibility?](https://esim.holafly.com/faq/compatibility/phones-compatible-holafly-esims/) — 2026-11-09 확인
- [Holafly FAQ: Is my phone unlocked to use with another carrier?](https://esim.holafly.com/faq/compatibility/is-my-phone-unlocked-and-able-to-use-esims/) — 2026-11-09 확인
- [Holafly: eSIM Compatible Phones](https://esim.holafly.com/how-to/esim-phones/) — 2026-11-09 확인
- [Holafly: eSIM 지원 모델 목록(한국어)](https://esim.holafly.com/ko/guides-esim/esim-phones/) — 2026-11-09 확인
