#!/usr/bin/env python3
"""Check local documentation navigation. Run with --write-nav to refresh contents."""
import argparse
import collections
import html
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

def mask(source):
    """Preserve offsets while ignoring comments and fenced examples."""
    return re.sub(r'<!--.*?-->|^[ \t]*(`{3,}|~{3,})[^\n]*\n.*?^[ \t]*\1[^\n]*$',
                  lambda m: ''.join('\n' if c == '\n' else ' ' for c in m.group()),
                  source, flags=re.S | re.M)

def plain(value):
    return html.unescape(re.sub(r'<[^>]+>|[*`]', '', re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', value))).strip()

def slug(value):
    value=plain(value).lower()
    return ''.join(c for c in value if c.isalnum() or c in ' _-').replace(' ', '-')

def headings(source):
    clean=mask(source)
    pattern=r'^ {0,3}(#{1,6})[ \t]+([^\n]+)|<h([1-6])\b[^>]*>(.*?)</h\3>'
    return [(m.start(),int(m[3]) if m[3] else len(m[1]),plain(m[4] if m[3] else m[2].rstrip('# ')))
            for m in re.finditer(pattern,clean,re.M | re.S)]

def readme(folder):
    return next((p for p in folder.iterdir() if p.is_file() and p.name.lower()=='readme.md'),None)

def rel_link(source,target):
    return os.path.relpath(target,source.parent).replace(os.sep,'/').replace(' ','%20')

def refresh_navigation():
    docs=sorted(p for p in ROOT.rglob('*.md') if p.name.lower()=='readme.md' or p in {ROOT/'wallets.md',ROOT/'CATALOG.md'})
    for p in docs:
        source=p.read_text(encoding='utf-8')
        source=re.sub(r'<!-- doc-nav:start -->.*?<!-- doc-nav:end -->\n*','',source,flags=re.S)
        source=re.sub(r'<!-- contents:start -->.*?<!-- contents:end -->\n*','',source,flags=re.S)
        source=re.sub(r'<a id="section-[^"]+"></a>\n','',source)
        hs=[h for h in headings(source) if h[1]==2]
        if len(hs)>=2:
            seen=collections.Counter();items=[]
            for pos,level,title in hs:
                key=slug(title);n=seen[key];seen[key]+=1;anchor='section-'+key+('-'+str(n) if n else '')
                items.append((pos,title,anchor))
            for pos,title,anchor in reversed(items):
                source=source[:pos]+f'<a id="{anchor}"></a>\n'+source[pos:]
            toc='<!-- contents:start -->\n<details>\n<summary>Contents</summary>\n<ul>\n'+''.join(f'<li><a href="#{a}">{html.escape(t)}</a></li>\n' for _,t,a in items)+'</ul>\n</details>\n<!-- contents:end -->\n\n'
            pos=source.index(f'<a id="{items[0][2]}">');source=source[:pos]+toc+source[pos:]
        links=[]
        if p != ROOT/'readme.md':links.append((ROOT/'readme.md','Home'))
        if p != ROOT/'wallets.md':links.append((ROOT/'wallets.md','Wallet index'))
        if p != ROOT/'CATALOG.md':links.append((ROOT/'CATALOG.md','All case files'))
        parent=p.parent.parent
        while parent.is_relative_to(ROOT) and parent!=ROOT:
            target=readme(parent)
            if target and target!=p:links.append((target,'Parent index'));break
            parent=parent.parent
        nav='<!-- doc-nav:start -->\n<p>'+ ' · '.join(f'<a href="{rel_link(p,t)}">{label}</a>' for t,label in links)+'</p>\n<!-- doc-nav:end -->\n\n'
        marker='<!-- case-visual:end -->\n\n'
        if marker in source:source=source.replace(marker,marker+nav,1)
        elif p==ROOT/'readme.md':
            source=source.replace('<!-- contents:start -->',nav+'<!-- contents:start -->',1)
        else:source=nav+source
        p.write_text(source,encoding='utf-8')

class Elements(HTMLParser):
    def __init__(self):
        super().__init__();self.links=[];self.ids=[];self.images=[];self.tables=[];self.table=None;self.row=None
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'):self.ids.append(a['id'])
        if tag=='a' and a.get('name'):self.ids.append(a['name'])
        if tag in {'a','img','link'}:
            value=a.get('src' if tag=='img' else 'href')
            if value is not None:self.links.append(value)
        if tag=='img':self.images.append(a)
        if tag=='table':self.table=[]
        if tag=='tr' and self.table is not None:self.row=0
        if tag in {'td','th'} and self.row is not None:self.row+=int(a.get('colspan','1'))
    def handle_endtag(self,tag):
        if tag=='tr' and self.row is not None:self.table.append(self.row);self.row=None
        if tag=='table' and self.table is not None:self.tables.append(self.table);self.table=None

def inspect_document(p):
    source=p.read_text(encoding='utf-8'); clean=mask(source)
    e=Elements();e.feed(clean)
    counts=collections.Counter()
    for _,_,name in headings(source):
        key=slug(name);n=counts[key];counts[key]+=1;e.ids.append(key+('-'+str(n) if n else ''))
    e.links+=re.findall(r'!?\[[^\]\n]*\]\(<?([^\s)>]+)>?(?:\s+["\'][^\n]*?["\'])?\)',clean)
    refs={m[1].lower():m[2] for m in re.finditer(r'^\s*\[([^]]+)\]:\s*(\S+)',clean,re.M)}
    e.links+=list(refs.values())
    errors=[]
    for match in re.finditer(r'\[[^]\n]+\]\[([^]\n]+)\]',clean):
        if match[1].lower() not in refs:errors.append('undefined reference: '+match[1])
    for im in e.images:
        if not im.get('alt','').strip():errors.append('image lacks alt text: '+str(im.get('src')))
    for n,t in enumerate(e.tables,1):
        if len(set(t))>1:errors.append(f'HTML table {n} has inconsistent row widths: {sorted(set(t))}')
    return source,e,errors

def check():
    docs=sorted(ROOT.rglob('*.md')); parsed={p:inspect_document(p) for p in docs};errors=[];link_count=0;toc_count=0
    for p,(source,e,issues) in parsed.items():
        label=p.relative_to(ROOT).as_posix();errors += [label+': '+x for x in issues]
        if '<!-- contents:start -->' in source:
            toc_count+=1;toc=re.search(r'<!-- contents:start -->(.*?)<!-- contents:end -->',source,re.S)[1]
            entries=re.findall(r'href="#([^"]+)"',toc)
            explicit=re.findall(r'<a id="(section-[^"]+)"></a>',source)
            if entries!=explicit:errors.append(label+': contents entries do not match section anchors')
            if len(entries)!=sum(h[1]==2 for h in headings(source)):errors.append(label+': contents omits a level-two heading')
        if len(e.ids)!=len(set(e.ids)):errors.append(label+': duplicate anchors')
        for link in e.links:
            u=urlsplit(html.unescape(link))
            if u.scheme or u.netloc:continue
            link_count+=1
            target=(ROOT/u.path.lstrip('/')) if u.path.startswith('/') else (p.parent/unquote(u.path)) if u.path else p
            target=target.resolve()
            if not target.exists():errors.append(label+': missing local target '+link);continue
            if target.is_dir():target=readme(target)
            if u.fragment and target in parsed and unquote(u.fragment) not in parsed[target][1].ids:errors.append(label+': missing section '+link)
    manifest=json.loads((ROOT/'assets/visuals.json').read_text())
    readmes={p.relative_to(ROOT).as_posix() for p in docs if p.name.lower()=='readme.md'}
    if readmes!={x['readme'] for x in manifest['headers']}:errors.append('visual manifest does not match README inventory')
    catalog=ROOT/'CATALOG.md';catalog_readmes=set()
    for link in parsed[catalog][1].links:
        u=urlsplit(html.unescape(link))
        if u.scheme or u.netloc or not u.path:continue
        target=(catalog.parent/unquote(u.path)).resolve()
        if target.is_dir():target=readme(target)
        if target and target.name.lower()=='readme.md' and target.is_relative_to(ROOT):
            catalog_readmes.add(target.relative_to(ROOT).as_posix())
    if readmes!=catalog_readmes:
        missing=sorted(readmes-catalog_readmes);extra=sorted(catalog_readmes-readmes)
        if missing:errors.append('catalog omits README files: '+', '.join(missing))
        if extra:errors.append('catalog has unknown README files: '+', '.join(extra))
    for item in manifest['headers']:
        p=ROOT/item['readme'];image=ROOT/item['image']
        if not image.exists():errors.append('missing visual '+item['image'])
        elif image.resolve() not in {(p.parent/unquote(x)).resolve() for x in parsed[p][1].links if not urlsplit(x).scheme}:errors.append('unreferenced visual '+item['image'])
    report={'markdown_files':len(docs),'readmes':len(readmes),'contents_menus':toc_count,'local_links_checked':link_count,'errors':errors}
    print(json.dumps(report,indent=2));return bool(errors)

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--write-nav',action='store_true');args=ap.parse_args()
    if args.write_nav:refresh_navigation()
    raise SystemExit(check())
