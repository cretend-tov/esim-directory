# 매일 밤 새 페이지 1개 추가하기

1. `data/queue.txt`에서 `[x]`가 없는 첫 줄을 고른다.
2. 각 제공사 **공식 페이지만** WebFetch로 읽는다 (예: airalo.com/<country>-esim, saily.com/esim-<country>/, esim.holafly.com/esim-<country>/).
   - 확인 못 한 가격·규정은 절대 추정하지 말고 "미확인"으로 쓰고 `unverified:`에 이유를 적는다.
   - 모든 사실 옆에 출처 URL과 확인일(KST)을 남긴다.
3. 파일 작성
   - `country` 유형 → `data/countries/<slug>.yaml` (`japan.yaml` 형식 복사)
   - `guide` 유형 → `data/guides/<slug>.md` (`_TEMPLATE.md.example` 복사, slug는 영문 소문자-하이픈)
4. 빌드: `.venv/bin/python build.py` → `dist/` 생성, sitemap.xml 자동 갱신.
5. 확인: `cd dist && python3 -m http.server 8000` 로 열어본 뒤 서버 종료.
6. `queue.txt` 해당 줄 앞에 `[x] YYYY-MM-DD ` 추가.
7. 배포(설정 후): `dist/`를 호스팅에 업로드(예: Cloudflare Pages/Netlify/GitHub Pages).
8. 큐가 10줄 이하로 줄면 레딧/X 불만글을 보고 '국가 × 문제' 주제를 보충.

제휴 링크는 `site.yaml`의 `affiliate:` 값만 바꾸면 전 페이지에 반영된다. 계정 승인 전까지 자리표시자 유지.
