---
title: "듀얼심 '데이터 전환' 때문에 여행 eSIM이 안 될 때 (셀룰러 데이터 전환 허용 끄기)"
description: "한국 유심과 여행 eSIM을 같이 켜 두면 폰이 데이터를 한국 회선으로 넘겨 eSIM이 안 되거나 로밍 요금이 나올 수 있습니다. 아이폰 '셀룰러 데이터 전환 허용', 갤럭시 'Data switching', 픽셀 'Automatic data switching' 설정법을 Airalo·Saily·Holafly·Apple·Google 공식 안내로 정리했습니다. 2026-11-17 확인."
country: 공통
problem: "데이터가 한국 회선으로 넘어감 / eSIM 사용량이 안 줄어듦 / 로밍 요금 청구"
verified_on: "2026-11-17"
---
## 증상

- 여행 eSIM을 설치했는데 **데이터가 eSIM이 아니라 한국 유심(원래 회선)으로 나간다.** 제공사 앱에서 eSIM 사용량이 거의 줄지 않는다.
- eSIM 신호가 약한 곳에서 잠깐 인터넷이 되다가, 귀국 후 **한국 통신사 로밍 요금**이 청구됐다.
- 통화 중에는 인터넷이 끊기거나, 반대로 통화 중에만 한국 회선으로 데이터가 나간다.
- eSIM은 신호가 잡히는데 인터넷이 안 되고, 상단에 두 회선 아이콘이 같이 보인다.

## 원인: 듀얼심은 데이터 회선이 하나뿐이고, '자동 전환' 기능이 있다

- Apple은 듀얼심 아이폰이 **한 번에 하나의 셀룰러 데이터 망만** 쓴다고 안내합니다. '셀룰러 데이터 전환 허용(Allow Cellular Data Switching)'을 켜면 **커버리지·가용성에 따라 두 회선의 데이터를 모두 쓸 수 있게** 됩니다. ([Apple](https://support.apple.com/en-us/109317))
- 삼성은 'Auto data switching'을 **기본 SIM이 망에 연결되지 못하면 다른 SIM으로 데이터를 쓰게 하는 기능**이라고 설명합니다. ([Samsung UK](https://www.samsung.com/uk/support/mobile-devices/how-to-install-nano-sim-card-and-esim-on-the-galaxy-s24-series/))
- 즉 여행 eSIM 신호가 약해지는 순간 폰이 **한국 회선으로 데이터를 넘길 수 있고**, 한국 회선의 데이터 로밍이 켜져 있으면 요금이 나올 수 있습니다. Holafly는 이 기능이 **신호 세기에 따라 회선을 자동 전환**하므로 꺼야 한다고 안내합니다.

## 제공사별 공식 안내 요약

| 제공사 | 데이터 전환 관련 공식 안내 | 출처 |
|---|---|---|
| Airalo | 해외 로밍 요금을 피하려면 '모바일 데이터 전환'을 막아 기본 SIM이 데이터를 쓰지 않게 하라고 안내. 아이폰: 설정 › 셀룰러 › 셀룰러 데이터 › eSIM 선택 › 'Allow Cellular Data Switching' 끄기. Airalo 회선은 켜기·데이터 회선 선택·데이터 로밍 켜기(이 로밍은 한국 통신사 요금이 아님) | [로밍 요금 피하기](https://www.airalo.com/help/getting-started-with-airalo/E8DFWD88SHUX/how-can-i-avoid-roaming-charges-when-using-airalo/XZLDPL0MI7C2) |
| Saily | 아이폰: 모바일 데이터에서 Saily 선택 후 같은 화면에서 'Allow Mobile Data Switching' 끄기. 삼성: 'Data switching'(또는 'Data switching and backup calling') 끄기 — **일부 미국·캐나다 모델엔 이 메뉴가 없음**. 픽셀: SIM이 둘 이상 켜져 있으면 'Automatic data switching' 끄기 | [설치 안내](https://support.saily.com/hc/en-us/articles/15751399206172-How-do-I-install-a-Saily-eSIM-on-my-phone) |
| Holafly | 한국 회선은 통화·문자용, Holafly는 데이터용으로 두고 아이폰 'Allow Cellular Data Switching' / 안드로이드 'Data Switching'을 끄라고 안내. **실물 SIM이 데이터용으로 켜져 있으면 Holafly eSIM 성능을 방해할 수 있다**고 명시 | [eSIM·실물 SIM 동시 사용](https://esim.holafly.com/faq/how-to-use-an-esim/use-sim-card-and-holafly-esim-at-the-same-time/) |

## 해결 순서 (공식 안내 기준)

1. **데이터 회선을 여행 eSIM으로 지정.**
    - 아이폰: 설정 › 셀룰러(모바일 데이터) › 셀룰러 데이터 › 여행 eSIM 선택 ([Apple](https://support.apple.com/en-us/109317))
    - 갤럭시: 설정 › 연결 › SIM 관리자(SIM card manager) › 모바일 데이터 › 여행 eSIM 선택 ([Holafly](https://esim.holafly.com/faq/how-to-use-an-esim/use-sim-card-and-holafly-esim-at-the-same-time/))
    - 픽셀: 설정 › 네트워크 및 인터넷 › SIM › '기본 SIM'에서 모바일 데이터 → 여행 eSIM ([Google](https://support.google.com/pixelphone/answer/9449293?hl=en))
2. **데이터 자동 전환 끄기.** 이 페이지의 핵심입니다.
    - 아이폰: 같은 '셀룰러 데이터' 화면 아래 **'셀룰러 데이터 전환 허용'** 끄기
    - 갤럭시: SIM 관리자의 **'Data switching'(Auto data switching)** 끄기
    - 픽셀: 네트워크 및 인터넷 › SIM › **'Automatic data switching'** 끄기. 픽셀 8 이하에는 통화 중 다른 SIM으로 데이터를 쓰는 **'Data during calls'** 옵션도 있으니 함께 확인하세요. ([Google](https://support.google.com/pixelphone/answer/9449293?hl=en))
3. **데이터 로밍: 여행 eSIM은 켜고, 한국 회선은 끄기.** 세 제공사 모두 여행 eSIM은 로밍을 켜야 연결된다고 안내합니다. 아이폰은 회선별로 설정됩니다(설정 › 셀룰러 › 회선 선택 › 데이터 로밍). Airalo는 **안드로이드에서는 데이터 로밍을 SIM별로 끌 수 없어** 로밍 요금을 피하려면 기본 SIM을 꺼야 한다고 안내합니다.
4. **한국 회선이 필요 없으면 아예 끄기.** Airalo는 기본 SIM을 끄거나 빼는 것이 요금을 막는 가장 확실한 방법이라고 안내합니다(아이폰: 설정 › 셀룰러 › 한국 회선 › '이 회선 켜기' 끄기). Holafly는 데이터가 바로 안 되면 다른 SIM을 **잠시 꺼 보라**고 안내합니다. 끄는 것은 삭제가 아니므로 귀국 후 다시 켜면 됩니다.
5. **비행기 모드 켰다 끄기 또는 재시작** 후 제공사 앱에서 eSIM 사용량이 실제로 줄어드는지 확인하세요. Airalo는 앱에서 사용량을 추적해 Airalo 데이터를 쓰고 있는지 확인하라고 안내합니다.

## 꺼 두면 생기는 일 (Apple·Google 공식 설명)

- **통화 중 인터넷:** Apple은 '셀룰러 데이터 전환 허용'을 끈 상태에서 데이터 회선이 아닌 번호(한국 번호)로 통화 중이면 **통화하는 동안 셀룰러 데이터가 안 된다**고 안내합니다. 켜 두면 통화 중에만 그 번호로 데이터가 넘어가는데, Apple 각주에 따르면 **데이터 로밍 중이면 이 통화 중 전환은 작동하지 않습니다.**
- **다른 번호로 오는 전화:** Apple은 데이터 회선이 아닌 회선으로 통화 중 다른 회선 전화를 받으려면 '데이터 전환 허용'이 필요하다고 안내합니다. 꺼 두면 통화 중 들어온 전화는 (설정돼 있다면) 음성사서함으로 갑니다.
- **비주얼 보이스메일·MMS:** Apple은 데이터 회선의 데이터 로밍이 켜져 있으면 음성 전용 회선(한국 번호)의 비주얼 보이스메일과 MMS가 꺼진다고 안내합니다.
- **픽셀 8a 이후:** 두 SIM으로 동시에 통화를 받으려면 'Automatic data switching'을 켜야 한다고 Google이 안내합니다. 여행 중에는 로밍 요금과 맞바꾸는 셈이므로, 한국 통신사 로밍 조건을 먼저 확인하세요.

## 데이터 전환을 꺼도 요금이 나오는 경우

- Airalo는 **데이터 로밍을 꺼도 켜져 있는 기본 회선의 수신 전화·음성사서함은 로밍 요금이 나올 수 있고**, 이는 Airalo가 아니라 원래 통신사 요금이라고 안내합니다. Saily·Holafly도 원래 통신사가 해외 통화·문자 요금을 받을 수 있으니 미리 확인하라고 안내합니다.
- 한국 통신사별 로밍 요금·자동 로밍 차단 여부는 이 페이지에서 확인하지 않았습니다(**미확인**). 출국 전 통신사에 직접 확인하세요.

## 실제 여행자 경험담 (레딧, 개인 경험)

아래는 공식 정보가 아니라 **레딧 이용자들이 직접 쓴 경험담**입니다.

- **데이터 로밍을 껐는데도 하루 로밍 요금:** Airalo를 쓰면서 기본 SIM 데이터 로밍을 껐는데도 매일 로밍 요금이 나왔다는 글에, '셀룰러 데이터 전환 허용'을 끄라는 답과 함께 전화·문자를 주고받았는지 확인하라는 댓글이 달렸습니다. ([r/Airalo](https://www.reddit.com/r/Airalo/comments/1f1vxyt/ive_got_my_data_roaming_off_for_my_primary_sim/))
- **여행 eSIM을 썼는데 원래 통신사 청구:** 유럽·아시아 65일 여행 중 eSIM을 썼는데도 원래 통신사에서 로밍 요금이 나왔다는 글에, 데이터 전환이 켜져 있었거나 원래 회선 데이터가 켜져 있었을 가능성, 그리고 **문자 인증·수신 전화만으로도 하루 로밍 요금이 붙었다**는 경험 댓글이 있습니다. ([r/eSIMs](https://www.reddit.com/r/eSIMs/comments/1iay2r4/spectrum_mobile_robs_you_when_you_travel/))
- **갤럭시 데이터 전환이 기대대로 안 됨:** 미국판 갤럭시에서 데이터 전환을 켰는데도 데이터 전용 SIM으로 넘어가지 않았다는 글과, 다른 나라 모델에서도 전환이 안 됐다는 댓글이 있습니다. 자동 전환에 기대지 말고 **데이터 회선을 직접 지정**하는 편이 확실합니다. ([r/samsung](https://www.reddit.com/r/samsung/comments/1hmx70h/data_switching_not_working/))

그래도 데이터가 안 되면 [일본 eSIM 데이터가 안 될 때(로밍·APN 점검)](../japan-esim-no-data/), 내 폰이 듀얼심·eSIM을 지원하는지는 [내 폰이 eSIM 지원하는지 확인하는 법](../check-phone-esim-support-unlocked/) 가이드를 참고하세요.

## 확인하지 못한 정보

- 갤럭시·픽셀 **한국어 메뉴 이름**(예: 'Data switching'의 한국어 표기): 공식 한국어 안내를 확인하지 못해 **미확인**입니다. 위 영문 이름과 비슷한 '데이터 전환' 항목을 찾으세요.
- 한국판 갤럭시(모델명 끝 N)에 'Data switching' 메뉴가 있는지: Saily는 일부 미국·캐나다 모델에 없다고만 안내해 한국판은 **미확인**입니다.
- Airalo의 안드로이드 '데이터 전환 끄기' 안내는 모바일 데이터 SIM을 Airalo로 지정하는 단계만 있고, 별도 자동 전환 토글 언급은 없습니다. 기기별 메뉴 차이는 **미확인**입니다.
- 한국 통신사(SKT·KT·LG U+)의 로밍 요금·차단 정책: **미확인**.
- 실제 기기에서 직접 테스트하지는 않았습니다.

## 출처

- [Apple: Using Dual SIM with an eSIM](https://support.apple.com/en-us/109317) — 2026-11-17 확인
- [Google Pixel 도움말: How to use dual SIMs](https://support.google.com/pixelphone/answer/9449293?hl=en) — 2026-11-17 확인
- [Samsung UK: Galaxy S24 nano-SIM·eSIM (SIM card manager)](https://www.samsung.com/uk/support/mobile-devices/how-to-install-nano-sim-card-and-esim-on-the-galaxy-s24-series/) — 2026-11-17 확인
- [Airalo 도움말: How can I avoid roaming charges when I use Airalo?](https://www.airalo.com/help/getting-started-with-airalo/E8DFWD88SHUX/how-can-i-avoid-roaming-charges-when-using-airalo/XZLDPL0MI7C2) — 2026-11-17 확인
- [Saily 도움말: How do I install a Saily eSIM on my phone?](https://support.saily.com/hc/en-us/articles/15751399206172-How-do-I-install-a-Saily-eSIM-on-my-phone) — 2026-11-17 확인
- [Saily 도움말: How to avoid roaming charges while using Saily?](https://support.saily.com/hc/en-us/articles/20793044376092-How-to-avoid-roaming-charges-while-using-Saily) — 2026-11-17 확인
- [Holafly FAQ: Can I use an eSIM and a physical SIM at the same time?](https://esim.holafly.com/faq/how-to-use-an-esim/use-sim-card-and-holafly-esim-at-the-same-time/) — 2026-11-17 확인
- [Holafly FAQ: How to set up and activate an eSIM?](https://esim.holafly.com/faq/esim-setup-guide/how-do-i-set-up-my-esim/) — 2026-11-17 확인
- 레딧 경험담: [r/Airalo](https://www.reddit.com/r/Airalo/comments/1f1vxyt/ive_got_my_data_roaming_off_for_my_primary_sim/), [r/eSIMs](https://www.reddit.com/r/eSIMs/comments/1iay2r4/spectrum_mobile_robs_you_when_you_travel/), [r/samsung](https://www.reddit.com/r/samsung/comments/1hmx70h/data_switching_not_working/) — 2026-11-17 확인
