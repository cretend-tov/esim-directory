---
title: "제공사 장애로 eSIM 데이터가 한꺼번에 끊겼을 때 대처법 (Airalo · Saily · Holafly)"
description: "잘 되던 여행 eSIM이 나만이 아니라 여러 사람·여러 나라에서 동시에 끊겼다면 제공사 장애일 수 있습니다. 공식 상태 페이지 확인법, 실제 장애 사례(복구까지 걸린 시간), 기다리는 동안 할 일, Airalo·Saily·Holafly 공식 환불 조건을 정리했습니다. 2026-11-26 확인."
country: 공통
problem: "여러 사람·여러 나라에서 동시에 데이터 끊김 / 신호는 꽉 찼는데 인터넷 안 됨 / 제공사(또는 현지 통신망) 장애"
verified_on: "2026-11-26"
---
## 이런 경우에 해당합니다

- 며칠 잘 쓰던 여행 eSIM이 **갑자기** 데이터가 안 된다. 안테나는 꽉 찼는데 인터넷만 안 되거나, '서비스 없음'이 뜬다.
- **같이 간 일행도 같은 제공사 eSIM이면 동시에** 안 된다.
- 레딧 등에 "나도 지금 안 된다"는 글이 **여러 나라에서** 올라온다.

이 경우는 내 폰 설정보다 **제공사(또는 제공사가 빌려 쓰는 통신망 업체) 쪽 장애**일 가능성이 큽니다. 실제로 2026년 3월 27일 Holafly 이용자들이 레딧에 일본·이탈리아·튀르키예·독일·모로코·중국 등에서 동시에 끊겼다는 글을 올렸고, Holafly 공식 계정은 "현지 서비스 제공사 중 한 곳이 시스템 개선 작업을 하다 예상치 못한 장애가 났다"고 답했습니다([레딧 1](https://www.reddit.com/r/eSIMs/comments/1s58575/holafly_service_down_3272026/), [레딧 2](https://www.reddit.com/r/eSIMs/comments/1s57lv3/terrible_experience_with_holafly/)).

**가장 중요한 원칙: 장애가 의심되면 eSIM을 지우지 마세요.** 장애는 복구되면 그대로 다시 됩니다. 지우면 재설치가 안 되는 경우가 많고, 교체·환불 심사에도 불리할 수 있습니다([eSIM 삭제·QR 분실 시 재설치 가능 여부](../esim-deleted-qr-lost-reinstall/)).

## 1단계: 나만 그런지, 제공사 장애인지 3분 안에 구분하기

1. **남은 데이터·유효기간부터 확인.** Saily 공식 블로그는 잘 되다가 끊겼을 때 가장 흔한 원인으로 **요금제 만료나 데이터 소진**을 꼽습니다. 와이파이를 잡아 앱에서 확인하세요.
2. **공식 상태(Status) 페이지 확인.** (아래 표 참고) 내 eSIM이 해당하는 국가·지역 항목이 'Operational'이 아니거나 진행 중인 장애(incident)가 있으면 제공사 장애입니다.
3. **일행 폰과 비교.** 같은 제공사 eSIM을 쓰는 일행도 동시에 안 되면 장애 가능성이 높고, 일행은 되는데 나만 안 되면 내 폰 설정 문제일 가능성이 높습니다.
4. **레딧 검색.** r/eSIMs, r/Airalo, r/saily에서 제공사 이름 + "down"으로 최근 글을 찾아보세요. 공식 상태 페이지보다 레딧 글이 먼저 올라오는 경우가 많습니다(아래 사례 참고). 단, 이용자 글은 공식 확인이 아닙니다.
5. 장애 징후가 없다면 장애가 아니라 설정 문제일 수 있습니다. [여행 중 eSIM이 갑자기 끊겼을 때 환불·재발급 받는 법](../esim-stopped-working-mid-trip-refund-replacement/)의 5분 점검(데이터 회선 선택·로밍·통신망 수동 선택·APN)을 먼저 해 보세요.

## 제공사별 공식 상태 페이지

| 제공사 | 공식 상태 페이지 | 무엇을 보면 되나 | 알림 받기 | 출처 |
|---|---|---|---|---|
| Airalo | [status.airalo.com](https://status.airalo.com) | **국가별 eSIM 이름**(예: 일본 'Moshi Moshi', 스페인 'Guay Mobile', 호주 'Yes! Go!', 한국 'LG U⁺')과 **지역 eSIM**(Asialink, Eurolink 등)이 항목별로 표시됨. 과거 장애 기록(Past Incidents)도 공개 | 페이지에 이메일·SMS·Slack 등 **업데이트 구독** 기능이 있음 | [Airalo Status](https://status.airalo.com) |
| Saily | 공식 상태 페이지는 **미확인** (status.saily.com 접속 안 됨, 2026-11-26) | 앱 안내, 고객지원 채팅(앱 Help → Chat with us), 공식 레딧 계정(u/Saily_eSIM) 답변 | 미확인 | [r/saily 공식 계정 답변](https://www.reddit.com/r/saily/comments/1t84uv0/is_sailycom_website_down/) |
| Holafly | [status.holafly.com](https://status.holafly.com) | **Data-Roaming**(데이터 연결), Platform, Payment 등 서비스별 상태와 날짜별 과거 기록. 국가별 구분은 없음 | 페이지의 Subscribe 기능 (2026-11-26 페이지에서 확인) | [Holafly Service Status](https://status.holafly.com) |

주의: 상태 페이지가 '정상'이어도 장애가 아니라는 보장은 없습니다. 아래 2026년 Holafly 사례들이 상태 페이지에 장애로 올라왔는지는 **미확인**입니다.

## 실제 장애 사례: 복구까지 얼마나 걸렸나

공식 상태 페이지 기록(Airalo)과 이용자 신고(레딧)입니다. 시간은 모두 한국시간(KST)으로 바꿨습니다.

| 날짜 | 제공사·범위 | 경과 (KST) | 출처 |
|---|---|---|---|
| 2025-01-02~03 | Airalo, **여러 나라** 서비스 저하 | 1/3 02:42 장애 공지 → 04:20 "복구됨, 기기 재시동해 보라" → 07:36 해결 | [Airalo Status 기록](https://stspg.io/dq9w7nj4nxk2) |
| 2025-01-15 | Airalo 스페인(Guay Mobile·Movistar망) 연결 문제 | 18:36 조사 시작 → 20:11 해결 | [Airalo Status 기록](https://stspg.io/scl8szhv9sdl) |
| 2025-03-14~15 | Airalo 호주(Yes! Go!·Optus망) 연결 불가 | 3/14 18:42 확인 → 3/15 05:37 "복구됨" → 3/15 19:19 해결 처리 | [Airalo Status 기록](https://stspg.io/3bj3z0pcbmv5) |
| 2025-06-27~28 | Airalo, **여러 나라** 서비스 저하 | 6/27 16:00 공지 → 6/28 20:14 "복구됨, 기기 재시동" (**하루 이상**) | [Airalo Status 기록](https://stspg.io/s8088jdrhm8t) |
| 2026-03-27~28 | Holafly, 일본·유럽·미주·중국 등 **전 세계** 이용자 동시 신고 | 3/28 00:57 첫 레딧 글(이미 약 2시간째) → 04:39 "전 세계 복구" 댓글. 이용자 1명은 "7시간 끊겼다"고 씀 | [레딧](https://www.reddit.com/r/eSIMs/comments/1s58575/holafly_service_down_3272026/) |
| 2026-05-07 | Holafly, 일본·한국·베트남·미국·중국 등 동시 신고 | 11:01 첫 레딧 글 → 일부 이용자 1~2시간 뒤 복구 댓글 | [레딧](https://www.reddit.com/r/eSIMs/comments/1t5x0fu/holafly_not_working_in_japan/) |
| 2026-10-31 | Holafly, 중국·발리·일본 동시 신고 ("신호 꽉 찼는데 데이터 없음") | 13:22 첫 레딧 글(약 3시간째) → 14:04~15:07 복구 댓글 | [레딧](https://www.reddit.com/r/eSIMs/comments/1xk0stt/holafly_service_down_in_china_full_bar_no_data/) |

레딧 사례에서 반복되는 불만은 **"고객센터가 AI 봇 답변만 하고 기술팀 연결 후 연락이 없었다"**, **"지도 앱이 안 돼서 와이파이 찾아 헤맸다"**, **"급해서 다른 eSIM을 또 샀다"**였습니다.

## 2단계: 장애로 끊겼을 때 할 일

1. **와이파이부터 확보.** 공항·역·카페·호텔 와이파이로 상태 페이지·고객센터에 접속합니다.
2. **eSIM은 지우지 말고 그대로 두기.** 공식 복구 공지(Airalo)는 "복구됐으니 **기기를 재시동**해 보라"고 안내합니다. 복구 소식이 들리면 재시동 → 비행기 모드 켰다 끄기를 해 보세요.
3. **여행 중에 바로 고객센터에 신고하고 기록 남기기.** 언제부터 안 됐는지, 어느 나라·도시인지, 상태 페이지 화면을 캡처해 두세요. 특히 Holafly는 **여행이 끝난 뒤 연락하면 환불을 보장하지 않는다**고 명시합니다.
   - Airalo: 앱의 주황색 채팅 아이콘 → 앱 채팅 또는 왓츠앱
   - Saily: 앱 Help → Chat with us (공식 레딧 계정 안내)
   - Holafly: help@holafly.com 또는 채팅, 왓츠앱 +1 (661) 384-8482 (환불 규정 페이지 표기)
4. **급하면 다른 제공사 eSIM을 임시로 사기.** 장애는 보통 한 제공사(또는 그 제공사가 쓰는 망 업체)에만 생깁니다. 길 찾기·택시 호출이 급하다면 소량 요금제를 하나 사 두는 게 현실적입니다. 다만 **두 번째 eSIM 비용을 원래 제공사가 보상해 주는지는 세 곳 모두 공식 규정에서 확인하지 못했습니다(미확인).**
5. **출국 전 대비:** 장거리 여행이면 오프라인 지도를 내려받고, 일행끼리 **서로 다른 제공사 eSIM**을 쓰면 한 곳이 장애가 나도 핫스팟으로 버틸 수 있습니다.

## 3단계: 장애로 못 쓴 기간 환불·교체 (공식 규정)

| 제공사 | 장애·연결 문제 시 공식 규정 | 신청 기한 | 신청 경로 | 출처 |
|---|---|---|---|---|
| Airalo | 개통했는데 **Airalo 측 오류**로 못 쓰면 **교체 또는 전액 환불**(고객 선택). 단 신청 후 **10일 안에 복구하지 못한 경우**이고, 일부 썼다면 **안 쓴 부분만** 환불. 앱에서 사유를 **eSIM not working**으로 고르면 교체도 선택 가능. 앱 내 환불은 **Airmoney(앱 포인트)만** | 문제 발생 후 **30일 이내** | 앱: 해당 eSIM/패키지 → 주문 상세 → **Request Refund** | [Airalo 이용약관](https://www.airalo.com/legal/terms-of-use), [Airalo 도움말: 환불](https://www.airalo.com/help/using-managing-esims/ZSEEHBT5HW6F/what-can-i-do-if-i-didnt-purchase-the-right-esim-or-have-a-change-of-plans/NYBBU4NC7KN6) |
| Saily | 개통 후에는 '사용'으로 간주해 보장 불가. 다만 **Saily 관련 품질 문제로 데이터를 많이 못 쓴 경우** 또는 **데이터가 99% 넘게 남은 경우** 전액·부분 환불 검토 | 미개통 환불은 구매 후 30일. 개통 후 품질 문제 환불 기한은 **미확인** | **웹사이트 환불 요청서**가 가장 빠르다고 안내 | [Saily 도움말: 환불 규정](https://support.saily.com/hc/en-us/articles/16420576170652-What-is-Saily-s-refund-policy) |
| Holafly | **Holafly 측 문제** 또는 **목적지 통신망 인프라가 불안정**해 eSIM이 안 되면 **전액·부분 환불** 가능. 그 밖의 경우 사용량에 따라 부분·전액 환불(**관리 수수료 US$3.50**) | 구매 후 6개월. 단 **여행 중에 먼저 연결 문제를 신고**해야 하며 여행 후 연락 시 보장 안 함 | help@holafly.com 또는 채팅. 결제 계좌로 **3~5영업일** 내 환불 | [Holafly 환불 규정](https://esim.holafly.com/refund-policy/) |

**현실적인 기대치:** 몇 시간짜리 장애는 Airalo 규정(신청 후 10일 안에 복구되면 환불 대상 아님)상 복구되면 환불 대상이 아닐 수 있습니다. 장애 시간만큼 기간 연장이나 보상을 해 주는지는 세 곳 모두 공식 문서에서 확인하지 못했습니다(**미확인**). 그래도 기록을 남겨 고객센터에 요청해 볼 수는 있습니다.

## 확인하지 못한 정보

- **Saily 공식 상태 페이지**가 있는지: status.saily.com은 2026-11-26 접속되지 않았고, 다른 공식 상태 페이지도 찾지 못해 **미확인**입니다.
- 2026년 3월·5월·10월 Holafly 동시 장애가 **status.holafly.com에 장애로 기록됐는지**: 과거 기록의 세부 내용을 확인하지 못해 **미확인**입니다.
- 장애 중 산 **다른 eSIM 비용 보상**, 장애 시간만큼 **유효기간 연장** 여부: 세 곳 모두 공식 규정에 없어 **미확인**입니다.
- Saily 개통 후 품질 문제 환불의 구체적 신청 기한: 도움말은 이용약관 3.5항을 참고하라고만 안내하며, 이번 확인에서 약관 페이지가 열리지 않아(HTTP 403) **미확인**입니다.
- 레딧 사례의 시간·범위는 **이용자 신고**이며 제공사가 공식 발표한 수치가 아닙니다(Holafly 3월 장애 원인 설명만 공식 계정 답변).

## 출처

- [Airalo Status (공식 상태 페이지)](https://status.airalo.com) — 2026-11-26 확인
- Airalo Status 과거 장애 기록: [2025-01-02 여러 나라](https://stspg.io/dq9w7nj4nxk2), [2025-01-15 스페인](https://stspg.io/scl8szhv9sdl), [2025-03-14 호주](https://stspg.io/3bj3z0pcbmv5), [2025-06-27 여러 나라](https://stspg.io/s8088jdrhm8t) — 2026-11-26 확인
- [Airalo 이용약관(Replacements and Refunds 항목)](https://www.airalo.com/legal/terms-of-use) — 2026-11-26 확인
- [Airalo 도움말: Can I get an Airalo refund?](https://www.airalo.com/help/using-managing-esims/ZSEEHBT5HW6F/what-can-i-do-if-i-didnt-purchase-the-right-esim-or-have-a-change-of-plans/NYBBU4NC7KN6) — 2026-11-26 확인
- [Holafly Service Status (공식 상태 페이지)](https://status.holafly.com) — 2026-11-26 확인
- [Holafly Refund Policy](https://esim.holafly.com/refund-policy/) — 2026-11-26 확인
- [Saily 도움말: What is Saily's refund policy?](https://support.saily.com/hc/en-us/articles/16420576170652-What-is-Saily-s-refund-policy) — 2026-11-26 확인
- [Saily 블로그: Saily eSIM not working](https://saily.com/blog/saily-esim-not-working/) — 2026-11-26 확인
- 이용자 신고(레딧): [Holafly Service Down - 3/27/2026](https://www.reddit.com/r/eSIMs/comments/1s58575/holafly_service_down_3272026/), [Terrible experience with Holafly (Holafly 공식 답변 포함)](https://www.reddit.com/r/eSIMs/comments/1s57lv3/terrible_experience_with_holafly/), [Holafly Not Working in Japan (2026-05-07)](https://www.reddit.com/r/eSIMs/comments/1t5x0fu/holafly_not_working_in_japan/), [Holafly service down in China (2026-10-31)](https://www.reddit.com/r/eSIMs/comments/1xk0stt/holafly_service_down_in_china_full_bar_no_data/), [Is saily.com website down? (Saily 공식 답변)](https://www.reddit.com/r/saily/comments/1t84uv0/is_sailycom_website_down/) — 2026-11-26 확인
