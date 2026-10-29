#!/usr/bin/env python3
"""Build the bilingual static site using Python 3 standard library only."""
from pathlib import Path
import html
import re
import json

ROOT = Path(__file__).resolve().parent
ORIGIN = 'https://nimble-rivet.github.io'
EMAIL = 'nimblerivet@gmail.com'

COPY = {
 'ru': {
  'lang_name':'Русский','other':'en','apps':'Приложения','about':'О студии','contact':'Написать нам','privacy':'Конфиденциальность','skip':'К содержимому',
  'title':'Nimble Rivet — приложения для повседневных дел',
  'description':'Retendly для повторяющихся дел, Listback для многоразовых чек-листов и Matcholio для игр с друзьями. Приложения Nimble Rivet для Android.',
  'eyebrow':'Независимая студия приложений',
  'headline':'Небольшие<br>приложения.<br><em>Больше порядка.</em>',
  'intro':'Повторяющиеся дела, привычные списки и результаты игр — всё на своём месте.',
  'explore':'Найти своё приложение','hello':'Связаться с нами','hero_note':'Продумано до мелочей',
  'built_for':'Для вашего Android. В вашем ритме.',
  'catalog_label':'Наши приложения','catalog_title':'На каждый день.<br>И на следующий.',
  'catalog_intro':'Для дел, к которым вы возвращаетесь. Для списков, которые пригодятся снова. Для игр, которые хочется запомнить.',
  'policy':'Политика конфиденциальности','screen':'Экран приложения','demo':'Демонстрационные данные',
  'availability':'Готовим приложения к публикации в магазинах. Вопросы о доступности и обратную связь можно отправить на нашу почту.',
  'about_label':'Nimble Rivet','about_title':'Внимание к тому,<br>из чего состоит день.',
  'about_body':'Nimble Rivet — независимая студия Android-приложений. Мы делаем инструменты для небольших, конкретных задач: вовремя вспомнить о деле, пройти знакомый список, сохранить результат игры.',
  'about_second':'В основе каждого приложения — понятный сценарий, к которому удобно возвращаться. А детали работы с данными описаны отдельно для каждого продукта.',
  'contact_label':'Давайте на связи','contact_title':'Есть вопрос<br>или идея?',
  'contact_body':'Расскажите, чего не хватает, что получилось хорошо или где что-то пошло не так. Нам важен ваш опыт.',
  'contact_hint':'Для вопроса об ошибке укажите приложение, модель устройства и версию Android.',
  'website_privacy':'Сайт и поддержка','back':'На главную','toc':'На этой странице','legal_label':'Прозрачно о данных',
  'legal_intro':'Как приложения и сайт Nimble Rivet работают с данными. Выберите нужную политику.',
  'legal_app':'Хранение, резервные копии и удаление данных приложения.',
  'legal_site':'GitHub Pages, посещение сайта и обращения по электронной почте.',
  'not_found':'Этой страницы нет','not_found_text':'Возможно, адрес изменился. Вернитесь на главную или откройте раздел конфиденциальности.'
 },
 'en': {
  'lang_name':'English','other':'ru','apps':'Apps','about':'About','contact':'Get in touch','privacy':'Privacy','skip':'Skip to content',
  'title':'Nimble Rivet — small apps for everyday life',
  'description':'Retendly for recurring reminders, Listback for reusable checklists, and Matcholio for games with friends. Android apps by Nimble Rivet.',
  'eyebrow':'Independent app studio',
  'headline':'Small apps.<br>Everyday life.<br><em>A little simpler.</em>',
  'intro':'Recurring tasks, familiar checklists and memorable games. A little space for everything.',
  'explore':'Find your app','hello':'Say hello','hero_note':'Thoughtful by design',
  'built_for':'For your Android. At your own pace.',
  'catalog_label':'Our apps','catalog_title':'For today.<br>And the next time.',
  'catalog_intro':'For the things you come back to. The lists you will use again. And the games you want to remember.',
  'policy':'Privacy policy','screen':'App preview','demo':'Demonstration data',
  'availability':'We are preparing our apps for release in app stores. Email us with availability questions or feedback.',
  'about_label':'Nimble Rivet','about_title':'Care for the details<br>that make up a day.',
  'about_body':'Nimble Rivet is an independent Android app studio. We build tools for small, specific tasks: remembering a recurring chore, working through a familiar checklist, and keeping the score of a game.',
  'about_second':'Each app starts with a clear purpose you can return to. How each product handles data is explained in its own privacy policy.',
  'contact_label':'Let’s stay in touch','contact_title':'A question<br>or an idea?',
  'contact_body':'Tell us what is missing, what worked well, or what went wrong. We would like to hear about your experience.',
  'contact_hint':'For a bug report, include the app name, device model and Android version.',
  'website_privacy':'Website & support','back':'Back to home','toc':'On this page','legal_label':'Clear about your data',
  'legal_intro':'How Nimble Rivet apps and this website handle data. Choose the policy you need.',
  'legal_app':'App data storage, backups and deletion.',
  'legal_site':'GitHub Pages, website visits and email support.',
  'not_found':'This page is missing','not_found_text':'The address may have changed. Visit the home page or explore the privacy policies.'
 }
}

APPS = [
 {'slug':'retendly','name':'Retendly','category':{'ru':'Повторяющиеся дела','en':'Recurring reminders'},
  'tagline':{'ru':'Вспомнить вовремя. И снова.','en':'Remember. Repeat. Relax.'},
  'description':{'ru':'Напоминания о делах, которые повторяются. Задайте интервал, отмечайте выполнение и держите историю под рукой.','en':'Reminders for the things you do again. Set a repeat interval, record completions, and keep the history close at hand.'},
  'features':{'ru':['Повторы по календарю или после выполнения','Уведомления, предупреждения заранее и виджет','История выполнения с датами и заметками'],'en':['Repeat by calendar or after completion','Notifications, advance reminders and a widget','Completion history with dates and notes']},
  'screen':{'ru':'retendly-screen.webp','en':'retendly-screen.webp'},'screen_lang':{'ru':'ru','en':'ru'}},
 {'slug':'listback','name':'Listback','category':{'ru':'Многоразовые чек-листы','en':'Reusable checklists'},
  'tagline':{'ru':'Знакомый список. Новый старт.','en':'A familiar list. A fresh start.'},
  'description':{'ru':'Соберите шаблон один раз и проходите его снова. Сборы в поездку, домашние дела или рабочие процедуры — у каждого запуска своя история.','en':'Create a template once and use it again. Packing for a trip, household chores or work routines — every run has its own history.'},
  'features':{'ru':['Шаблоны с разделами и инструкциями','Отметки, пропуски и заметки к прохождению','История и ручные резервные копии'],'en':['Templates with sections and instructions','Checkmarks, skipped items and notes','Run history and manual backups']},
  'screen':{'ru':'listback-screen-ru.webp','en':'listback-screen-en.webp'},'screen_lang':{'ru':'ru','en':'en'}},
 {'slug':'matcholio','name':'Matcholio','category':{'ru':'Игры с друзьями','en':'Games with friends'},
  'tagline':{'ru':'Каждая игра — в истории.','en':'Every match, remembered.'},
  'description':{'ru':'Выбирайте игроков и команды, записывайте победы и очки. Возвращайтесь к истории и статистике — или сразу сыграйте реванш.','en':'Choose players and teams, record wins and scores. Revisit your history and statistics — or go straight into a rematch.'},
  'features':{'ru':['Разные правила подсчёта результатов','Игроки, команды и собственные аватары','История, статистика и экспорт в ZIP'],'en':['Flexible scoring rules','Players, teams and custom avatars','History, statistics and ZIP backups']},
  'screen':{'ru':'matcholio-screen.webp','en':'matcholio-screen.webp'},'screen_lang':{'ru':'en','en':'en'}}
]

def route(lang, tail=''):

 if tail.endswith('.html'):return '/'+tail
 prefix='en-' if lang=='en' else ''
 if not tail:return '/en.html' if lang=='en' else '/'
 return '/'+prefix+tail.strip('/').replace('/','-')+'.html'

def inline(value):
 value=html.escape(value,quote=True)
 value=re.sub(r'https://[^\s<]+',lambda m:'<a href="'+m[0].rstrip('.,')+'">'+m[0].rstrip('.,')+'</a>'+m[0][len(m[0].rstrip('.,')):],value)
 value=re.sub(r'\*\*(.*?)\*\*',r'<strong>\1</strong>',value)
 value=re.sub(r'(?<![\w:/])nimblerivet@gmail\.com',f'<a href="mailto:{EMAIL}">{EMAIL}</a>',value)
 return value

def write(path,text):
 p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')

def shell(lang,tail,title,description,body,home=False):
 c=COPY[lang];r=route(lang);other=route(c['other'],tail);canonical=ORIGIN+route(lang,tail)
 language=''.join(f'<a href="{route(l,tail) if tail!='404.html' else route(l)}" lang="{l}" hreflang="{l}"'+(' aria-current="page"' if l==lang else '')+f'>{l.upper()}</a>'+('<span aria-hidden="true">/</span>' if l=='ru' else '') for l in ('ru','en'))
 schema={'@context':'https://schema.org','@type':'Organization','name':'Nimble Rivet','url':ORIGIN,'email':EMAIL,'logo':ORIGIN+'/brand.webp'} if home else None
 return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(description,quote=True)}">
<meta name="theme-color" content="#17272b"><link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="ru" href="{ORIGIN+route('ru',tail)}"><link rel="alternate" hreflang="en" href="{ORIGIN+route('en',tail)}"><link rel="alternate" hreflang="x-default" href="{ORIGIN+route('ru',tail)}">
<meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title,quote=True)}"><meta property="og:description" content="{html.escape(description,quote=True)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{ORIGIN}/social.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="675"><meta property="og:locale" content="{'ru_RU' if lang=='ru' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image"><link rel="icon" type="image/png" href="/favicon.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="stylesheet" href="/style.css">
{('<script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False)+'</script>') if schema else ''}
</head><body><a class="skip" href="#main">{c['skip']}</a>
<header class="site-header"><div class="wrap"><nav class="nav" aria-label="{'Основная навигация' if lang=='ru' else 'Main navigation'}">
<a class="brand-link" href="{r}" aria-label="Nimble Rivet — {c['back']}"><img src="/favicon.png" alt="" width="44" height="44">Nimble Rivet</a>
<div class="nav-links"><a href="{r}#apps">{c['apps']}</a><a class="nav-about" href="{r}#about">{c['about']}</a><a class="nav-contact" href="{r}#contact">{c['contact']}</a><div class="language" aria-label="{'Язык' if lang=='ru' else 'Language'}">{language}</div></div>
</nav></div></header>
{body}
<div class="wrap"><footer class="site-footer"><span><span class="footer-name">Nimble Rivet</span> &nbsp; © 2026</span><div class="footer-links"><a href="{route(lang,'privacy/')}">{c['privacy']}</a><a href="mailto:{EMAIL}">{EMAIL}</a><a href="https://github.com/Nimble-Rivet">GitHub ↗</a></div></footer></div></body></html>'''

def home(lang):
 c=COPY[lang];r=route(lang)
 mini=''.join(f'<a href="#{a["slug"]}"><img src="/{a["slug"]}.webp" alt="" width="23" height="23">{a["name"]}</a>' for a in APPS)
 cards=[]
 for i,a in enumerate(APPS,1):
  screen_note=('Интерфейс на английском' if a['screen_lang'][lang]=='en' else 'Интерфейс на русском') if lang=='ru' else ('Russian interface' if a['screen_lang'][lang]=='ru' else 'English interface')
  features=''.join(f'<li>{f}</li>' for f in a['features'][lang])
  cards.append(f'''<article class="app-showcase {a['slug']}" id="{a['slug']}" aria-labelledby="title-{a['slug']}">
<div class="app-copy"><div class="app-meta"><img class="app-icon" src="/{a['slug']}.webp" alt="" width="52" height="52" loading="lazy"><span class="app-number">0{i} / ANDROID</span></div><p class="category">{a['category'][lang]}</p><h3 id="title-{a['slug']}">{a['name']}</h3><p class="app-tagline">{a['tagline'][lang]}</p><p class="app-description">{a['description'][lang]}</p><ul class="features">{features}</ul><a class="text-link" href="{route(lang, 'privacy/'+a['slug']+'/')}">{c['policy']} <span aria-hidden="true">↗</span><span class="sr-only"> — {a['name']}</span></a></div>
<figure class="app-visual"><figcaption class="visual-label"><span>{c['screen']}</span><span>{a['name']}</span></figcaption><div class="phone"><img src="/{a['screen'][lang]}" alt="{a['name']}: {screen_note.lower()}. {c['demo']}." loading="lazy" width="540" height="{'960' if a['slug']=='matcholio' else '1200' if a['slug']=='retendly' else '960'}"></div></figure></article>''')
 body=f'''<main id="main"><section class="hero" aria-labelledby="hero-title"><div class="wrap"><div class="hero-grid"><div class="hero-copy"><div class="eyebrow"><span class="dot" aria-hidden="true"></span>{c['eyebrow']}</div><h1 id="hero-title">{c['headline']}</h1><p>{c['intro']}</p><div class="hero-actions"><a class="button" href="#apps">{c['explore']} <span class="arrow" aria-hidden="true">↗</span></a><a class="text-link" href="#contact">{c['hello']}</a></div></div><div class="hero-art" aria-hidden="true"><div class="orbit"></div><img class="brand-tile" src="/brand.webp" alt="" width="640" height="640" fetchpriority="high"><span class="art-note">{c['hero_note']}</span></div></div><div class="hero-bottom"><strong>{c['built_for']}</strong><div class="mini-apps">{mini}</div></div></div></section>
<div class="wrap"><section id="apps" aria-labelledby="apps-title"><div class="section-intro"><div><p class="eyebrow"><span class="dot" aria-hidden="true"></span>{c['catalog_label']}</p><h2 id="apps-title">{c['catalog_title']}</h2></div><p>{c['catalog_intro']}</p></div>{''.join(cards)}<p class="catalog-note"><span class="dot" aria-hidden="true"></span>{c['availability']}</p></section>
<section class="about" id="about" aria-labelledby="about-title"><div><p class="eyebrow">{c['about_label']}</p><h2 id="about-title">{c['about_title']}</h2></div><div class="about-body"><p>{c['about_body']}</p><p>{c['about_second']}</p><div class="signature"><span class="dot" aria-hidden="true"></span>Small apps for everyday life.</div></div></section>
<section class="contact" id="contact" aria-labelledby="contact-title"><div><p class="eyebrow"><span class="dot" aria-hidden="true"></span>{c['contact_label']}</p><h2 id="contact-title">{c['contact_title']}</h2><p>{c['contact_body']}</p></div><div class="contact-right"><a class="email-link" href="mailto:{EMAIL}">{EMAIL} <span aria-hidden="true">↗</span></a><p class="contact-hint">{c['contact_hint']}</p><a class="text-link" href="{route(lang,'privacy/site/')}">{c['website_privacy']}</a></div></section></div></main>'''
 write('en.html' if lang=='en' else 'index.html',shell(lang,'',c['title'],c['description'],body,True))

def render_policy(lang,slug):
 text=(ROOT/f'policy-{slug}.{lang}.md').read_text()
 blocks=re.split(r'\n\s*\n',text.strip());title=blocks.pop(0).lstrip('# ').strip();sections=[];content=[]
 for block in blocks:
  if block.startswith('## '):
   heading=block[3:].strip();anchor=f'section-{len(sections)+1}';sections.append((anchor,heading));content.append(f'<h2 id="{anchor}">{inline(heading)}</h2>')
  else:content.append('<p>'+inline(' '.join(block.splitlines()))+'</p>')
 c=COPY[lang];r=route(lang);tail=f'privacy/{slug}/'
 toc=''.join(f'<li><a href="#{anchor}">{html.escape(h)}</a></li>' for anchor,h in sections)
 body=f'''<main id="main"><div class="wrap"><section class="legal-hero"><a class="back-link" href="{route(lang,'privacy/')}">← {c['privacy']}</a><p class="eyebrow"><span class="dot" aria-hidden="true"></span>Nimble Rivet</p><h1>{html.escape(title)}</h1></section><div class="legal-layout"><aside class="legal-toc" aria-label="{c['toc']}"><strong>{c['toc']}</strong><ol>{toc}</ol></aside><article class="legal-content" aria-label="{html.escape(title,quote=True)}">{''.join(content)}</article></div></div></main>'''
 write(route(lang,tail).lstrip('/'),shell(lang,tail,title+' — Nimble Rivet',title+'. '+EMAIL,body))

def privacy_index(lang):
 c=COPY[lang];r=route(lang);cards=[]
 for slug,name in [(a['slug'],a['name']) for a in APPS]+[('site',c['website_privacy'])]:
  cards.append(f'<a class="policy-card" href="{route(lang, 'privacy/'+slug+'/')}"><h2>{name}</h2><p>{c["legal_site"] if slug=="site" else c["legal_app"]}</p><span class="arrow" aria-hidden="true">↗</span></a>')
 body=f'<main id="main"><div class="wrap"><section class="legal-hero"><a class="back-link" href="{r}">← {c["back"]}</a><p class="eyebrow"><span class="dot" aria-hidden="true"></span>{c["legal_label"]}</p><h1>{c["privacy"]}</h1><p class="legal-lead">{c["legal_intro"]}</p></section><div class="policy-grid">{"".join(cards)}</div></div></main>'
 write(route(lang,'privacy/').lstrip('/'),shell(lang,'privacy/',c['privacy']+' — Nimble Rivet',c['legal_intro'],body))

def main():
 for lang in ('ru','en'):
  home(lang);privacy_index(lang)
  for slug in ('retendly','listback','matcholio','site'):render_policy(lang,slug)
 c=COPY['ru'];body=f'<main id="main" class="wrap not-found"><p class="eyebrow">Nimble Rivet / 404</p><h1>{c["not_found"]}</h1><p>{c["not_found_text"]}</p><a class="button" href="/">{c["back"]} →</a><p lang="en" style="margin-top:24px">Page not found. <a href="/en.html">Visit the English home page</a>.</p></main>'
 error_page=shell('ru','404.html','Страница не найдена — Nimble Rivet',c['not_found_text'],body).replace('<meta name="theme-color"','<meta name="robots" content="noindex"><meta name="theme-color"').replace('href="/en/404.html"','href="/en.html"')
 error_page=re.sub(r'<link rel="alternate"[^>]*>','',error_page)
 write('404.html',error_page)
 urls=[ORIGIN+route(l,t) for l in ('ru','en') for t in ('','privacy/','privacy/retendly/','privacy/listback/','privacy/matcholio/','privacy/site/')]
 write('sitemap.xml','<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('<url><loc>'+u+'</loc></url>\n' for u in urls)+'</urlset>\n')
 write('robots.txt','User-agent: *\nAllow: /\nSitemap: '+ORIGIN+'/sitemap.xml\n')
 write('.nojekyll','')
 print('Built 12 pages and 404.html, sitemap.xml, robots.txt.')

if __name__=='__main__':main()
