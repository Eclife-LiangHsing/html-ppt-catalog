# World Cup Fun Picks Apps Script

目的：讓 GitHub Pages 的「良興世界盃預測挑戰」可以把大家的預測集中寫進 Google Sheet，並讓網頁讀回全部參加者紀錄。

## 部署步驟

1. 在 Google Drive 建立一份 Google Sheet，例如 `良興世界盃預測挑戰_預測紀錄_20260613`。
2. 開啟 `Extensions > Apps Script`。
3. 把 `Code.gs` 內容貼到 Apps Script 專案。
4. Deploy > New deployment > Web app。
5. Execute as: `Me`。
6. Who has access: 若只做內部測試可選公司帳號範圍；若 GitHub Pages 公開頁要可寫入，需選可匿名存取的 Web App，且頁面不放個資欄位。
7. 複製 Web App URL。
8. 回到 `index.html`，把 `centralApiEndpoint = ""` 改成該 Web App URL，再重新發布 GitHub Pages。

## API

- 送出：`GET ?action=submit&payload=<encoded json>&callback=<function>`
- 讀取：`GET ?action=list&callback=<function>`

使用 JSONP 是為了避開 GitHub Pages 讀寫 Apps Script 時常見的 CORS 問題。
