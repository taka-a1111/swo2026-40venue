"""SWO40万円 商品LP10月修正：佐々木様共有の現状HTML（ver5.5wB）に修正原稿①〜104を反映する。
置換は件数を数え、期待値と違えば止める。"""
import sys, re

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()


def rep(old, new, n=1):
    global s
    c = s.count(old)
    if c != n:
        sys.exit(f'COUNT {c} != {n}: {old[:80]!r}')
    s = s.replace(old, new)


MAIL_HREF = 'mailto:swo-mail@science-web.online?subject=%E3%83%A1%E3%83%BC%E3%83%AB%E7%9B%B8%E8%AB%87%E3%81%8A%E7%94%B3%E8%BE%BC%E3%81%BF'
ZOOM_HREF = 'mailto:swo-zoom@science-web.online?subject=Zoom%E7%9B%B8%E8%AB%87%E3%81%8A%E7%94%B3%E8%BE%BC%E3%81%BF&amp;body=%E3%81%94%E5%B8%8C%E6%9C%9B%E6%97%A5%E6%99%82%EF%BC%88%E7%AC%AC3%E5%B8%8C%E6%9C%9B%E3%81%BE%E3%81%A7%EF%BC%89%EF%BC%9A%0D%0A%0D%0A%E3%81%94%E6%89%80%E5%B1%9E%EF%BC%9A%0D%0A%E3%81%8A%E5%90%8D%E5%89%8D%EF%BC%9A%0D%0A'
BTN3 = ('<div class="btns" style="margin-top:26px;">\n'
        f'      <a class="btn btn-contact" href="{MAIL_HREF}">メールで相談する</a>\n'
        f'      <a class="btn btn-zoom" href="{ZOOM_HREF}">Zoom相談を申し込む</a>\n'
        '      <a class="btn btn-tel" href="tel:050-3538-7006">電話　050-3538-7006<small>（平日10時〜15時）</small></a>\n'
        '    </div>')

# ---- BUILD_TAG ----
rep('<!-- BUILD_TAG: swo2026_40venue_ver5.5wB / 2026-08-18 -->',
    '<!-- BUILD_TAG: swo2026_40venue_oct_ver1.0 / 2026-10-21 -->')

# ---- ①-2 メニュー ----
rep('<li><a href="#price40">40万円</a></li>', '<li><a href="#price40">プラン内容</a></li>')

# ---- ③④ ヒーロー価格 ----
rep('<div class="p"><span class="p-pre">基本</span><span class="p-num">40</span><span class="p-unit">万円</span></div>\n          <div class="p-tax">（消費税　含みません）</div>',
    '<div class="p"><span class="p-pre">基本料金</span><span class="p-num">40</span><span class="p-unit">万円</span></div>\n          <div class="p-tax">（税別）</div>')

# ---- ⑤-2 スライドショー画像3枚 ＋ ⑥ ボタン3つ ----
rep('''      <img src="images/hall.png" alt="学会会場の様子" class="on">
      <img src="images/presentation.png" alt="質疑応答の様子">
      <img src="images/lecture.png" alt="公演の様子">
    </div>''' + '    ' + '''
  </div>''',
    '''      <img src="images/metaverse-entrance.png" alt="メタバース学会の会場入口" class="on">
      <img src="images/professor-lecture.png" alt="品格ある教授の学術講演">
      <img src="images/metaverse-meeting.png" alt="第12回メタバース学会の打ち合わせ">
    </div>
    ''' + BTN3.replace('margin-top:26px', 'margin-top:20px') + '''
  </div>''')

# ---- ⑦〜⑪ お悩み ----
rep('<h2 class="sec-ttl">大会長・組織委員長　お悩みですか</h2>', '<h2 class="sec-ttl">大会長・組織委員長の皆さま、こんなお悩みはありませんか？</h2>')
rep('ホームページ・演題登録・参加登録を、別々に準備している', 'ホームページ・登録システムをまとめて準備したい')
rep('<span style="color: #000000;">短期間で公開しなければならない</span>', '<span style="color: #000000;">開催案内ホームページの公開まで時間がない</span>')
rep('運営委員は、国内あちこちに。<br>国際委員は、世界のアチコチに', '委員が国内外に分散しており、連絡・調整に手間がかかる')
rep('海外招へい費用、協賛金、懇親会の会場予約、研究施設訪問', '海外招へい・協賛金の募集・懇親会・施設訪問など、手配することが多い')

# ---- ⑫⑬ 青枠 ／ ⑭ ボタン削除 ----
rep('<p class="answer-ttl"><span style="color: #ffffff;">開催準備の作業と負担をまとめて軽減します</span></p>\n      <p class="answer-txt"><span style="color: #ffffff;">学会準備にて必要な機能を、最初からセットアップします。<br>学会開催前も、閉会後も。</span></p>',
    '<p class="answer-ttl"><span style="color: #ffffff;">ホームページと登録システムを、ひとつの窓口で</span></p>\n      <ul class="answer-list">\n        <li><span style="color: #ffffff;">開催案内ホームページを制作</span></li>\n        <li><span style="color: #ffffff;">演題登録・参加登録・カード決済を用意</span></li>\n        <li><span style="color: #ffffff;">公開後の修正・更新にも対応</span></li>\n      </ul>')
rep('''    </div>

    <div class="btns two" style="margin-top:26px;">
      <a class="btn btn-contact" href="''' + MAIL_HREF + '''">メール相談お申込み</a>
      <a class="btn btn-zoom" href="''' + ZOOM_HREF + '''">Zoom相談お申込み<small></a>
    </div>
  </div>
</section>''', '''    </div>
  </div>
</section>''')

# ---- ⑮〜27 プラン表 ----
rep('<h2 class="sec-ttl" id="sec-price40">必要な開催案内を、まとめて制作・準備します</h2>', '<h2 class="sec-ttl" id="sec-price40">40万円プランに含まれる内容</h2>')
rep('<span style="color: #000000;">10画面</span>', '<span style="color: #000000;">ナビゲーション10項目まで</span>')
rep('<tr><th>演題登録フォーム</th><td><span style="color: #000000;">アブストラクト受付・収集</span></td></tr>',
    '<tr><th>演題登録システム</th><td><span style="color: #000000;">抄録の受付・収集</span></td></tr>')
rep('<tr><th>参加登録フォーム</th><td><span style="color: #000000;">本人・懇親会・見学・同行者</span></td></tr>',
    '<tr><th>参加登録システム</th><td><span style="color: #000000;">懇親会・見学・同行者の登録</span></td></tr>')
rep('ＶＩＳＡ・ＭＡＳＴＥＲ・ＪＣＢ・ほか', 'Visa・Mastercard・JCBなど')
rep('<span style="color: #000000;">ＣＭＳ・アクセス解析</span>', '<span style="color: #000000;">スマートフォンでの閲覧・操作に対応</span>')
rep('<tr><th>登録者マイページ</th><td><span style="color: #000000;">管理画面・２段階認証</span></td></tr>',
    '<tr><th>登録者マイページ<br>管理画面</th><td><span style="color: #000000;">2段階認証</span></td></tr>')
rep('<li>アクセス解析　公開から６か月間</li>', '<li>アクセス解析　公開から6か月間</li>')
rep('<li>ドメイン　　　発注から閉会後２か月間まで利用</li>\n          <li>サーバ</li>',
    '<li>ドメイン　　　発注から閉会後2か月まで利用可能</li>\n          <li>サーバ　　　　発注から閉会後2か月まで利用可能</li>')

# ---- 28 スタンダードプラン導線 ----
rep('<span class="bl-name">演題登録・参加登録フォームのみでOKなら　　　</span>',
    '<span class="bl-name">ホームページをお持ちで、登録システムとカード決済をご希望の場合は　　　</span>')

# ---- 29〜39 追加業務 ----
rep('<h3 class="box-ttl">追加できます　業務委託</h3>', '<h3 class="box-ttl">追加でご依頼いただける業務</h3>')
rep('<tr><th>保守管理業務委託契約</th><td class="num">10,000円／月</td><td><span style="color: #000000;">サーバ管理・メール保守。</span>',
    '<tr><th>保守管理</th><td class="num">月額10,000円</td><td><span style="color: #000000;">サーバー管理・メール保守</span>')
rep('<tr><th>運用代行業務委託契約</th><td class="num">10,000円／月</td><td><span style="color: #000000;">メール対応（登録者・主催者）</span>',
    '<tr><th>運用代行</th><td class="num">月額10,000円</td><td><span style="color: #000000;">開催案内ホームページの修正・更新</span>')
rep('<tr><th>その他。更新・技術作業</th><td class="num">ご相談ください</td><td>&nbsp;</td></tr>',
    '<tr><th>オンライン事務局</th><td class="num">月額35,000円から</td><td><span style="color: #000000;">メール対応（参加者／投稿者）・支払い管理など</span><a class="bl-btn" href="https://science-web.online/online-secretariat/" target="_blank" rel="noopener">詳しくはこちら</a></td></tr>')

# ---- 40〜48 基本料金に含まれます ----
rep('''      <h3 class="box-ttl">無料です</h3>
      <ul class="free">
        <li><span style="font-size: 1.5rem;">テキスト修正は、</span><b>月３件</b></li>
        <li><span style="font-size: 1.5rem;">画像と表の更新は、</span><b>月３件</b></li>
        <li><span style="font-size: 1.5rem;">Zoomご相談は、</span><b>月３回</b></li>
      </ul>
    </div>''', '''      <h3 class="box-ttl">基本料金に含まれます</h3>
      <ul class="free">
        <li><span style="font-size: 1.5rem;">テキスト修正：</span><b>月3件まで</b></li>
        <li><span style="font-size: 1.5rem;">画像・表の更新：</span><b>月3件まで</b></li>
        <li><span style="font-size: 1.5rem;">Zoom相談：</span><b>月3回まで</b></li>
      </ul>
      <p class="free-note">※テキスト修正、画像・表の更新は、いずれも1件あたりの作業時間が30分以内のものが対象です。</p>
    </div>
    <p class="free-lead">担当者が交代した場合も、修正内容をお知らせいただければ、引き続きSWOが対応します。</p>''')

# ---- 49〜54・82〜87 書類ボタン（2か所） ----
rep('<button class="btn btn-quote" data-open="m-basic">基本見積書<br>ダウンロード<small>その場で作成・印刷</small></button>',
    '<button class="btn btn-quote" data-open="m-basic">基本見積書をダウンロード<small>PDF保存・印刷に対応</small></button>', 2)
rep('<button class="btn btn-quote2" data-open="m-ref">最適見積書<br>ダウンロード<small>希望項目を含めて計算</small></button>',
    '<button class="btn btn-quote2" data-open="m-ref">最適見積書をダウンロード<small>ご希望に応じた見積金額を確認できます</small></button>', 2)
rep('<button class="btn btn-order" data-open="m-order">仕様書・発注書・請書<small>入力してそのまま送信</small></button>',
    '<button class="btn btn-order" data-open="m-order">発注書<small>必要事項を入力して送信できます</small></button>', 2)

# ---- 55 「制作と公開で終わり」〜その解決策 を削除 ----
rep('''    <h2 class="sec-ttl" id="sec-faq">「制作と公開で終わり」ではありません</h2>

    <h3 class="sub-ttl">よくある失敗</h3>
    <ul class="worries">
      <li><span style="color: #000000;">学生・ポスドク任せで、卒業・異動後に更新が止まる</span></li>
      <li><span style="color: #000000;">秘書・事務局スタッフの交代後、誰も更新できない</span></li>
      <li><span style="color: #000000;">外部に外注したが、運用しにくい設計になっている</span></li>
    </ul>

    <h3 class="sub-ttl">その解決策</h3>
    <ul class="points">
      <li>ＣＭＳスタイル<span>誰でも引き継げます。</span></li>
      <li>更新・管理<span>専門知識なしでもＯＫ。</span></li>
      <li>保守管理・運用代行<span>公開後も業務委託が可能です。</span></li>
    </ul>

    <h3 class="sub-ttl">よくあるご質問</h3>''', '''    <h3 class="sub-ttl faq-ttl" id="sec-faq">よくあるご質問</h3>''')

# ---- 55〜64 FAQ ----
FAQ = [
    ('開催内容や予算が決まっていなくても相談できますか？',
     'はい。開催内容や予算が未確定の段階でもご相談いただけます。<br>開催時期、参加予定人数、現在の準備状況など、分かる範囲でお知らせください。<br>必要な機能やご予算を伺い、準備の進め方をご提案します。'),
    ('開催まで時間がありません。今からでも依頼できますか？',
     '入稿完了から3週間での公開を基本としています。<br>ご希望の内容や原稿の準備状況によって対応可能な日程が異なりますので、<br>まずは開催日とご希望の公開日をお知らせください。'),
    ('ホームページがある場合や、一部だけ依頼したい場合も相談できますか？',
     'はい。すでに準備されている内容と、依頼したい作業をお知らせください。<br>既存のホームページを活用し、演題登録・参加登録フォームとカード決済を導入する場合は、30万円プランをご案内できます。<br>一部の作業についても、内容を伺って対応範囲をご案内します。'),
    ('公開後の更新は、料金に含まれていますか？',
     'はい。ホームページのテキスト修正は月3件まで、画像・表の更新は月3件まで基本料金に含まれます。<br>いずれも、1件あたりの作業時間が30分以内のものが対象です。'),
    ('参加者からの問い合わせ対応も依頼できますか?',
     'はい。参加者からの問い合わせ対応や案内メールの送信などは、別途契約のオンライン事務局で承ります。<br>負担になっている作業をお知らせください。対応範囲と費用をご案内します。'),
]
old_qa = '''    <dl class="qa">
      <dt>どのくらいで公開できますか？</dt>
      <dd>入稿完了から３週間での公開を基本としています。</dd>
      <dt>担当者が交代しても大丈夫ですか？</dt>
      <dd>どなたでも引き継げるＣＭＳにて制作します。</dd>
      <dt>公開後も更新できますか？</dt>
      <dd>ＣＭＳで更新・管理できます。納品の際に「ＣＭＳガイド」を提供いたします。保守管理・運用代行も別途契約可能です。</dd>
      <dt>基本費用40万円以外の費用は？</dt>
      <dd>ほとんどは含まれております。カード決済手数料、消費税、などは別です。保守管理・運用代行は別途契約にてご案内します。</dd>
    </dl>'''
new_qa = '    <dl class="qa">\n' + ''.join(f'      <dt>{q}</dt>\n      <dd>{a}</dd>\n' for q, a in FAQ) + '    </dl>'
rep(old_qa, new_qa)

# FAQ の構造化データも表示内容に合わせる
import json
m = re.search(r'(<script type="application/ld\+json">\s*)(\{\s*"@context": "https://schema.org",\s*"@type": "FAQPage".*?\n\})(\s*</script>)', s, re.S)
if not m:
    sys.exit('FAQ JSON-LD not found')
ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a.replace('<br>', '')}} for q, a in FAQ]}
s = s[:m.start(2)] + json.dumps(ld, ensure_ascii=False, indent=2) + s[m.end(2):]

# ---- 65・102 ボタン3つ（FAQ下・業務内容下） ----
old2 = ('<div class="btns two" style="margin-top:26px;">\n'
        f'      <a class="btn btn-contact" href="{MAIL_HREF}">メール相談お申込み</a>\n'
        f'      <a class="btn btn-zoom" href="{ZOOM_HREF}">Zoom相談お申込み</a>\n'
        '    </div>')
rep(old2, BTN3, 2)

# ---- 66〜74 実績の数字 ----
rep('<p class="sec-desc">1997年から国際シンポジウムと学会開催を支援。研究者をサポートしています。</p>',
    '<p class="sec-desc works-desc">1997年から、国際シンポジウムや学会の開催を支援しています。</p>')
rep('<div class="st-num">30<span>件以上</span></div>\n        <div class="st-lbl">年間の学会開催実績</div>',
    '<div class="st-num"><span class="st-pre">年間</span>30<span>件以上</span></div>\n        <div class="st-lbl">学会開催を支援</div>')
rep('<div class="st-num">3<span>週間</span></div>\n        <div class="st-lbl">入稿完了から公開まで</div>',
    '<div class="st-num">130<span>機関</span></div>\n        <div class="st-lbl">大学・研究機関での導入実績</div>')

# ---- 75 実績表：1つの表に統合、支援内容を追加、開催済みと受託・準備中に分ける、リンク削除 ----
a = s.find('    <!-- 開催実績テーブル -->')
b = s.find('    <!--<h3 class="sub-ttl">直近の学会開催</h3>')
if a < 0 or b < 0 or b < a:
    sys.exit('works table range not found')
HP, EN, SA, CA = '開催案内ホームページ', '演題登録システム', '参加登録システム', 'カード決済'
groups = [
    ('2023年度の支援案件', [
        ('APN2023', [HP, SA, CA], 'Asian Pharmacometrics Network', '約100名'),
        ('10th MDM2', [HP, EN, SA, CA], '10th MDM2　組織委員会', '約200名'),
        ('第46回日本小児遺伝学会学術集会', [HP, EN, SA, CA], '日本小児遺伝学会', '約200名'),
        ('ヘルスコミュニケーションウィーク2023', [SA, CA], '日本ヘルスコミュニケーション学会', '約200名'),
    ]),
    ('2024年度の支援案件', [
        ('4thIAS', [EN, SA], '国際スポートロジー学会', '約500名'),
        ('ISMOM2024', [HP, EN, SA, CA], '国際土壌科学連合', '約200名'),
        ('頭頚部がん治療と就労の両立支援のためのシンポジウム', [HP, SA], '東京都保健医療局', '約100名'),
    ]),
    ('2025年度の支援案件', [
        ('第67回日本平滑筋学会総会', [HP, EN, SA, CA], '日本平滑筋学会', '約150名'),
    ]),
    ('2026年度の支援案件', [
        ('第38回日本軟骨代謝学会', [HP, EN, SA, CA], '日本軟骨代謝学会', '約300名'),
        ('FJC2026', [SA, CA], 'FJC2026　組織委員会', '約100名'),
        ('WASCON2026', [HP, EN, SA, CA], 'WASCON2026　組織委員会', '約150名'),
        ('ISAM5', [HP, EN, SA, CA], 'ISAM5　組織委員会', '約100名'),
    ]),
    ('受託・準備中の案件', [
        ('第24回日本機能性食品医用学会総会', [HP, SA, CA], '日本機能性食品医用学会', '約200名'),
        ('ICCDU2027', [HP, EN, SA, CA], 'ICCDU2027　組織委員会', '約400名'),
        ('PhotoIUPAC2028', [HP, EN, SA, CA], 'PhotoIUPAC2028　組織委員会', '約600名'),
    ]),
]
rows = []
for g, items in groups:
    rows.append(f'      <tr class="wk-group"><th colspan="4">{g}</th></tr>')
    for name, sup, org, num in items:
        rows.append(f'      <tr><td class="wk-name">{name}</td><td class="wk-sup">{"／".join(sup)}</td><td class="wk-org">{org}</td><td class="wk-num">{num}</td></tr>')
works = ('    <!-- 支援実績テーブル（10月修正：1つの表にまとめ、支援内容を追加） -->\n'
         '    <table class="tbl works-tbl">\n'
         '      <thead><tr><th class="wk-name">開催名</th><th class="wk-sup">支援内容</th><th class="wk-org">主催者</th><th class="wk-num">参加者数</th></tr></thead>\n'
         '      <tbody>\n' + '\n'.join(rows) + '\n      </tbody>\n    </table>\n'
         '    <p class="works-note">掲載している案件は、掲載許可をいただいた支援実績・受託案件の一部です。掲載していない案件もあります。</p>\n\n')
s = s[:a] + works + s[b:]

# ---- 76〜81 ご相談カード ----
rep('''        <div class="tc-ttl">ご相談ください</div>
        <p>学会名、開催時期、開催都市、参加予定人数、必要な登録機能、など、分かる範囲で</p>''',
    '''        <div class="tc-ttl">分かる範囲でお知らせください。</div>
        <p>・学会・大会名、開催時期、開催都市<br>・参加予定人数、ご希望の登録機能</p>''')
rep('''        <div class="tc-ttl">お教えください</div>
        <p>お困りごと、心配なこと、現在の準備状況、前回開催、など</p>''',
    '''        <div class="tc-ttl">ご相談ください</div>
        <p>お困りごとやご不安な点、現在の準備状況、前回開催時の課題をご相談ください。</p>''')
rep('''        <div class="tc-ttl">これ大丈夫です</div>
        <p>予算案作成、海外招へい、懇親会の会場予約、協賛金の募集、など</p>''',
    '''        <div class="tc-ttl">お任せください</div>
        <p>予算案の作成、海外からの招へい、懇親会の会場予約、協賛金の募集など</p>''')

# ---- 88〜101 業務内容 ----
rep('<td style="width: 30%;">・研究室  ５万円</td>', '<td style="width: 30%;">・研究室ホームページ 5万円（LP3ページ）</td>')
rep('<td>・研究室  20万円</td>', '<td>・研究室ホームページ 20万円（LP10ページ）</td>')
rep('<td>・学会   20万円</td>', '<td>・学会ホームページ 20万円（LP10ページ）</td>')
rep('<td>・研究費  20万円</td>', '<td>・研究費ホームページ 20万円（LP10ページ）</td>')
rep('開発　Webアプリ</th>', '開発　Webシステム</th>')
rep('<td style="padding-top: 24px;">・論文投稿 ５万円</td>', '<td style="padding-top: 24px;">・論文投稿システム 5万円（査読機能／マイページ・なし）</td>')
rep('<td>・論文投稿 20万円</td>', '<td>・論文投稿システム 20万円（査読機能なし）</td>')
rep('<td>・紀要管理 30万円</td>', '<td>・紀要管理システム 30万円（査読機能なし）</td>')
rep('<td>・役員選挙 20万円</td>', '<td>・役員選挙システム 20万円（選挙機能なし）</td>')
rep('<td>・学会事務 20万円</td>', '<td>・学会事務システム 20万円（会費徴収なし）</td>')
rep('<th rowspan="2" style="padding-top: 24px;">開発　会議開催サポート</th>', '<th rowspan="3" style="padding-top: 24px;">開発　会議開催サポート</th>')
rep('<td style="padding-top: 24px;">・フォーム 30万円</td>', '<td style="padding-top: 24px;">・演題登録・参加登録システム 30万円</td>')
rep('''        <td>・開催案内 40万円</td>
        <td style="word-break: break-all;"><a href="https://science-web.online/40venue" target="_blank" rel="noopener">https://science-web.online/40venue</a></td>
      </tr>''', '''        <td>・開催案内 ＋登録システム2点 40万円</td>
        <td style="word-break: break-all;"><a href="https://science-web.online/40venue" target="_blank" rel="noopener">https://science-web.online/40venue</a></td>
      </tr>
      <tr>
        <td>・オンライン事務局</td>
        <td style="word-break: break-all;"><a href="https://science-web.online/online-secretariat/" target="_blank" rel="noopener">https://science-web.online/online-secretariat/</a></td>
      </tr>''')

# 業務内容の表：文字が増えたので列幅を調整（中央の列が折り返さないように）
rep('<th rowspan="4" style="width: 25%;">制作　Webサイト</th>', '<th rowspan="4" style="width: 18%;">制作　Webサイト</th>')
rep('<td style="width: 30%;">・研究室ホームページ 5万円（LP3ページ）</td>', '<td style="width: 44%;">・研究室ホームページ 5万円（LP3ページ）</td>')
rep('<td style="width: 45%; word-break: break-all;"><a href="https://science-web.co.jp/lab.trial/"', '<td style="width: 38%; word-break: break-all;"><a href="https://science-web.co.jp/lab.trial/"')

# 書類（見積書・発注書）内の電話受付時間もフッターに合わせる（103と同じ事実の変更）
rep("+'（平日10時〜16時）", "+'（平日10時〜15時）", 2)

# ---- 103・104 フッター ----
rep('<a href="tel:050-3538-7006">050-3538-7006</a>（平日10時〜16時）', '<a href="tel:050-3538-7006">050-3538-7006</a>（平日10時〜15時）')
rep('<p class="ft-copy">＠SWC　Science Web Corp.</p>', '<p class="ft-copy">＠SWO　Science Web Corp.</p>')

# ---- CSS（10月修正分は末尾に追記） ----
CSS = '''
/* ===== 10月修正（2026-10）：ここから ===== */
/* ① サブ見出しを2倍 */
.hero h1 .sub{font-size:28px;letter-spacing:.06em;line-height:1.5;}
/* ② ⑤ 価格カードの見出し（左右とも2倍・同じ大きさ） */
.hero-card .n,.hero-card .hc-right .n{font-size:24px;letter-spacing:.08em;}
/* ③ 「基本料金」「万円」は数字より一回り小さく ／ ⑤ 右側も左側と同じ大きさに */
.hero-card .p-pre{font-size:26px;}
.hero-card .p-unit,.hero-card .hc-right .p-unit{font-size:34px;}
.hero-card .hc-right .p-num{font-size:92px;}
.hero-card .p-tax,.hero-card .hc-right .p-tax{font-size:14px;margin-top:8px;}
/* ⑤-2 スライドショー：支給画像（16:9）が切れない比率 */
.media-slot{aspect-ratio:1672/941;}
@media (max-width:760px){ .media-slot{aspect-ratio:1672/941;} }
/* ⑥ 電話ボタン */
.btn-tel{background:#fff;color:var(--navy);border:2px solid var(--navy);}
.btn-tel small{font-size:13px;font-weight:700;}
/* ⑫ ⑬ 青枠を大きく、文字も大きく */
.answer-box{padding:44px 40px;}
.answer-ttl{font-size:30px;line-height:1.5;margin:0 0 18px;}
.answer-list{list-style:none;margin:0 auto;padding:0;display:inline-block;text-align:left;}
.answer-list li{font-size:20px;font-weight:700;line-height:1.9;padding-left:1.2em;position:relative;}
.answer-list li::before{content:"・";position:absolute;left:0;color:#fff;}
/* 47 小さめの注記 ／ 48 大きめの一文 */
.free-note{font-size:12.5px;margin:14px 0 0;line-height:1.7;}
.free-lead{font-size:22px;font-weight:800;color:var(--navy-ink);text-align:center;line-height:1.6;margin:28px 0 0;}
/* 66〜74 実績の数字・説明を約1.2倍 */
.works-desc{font-size:17.5px;}
.st-num{font-size:62px;}
.st-lbl{font-size:15px;}
.st-num .st-pre{margin-left:0;margin-right:6px;}
/* 75 支援実績の表 */
table.works-tbl{margin-top:8px;}
table.works-tbl th.wk-name{width:28%;}
table.works-tbl th.wk-sup{width:36%;}
table.works-tbl th.wk-org{width:24%;}
table.works-tbl th.wk-num{width:12%;white-space:nowrap;}
table.works-tbl td{white-space:normal;}
table.works-tbl td.wk-num{white-space:nowrap;}
table.works-tbl tr.wk-group th{background:#FDE5DA;font-weight:800;}
.works-note{font-size:13px;margin:12px 0 0;}
/* 104 フッターの黒い文字を白に */
footer p,footer .ft-line,footer .ft-copy,footer .ft-brand{color:#fff !important;opacity:1;}
@media (max-width:760px){
  .hero h1 .sub{font-size:20px;}
  .hero-card .n,.hero-card .hc-right .n{font-size:20px;}
  .hero-card .p-num,.hero-card .hc-right .p-num{font-size:76px;}
  .hero-card .p-pre{font-size:22px;}
  .hero-card .p-unit,.hero-card .hc-right .p-unit{font-size:28px;}
  .answer-box{padding:32px 20px;}
  .answer-ttl{font-size:22px;}
  .answer-list li{font-size:16.5px;}
  .free-lead{font-size:18px;}
  .st-num{font-size:52px;}
  table.works-tbl thead{display:none;}
  table.works-tbl tr.wk-group th{display:block;}
  table.works-tbl td.wk-name{font-weight:800;}
  table.works-tbl td.wk-org::before{content:"主催者：";font-weight:700;}
  table.works-tbl td.wk-num::before{content:"参加者数：";font-weight:700;}
  table.works-tbl td.wk-sup::before{content:"支援内容：";font-weight:700;}
  table.works-tbl td{border-top:0;border-bottom:0;padding:3px 14px;}
  table.works-tbl td.wk-name{padding-top:14px;}
  table.works-tbl td.wk-num{padding-bottom:14px;border-bottom:1px solid var(--rule);}
}
/* ===== 10月修正：ここまで ===== */
'''
rep('</style>', CSS + '</style>')

open(dst, 'w', encoding='utf-8').write(s)
print('OK', len(s))
