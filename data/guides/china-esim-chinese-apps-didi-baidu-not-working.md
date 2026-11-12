---
title: "중국에서 디디·바이두 지도 등 중국 앱이 안 될 때 (해외 경유 eSIM 점검법)"
description: "구글·인스타는 되는데 디디(DiDi)·바이두 지도·고덕(Amap) 같은 중국 앱이 오류를 낼 때. Airalo·Saily·Holafly 공식 안내와 레딧 경험담을 바탕으로 원인과 점검 순서를 정리했습니다. 공식 호환성 안내가 없는 부분은 미확인 표시. 2026-11-12 확인."
country: 중국
problem: "디디 'Network Exception' / 바이두 지도·고덕 지도 로딩 안 됨 / 다핑(Dianping) 오류"
verified_on: "2026-11-12"
---
## 이런 경우에 해당합니다

- 중국에서 여행용 eSIM으로 **구글·인스타그램·왓츠앱은 잘 되는데**, 디디(DiDi)가 'Network Exception' 오류를 내거나 바이두 지도·고덕 지도(Amap)가 로딩되지 않는다.
- 처음 며칠은 괜찮았는데 **일주일쯤 지나서** 고덕 지도·다핑(Dianping) 같은 앱이 제대로 동작하지 않는다.
- 알리페이는 되는데 같은 폰의 다른 중국 앱만 안 된다.

> 막힌 해외 앱(카카오톡·구글 등)이 안 되는 문제는 [중국에서 카카오톡·구글이 안 될 때](../china-esim-kakaotalk-google-access/)를 보세요. 이 페이지는 그 **반대 상황**, 즉 중국 앱 쪽 문제를 다룹니다.

## 왜 이런 일이 생기나 (공식 안내 기준)

- **Airalo**는 중국 eSIM·아시아 지역·글로벌 eSIM이 국제 로밍 방식이라 데이터가 **중국 본토 밖 게이트웨이**를 거쳐 나가고, 그래서 방화벽 입장에서는 "해외 로밍 이용자"로 보인다고 공식 도움말에서 설명합니다.
- 즉 해외 경유 eSIM을 쓰면 **중국 앱 입장에서도 접속이 해외에서 들어오는 것처럼** 보일 수 있습니다. 이것이 중국 앱 오류의 원인인지에 대해 Airalo·Saily·Holafly 모두 **공식 설명이 없습니다(미확인)**. 아래 레딧 경험담과 이용자 추정이 있을 뿐입니다.
- **Holafly** 공식 블로그는 중국에서 필요한 앱으로 바이두 지도·고덕 지도·디디·위챗·알리페이를 꼽고, 디디 국제 버전은 영어 화면·해외 전화번호·해외 카드를 지원한다고 안내합니다. 또 "Holafly eSIM이면 체크리스트의 앱이 도착 즉시 모두 작동한다"고 홍보하지만, 해외 경유 접속에서 중국 앱이 막히는 경우에 대한 별도 안내는 없습니다.
- **Saily** 중국 eSIM 공식 페이지는 China Telecom·China Unicom 망을 쓴다고 적고 있지만, 데이터가 어디로 나가는지(해외 경유 여부)나 중국 앱 호환성은 **언급이 없습니다(미확인)**.

## 3사 공식 안내 비교

| 제공사 | 데이터 경로(공식) | 중국 앱 관련 공식 언급 | 출처 |
|---|---|---|---|
| Airalo | 중국 본토 밖 게이트웨이 경유(국제 로밍), VPN 불필요 | 없음(미확인) | [도움말: 중국 VPN 필요 여부](https://www.airalo.com/help/using-managing-esims/ZSEEHBT5HW6F/stay-connected-in-china-your-guide-to-unfiltered-international-access-is-a-vpn-required/ZDZBNIKI4TFP) |
| Saily | 공식 언급 없음(미확인). 망은 China Telecom·China Unicom. 구글·인스타는 앱의 '가상 위치'로 접속 가능 | 없음(미확인) | [중국 eSIM 페이지](https://saily.com/esim-china/) |
| Holafly | 중국 eSIM에 VPN 포함(기존 페이지 확인 내용, 2026-11-01). 데이터 로밍을 켜야 함 | 디디·바이두 지도·고덕·위챗·알리페이를 필수 앱으로 소개, "도착 즉시 작동"이라고 홍보. 오류 시 대처 안내는 없음 | [중국 eSIM 페이지](https://esim.holafly.com/esim-china/), [블로그: 중국 여행 앱](https://esim.holafly.com/travel-tips/china-travel-apps/) |

## 안 될 때 점검 순서

1. **와이파이와 eSIM 데이터를 바꿔 가며 시험합니다.** 호텔·카페 와이파이는 중국 국내망이라, 레딧에서는 "중국 앱은 와이파이로, 막힌 해외 앱은 eSIM 데이터로" 나눠 쓰라는 조언이 자주 보입니다(이용자 경험담). 와이파이에서 디디가 된다면 eSIM 경로 문제일 가능성이 큽니다.
2. **데이터 회선과 데이터 로밍을 확인합니다.** 폰 설정에서 데이터 회선이 여행 eSIM인지, eSIM 회선의 데이터 로밍이 켜져 있는지 봅니다. Saily와 Holafly 모두 공식 페이지에서 데이터 로밍을 켜야 한다고 안내합니다.
3. **Saily 사용자: 가상 위치를 끄고 다시 시도합니다.** 가상 위치는 구글·인스타 접속용 기능으로 안내돼 있어, 켜 둔 채로 중국 앱을 쓰면 위치가 다른 나라로 잡힐 수 있습니다(이 영향은 공식 언급이 없어 미확인).
4. **Holafly 사용자: 포함된 VPN 기능이 켜져 있다면 꺼 보고**, 그래도 안 되면 24시간 고객지원에 연락합니다. Holafly는 중국 eSIM에 VPN이 포함된다고 안내하지만, 켜고 끄는 방식은 공식 페이지에 설명이 없습니다(미확인).
5. **알리페이 안의 디디 미니프로그램을 써 봅니다.** 레딧·여행자들 사이에서는 디디 단독 앱 대신 알리페이(또는 위챗) 안에서 디디를 부르는 방법이 자주 언급됩니다. 앞서 소개한 r/Airalo 글에서도 디디·바이두 지도는 안 됐지만 **알리페이는 계속 정상**이었다고 했습니다.
6. **지도는 대안을 준비합니다.** 바이두 지도가 안 되면 고덕 지도(Amap)로, 둘 다 안 되면 오프라인 지도를 씁니다. Holafly 블로그는 대도시는 고덕, 시골은 바이두가 낫다며 둘 다 받아 두라고 권합니다.
7. **그래도 안 되면 판매처 고객센터에 "중국 앱(디디·바이두 지도)이 이 eSIM에서 되는지" 물어보고**, 안 된다면 환불·교체를 요청합니다. 레딧 글쓴이는 결국 다른 eSIM을 새로 사서 해결했다고 했습니다. 환불 규정은 [여행 중 eSIM 환불 규정 비교](../esim-refund-trip-cancelled/)를 참고하세요.

## 레딧 경험담 (공식 정보 아님)

- **Airalo로 해외 앱은 되는데 디디·바이두 지도가 안 됨:** 상하이 여행자가 인스타그램·왓츠앱·텔레그램은 됐지만 디디는 'Network Exception', 바이두 지도는 로딩이 안 됐고 알리페이만 정상이었다고 썼습니다. 같은 글에 "상하이·베이징에서 Airalo로 다 잘 됐다"는 반대 경험도 있습니다. ([r/Airalo](https://www.reddit.com/r/Airalo/comments/1eog9g1/china_airalo_esim_unreliable/))
- **홍콩·싱가포르 경유 eSIM에서 일주일 뒤 고덕·다핑 오류:** 2026년 6월, 여행 플랫폼에서 산 홍콩·싱가포르 경유 eSIM으로 해외 앱은 잘 됐지만 약 일주일 뒤 다핑과 고덕 지도가 제대로 동작하지 않았고, 고덕은 다시 됐지만 다핑은 끝내 안 됐다는 글이 있습니다. 글쓴이는 다음엔 중국 현지 유심과 해외 경유 eSIM을 같이 쓰겠다고 했습니다. ([r/travelchina](https://www.reddit.com/r/travelchina/comments/1tuguqt/china_esim_for_google_mapsgmail_without_fighting/))
- **Holafly 신호 끊김으로 디디 호출 실패:** 2026년 5월, 베이징 도착 직후 Holafly 신호가 완전히 끊겨 디디를 못 불렀고, 고객지원이 eSIM을 교체해 줬다는 글이 있습니다. 이 경우는 중국 앱 차단이 아니라 연결 자체의 문제였습니다. ([r/chinatravel](https://www.reddit.com/r/chinatravel/comments/1tgxbxm/issues_with_holafly_esim_is_it_too_late_to_change/))

## 출국 전에 할 것

- 디디·알리페이·위챗·고덕/바이두 지도는 **한국에서 미리 설치하고 가입·카드 등록**까지 마칩니다. Holafly 블로그는 구글 플레이가 중국에서 막혀 있어 안드로이드는 현지에서 앱을 받기 어렵다고 안내합니다.
- 여행 eSIM은 대부분 데이터 전용이라 가입 인증 문자는 **한국 번호**로 받습니다. 한국 유심은 꺼 두지 말고 문자만 받을 수 있게 두세요(데이터 로밍은 끔).
- eSIM은 한국에서 미리 구매·설치합니다(Saily는 중국 안에서 eSIM을 구매할 수 없다고 안내).
- 가격·망 비교는 [중국 eSIM 비교](../../esim/china/)를 참고하세요.

## 확인하지 못한 정보

- 해외 경유 eSIM에서 디디·바이두 지도·고덕·다핑이 오류를 내는 **정확한 원인**: 세 곳 모두 공식 설명이 없어 **미확인**입니다(접속 위치가 해외로 잡히기 때문이라는 것은 이용자 추정).
- Airalo·Saily·Holafly 각 사 중국 eSIM에서 중국 앱이 정상 작동하는지에 대한 **공식 호환성 안내**: 없음(미확인). Holafly는 홍보 문구로 "작동한다"고만 적고 있습니다.
- Saily 중국 eSIM의 데이터 출구 위치(해외 경유 여부): **미확인**.
- Holafly '포함 VPN'을 켜고 끄는 방법: **미확인**.
- 실제 중국 현지 접속 테스트는 하지 않았습니다.

## 출처

- [Airalo 도움말: Stay Connected in China (Is a VPN Required?)](https://www.airalo.com/help/using-managing-esims/ZSEEHBT5HW6F/stay-connected-in-china-your-guide-to-unfiltered-international-access-is-a-vpn-required/ZDZBNIKI4TFP) — 2026-11-12 확인
- [Saily 중국 eSIM 공식 페이지 (망·데이터 로밍·VPN·가상 위치 FAQ)](https://saily.com/esim-china/) — 2026-11-12 확인
- [Holafly 중국 eSIM 공식 페이지 (데이터 로밍 설정)](https://esim.holafly.com/esim-china/) — 2026-11-12 확인
- [Holafly 블로그: China runs on completely different apps](https://esim.holafly.com/travel-tips/china-travel-apps/) — 2026-11-12 확인
- 레딧 경험담: [r/Airalo](https://www.reddit.com/r/Airalo/comments/1eog9g1/china_airalo_esim_unreliable/), [r/travelchina](https://www.reddit.com/r/travelchina/comments/1tuguqt/china_esim_for_google_mapsgmail_without_fighting/), [r/chinatravel](https://www.reddit.com/r/chinatravel/comments/1tgxbxm/issues_with_holafly_esim_is_it_too_late_to_change/) — 2026-11-12 확인
