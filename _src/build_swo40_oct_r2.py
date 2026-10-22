"""SWO40万円 商品LP10月修正 再校：初校 ver1.1（build_swo40_oct.py の出力）に、
10/22 佐藤様の初校戻し（pptx 3枚）を反映する。置換は件数を数え、期待値と違えば止める。
使い方：python3 build_swo40_oct.py base_sasaki_ver5.5wB.html v11.html
        python3 build_swo40_oct_r2.py v11.html ../index.html"""
import sys

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()


def rep(old, new, n=1):
    global s
    c = s.count(old)
    if c != n:
        sys.exit(f'COUNT {c} != {n}: {old[:80]!r}')
    s = s.replace(old, new)


rep('<!-- BUILD_TAG: swo2026_40venue_oct_ver1.1 / 2026-10-21 -->',
    '<!-- BUILD_TAG: swo2026_40venue_oct_ver2.0 / 2026-10-22 -->')

# ---- 1枚目：「スタンダードプラン 30万円」の枠を中央ぞろえ ----
rep('''      <span class="bl-name">ホームページをお持ちで、登録システムとカード決済をご希望の場合は　　　</span>
      <span class="bl-price">スタンダードプラン</span>
      <span class="bl-price">30万円　　　</span>''',
    '''      <span class="bl-name">ホームページをお持ちで、登録システムとカード決済をご希望の場合は</span>
      <span class="bl-plan"><span class="bl-price">スタンダードプラン</span><span class="bl-price">30万円</span></span>''')

# ---- 2・3枚目：実績表の支援内容を短い文言に（3枚目の表のとおり） ----
start = s.index('<table class="tbl works-tbl">')
end = s.index('</table>', start)
tbl = s[start:end]
n1 = tbl.count('開催案内ホームページ'); n2 = tbl.count('演題登録システム'); n3 = tbl.count('参加登録システム')
if (n1, n2, n3) != (12, 10, 15):
    sys.exit(f'支援内容の件数が想定と違う: {(n1, n2, n3)}')
tbl = tbl.replace('開催案内ホームページ', '開催案内').replace('演題登録システム', '演題登録').replace('参加登録システム', '参加登録')
s = s[:start] + tbl + s[end:]

CSS = '''
/* ===== 10月修正 再校：ここから ===== */
/* 1枚目：30万円の枠を中央ぞろえ */
.basic-link{flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:10px;}
.basic-link .bl-plan{display:flex;flex-wrap:wrap;justify-content:center;align-items:baseline;gap:0 14px;}
@media (max-width:760px){ .basic-link{align-items:center;} .basic-link .bl-btn{width:auto;min-width:200px;} }
/* 2枚目：年度の行の色 */
table.works-tbl tr.wk-group th{background:#E2F1F6;}
/* 2枚目：表はなるべく1行に。主催者は「日本ヘルスコミュニケーション学会」が1行に収まる大きさでそろえる */
@media (min-width:761px){
  table.works-tbl th.wk-name{width:31%;}
  table.works-tbl th.wk-sup{width:31%;}
  table.works-tbl th.wk-org{width:27%;}
  table.works-tbl th.wk-num{width:11%;}
  table.works-tbl td.wk-org{font-size:13px;white-space:nowrap;}
}
/* ===== 10月修正 再校：ここまで ===== */
'''
rep('/* ===== 10月修正：ここまで ===== */\n', '/* ===== 10月修正：ここまで ===== */\n' + CSS)

open(dst, 'w', encoding='utf-8').write(s)
print('OK', len(s))
