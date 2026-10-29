#!/usr/bin/env python3
"""Check generated pages, internal navigation and production assets."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as ET
import re

ROOT=Path(__file__).resolve().parent
DOMAIN='nimble-rivet.github.io'

class Page(HTMLParser):
 def __init__(self,text):
  super().__init__(convert_charrefs=True)
  self.ids=set();self.duplicate_ids=[];self.refs=[];self.h1=0;self.lang=None;self.images=[];self.runtime_scripts=[]
  self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):
   if a['id'] in self.ids:self.duplicate_ids.append(a['id'])
   self.ids.add(a['id'])
  if tag=='html':self.lang=a.get('lang')
  if tag=='h1':self.h1+=1
  if tag=='img':self.images.append(a)
  if tag=='script' and a.get('type')!='application/ld+json':self.runtime_scripts.append(a)
  for k in ('href','src'):
   if k in a:self.refs.append(a[k])

def target(url,page):
 u=urlsplit(url)
 if u.scheme in ('mailto','tel','data'):return None,None
 if u.netloc and u.netloc!=DOMAIN:return None,None
 path=unquote(u.path)
 p=ROOT/path.lstrip('/') if path.startswith('/') else page.parent/path if path else page
 if p.is_dir():p=p/'index.html'
 return p,u.fragment

def main():
 pages={p:Page(p.read_text()) for p in ROOT.rglob('*.html') if '.git' not in p.parts}
 errors=[];checked=0
 for p,page in pages.items():
  label=str(p.relative_to(ROOT))
  if page.h1!=1:errors.append(f'{label}: expected one h1, got {page.h1}')
  if page.lang not in ('ru','en'):errors.append(f'{label}: missing language')
  if page.duplicate_ids:errors.append(f'{label}: duplicate IDs {page.duplicate_ids}')
  if page.runtime_scripts:errors.append(f'{label}: unexpected runtime JavaScript')
  for im in page.images:
   if 'alt' not in im:errors.append(f'{label}: image without alt')
  for ref in page.refs:
   dest,anchor=target(ref,p)
   if dest is None:continue
   checked+=1
   if not dest.exists():errors.append(f'{label}: missing {ref}')
   elif anchor and dest in pages and anchor not in pages[dest].ids:errors.append(f'{label}: missing fragment {ref}')
 for item in ET.parse(ROOT/'sitemap.xml').getroot():
  url=item.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
  dest,_=target(url,ROOT/'index.html')
  if not dest or not dest.exists():errors.append(f'sitemap: missing {url}')
 css=(ROOT/'style.css').read_text()
 for value in re.findall(r'url\([\'\"]?([^\)\'\"]+)',css):
  if not (ROOT/value).is_file():errors.append(f'CSS asset missing: {value}')
 for lang in ('ru','en'):
  for app in ('retendly','listback','matcholio','site'):
   p=ROOT/(('en-' if lang=='en' else '')+'privacy-'+app+'.html')
   source=p.read_text()
   for required in ('Nimble Rivet','nimblerivet@gmail.com'):
    if required not in source:errors.append(f'{p.relative_to(ROOT)}: missing {required}')
 if len(pages)!=13:errors.append(f'Expected 13 HTML pages; got {len(pages)}')
 if errors:raise SystemExit('\n'.join(errors))
 print(f'PASS: {len(pages)} pages; {checked} internal links/assets; sitemap, image descriptions, policies, language attributes and headings.')

if __name__=='__main__':main()
