"""SWO40万円 商品LP10月修正 三校：再校 ver2.0（build_swo40_oct_r2.py の出力）に、
10/23 佐藤様の再校戻し（pptx 3枚）を反映する。置換は件数を数え、期待値と違えば止める。
使い方：python3 build_swo40_oct.py base_sasaki_ver5.5wB.html v11.html
        python3 build_swo40_oct_r2.py v11.html v20.html
        python3 build_swo40_oct_r3.py v20.html ../index.html"""
import sys

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()


def rep(old, new, n=1):
    global s
    c = s.count(old)
    if c != n:
        sys.exit(f'COUNT {c} != {n}: {old[:80]!r}')
    s = s.replace(old, new)


rep('<!-- BUILD_TAG: swo2026_40venue_oct_ver2.0 / 2026-10-22 -->',
    '<!-- BUILD_TAG: swo2026_40venue_oct_ver3.1 / 2026-10-23 -->')

# ---- 1枚目：お悩みの項目を1行に（「施設訪問」を削除） ----
rep('海外招へい・協賛金の募集・懇親会・施設訪問など、手配することが多い',
    '海外招へい・協賛金の募集・懇親会など、手配することが多い')

# ---- 2・3枚目：業務内容を、業務と料金がそろった表に ----
start = s.index('<table class="tbl-clear">')
end = s.index('</table>', start) + len('</table>')
old_tbl = s[start:end]
for w, n in [('LP3ページ', 1), ('研究費ホームページ 20万円', 1), ('tokyo/jimu/', 2), ('オンライン事務局</td>', 1), ('<tr>', 12)]:
    if old_tbl.count(w) != n:
        sys.exit(f'業務内容の表が想定と違う: {w} {old_tbl.count(w)}')

GROUPS = [
    ('制作　Webサイト', [
        ('研究室ホームページ', '5万円', 'https://science-web.co.jp/lab.trial/'),
        ('研究室ホームページ', '20万円', 'https://science-web.co.jp/lab/'),
        ('学会ホームページ', '20万円', 'https://science-web.co.jp/gakkai/'),
        ('研究費ホームページ', '20万円', 'https://science-web.co.jp/science'),
    ]),
    ('開発　Webシステム', [
        ('論文投稿システム', '5万円', 'https://science-web.tokyo/ronbun.trial/'),
        ('論文投稿システム', '20万円', 'https://science-web.tokyo/ronbun/'),
        ('紀要管理システム', '30万円', 'https://science-web.tokyo/bulletin/'),
        ('役員選挙システム', '20万円', 'https://science-web.tokyo/senkyo/'),
        ('学会事務システム', '20万円', 'https://science-web.tokyo/jimu-system/'),
    ]),
    ('開発　会議開催サポート', [
        ('演題登録・参加登録システム', '30万円', 'https://science-web.online/30venue'),
        ('開催案内 ＋登録システム2点', '40万円', 'https://science-web.online/40venue'),
        ('オンライン事務局', '', 'https://science-web.online/online-secretariat/'),
    ]),
]
rows = []
for gi, (cat, items) in enumerate(GROUPS):
    rows.append(f'      <tbody class="biz-group">')
    for i, (name, price, url) in enumerate(items):
        th = f'<th rowspan="{len(items)}" class="biz-cat" scope="rowgroup">{cat}</th>' if i == 0 else ''
        rows.append(
            f'      <tr>{th}<td class="biz-name">・{name}</td>'
            f'<td class="biz-price">{price}</td>'
            f'<td class="biz-url"><a href="{url}" target="_blank" rel="noopener">{url}</a></td></tr>')
    rows.append('      </tbody>')
new_tbl = '<table class="tbl-clear biz-tbl">\n' + '\n'.join(rows) + '\n    </table>'
s = s[:start] + new_tbl + s[end:]

CSS = '''
/* ===== 10月修正 三校：ここから ===== */
/* 業務内容：業務と料金をそろえた表（区分は左ぞろえ、金額は右ぞろえ） */
table.biz-tbl{width:100%;border-collapse:separate;border-spacing:0 2px;font-size:14.5px;margin-top:6px;}
table.biz-tbl th,table.biz-tbl td{padding:8px 12px;text-align:left;vertical-align:middle;line-height:1.5;}
table.biz-tbl th.biz-cat{width:21%;background:#e3e6ea;font-weight:800;white-space:nowrap;border-right:2px solid #fff;}
table.biz-tbl td{background:#f2f4f6;}
table.biz-tbl td.biz-name{width:30%;}
table.biz-tbl td.biz-price{width:9%;text-align:right;white-space:nowrap;font-weight:700;font-variant-numeric:tabular-nums;border-right:2px solid #fff;}
table.biz-tbl td.biz-url{word-break:break-all;}
table.biz-tbl tbody.biz-group + tbody.biz-group tr:first-child > *{border-top:10px solid #fff;}
/* 761〜1023px：見本どおりの4列のまま、URLの文字を少し小さくして収める */
@media (min-width:761px) and (max-width:1023px){
  table.biz-tbl{font-size:13.5px;}
  table.biz-tbl th,table.biz-tbl td{padding:8px 8px;}
  table.biz-tbl th.biz-cat{width:20%;white-space:normal;}
  table.biz-tbl td.biz-name{width:28%;}
  table.biz-tbl td.biz-price{width:9%;}
  table.biz-tbl td.biz-url{font-size:12px;}
}
/* スマホ（760px以下）：区分を見出し行にし、左列＝業務名とURL、右列＝金額の2列の表（罫線あり） */
@media (max-width:760px){
  table.biz-tbl{display:block;width:100%;}
  table.biz-tbl tbody.biz-group{display:block;border:1px solid #c9ced4;margin-bottom:14px;}
  table.biz-tbl tbody.biz-group + tbody.biz-group tr:first-child > *{border-top:0;}
  table.biz-tbl tr{display:grid;grid-template-columns:1fr 64px;background:#f2f4f6;border-top:1px solid #c9ced4;}
  table.biz-tbl tr:first-child{border-top:0;}
  table.biz-tbl th.biz-cat{display:block;grid-column:1 / -1;width:auto;border-right:0;border-bottom:1px solid #c9ced4;padding:8px 12px;}
  table.biz-tbl td{display:block;width:auto!important;background:transparent;border-right:0!important;}
  table.biz-tbl td.biz-name{grid-column:1;padding:8px 8px 2px 12px;}
  table.biz-tbl td.biz-price{grid-column:2;grid-row:span 2;display:flex;align-items:center;justify-content:flex-end;padding:8px 12px 8px 4px;border-left:1px solid #c9ced4;}
  table.biz-tbl td.biz-url{grid-column:1;padding:0 8px 8px 12px;font-size:12px;line-height:1.45;}
}
/* ===== 10月修正 三校：ここまで ===== */
'''
rep('/* ===== 10月修正 再校：ここまで ===== */\n', '/* ===== 10月修正 再校：ここまで ===== */\n' + CSS)

open(dst, 'w', encoding='utf-8').write(s)
print('OK', len(s))
