from __future__ import annotations

import html
import os
import zipfile
from pathlib import Path


OUT = Path(__file__).resolve().parent


TITLE = "良興 2026 年 7 月兩線行銷活動提案"
SUBTITLE = "夏日換機・AI 效率補給站"
PERIOD = "2026/7/1–2026/7/31"


slides = [
    {
        "title": TITLE,
        "bullets": [
            SUBTITLE,
            f"活動期間：{PERIOD}",
            "兩線策略：線上會員電商轉換 + 線下門市服務導購",
            "目標：把暑假、AI 辦公、開學前採購需求導回良興官網與門市",
        ],
        "note": "開場先定義：這不是單純夏季特賣，而是把 7 月需求整理成兩條可執行的行銷線。",
    },
    {
        "title": "7 月市場切入點",
        "bullets": [
            "暑假娛樂：電競鍵盤滑鼠、螢幕、電競筆電、耳麥",
            "AI 辦公與直播：攝影機、麥克風、筆電、螢幕、擴充座",
            "開學補給：行動電源、充電線、SSD、USB Hub、筆電周邊",
            "居家/小辦公：Wi-Fi 7、Mesh、網卡、NAS/儲存周邊",
        ],
        "note": "7 月不是只有折扣檔，真正的購買理由來自暑假、開學、辦公效率和網路升級。",
    },
    {
        "title": "兩線活動設計",
        "bullets": [
            "A 線｜線上會員電商：官網活動頁、LINE、EDM、SEO 內容、再行銷受眾",
            "B 線｜線下門市導購：門市情境陳列、店員話術、QR 導流、現場加購",
            "共同主題：夏日換機・AI 效率補給站",
            "共同追蹤：每一波素材與 QR 都掛 UTM，回收活動成效",
        ],
        "note": "賴總提到兩線，我先用線上與線下做設計，這最符合良興全通路零售的優勢。",
    },
    {
        "title": "A 線：線上會員電商轉換",
        "bullets": [
            "官網活動頁用四大情境導購，不只堆商品",
            "LINE 每週一波：開跑、AI 辦公、電競升級、開學補給、倒數收尾",
            "EDM 用會員分眾：辦公族、學生/家長、玩家、SOHO/小企業",
            "SEO 先卡長尾題：開學 3C 清單、視訊會議攝影機、Wi-Fi 7 升級",
        ],
        "note": "線上主軸是讓會員快速找到自己的情境，並把內容流量導到商品頁。",
    },
    {
        "title": "B 線：線下門市服務導購",
        "bullets": [
            "門市設四個小情境：AI 會議桌、電競體驗、開學補給、Wi-Fi 升級",
            "店員話術從規格轉為問題：會議畫面不清楚？宿舍 Wi-Fi 不穩？筆電容量不夠？",
            "每區放 QR Code 導到對應活動頁與商品集合",
            "門市加購：線材、保護、延保、清潔、備份儲存",
        ],
        "note": "門市線不要只是擺 POP，而是讓店員更容易用場景帶商品與加購。",
    },
    {
        "title": "四大活動分區",
        "bullets": [
            "AI 辦公/直播效率：攝影機、麥克風、商務筆電、螢幕、擴充座",
            "暑假電競升級：鍵盤滑鼠、耳機、螢幕、電競椅、電競筆電",
            "開學/返校 3C 補給：行動電源、快充線、SSD、Hub、背包周邊",
            "居家/小辦公網通：Wi-Fi 7 路由器、Mesh、網卡、NAS/備份",
        ],
        "note": "四大分區可同時支援官網活動頁、門市陳列、社群內容和 SEO 文章。",
    },
    {
        "title": "線上素材建議",
        "bullets": [
            "LINE 推播：每則只打一個情境，短句 + 明確 CTA",
            "EDM：首屏主題、四區商品、會員優惠、配送付款提醒",
            "社群：清單型、痛點型、比較型、限時型、門市導購型",
            "短影音：30 秒解決一個問題，例如視訊畫面糊、宿舍 Wi-Fi 弱、SSD 不夠",
        ],
        "note": "素材要能重複使用，同一套內容可拆成 LINE、EDM、社群與門市話術。",
    },
    {
        "title": "門市執行建議",
        "bullets": [
            "每店選 2 個最適合的情境，不要求所有門市都做滿四區",
            "導購卡：問題、推薦品類、加購品、官網 QR",
            "店員週會 15 分鐘快速訓練：每週一個主推情境",
            "門市回報熱問問題，月底整理成 FAQ 與下一檔內容",
        ],
        "note": "門市執行要輕量化，否則活動會卡在陳列與教育成本。",
    },
    {
        "title": "7 月推進節奏",
        "bullets": [
            "6/24–6/30：商品、價格、庫存、贈品、素材確認",
            "7/1–7/7：活動開跑，主打夏日換機與全品類導購",
            "7/8–7/14：AI 辦公/直播週",
            "7/15–7/21：暑假電競升級週",
            "7/22–7/31：開學補給 + 最後倒數",
        ],
        "note": "節奏不是一次把所有素材打完，而是每週給消費者一個新理由。",
    },
    {
        "title": "KPI 與追蹤",
        "bullets": [
            "線上：活動頁 PV、商品點擊率、LINE CTR、EDM CTR、轉換率、營收",
            "線下：QR 掃碼、門市來客、主推品銷量、加購率、客單價",
            "內容：SEO 文章曝光、搜尋點擊、社群互動、短影音觀看完成率",
            "管理層摘要：哪個情境有效、哪個品類成交、下次檔期怎麼調整",
        ],
        "note": "兩線活動一定要先定追蹤，不然月底只能看營收，無法知道哪個動作有效。",
    },
    {
        "title": "需要良興確認的事項",
        "bullets": [
            "主推商品與毛利排序",
            "7 月優惠規則：滿額、贈品、會員點數、門市限定",
            "活動頁與素材尺寸規格",
            "門市參與店點、陳列空間、店員話術審核",
            "是否要加入 B2B/企業採購版本",
        ],
        "note": "最後收斂成決策事項，方便賴總指派內部同仁補齊資料。",
    },
    {
        "title": "小興建議的第一步",
        "bullets": [
            "先選 20–40 個 7 月主推商品，依四大情境排序",
            "用同一套商品資料生成：活動頁、LINE 文案、EDM、門市導購卡",
            "第一週先跑小規模 A/B，第二週開始加碼有效素材",
            "月底用數據回收，建立下一檔活動模板",
        ],
        "note": "結尾強調可落地：先用一套模板跑起來，再逐月優化。",
    },
]


doc_sections = [
    ("一、企劃摘要", [
        "本提案以 2026 年 7 月良興活動為目標，主題建議為「夏日換機・AI 效率補給站」。",
        "活動採兩線並行：A 線為線上會員電商轉換，B 線為線下門市服務導購。",
        "核心目的不是單純降價，而是用 7 月高需求情境帶動商品點擊、會員回流、門市諮詢與加購。",
    ]),
    ("二、活動定位", [
        "7 月需求可分為暑假娛樂、AI 辦公/直播、開學補給、居家/小辦公網通四大情境。",
        "良興的優勢在於商品品類完整、官網與門市並存、具備服務與導購信任感。",
        "活動頁與門市陳列應以「情境解決方案」呈現，降低消費者選品成本。",
    ]),
    ("三、兩線行銷設計", [
        "A 線：官網活動頁、LINE 推播、EDM、SEO 文章、社群與再行銷。",
        "B 線：門市情境陳列、店員導購話術、QR 導流、現場加購、門市問題回收。",
        "兩線共用同一套商品資料、活動主題與 UTM 追蹤邏輯，方便月底結案分析。",
    ]),
    ("四、四大活動分區", [
        "AI 辦公/直播效率：攝影機、麥克風、商務筆電、螢幕、擴充座。",
        "暑假電競升級：鍵盤滑鼠、耳機、螢幕、電競椅、電競筆電。",
        "開學/返校 3C 補給：行動電源、快充線、SSD、USB Hub、筆電周邊。",
        "居家/小辦公網通：Wi-Fi 7 路由器、Mesh、網卡、NAS/備份。",
    ]),
    ("五、7 月執行節奏", [
        "6/24–6/30：商品、價格、庫存、贈品、素材確認。",
        "7/1–7/7：活動開跑，主打夏日換機。",
        "7/8–7/14：AI 辦公/直播週。",
        "7/15–7/21：暑假電競升級週。",
        "7/22–7/31：開學補給與最後倒數。",
    ]),
    ("六、KPI", [
        "線上：活動頁 PV、商品點擊率、LINE CTR、EDM CTR、轉換率、營收。",
        "線下：QR 掃碼、門市來客、主推品銷量、加購率、客單價。",
        "內容：SEO 文章曝光、搜尋點擊、社群互動、短影音觀看完成率。",
    ]),
    ("七、待確認事項", [
        "主推商品與毛利排序。",
        "7 月優惠規則：滿額、贈品、會員點數、門市限定。",
        "活動頁與素材尺寸規格。",
        "門市參與店點、陳列空間、店員話術審核。",
        "是否加入 B2B/企業採購版本。",
    ]),
]


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def write_docx(path: Path) -> None:
    body = []
    body.append(f'<w:p><w:r><w:rPr><w:b/><w:sz w:val="36"/></w:rPr><w:t>{esc(TITLE)}</w:t></w:r></w:p>')
    body.append(f'<w:p><w:r><w:rPr><w:sz w:val="24"/></w:rPr><w:t>{esc(SUBTITLE)}｜{esc(PERIOD)}</w:t></w:r></w:p>')
    for heading, paragraphs in doc_sections:
        body.append(f'<w:p><w:r><w:rPr><w:b/><w:sz w:val="28"/></w:rPr><w:t>{esc(heading)}</w:t></w:r></w:p>')
        for p in paragraphs:
            body.append(f'<w:p><w:r><w:t>• {esc(p)}</w:t></w:r></w:p>')
    document = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    {''.join(body)}
    <w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/></w:sectPr>
  </w:body>
</w:document>'''
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>''')
        z.writestr("_rels/.rels", '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>''')
        z.writestr("word/document.xml", document)


def slide_xml(slide: dict[str, object], idx: int) -> str:
    title = esc(str(slide["title"]))
    bullets = "".join(
        f'<a:p><a:r><a:rPr lang="zh-TW" sz="2400"/><a:t>{esc("• " + b)}</a:t></a:r></a:p>'
        for b in slide["bullets"]
    )
    note = esc(str(slide["note"]))
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:bg><p:bgPr><a:solidFill><a:srgbClr val="071426"/></a:solidFill><a:effectLst/></p:bgPr></p:bg>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
      <p:sp>
        <p:nvSpPr><p:cNvPr id="2" name="Title"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>
        <p:spPr><a:xfrm><a:off x="620000" y="430000"/><a:ext cx="10800000" cy="1200000"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/></p:spPr>
        <p:txBody><a:bodyPr wrap="square"/><a:lstStyle/><a:p><a:r><a:rPr lang="zh-TW" sz="3900" b="1"><a:solidFill><a:srgbClr val="F5F9FF"/></a:solidFill></a:rPr><a:t>{title}</a:t></a:r></a:p></p:txBody>
      </p:sp>
      <p:sp>
        <p:nvSpPr><p:cNvPr id="3" name="Bullets"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>
        <p:spPr><a:xfrm><a:off x="750000" y="1900000"/><a:ext cx="10800000" cy="3900000"/></a:xfrm><a:prstGeom prst="roundRect"><a:avLst/></a:prstGeom><a:solidFill><a:srgbClr val="10233B"><a:alpha val="85000"/></a:srgbClr></a:solidFill><a:ln><a:solidFill><a:srgbClr val="62D5FF"/></a:solidFill></a:ln></p:spPr>
        <p:txBody><a:bodyPr wrap="square" lIns="240000" tIns="180000" rIns="240000" bIns="180000"/><a:lstStyle/>{bullets}</p:txBody>
      </p:sp>
      <p:sp>
        <p:nvSpPr><p:cNvPr id="4" name="Footer"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>
        <p:spPr><a:xfrm><a:off x="750000" y="6450000"/><a:ext cx="10800000" cy="520000"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/></p:spPr>
        <p:txBody><a:bodyPr wrap="square"/><a:lstStyle/><a:p><a:r><a:rPr lang="zh-TW" sz="1500"><a:solidFill><a:srgbClr val="B5C4D8"/></a:solidFill></a:rPr><a:t>{idx:02d}/12｜{note}</a:t></a:r></a:p></p:txBody>
      </p:sp>
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr>
</p:sld>'''


def write_pptx(path: Path) -> None:
    slide_overrides = "\n".join(
        f'<Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
        for i in range(1, len(slides) + 1)
    )
    slide_ids = "\n".join(
        f'<p:sldId id="{255 + i}" r:id="rId{i}"/>'
        for i in range(1, len(slides) + 1)
    )
    rels = "\n".join(
        f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i}.xml"/>'
        for i in range(1, len(slides) + 1)
    )
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
  <Override PartName="/ppt/presProps.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presProps+xml"/>
  <Override PartName="/ppt/viewProps.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.viewProps+xml"/>
  <Override PartName="/ppt/tableStyles.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.tableStyles+xml"/>
  {slide_overrides}
</Types>''')
        z.writestr("_rels/.rels", '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
</Relationships>''')
        z.writestr("ppt/_rels/presentation.xml.rels", f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  {rels}
</Relationships>''')
        z.writestr("ppt/presentation.xml", f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:sldIdLst>{slide_ids}</p:sldIdLst>
  <p:sldSz cx="12192000" cy="6858000" type="wide"/>
  <p:notesSz cx="6858000" cy="9144000"/>
</p:presentation>''')
        z.writestr("ppt/presProps.xml", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:presentationPr xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"/>')
        z.writestr("ppt/viewProps.xml", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:viewPr xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"/>')
        z.writestr("ppt/tableStyles.xml", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><a:tblStyleLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" def="{5C22544A-7EE6-4342-B048-85BDC9FD1C3A}"/>')
        for i, slide in enumerate(slides, 1):
            z.writestr(f"ppt/slides/slide{i}.xml", slide_xml(slide, i))


def write_markdown(path: Path) -> None:
    lines = [f"# {TITLE}", "", f"副標：{SUBTITLE}", f"活動期間：{PERIOD}", ""]
    for heading, paragraphs in doc_sections:
        lines.extend([f"## {heading}", ""])
        for p in paragraphs:
            lines.append(f"- {p}")
        lines.append("")
    lines.extend([
        "## 小興建議",
        "",
        "- 第一版先選 20–40 個主推商品，依四大情境排序。",
        "- 用同一套商品資料生成活動頁、LINE 文案、EDM、門市導購卡。",
        "- 每個素材與 QR 都掛 UTM，月底做成效回收。",
        "",
    ])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    write_markdown(OUT / "campaign-proposal.md")
    write_docx(OUT / "良興_2026年7月兩線行銷活動提案.docx")
    write_pptx(OUT / "良興_2026年7月兩線行銷活動提案.pptx")
    print("Generated:")
    for name in ["campaign-proposal.md", "良興_2026年7月兩線行銷活動提案.docx", "良興_2026年7月兩線行銷活動提案.pptx"]:
        p = OUT / name
        print(f"- {p} ({p.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
