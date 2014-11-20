#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: whois.py
Author: huxuan
Email: i(at)huxuan.org
Description: 
"""

WHOIS_SERVER = {
    '.ac': 'whois.nic.ac',
    '.ac.ac': 'whois.nic.ac',
    '.ac.at': 'whois.nic.at',
    '.ac.be': 'whois.dns.be',
    '.ac.cn': 'whois.cnnic.net.cn',
    '.ac.il': 'whois.isoc.org.il',
    '.ac.in': 'whois.inregistry.in',
    '.ac.jp': 'whois.nic.ad.jp',
    '.ac.ke': 'whois.kenic.or.ke',
    '.ac.kr': 'whois.nic.or.kr',
    '.ac.nz': 'whois.srs.net.nz',
    '.ac.th': 'whois.thnic.net',
    '.ac.uk': 'whois.ja.net',
    '.ac.za': 'whois.co.za',
    '.academy': 'whois.donuts.co',
    '.ad': 'whois.ripe.net',
    '.adm.br': 'whois.nic.br',
    '.adv.br': 'whois.nic.br',
    '.ae': 'whois.aeda.net.ae',
    '.aero': 'whois.aero',
    '.af': 'whois.nic.af',
    '.ag': 'whois.nic.ag',
    '.agency': 'whois.donuts.co',
    '.agro.pl': 'whois.dns.pl',
    '.ah.cn': 'whois.cnnic.net.cn',
    '.aid.pl': 'whois.dns.pl',
    '.airforce': 'whois.unitedtld.com',
    '.alt.za': 'whois.co.za',
    '.am': 'whois.amnic.net',
    '.am.br': 'whois.nic.br',
    '.archi': 'whois.ksregistry.net',
    '.arpa': 'whois.iana.org',
    '.arq.br': 'whois.nic.br',
    '.art.br': 'whois.nic.br',
    '.arts.ro': 'whois.rotld.ro',
    '.as': 'whois.nic.as',
    '.asia': 'whois.nic.asia',
    '.asn.au': 'whois.audns.net.au',
    '.asso.fr': 'whois.nic.fr',
    '.asso.mc': 'whois.ripe.net',
    '.associates': 'whois.donuts.co',
    '.at': 'whois.nic.at',
    '.atm.pl': 'whois.dns.pl',
    '.auto.pl': 'whois.dns.pl',
    '.ax': 'whois.ax',
    '.bargains': 'whois.donuts.co',
    '.bbs.tr': 'whois.metu.edu.tr',
    '.be': 'whois.dns.be',
    '.berlin': 'whois.nic.berlin',
    '.bike': 'whois.donuts.co',
    '.bio.br': 'whois.nic.br',
    '.biz': 'whois.nic.biz',
    '.biz.pl': 'whois.dns.pl',
    '.bj.cn': 'whois.cnnic.net.cn',
    '.blue': 'whois.afilias.net',
    '.boutique': 'whois.donuts.co',
    '.br': 'whois.nic.br',
    '.br.com': 'whois.centralnic.com',
    '.build': 'whois.nic.build ',
    '.builders': 'whois.donuts.co',
    '.buzz': 'whois.nic.buzz',
    '.by': 'whois.cctld.by',
    '.bz': 'whois.afilias-grs.info.',
    '.ca': 'whois.cira.ca',
    '.cab': 'whois.donuts.co',
    '.camera': 'whois.donuts.co',
    '.camp': 'whois.donuts.co',
    '.careers': 'whois.donuts.co',
    '.cat': 'whois.cat',
    '.cc': 'whois.nic.cc',
    '.cd': 'whois.cd',
    '.center': 'whois.donuts.co',
    '.ch': 'whois.nic.ch',
    '.cheap': 'whois.donuts.co',
    '.cl': 'whois.nic.cl',
    '.clothing': 'whois.donuts.co',
    '.club': 'whois.nic.club',
    '.cm': 'whois.netcom.cm',
    '.cn': 'whois.cnnic.net.cn',
    '.cn.com': 'whois.centralnic.com',
    '.cng.br': 'whois.nic.br',
    '.cnt.br': 'whois.nic.br',
    '.co': 'whois.nic.co',
    '.co.ac': 'whois.nic.ac',
    '.co.at': 'whois.nic.at',
    '.co.il': 'whois.isoc.org.il',
    '.co.in': 'whois.inregistry.in',
    '.co.jp': 'whois.nic.ad.jp',
    '.co.ke': 'whois.kenic.or.ke',
    '.co.kr': 'whois.nic.or.kr',
    '.co.nz': 'whois.srs.net.nz',
    '.co.rs': 'whois.rnids.rs',
    '.co.th': 'whois.thnic.net',
    '.co.uk': 'whois.nic.uk',
    '.co.ve': 'https://registro.nic.ve/modules/whois?query=',
    '.co.za': 'http://whois.registry.net.za/whois/whois.sh?Domain=',
    '.codes': 'whois.donuts.co',
    '.coffee': 'whois.donuts.co',
    '.com': 'whois.crsnic.net',
    '.com.au': 'whois.audns.net.au',
    '.com.br': 'whois.nic.br',
    '.com.cn': 'whois.cnnic.net.cn',
    '.com.co': 'whois.nic.co',
    '.com.ec': 'whois.lac.net',
    '.com.fr': 'whois.nic.fr',
    '.com.gr': 'http://grwhois.ics.forth.gr:800/plainwhois/plainWhois?domainName=',
    '.com.gt': 'http://www.gt/cgi-bin/whois.cgi?domain=',
    '.com.hk': 'whois.hkdnr.net.hk',
    '.com.mm': 'whois.nic.mm',
    '.com.mx': 'whois.nic.mx',
    '.com.my': 'whois.mynic.net.my',
    '.com.pa': 'http://www.nic.pa/whois.php?nombre_d=',
    '.com.ph': 'http://www2.dot.ph/WhoIs.asp?Domain=',
    '.com.pl': 'whois.dns.pl',
    '.com.pt': 'whois.dns.pt',
    '.com.ro': 'whois.rotld.ro',
    '.com.ru': 'whois.ripn.net',
    '.com.sg': 'whois.nic.net.sg',
    '.com.tr': 'whois.metu.edu.tr',
    '.com.tw': 'whois.twnic.net',
    '.com.ua': 'whois.net.ua',
    '.com.ve': 'https://registro.nic.ve/modules/whois?query=',
    '.company': 'whois.donuts.co',
    '.computer': 'whois.donuts.co',
    '.construction': 'whois.donuts.co',
    '.contractors': 'whois.donuts.co',
    '.cool': 'whois.donuts.co',
    '.cq.cn': 'whois.cnnic.net.cn',
    '.cx': 'whois.nic.cx',
    '.cz': 'whois.nic.cz',
    '.de': 'whois.denic.de',
    '.diamonds': 'whois.donuts.co',
    '.directory': 'whois.donuts.co',
    '.dk': 'whois.dk-hostmaster.dk',
    '.dn.ua': 'whois.net.ua',
    '.ecn.br': 'whois.nic.br',
    '.edu': 'whois.internic.net',
    '.edu.au': 'whois.audns.net.au',
    '.edu.cn': 'whois.cnnic.net.cn',
    '.edu.gr': 'http://grwhois.ics.forth.gr:800/plainwhois/plainWhois?domainName=',
    '.edu.gt': 'http://www.gt/cgi-bin/whois.cgi?domain=',
    '.edu.hk': 'whois.hkdnr.net.hk',
    '.edu.mm': 'whois.nic.mm',
    '.edu.mx': 'whois.nic.mx',
    '.edu.my': 'whois.mynic.net.my',
    '.edu.pl': 'whois.dns.pl',
    '.edu.pt': 'whois.dns.pt',
    '.edu.rs': 'whois.rnids.rs',
    '.edu.sg': 'whois.nic.net.sg',
    '.edu.tr': 'whois.metu.edu.tr',
    '.edu.za': 'whois.co.za',
    '.education': 'whois.donuts.co',
    '.ee': 'whois.tld.ee',
    '.email': 'whois.donuts.co',
    '.eng.br': 'whois.nic.br',
    '.enterprises': 'whois.donuts.co',
    '.equipment': 'whois.donuts.co',
    '.ernet.in': 'whois.inregistry.in',
    '.es': 'http://whois.virtualname.es/whois.php?domain=',
    '.esp.br': 'whois.nic.br',
    '.estate': 'whois.donuts.co',
    '.etc.br': 'whois.nic.br',
    '.eti.br': 'whois.nic.br',
    '.eu': 'whois.eu',
    '.eu.com': 'whois.centralnic.com',
    '.eu.lv': 'whois.biz',
    '.expert': 'whois.donuts.co',
    '.exposed': 'whois.donuts.co',
    '.farm': 'whois.donuts.co',
    '.fi': 'whois.ficora.fi',
    '.fin.ec': 'whois.lac.net',
    '.firm.ro': 'whois.rotld.ro',
    '.flights': 'whois.donuts.co',
    '.florist': 'whois.donuts.co',
    '.fm': 'whois.nic.fm',
    '.fm.br': 'whois.nic.br',
    '.fo': 'whois.nic.fo',
    '.fot.br': 'whois.nic.br',
    '.fr': 'whois.nic.fr',
    '.fst.br': 'whois.nic.br',
    '.futbol': 'whois.unitedtld.com',
    '.g12.br': 'whois.nic.br',
    '.gallery': 'whois.donuts.co',
    '.gb.com': 'whois.centralnic.com',
    '.gb.net': 'whois.centralnic.com',
    '.gd': 'whois.nic.gd',
    '.gd.cn': 'whois.cnnic.net.cn',
    '.geek.nz': 'whois.srs.net.nz',
    '.gen.nz': 'whois.srs.net.nz',
    '.gf': 'whois.nplus.gf',
    '.gift': 'whois.uniregistry.net',
    '.glass': 'whois.donuts.co',
    '.gmina.pl': 'whois.dns.pl',
    '.go.id': 'whois.idnic.net.id',
    '.go.jp': 'whois.nic.ad.jp',
    '.go.ke': 'whois.kenic.or.ke',
    '.go.kr': 'whois.nic.or.kr',
    '.go.th': 'whois.thnic.net',
    '.gob.gt': 'http://www.gt/cgi-bin/whois.cgi?domain=',
    '.gob.mx': 'whois.nic.mx',
    '.gov': 'whois.nic.gov',
    '.gov.br': 'whois.nic.br',
    '.gov.cn': 'whois.cnnic.net.cn',
    '.gov.ec': 'whois.lac.net',
    '.gov.gr': 'http://grwhois.ics.forth.gr:800/plainwhois/plainWhois?domainName=',
    '.gov.il': 'whois.isoc.org.il',
    '.gov.in': 'whois.inregistry.in',
    '.gov.mm': 'whois.nic.mm',
    '.gov.mx': 'whois.nic.mx',
    '.gov.my': 'whois.mynic.net.my',
    '.gov.sg': 'whois.nic.net.sg',
    '.gov.tr': 'whois.metu.edu.tr',
    '.gov.za': 'whois.co.za',
    '.gr': 'http://grwhois.ics.forth.gr:800/plainwhois/plainWhois?domainName=',
    '.graphics': 'whois.donuts.co',
    '.gs': 'whois.nic.gs',
    '.gs.cn': 'whois.cnnic.net.cn',
    '.gsm.pl': 'whois.dns.pl',
    '.guitars': 'whois.uniregistry.net',
    '.guru': 'whois.donuts.co',
    '.gv.ac': 'whois.nic.ac',
    '.gv.at': 'whois.nic.at',
    '.gx.cn': 'whois.cnnic.net.cn',
    '.gz.cn': 'whois.cnnic.net.cn',
    '.hb.cn': 'whois.cnnic.net.cn',
    '.he.cn': 'whois.cnnic.net.cn',
    '.hi.cn': 'whois.cnnic.net.cn',
    '.hk': 'whois.hkirc.hk',
    '.hk.cn': 'whois.cnnic.net.cn',
    '.hl.cn': 'whois.cnnic.net.cn',
    '.hn.cn': 'whois.cnnic.net.cn',
    '.holdings': 'whois.donuts.co',
    '.holiday': 'whois.donuts.co',
    '.house': 'whois.donuts.co',
    '.hu': 'whois.nic.hu',
    '.hu.com': 'whois.centralnic.com',
    '.id.au': 'whois.audns.net.au',
    '.ie': 'whois.domainregistry.ie',
    '.im': 'whois.nic.im',
    '.in': 'whois.inregistry.in',
    '.in.rs': 'whois.rnids.rs',
    '.in.th': 'whois.thnic.net',
    '.ind.br': 'whois.nic.br',
    '.ind.gt': 'http://www.gt/cgi-bin/whois.cgi?domain=',
    '.inf.br': 'whois.nic.br',
    '.info': 'whois.afilias.net',
    '.info.ke': 'whois.kenic.or.ke',
    '.info.pl': 'whois.dns.pl',
    '.info.ro': 'whois.rotld.ro',
    '.info.ve': 'https://registro.nic.ve/modules/whois?query=',
    '.ink': 'whois.donuts.co',
    '.institute': 'whois.donuts.co',
    '.international': 'whois.donuts.co',
    '.io': 'whois.nic.io',
    '.ir': 'whois.nic.ir',
    '.is': 'whois.isnic.is',
    '.it': 'whois.nic.it',
    '.iwi.nz': 'whois.srs.net.nz',
    '.jl.cn': 'whois.cnnic.net.cn',
    '.jor.br': 'whois.nic.br',
    '.jp': 'whois.jprs.jp',
    '.js.cn': 'whois.cnnic.net.cn',
    '.k12.il': 'whois.isoc.org.il',
    '.k12.tr': 'whois.metu.edu.tr',
    '.kh.ua': 'whois.net.ua',
    '.kiev.ua': 'whois.net.ua',
    '.kim': 'whois.donuts.co',
    '.kitchen': 'whois.donuts.co',
    '.kiwi.nz': 'whois.srs.net.nz',
    '.kz': 'whois.domain.kz',
    '.la': 'whois.nic.la',
    '.land': 'whois.donuts.co',
    '.lel.br': 'whois.nic.br',
    '.lg.ua': 'whois.net.ua',
    '.li': 'whois.nic.li',
    '.lighting': 'whois.donuts.co',
    '.limo': 'whois.donuts.co',
    '.link': 'whois.uniregistry.net',
    '.ln.cn': 'whois.cnnic.net.cn',
    '.lt': 'whois.domreg.lt',
    '.ltd.uk': 'whois.nic.uk',
    '.lu': 'whois.dns.lu',
    '.luxury': 'whois.donuts.co',
    '.lv': 'whois.nic.lv',
    '.lviv.ua': 'whois.net.ua',
    '.mail.pl': 'whois.dns.pl',
    '.maison': 'whois.donuts.co',
    '.management': 'whois.donuts.co',
    '.maori.nz': 'whois.srs.net.nz',
    '.marketing': 'whois.donuts.co',
    '.md': 'whois.nic.md',
    '.me': 'whois.meregistry.net',
    '.me.ke': 'whois.kenic.or.ke',
    '.me.uk': 'whois.nic.uk',
    '.med.br': 'whois.nic.br',
    '.med.ec': 'whois.lac.net',
    '.media.pl': 'whois.dns.pl',
    '.menu': 'whois.nic.menu',
    '.mi.th': 'whois.thnic.net',
    '.miasta.pl': 'whois.dns.pl',
    '.mil': 'whois.internic.net',
    '.mil.br': 'whois.nic.br',
    '.mil.ec': 'whois.lac.net',
    '.mil.gt': 'http://www.gt/cgi-bin/whois.cgi?domain=',
    '.mil.id': 'whois.idnic.net.id',
    '.mil.pl': 'whois.dns.pl',
    '.mil.tr': 'whois.metu.edu.tr',
    '.mil.za': 'whois.co.za',
    '.mn': 'whois.afilias-grs.info',
    '.mo.cn': 'whois.cnnic.net.cn',
    '.mobi': 'whois.dotmobiregistry.net',
    '.mobi.ke': 'whois.kenic.or.ke',
    '.moda': 'whois.donuts.co',
    '.ms': 'whois.nic.ms',
    '.msk.ru': 'whois.relcom.ru',
    '.muni.il': 'whois.isoc.org.il',
    '.mx': 'whois.nic.mx',
    '.my': 'whois.mynic.net.my',
    '.name': 'whois.nic.name',
    '.ne.jp': 'whois.nic.ad.jp',
    '.ne.ke': 'whois.kenic.or.ke',
    '.ne.kr': 'whois.nic.or.kr',
    '.net': 'whois.crsnic.net',
    '.net.au': 'whois.audns.net.au',
    '.net.br': 'whois.nic.br',
    '.net.cn': 'whois.cnnic.net.cn',
    '.net.co': 'whois.nic.co',
    '.net.ec': 'whois.lac.net',
    '.net.gr': 'http://grwhois.ics.forth.gr:800/plainwhois/plainWhois?domainName=',
    '.net.gt': 'http://www.gt/cgi-bin/whois.cgi?domain=',
    '.net.hk': 'whois.hkdnr.net.hk',
    '.net.il': 'whois.isoc.org.il',
    '.net.in': 'whois.inregistry.in',
    '.net.mm': 'whois.nic.mm',
    '.net.mx': 'whois.nic.mx',
    '.net.my': 'whois.mynic.net.my',
    '.net.nz': 'whois.srs.net.nz',
    '.net.pa': 'http://www.nic.pa/whois.php?nombre_d=',
    '.net.ph': 'http://www2.dot.ph/WhoIs.asp?Domain=',
    '.net.pl': 'whois.dns.pl',
    '.net.ru': 'whois.ripn.net',
    '.net.sg': 'whois.nic.net.sg',
    '.net.th': 'whois.thnic.net',
    '.net.tr': 'whois.metu.edu.tr',
    '.net.tw': 'whois.twnic.net',
    '.net.ua': 'whois.net.ua',
    '.net.uk': 'whois.nic.uk',
    '.net.ve': 'https://registro.nic.ve/modules/whois?query=',
    '.net.za': 'whois.co.za',
    '.ngo.ph': 'http://www2.dot.ph/WhoIs.asp?Domain=',
    '.ngo.za': 'whois.co.za',
    '.ninja': 'whois.donuts.co',
    '.nl': 'whois.domain-registry.nl',
    '.nm.cn': 'whois.cnnic.net.cn',
    '.nm.kr': 'whois.nic.or.kr',
    '.no': 'finger.norid.no:79',
    '.no.com': 'whois.centralnic.com',
    '.nom.br': 'whois.nic.br',
    '.nom.co': 'whois.nic.co',
    '.nom.pl': 'whois.dns.pl',
    '.nom.ro': 'whois.rotld.ro',
    '.nom.za': 'whois.co.za',
    '.nt.ro': 'whois.rotld.ro',
    '.ntr.br': 'whois.nic.br',
    '.nu': 'whois.nic.nu',
    '.nx.cn': 'whois.cnnic.net.cn',
    '.odo.br': 'whois.nic.br',
    '.onl': 'whois.donuts.co',
    '.or.ac': 'whois.nic.ac',
    '.or.at': 'whois.nic.at',
    '.or.jp': 'whois.nic.ad.jp',
    '.or.ke': 'whois.kenic.or.ke',
    '.or.kr': 'whois.nic.or.kr',
    '.or.th': 'whois.thnic.net',
    '.org': 'whois.publicinterestregistry.net',
    '.org.au': 'whois.audns.net.au',
    '.org.br': 'whois.nic.br',
    '.org.cn': 'whois.cnnic.net.cn',
    '.org.ec': 'whois.lac.net',
    '.org.gr': 'http://grwhois.ics.forth.gr:800/plainwhois/plainWhois?domainName=',
    '.org.gt': 'http://www.gt/cgi-bin/whois.cgi?domain=',
    '.org.hk': 'whois.hkdnr.net.hk',
    '.org.il': 'whois.isoc.org.il',
    '.org.in': 'whois.inregistry.in',
    '.org.mm': 'whois.nic.mm',
    '.org.mx': 'whois.nic.mx',
    '.org.my': 'whois.mynic.net.my',
    '.org.nz': 'whois.srs.net.nz',
    '.org.pa': 'http://www.nic.pa/whois.php?nombre_d=',
    '.org.ph': 'http://www2.dot.ph/WhoIs.asp?Domain=',
    '.org.pl': 'whois.dns.pl',
    '.org.ro': 'whois.rotld.ro',
    '.org.rs': 'whois.rnids.rs',
    '.org.ru': 'whois.ripn.net',
    '.org.sg': 'whois.nic.net.sg',
    '.org.tr': 'whois.metu.edu.tr',
    '.org.tw': 'whois.twnic.net',
    '.org.ua': 'whois.net.ua',
    '.org.uk': 'whois.nic.uk',
    '.org.ve': 'https://registro.nic.ve/modules/whois?query=',
    '.org.za': 'http://org.za/cgi-bin/rwhois?format=full&domain=',
    '.pa': 'http://www.nic.pa/whois.php?nombre_d=',
    '.pc.pl': 'whois.dns.pl',
    '.ph': 'http://www2.dot.ph/WhoIs.asp?Domain=',
    '.photography': 'whois.donuts.co',
    '.photos': 'whois.donuts.co',
    '.pics': 'whois.uniregistry.net',
    '.pink': 'whois.afilias.net',
    '.pl': 'whois.dns.pl',
    '.plc.uk': 'whois.nic.uk',
    '.plumbing ': 'whois.donuts.co',
    '.pm': 'whois.nic.pm',
    '.pp.ru': 'whois.ripn.net',
    '.ppg.br': 'whois.nic.br',
    '.presse.fr': 'whois.nic.fr',
    '.priv.pl': 'whois.dns.pl',
    '.pro': 'whois.registrypro.pro',
    '.pro.br': 'whois.nic.br',
    '.psc.br': 'whois.nic.br',
    '.psi.br': 'whois.nic.br',
    '.pt': 'whois.dns.pt',
    '.pw': 'whois.nic.pw',
    '.qc.com': 'whois.centralnic.com',
    '.qh.cn': 'whois.cnnic.net.cn',
    '.re': 'whois.nic.re',
    '.re.kr': 'whois.nic.or.kr',
    '.realestate.pl': 'whois.dns.pl',
    '.rec.br': 'whois.nic.br',
    '.rec.ro': 'whois.rotld.ro',
    '.recipes': 'whois.donuts.co',
    '.rel.pl': 'whois.dns.pl',
    '.repair': 'whois.donuts.co',
    '.res.in': 'whois.inregistry.in',
    '.ro': 'whois.rotld.ro',
    '.rs': 'whois.rnids.rs',
    '.ru': 'whois.ripn.net',
    '.sa.com': 'whois.centralnic.com',
    '.sc': 'wawa.eahd.or.ug',
    '.sc.cn': 'whois.cnnic.net.cn',
    '.sc.ke': 'whois.kenic.or.ke',
    '.school.nz': 'whois.srs.net.nz',
    '.school.za': 'whois.co.za',
    '.se': 'whois.iis.se',
    '.se.com': 'whois.centralnic.com',
    '.se.net': 'whois.centralnic.com',
    '.sexy': 'whois.uniregistry.net',
    '.sg': 'whois.nic.net.sg',
    '.sh': 'whois.nic.sh',
    '.sh.cn': 'whois.cnnic.net.cn',
    '.shiksha': 'whois.nic.shiksha',
    '.shoes': 'whois.donuts.co',
    '.shop.pl': 'whois.dns.pl',
    '.si': 'whois.arnes.si',
    '.singles': 'whois.donuts.co',
    '.sk': 'whois.sk-nic.sk',
    '.sklep.pl': 'whois.dns.pl',
    '.slg.br': 'whois.nic.br',
    '.sn.cn': 'whois.cnnic.net.cn',
    '.social': 'whois.donuts.co',
    '.solar': 'whois.donuts.co',
    '.solutions': 'whois.donuts.co',
    '.sos.pl': 'whois.dns.pl',
    '.spb.ru': 'whois.relcom.ru',
    '.st': 'whois.nic.st',
    '.store.ro': 'whois.rotld.ro',
    '.su': 'whois.ripn.net',
    '.supplies': 'whois.donuts.co',
    '.supply': 'whois.donuts.co',
    '.support': 'whois.donuts.co',
    '.sx': 'whois.sx',
    '.systems': 'whois.donuts.co',
    '.targi.pl': 'whois.dns.pl',
    '.tc': 'whois.adamsnames.tc',
    '.technology': 'whois.donuts.co',
    '.tel': 'whois.nic.tel',
    '.tf': 'whois.nic.tf',
    '.tips': 'whois.donuts.co',
    '.tj': 'whois.nic.tj',
    '.tj.cn': 'whois.cnnic.net.cn',
    '.tk': 'https://partners.nic.tk/cgi-bin/whmcs-whois.taloha?d=',
    '.tm': 'whois.nic.tm',
    '.tm.fr': 'whois.nic.fr',
    '.tm.mc': 'whois.ripe.net',
    '.tm.pl': 'whois.dns.pl',
    '.tm.ro': 'whois.rotld.ro',
    '.tm.za': 'whois.co.za',
    '.tmp.br': 'whois.nic.br',
    '.to': 'monarch.tonic.to',
    '.today': 'whois.donuts.co',
    '.tourism.pl': 'whois.dns.pl',
    '.training': 'whois.donuts.co',
    '.travel': 'whois.nic.travel',
    '.travel.pl': 'whois.dns.pl',
    '.tur.br': 'whois.nic.br',
    '.turystyka.pl': 'whois.dns.pl',
    '.tv': 'whois.nic.tv',
    '.tv.br': 'whois.nic.br',
    '.tw': 'whois.twnic.net.tw',
    '.tw.cn': 'whois.cnnic.net.cn',
    '.ua': 'whois.net.ua',
    '.uk': 'whois.nic.uk',
    '.uk.co': 'whois.uk.co',
    '.uk.com': 'whois.centralnic.com',
    '.uk.net': 'whois.centralnic.com',
    '.uno': 'whois.uno.nic',
    '.us': 'whois.nic.us',
    '.us.com': 'whois.centralnic.com',
    '.uy.com': 'whois.centralnic.com',
    '.vc': 'whois.adamsnames.tc',
    '.ventures': 'whois.donuts.co',
    '.vet.br': 'whois.nic.br',
    '.vg': 'whois.adamsnames.tc',
    '.viajes': 'whois.donuts.co',
    '.voyage': 'whois.donuts.co',
    '.web.ve': 'https://registro.nic.ve/modules/whois?query=',
    '.web.za': 'whois.co.za',
    '.wf': 'whois.nic.wf',
    '.wiki': 'whois.donuts.co',
    '.work': 'whois-dub.mm-registry.com',
    '.ws': 'whois.website.ws',
    '.www.ro': 'whois.rotld.ro',
    '.xj.cn': 'whois.cnnic.net.cn',
    '.xxx': 'whois.nic.xxx',
    '.xz.cn': 'whois.cnnic.net.cn',
    '.yn.cn': 'whois.cnnic.net.cn',
    '.yt': 'whois.nic.yt',
    '.za.com': 'whois.centralnic.com',
    '.za.net': 'http://www.za.net/cgi-bin/whois.cgi?domain=',
    '.za.org': 'http://www.za.net/cgi-bin/whois.cgi?domain=',
    '.zj.cn': 'whois.cnnic.net.cn',
    '.zlg.br': 'whois.nic.br',
    '.zone': 'whois.donuts.co',
}

WHOIS_AVAIL = {
    '.ac': 'is available for purchase',
    '.ac.ac': 'is not registered',
    '.ac.at': 'nothing found',
    '.ac.be': 'No such domain',
    '.ac.cn': 'no matching record',
    '.ac.il': 'No data was found',
    '.ac.in': 'NOT FOUND',
    '.ac.jp': 'No match!!',
    '.ac.ke': 'Not Registered',
    '.ac.kr': 'is not registered',
    '.ac.nz': '220 Available',
    '.ac.th': 'No match for',
    '.ac.uk': 'Sorry - no',
    '.ac.za': 'No information available',
    '.academy': 'Domain not found.',
    '.ad': 'no entries found',
    '.adm.br': 'No match for',
    '.adv.br': 'No match for',
    '.ae': 'No Data Found',
    '.aero': 'NOT FOUND',
    '.af': 'No Object Found',
    '.ag': 'NOT FOUND',
    '.agency': 'Domain not found.',
    '.agro.pl': 'No information available',
    '.ah.cn': 'no matching record',
    '.aid.pl': 'No information available',
    '.airforce': 'Domain not found',
    '.alt.za': 'No information available',
    '.am': 'No match',
    '.am.br': 'No match for',
    '.archi': 'not found',
    '.arpa': '0 objects',
    '.arq.br': 'No match for',
    '.art.br': 'No match for',
    '.arts.ro': 'No entries found',
    '.as': 'Available',
    '.asia': 'NOT FOUND',
    '.asn.au': 'No Data Found',
    '.asso.fr': 'No entries found',
    '.asso.mc': 'no entries found',
    '.associates': 'Domain not found',
    '.at': 'nothing found',
    '.atm.pl': 'No information available',
    '.auto.pl': 'No information available',
    '.ax': 'No records matching',
    '.bargains': 'Domain not found.',
    '.bbs.tr': 'No match found',
    '.be': 'Status:\tAVAILABLE',
    '.berlin': 'No match',
    '.bike': 'Domain not found',
    '.bio.br': 'No match for',
    '.biz': 'Not found',
    '.biz.pl': 'No information available',
    '.bj.cn': 'no matching record',
    '.blue': 'NOT FOUND',
    '.boutique': 'Domain not found.',
    '.br': 'No match for',
    '.br.com': 'DOMAIN NOT FOUND',
    '.build': 'No Data Found',
    '.builders': 'Domain not found',
    '.buzz': 'Not found:',
    '.by': 'Object does not exist',
    '.bz': 'NOT FOUND',
    '.ca': 'Domain status:         available',
    '.cab': 'Domain not found.',
    '.camera': 'Domain not found',
    '.camp': 'Domain not found.',
    '.careers': 'Domain not found',
    '.cat': 'NOT FOUND',
    '.cc': 'No match',
    '.cd': 'No match',
    '.center': 'Domain not found.',
    '.ch': 'not have an entry',
    '.cheap': 'Domain not found.',
    '.cl': 'no existe',
    '.clothing': 'Domain not found',
    '.club': 'Not found',
    '.cm': 'Not Registered',
    '.cn': 'no matching record',
    '.cn.com': 'DOMAIN NOT FOUND',
    '.cng.br': 'No match for',
    '.cnt.br': 'No match for',
    '.co': 'Not found',
    '.co.ac': 'is not registered',
    '.co.at': 'nothing found',
    '.co.il': 'No data was found',
    '.co.in': 'NOT FOUND',
    '.co.jp': 'No match!!',
    '.co.ke': 'Not Registered',
    '.co.kr': 'is not registered',
    '.co.nz': '220 Available',
    '.co.rs': '%ERROR:103',
    '.co.th': 'No match for',
    '.co.uk': 'No match',
    '.co.ve': 'HTTPREQUEST-No match for',
    '.co.za': 'HTTPREQUEST-No Matches',
    '.codes': 'Domain not found.',
    '.coffee': 'Domain not found',
    '.com': 'No match for',
    '.com.au': 'No Data Found',
    '.com.br': 'No match for',
    '.com.cn': 'no matching record',
    '.com.co': 'Not found',
    '.com.ec': 'No match found',
    '.com.fr': 'No entries found',
    '.com.gr': 'HTTPREQUEST-not exist',
    '.com.gt': 'HTTPREQUEST-DOMINIO NO REGISTRADO',
    '.com.hk': 'The domain has not been registered',
    '.com.mm': 'No domains matched',
    '.com.mx': 'Object_Not_Found',
    '.com.my': 'does not exist',
    '.com.pa': 'HTTPREQUEST-esta disponible para ser Registrado',
    '.com.ph': 'HTTPREQUEST-is still available',
    '.com.pl': 'No information available',
    '.com.pt': 'no match',
    '.com.ro': 'No entries found',
    '.com.ru': 'No entries found',
    '.com.sg': 'Domain Not Found',
    '.com.tr': 'No match found',
    '.com.tw': 'No Found',
    '.com.ua': 'No entries found',
    '.com.ve': 'HTTPREQUEST-No match for',
    '.company': 'Domain not found.',
    '.computer': 'Domain not found.',
    '.construction': 'Domain not found',
    '.contractors': 'Domain not found',
    '.cool': 'Domain not found',
    '.cq.cn': 'no matching record',
    '.cx': 'No match for',
    '.cz': 'No entries found',
    '.de': 'Status: free',
    '.diamonds': 'Domain not found',
    '.directory': 'Domain not found',
    '.dk': 'No entries found',
    '.dn.ua': 'No entries found',
    '.ecn.br': 'No match for',
    '.edu': 'No match for',
    '.edu.au': 'No Data Found',
    '.edu.cn': 'no matching record',
    '.edu.gr': 'HTTPREQUEST-not exist',
    '.edu.gt': 'HTTPREQUEST-DOMINIO NO REGISTRADO',
    '.edu.hk': 'The domain has not been registered',
    '.edu.mm': 'No domains matched',
    '.edu.mx': 'Object_Not_Found',
    '.edu.my': 'does not exist',
    '.edu.pl': 'No information available',
    '.edu.pt': 'no match',
    '.edu.rs': '%ERROR:103',
    '.edu.sg': 'Domain Not Found',
    '.edu.tr': 'No match found',
    '.edu.za': 'No information available',
    '.education': 'Domain not found.',
    '.ee': 'no entries found',
    '.email': 'Domain not found.',
    '.eng.br': 'No match for',
    '.enterprises': 'Domain not found',
    '.equipment': 'Domain not found',
    '.ernet.in': 'NOT FOUND',
    '.es': 'HTTPREQUEST-LIBRE',
    '.esp.br': 'No match for',
    '.estate': 'Domain not found',
    '.etc.br': 'No match for',
    '.eti.br': 'No match for',
    '.eu': 'Status:\tAVAILABLE',
    '.eu.com': 'DOMAIN NOT FOUND',
    '.eu.lv': 'Not found',
    '.expert': 'Domain not found',
    '.exposed': 'Domain not found.',
    '.farm': 'Domain not found.',
    '.fi': 'Domain not found',
    '.fin.ec': 'No match found',
    '.firm.ro': 'No entries found',
    '.flights': 'Domain not found',
    '.florist': 'Domain not found.',
    '.fm': 'Not Registered',
    '.fm.br': 'No match for',
    '.fo': 'no entries found',
    '.fot.br': 'No match for',
    '.fr': 'No entries found',
    '.fst.br': 'No match for',
    '.futbol': 'Domain not found',
    '.g12.br': 'No match for',
    '.gallery': 'Domain not found',
    '.gb.com': 'DOMAIN NOT FOUND',
    '.gb.net': 'DOMAIN NOT FOUND',
    '.gd': 'not found...',
    '.gd.cn': 'no matching record',
    '.geek.nz': '220 Available',
    '.gen.nz': '220 Available',
    '.gf': 'not found in our database',
    '.gift': 'available for registration',
    '.glass': 'Domain not found.',
    '.gmina.pl': 'No information available',
    '.go.id': 'Not found',
    '.go.jp': 'No match!!',
    '.go.ke': 'Not Registered',
    '.go.kr': 'is not registered',
    '.go.th': 'No match for',
    '.gob.gt': 'HTTPREQUEST-DOMINIO NO REGISTRADO',
    '.gob.mx': 'Object_Not_Found',
    '.gov': 'No match for',
    '.gov.br': 'No match for',
    '.gov.cn': 'no matching record',
    '.gov.ec': 'No match found',
    '.gov.gr': 'HTTPREQUEST-not exist',
    '.gov.il': 'No data was found',
    '.gov.in': 'NOT FOUND',
    '.gov.mm': 'No domains matched',
    '.gov.mx': 'Object_Not_Found',
    '.gov.my': 'does not exist',
    '.gov.sg': 'Domain Not Found',
    '.gov.tr': 'No match found',
    '.gov.za': 'No information available',
    '.gr': 'HTTPREQUEST-not exist',
    '.graphics': 'Domain not found',
    '.gs': 'No Object Found',
    '.gs.cn': 'no matching record',
    '.gsm.pl': 'No information available',
    '.guitars': 'available for registration',
    '.guru': 'Domain not found',
    '.gv.ac': 'is not registered',
    '.gv.at': 'nothing found',
    '.gx.cn': 'no matching record',
    '.gz.cn': 'no matching record',
    '.hb.cn': 'no matching record',
    '.he.cn': 'no matching record',
    '.hi.cn': 'no matching record',
    '.hk': 'The domain has not been registered',
    '.hk.cn': 'no matching record',
    '.hl.cn': 'no matching record',
    '.hn.cn': 'no matching record',
    '.holdings': 'Domain not found',
    '.holiday': 'Domain not found.',
    '.house': 'Domain not found.',
    '.hu': 'No match',
    '.hu.com': 'DOMAIN NOT FOUND',
    '.id.au': 'No Data Found',
    '.ie': '% Not Registered',
    '.im': 'was not found',
    '.in': 'NOT FOUND',
    '.in.rs': '%ERROR:103',
    '.in.th': 'No match for',
    '.ind.br': 'No match for',
    '.ind.gt': 'HTTPREQUEST-DOMINIO NO REGISTRADO',
    '.inf.br': 'No match for',
    '.info': 'NOT FOUND',
    '.info.ke': 'Not Registered',
    '.info.pl': 'No information available',
    '.info.ro': 'No entries found',
    '.info.ve': 'HTTPREQUEST-No match for',
    '.ink': 'Domain not found',
    '.institute': 'Domain not found.',
    '.international': 'Domain not found.',
    '.io': 'is available',
    '.ir': 'no entries found',
    '.is': 'No entries found',
    '.it': 'AVAILABLE',
    '.iwi.nz': '220 Available',
    '.jl.cn': 'no matching record',
    '.jor.br': 'No match for',
    '.jp': 'No match!!',
    '.js.cn': 'no matching record',
    '.k12.il': 'No data was found',
    '.k12.tr': 'No match found',
    '.kh.ua': 'No entries found',
    '.kiev.ua': 'No entries found',
    '.kim': 'Domain not found.',
    '.kitchen': 'Domain not found',
    '.kiwi.nz': '220 Available',
    '.kz': 'No entries found',
    '.la': 'NOT FOUND',
    '.land': 'Domain not found',
    '.lel.br': 'No match for',
    '.lg.ua': 'No entries found',
    '.li': 'do not have an entry in our database matching your query',
    '.lighting': 'Domain not found',
    '.limo': 'Domain not found.',
    '.link': 'available for registration',
    '.ln.cn': 'no matching record',
    '.lt': 'Status:\t\t\tavailable',
    '.ltd.uk': 'No match',
    '.lu': 'No such domain',
    '.luxury': 'Domain not found',
    '.lv': 'Status: free',
    '.lviv.ua': 'No entries found',
    '.mail.pl': 'No information available',
    '.maison': 'Domain not found',
    '.management': 'Domain not found.',
    '.maori.nz': '220 Available',
    '.marketing': 'Domain not found.',
    '.md': 'No match for',
    '.me': 'NOT FOUND',
    '.me.ke': 'Not Registered',
    '.me.uk': 'No match',
    '.med.br': 'No match for',
    '.med.ec': 'No match found',
    '.media.pl': 'No information available',
    '.menu': 'No Data Found',
    '.mi.th': 'No match for',
    '.miasta.pl': 'No information available',
    '.mil': 'No match for',
    '.mil.br': 'No match for',
    '.mil.ec': 'No match found',
    '.mil.gt': 'HTTPREQUEST-DOMINIO NO REGISTRADO',
    '.mil.id': 'Not found',
    '.mil.pl': 'No information available',
    '.mil.tr': 'No match found',
    '.mil.za': 'No information available',
    '.mn': 'NOT FOUND',
    '.mo.cn': 'no matching record',
    '.mobi': 'NOT FOUND',
    '.mobi.ke': 'Not Registered',
    '.moda': 'Domain not found',
    '.ms': 'No Object Found',
    '.msk.ru': 'No entries found',
    '.muni.il': 'No data was found',
    '.mx': 'No_Se_Encontro_El_Objeto/Object_Not_Found',
    '.my': 'does not exist in database',
    '.name': 'No match',
    '.ne.jp': 'No match!!',
    '.ne.ke': 'Not Registered',
    '.ne.kr': 'is not registered',
    '.net': 'No match for',
    '.net.au': 'No Data Found',
    '.net.br': 'No match for',
    '.net.cn': 'no matching record',
    '.net.co': 'Not found',
    '.net.ec': 'No match found',
    '.net.gr': 'HTTPREQUEST-not exist',
    '.net.gt': 'HTTPREQUEST-DOMINIO NO REGISTRADO',
    '.net.hk': 'The domain has not been registered',
    '.net.il': 'No data was found',
    '.net.in': 'NOT FOUND',
    '.net.mm': 'No domains matched',
    '.net.mx': 'Object_Not_Found',
    '.net.my': 'does not exist',
    '.net.nz': '220 Available',
    '.net.pa': 'HTTPREQUEST-esta disponible para ser Registrado',
    '.net.ph': 'HTTPREQUEST-is still available',
    '.net.pl': 'No information available',
    '.net.ru': 'No entries found',
    '.net.sg': 'Domain Not Found',
    '.net.th': 'No match for',
    '.net.tr': 'No match found',
    '.net.tw': 'No Found',
    '.net.ua': 'No entries found',
    '.net.uk': 'No match',
    '.net.ve': 'HTTPREQUEST-No match for',
    '.net.za': 'No information available',
    '.ngo.ph': 'HTTPREQUEST-is still available',
    '.ngo.za': 'No information available',
    '.ninja': 'Domain not found',
    '.nl': 'is free',
    '.nm.cn': 'no matching record',
    '.nm.kr': 'is not registered',
    '.no': 'is available',
    '.no.com': 'DOMAIN NOT FOUND',
    '.nom.br': 'No match for',
    '.nom.co': 'Not found',
    '.nom.pl': 'No information available',
    '.nom.ro': 'No entries found',
    '.nom.za': 'No information available',
    '.nt.ro': 'No entries found',
    '.ntr.br': 'No match for',
    '.nu': 'not found',
    '.nx.cn': 'no matching record',
    '.odo.br': 'No match for',
    '.onl': 'Domain not found',
    '.or.ac': 'is not registered',
    '.or.at': 'nothing found',
    '.or.jp': 'No match!!',
    '.or.ke': 'Not Registered',
    '.or.kr': 'is not registered',
    '.or.th': 'No match for',
    '.org': 'NOT FOUND',
    '.org.au': 'No Data Found',
    '.org.br': 'No match for',
    '.org.cn': 'no matching record',
    '.org.ec': 'No match found',
    '.org.gr': 'HTTPREQUEST-not exist',
    '.org.gt': 'HTTPREQUEST-DOMINIO NO REGISTRADO',
    '.org.hk': 'The domain has not been registered',
    '.org.il': 'No data was found',
    '.org.in': 'NOT FOUND',
    '.org.mm': 'No domains matched',
    '.org.mx': 'Object_Not_Found',
    '.org.my': 'does not exist',
    '.org.nz': '220 Available',
    '.org.pa': 'HTTPREQUEST-esta disponible para ser Registrado',
    '.org.ph': 'HTTPREQUEST-is still available',
    '.org.pl': 'No information available',
    '.org.ro': 'No entries found',
    '.org.rs': '%ERROR:103',
    '.org.ru': 'No entries found',
    '.org.sg': 'Domain Not Found',
    '.org.tr': 'No match found',
    '.org.tw': 'No Found',
    '.org.ua': 'No entries found',
    '.org.uk': 'No match',
    '.org.ve': 'HTTPREQUEST-No match for',
    '.org.za': 'HTTPREQUEST-Domain not registered',
    '.pa': 'HTTPREQUEST-esta disponible para ser Registrado',
    '.pc.pl': 'No information available',
    '.ph': 'HTTPREQUEST-is still available',
    '.photography': 'Domain not found',
    '.photos': 'Domain not found',
    '.pics': 'available for registration',
    '.pink': 'NOT FOUND',
    '.pl': 'No information available',
    '.plc.uk': 'No match',
    '.plumbing ': 'Domain not found',
    '.pm': 'No entries found',
    '.pp.ru': 'No entries found',
    '.ppg.br': 'No match for',
    '.presse.fr': 'No entries found',
    '.priv.pl': 'No information available',
    '.pro': 'NOT FOUND',
    '.pro.br': 'No match for',
    '.psc.br': 'No match for',
    '.psi.br': 'No match for',
    '.pt': 'no match',
    '.pw': 'DOMAIN NOT FOUND',
    '.qc.com': 'DOMAIN NOT FOUND',
    '.qh.cn': 'no matching record',
    '.re': 'No entries found',
    '.re.kr': 'is not registered',
    '.realestate.pl': 'No information available',
    '.rec.br': 'No match for',
    '.rec.ro': 'No entries found',
    '.recipes': 'Domain not found',
    '.rel.pl': 'No information available',
    '.repair': 'Domain not found.',
    '.res.in': 'NOT FOUND',
    '.ro': 'No entries found',
    '.rs': '%ERROR:103',
    '.ru': 'No entries found',
    '.sa.com': 'DOMAIN NOT FOUND',
    '.sc': 'No entries found',
    '.sc.cn': 'no matching record',
    '.sc.ke': 'Not Registered',
    '.school.nz': '220 Available',
    '.school.za': 'No information available',
    '.se': 'not found',
    '.se.com': 'DOMAIN NOT FOUND',
    '.se.net': 'DOMAIN NOT FOUND',
    '.sexy': 'is available for registration',
    '.sg': 'Domain Not Found',
    '.sh': 'is available for purchase',
    '.sh.cn': 'no matching record',
    '.shiksha': 'NOT FOUND',
    '.shoes': 'Domain not found',
    '.shop.pl': 'No information available',
    '.si': 'No entries found',
    '.singles': 'Domain not found',
    '.sk': 'Not found',
    '.sklep.pl': 'No information available',
    '.slg.br': 'No match for',
    '.sn.cn': 'no matching record',
    '.social': 'Domain not found',
    '.solar': 'Domain not found.',
    '.solutions': 'Domain not found.',
    '.sos.pl': 'No information available',
    '.spb.ru': 'No entries found',
    '.st': 'No entries found',
    '.store.ro': 'No entries found',
    '.su': 'No entries found',
    '.supplies': 'Domain not found.',
    '.supply': 'Domain not found.',
    '.support': 'Domain not found.',
    '.sx': 'Status: AVAILABLE',
    '.systems': 'Domain not found.',
    '.targi.pl': 'No information available',
    '.tc': 'No Object Found',
    '.technology': 'Domain not found',
    '.tel': 'Not found',
    '.tf': 'No entries found',
    '.tips': 'Domain not found.',
    '.tj': 'No match',
    '.tj.cn': 'no matching record',
    '.tk': 'HTTPREQUEST-has no matches',
    '.tm': 'is available for purchase',
    '.tm.fr': 'No entries found',
    '.tm.mc': 'no entries found',
    '.tm.pl': 'No information available',
    '.tm.ro': 'No entries found',
    '.tm.za': 'No information available',
    '.tmp.br': 'No match for',
    '.to': 'No match for',
    '.today': 'Domain not found',
    '.tourism.pl': 'No information available',
    '.training': 'Domain not found.',
    '.travel': 'Not found',
    '.travel.pl': 'No information available',
    '.tur.br': 'No match for',
    '.turystyka.pl': 'No information available',
    '.tv': 'No match for',
    '.tv.br': 'No match for',
    '.tw': 'No Found',
    '.tw.cn': 'no matching record',
    '.ua': 'No entries found',
    '.uk': 'No match',
    '.uk.co': 'NO MATCH',
    '.uk.com': 'DOMAIN NOT FOUND',
    '.uk.net': 'DOMAIN NOT FOUND',
    '.uno': 'Not found',
    '.us': 'Not found',
    '.us.com': 'DOMAIN NOT FOUND',
    '.uy.com': 'DOMAIN NOT FOUND',
    '.vc': 'Available',
    '.ventures': 'Domain not found',
    '.vet.br': 'No match for',
    '.vg': 'No Object Found',
    '.viajes': 'Domain not found.',
    '.voyage': 'Domain not found',
    '.web.ve': 'HTTPREQUEST-No match for',
    '.web.za': 'No information available',
    '.wf': 'No entries found',
    '.wiki': 'Domain not found',
    '.work': 'Not Registered',
    '.ws': 'No match for',
    '.www.ro': 'No entries found',
    '.xj.cn': 'no matching record',
    '.xxx': 'NOT FOUND',
    '.xz.cn': 'no matching record',
    '.yn.cn': 'no matching record',
    '.yt': 'No entries found',
    '.za.com': 'DOMAIN NOT FOUND',
    '.za.net': 'HTTPREQUEST-No such domain',
    '.za.org': 'HTTPREQUEST-No such domain',
    '.zj.cn': 'no matching record',
    '.zlg.br': 'No match for',
    '.zone': 'Domain not found.',
}