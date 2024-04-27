# Desc: Data for training NER model
# Available entities: FN, ORG, TITLE, STREET, CITY, REGION, POSTCODE, COUNTRY, TEL, FAX, EMAIL, URL

corpus_lt = [
    'Grafo (H) Dvaras kavinė UAB "{Hovalta}(ORG)" {Algirdo g. 9b}(STREET) {Maišiagala}(CITY), {Vilniaus raj.}(REGION) Mob.: {+37065945402}(TEL), {+37065590907}(TEL) El.paštas: {info@grafodvaras.lt}(EMAIL) {www.grafodvaras.lt}(URL)',
    'PROTECTIVE COATINGS APSAUGINĖS / HIDROIZOLIACINĖS / GRINDŲ DANGOS {GENADIJUS KAREIVA}(FN) {Pardavimų vadovas}(TITLE) UAB "{Line-x}(ORG)" LT {V.Bielskio g. 6}(STREET), {LT-76126}(POSTCODE) {Šiauliai}(CITY), {Lietuva}(COUNTRY) Tel: {+37069858099}(TEL) . «  el.p. {genadijus@line-x.lt}(EMAIL) {www.line-x.lt}(URL) PASTATŲ ŠILTINIMAS',
    'CD-R/RW, DVD +/-R/RW, BD-R/RE, FLASH Kompiuteriai ir komponentai Skaitmeninė technika MediaSpektras LED ekranai Stovai, deklai, dežutes Maitinimo blokai, laidai, ausinės {Piotr Jasinski}(FN) {direktorius}(TITLE) UAB "{MediaSpektras}(ORG)", {Pylimo g. 49-3}(STREET), {01137}(POSTCODE) {Vilnius}(CITY) Tel./Fax {+37052608260}(FAX) Mob.{+37067604754}(TEL) El.p. {piotrjasinski@dvadr.lt}(EMAIL), skype: piotrjasO0',
    '{HOUSE OF PRINCE}(ORG) {Ginataras Paukštė}(FN) {prekybos plėtros vadybininkas}(TITLE), UAB \'{House of Prince Lietuva}(ORG)\' {Verkių g. 29}(STREET) Tel. {+37052722790}(TEL) {LT-09108}(POSTCODE), {Vilnius}(CITY) Faksas {+37052722757}(FAX) {Lietuva}(COUNTRY) {gintaras@prince.lt}(EMAIL) Mob. tel. {+37065256656}(TEL)',
    'S|E|B {Tatjana Radzevič}(FN) {Draudimo ekspertė}(TITLE) {Vilniaus regionas}(REGION) UAB {SEB gyvybės draudimas}(ORG)   {Saltoniškių g. 29/73}(STREET), {LT-08105}(POSTCODE) {Vilnius}(CITY) Tel. {852431675}(TEL), faks. {852732986}(FAX) Mob. {861623726}(TEL) {tatjana.radzevic@gmail.com}(EMAIL) {www.seb.lt}(URL)',
    '{Algirdas Morkūnas}(FN) {Sabelija}(ORG) KONSULTACINĖ FIRMA tel./Faksas {52758866}(FAX), Mob. tel. {868676491}(TEL) {Laisvės pr. 77B}(STREET), {Vilnius}(CITY) {a.morkunas@darbusauga.lt}(EMAIL) {www.sabelija.lt}(URL)',
    '{Božena Stanekvič}(FN) Mob. tel. {+37068263746}(TEL); El. p. {BozenaStanekvic@one.lt}(EMAIL)',
    '{inter cars}(ORG) automobilių dalys    automobilių dalys ir aksesuarai {Ukmergės g. 317B}(STREET), {Vilnius}(CITY) Tel. {852491070}(TEL) Tel./faks. {852491071}(FAX) El.paštas ir užsakymai: {ukmerges@vilnius.intercars.lt}(EMAIL)',
    'VILNIAUS UNIVERSITETO PRIĖMIMO KOMISIJA tel. (8— 523662517 r (8— 52366255 » faksas 852366254 el. paštas v1ec13me©vu interneto svetainė http://www.studijos.cr.vu.lt/ sesaarrenenatonnntsamoto8b91b0m 0100992 naprotetoonast0bono2ben0220002m 040700000900000000 m009: 2429000000 m 0878072400 m 120007000 m0200m 0000220000000700 m 2200922008 mm0000078m 0090700400990090020 m 0414090000002204704  0204940000 m01v002m0m0mm00 nantask0nm00m04004m6m0007m2mątnangtEtan2 nn mannanmanonsonanonananSVaDS monennoognoaMEmEEuramtaS Sa nEEnE m noma',
    'VILNIAUSUNIVERSITETO PRIĖMIMOKOMISIJA tel {8523662517}(TEL) r {852366255}(TEL) ofaksas {852366254}(FAX) elpaštas VĮeCIameru internetosvetainė httpwwwstudijoscrvult sesaarrenenatonnntsamoto8b91b0m0100992naprotetoonast0bono2ben0220002m 040700000900000000 m 00912429000080 m 08278072400 m 120007000 m0200m 0000220000000700 m 2200922008 mm0000078m 0090700400990090020 m 04174090000002204704  0204940000 m01v002m0m0mm00nantask0nm00m04004m6m0007m2mątnangtEtan2nmsmannanmanonsonanonananSVaDSmonennoognoaMEmEEuramtaStanEEnEmenoma',
    'siEIB {Tatjana Radzevič}(FN) Draudimoekspertė Vilniausregionas UABSEBgyvybėsdraudimas    Saltoniškiųg2973LT081095Vilnius Tel 852431675 faks 852732986 Mob 861623726 tatjanaradzevicOgmailcom',
    'OF PRINCE I i {Gintaras Paukštė}(FN) {Prekybos plėtros vadybininkas}(TITLE) i UAB {House of Prince}(ORG) {Lietuva}(COUNTRY) {Verkių g. 29}(STREET) Tel.  {+37052722790}(TEL) {LT-09108}(POSTCODE) {Vilnius}(CITY) Faksas  {+37052722757}(FAX) j Lietuva 0 j {gintaras@prince.lt}(EMAIL) Mob. tel.  {+37065256656}(TEL) p.',
    '{Tatjana Radzevič}(FN) {Draudimo ekspertė}(TITLE) {Vilniaus regionas}(REGION) UAB {SEB gyvybės draudimas}(ORG) {Saltoniškių g. 29/73}(STREET), {LT 081095}(POSTCODE) {Vilnius}(CITY) Tel. {852431675}(TEL) , faks. {852732986}(FAX) Mob. {861623726}(TEL) tatjana.radzevicOgmail.com {www.seb.lt}(URL) 9',
    'i aaa X {Robertas TARGONSKIS}(FN) {Vadybininkas}(TITLE) AB {Higėja}(ORG) Tel. {837310727}(TEL) {Savanonų pr. 339a}(STREET) Fax {837310733}(FAX) {LT-50120}(POSTCODE) {Kaunas}(CITY) Mob. {865273645}(TEL) www {higeja.lt}(URL) Ei.p. robertasYhigeja.lt',
    'Aprile a ip Inji ien Espo EK in babbino eeenmizrigponii p tagai T PTE IpoE ili is Aku CE E ka NICH Ša iii ESU MEI eat mas iai E eri iš, Iafii Ašvos Ii js lei e Elipi ET i ARA Tiki iflintilisi reiia kiai Afeakiao io raktais Epitipol Ji aPilio SRT NN ii iiių i i io J aai Ti ser Sil kiai ai UEI Jai p aa sai M To ii Kitas ias I I unerac TARGONSKIs ji E i EE ais a ng bertas TARGĖ gestas it, Rial ae lip sai 1 i Robertas TARGONSKIS TI i E IA 1 Jo vadveininks TT Fasa Ro rie šktals šitas a gelb Aagingaaissi Ei IIS gi k siais Sau aa ai saga ilkII i ili UE Milio p1el 8+37310712711 E si Devas pr. 33Ša iii Ei iriaitik Epson plliojss Fa B 2973107133 ET iii ona 0120 Kaunas šia ipili Aieadiji Mob {865273648117}(TEL) si wwwniadala ITIL riai El plrabertasaNigoja i sriti ania Dlana iui Jekesas ili Mei',
    'LOLOR + XX 0091060444004700+ 4 Ctia.DiuS aAūtYvaA 1 a i m Pertinių ltmo i į Kišit ukio L i V Šiuttnis e, 6 42 Site Ozas, Aūaviliti Kydttkenog Šano pi drūo tid Gris , 4Rb Garris 4, i E D Yu wvasiaa. Hteb4, MMdiutiotą, sinrtrirituanUraĖS į GRIOJŲ Grktitato OV2419 ketini St',
    'X- {Robertas TARGONSKIS}(FN) {Vadybininkas}(TITLE) AB {Higėja}(ORG) Tel {837310727}(TEL) {Savanorių pr. 339a}(STREET) Fax {837310733}(FAX) {LT-50120}(POSTCODE) {Kaunas}(CITY) Mob {8805273645}(TEL) {www.higeja.lt}(URL) El.p. robertasgbhigeja.lt',
    'Y . - - aibė Aljansas i {Aljansas AIBĖ}(ORG), UAB {Andrius Tebelškis}(FN) {L. Zamenhoto g. 5}(STREET), {LT 06332}(POSTCODE) {Vilnius}(CITY) {Versko plėtros departamento vadybininkas}(TITLE) Mob {+37065949520}(TEL) andrius.tebeiskistijaibe.lt wera.aibe.lt',
    'i 1NE- {GENADIJUS KAREIVA}(FN) {Pardavimų vadovas}(TITLE) i iaininisaininisaiisimn UAB {Line-x}(ORG) LT {V.Bietskio g. 6.}(STREET) {LT-76126}(POSTCODE) {Šiauliai}(CITY), {Lietuva}(COUNTRY) i Tet {+37069858099}(TEL) io el.p. genadijus6tine-1 lt asranr x www .line-1.lt g Kg',
    'Grafo G Dvaras kavinė UAB ,{Hovaita}(ORG) {Algirdo g. 907}(STREET) i {Maišiagala}(CITY), {Vilniaus raj}(REGION), Mob {+37065945402}(TEL)+370  65590907 i ki. El.paštas infoG2grafodvaras.lt es Wewx.grafodvaras.lt',
    'ISEUenpoje.B MM Šis Ir se1enpoje.B90Jų se158d 31060659904+ ZO-S6590ZE+ JOIN fe1 sneiujiĄ ereGeIsrejų 966 0p1lBjy BĮIEnOH gVN  9UIAByY svwag GĖ ojv16G',
    '{VILNIAUS UNIVERSITETO PRIEMIMO KOMISIJA}(ORG) į SV į, Padi 71852366251 iš b 852366255 į is, UP laksas 852366254 Į x y el. paštas kvieciamedvu.lt r FAB7S interneto svetainė jų http //{www.studijos.cr.vu.lt}(URL)',
    'Eglė O +07065524441 Miusis e --- piugiainas',
    '{Jolanta Baniulienė}(FN) {kosmetikė}(TITLE) {+37061184150837}(TEL)  207014 {Miško g. 15}(STREET), {Kaunas}(CITY) -',
    'a Kaas. NE {GENADIJUS KAREIVA}(FN) {Pardavimų vadovas}(TITLE) UAB {Line-x}(ORG) LT {V.Bielskio g. 6}(STREET), {LT-76126}(POSTCODE) {Šiauliai}(CITY), {Lietuva}(COUNTRY) Tel {+37069858099}(TEL)  el.p. genadijusėline-x.lt Ensrnnr x www.line-x.lt',
    '0 {GIEDRIUS ALDAKAUSKAS}(FN) {REDLINK}(ORG) JSCREDLINK81CO  MANAGINI 9 {Putvinskio str. 49}(STREET), {Kaunas}(CITY) {LT-44243}(POSTCODE) Ų k Ė e Ė M i',
    '{EMKO}(ORG) {RAMINTA MUSTEIKIENĖ}(FN) {Project Manager}(TITLE) M {+37065607456}(TEL) E. info/Oemko.lt A. {Kalvariju 1-3.1}(STREET) {Vilnius}(CITY) {LT-09310}(POSTCODE) {Lithuania}(COUNTRY) os vo sp9 Osxi 9',
    'andnst, k š zu ds Čomas Aeediis, Ė. RE a K t . , į ai 2 008 į . {Dovile Kharkan}(FN), 4 A Artas E a as, + į ę ladorcinaaų com za k Hedera, j r 4',
    'Ms, os tan VaAizng STEčĖnyo ŠišTEMOS MW sisiep,, Petris ko šonas {Arūnas Čebatavičius}(FN), ga . {V.Krėvės Pr. 53}(STREET) UT-{50354}(POSTCODE) {Kaunas}(CITY) Mob g 68654585 vals sd --a Www. YSsisteps lt',
    '2 8 L a 3-7 ATB Ss. 2 4 ais zi SEs2 k.M-M- 13 SB ššS 4-2',
    '{Eglė}(FN) {Blakstienų priauginimo meistrė}(TITLE) G V {+37065524441}(TEL) E I T L IA SH i S elitlasheskaunas BAE IENSIONSe f Blakstienų aminavimas priauginimas. ElitCashes',


    '{EMKO}(ORG) {RAMINTA MUSTEIKIENĖ}(FN) \
{Project Manager}(TITLE) \
M {+37065607456}(TEL) \
E. infoOemko.lt \
A. {Kalvariju 1-3.1}(STREET) \
{Vilnius}(CITY) {LT-09310}(POSTCODE) \
{Lithuania}(COUNTRY) \
os \
vo pS \
Os \
9',
    'ki. ar KA "ps En \
ų m "K i - A Li 0 9 fa i \
ka KIT. kas + MN d 7 \
\
a ų a iš ų k , 28 pt. \
\
į 2423 Šios "a d A 3 \
\
rj . \
\
iki ji 1 , į 4 i - i 4 - \
Nkiinaas jį į i a i 4, \
niai Ar Ad Ė ii \
HOUSE OF PRINCE "27 a 42 alia ma i\
si is 4 m ,\
- 2 T \
{Gintaras Paukštė}(FN) a \
surastas {Prekybos plėtros vadybininkas}(TITLE)  i a \
UAB "{House of Prince Lietuva}(ORG) al - r 2 \
i {Verkių g. 29}(STREET) Tel {+37052722790}(TEL) wo a \
1 {LT-09108}(POSTCODE) Vilnius Faksas {+37052722757}(FAX) ai ki \
d ietuva r \
į i tel {+37065256656}(TEL) pro \
a ntarasOprince.lt Mob. p a',


    'iš r Paamč B -\
.\
o .\
- Ei e -\
į i 2 i S I\
e . Mrma-\
saaa i ,\
si į e 8 tai k- . az\
wi a pr\
e po par ri ta. i i\
ar ar "ai ikiaaaiaai\
29 e m a k ,\
is us kas an i\
I ją iai k. 4 a\
i ar r i\
"+ i kui i 2 1 0 ik I a\
a kit + a -m. ų - b-\
- 2. Visi i jo h i a. 8 2 i.\
uk" "Mr T i i .\
m a r . T Ta Usui aa S.\
ias - Kia 4. 5\
Ua akli. a. si i ip. tų\
iš - 24, kar si į d r\
uu sa - ai "mai i\
Ala m 6\
l ši I li +\
- ai e\
a. 4 ą e m a\
art 6 - . a...\
liki Vai. A. Dai ią\
j- sr RNW r Ša č T lę . i\
FIS Kali Ę\
S pra a i\
p ta, - p taų, .\
sis S m\
tara ptaitio, ESS i gite i ji\
BSS ES Uštiči\
AE eo T 175 Tak\
BEF S Eto A -.\
3 EG Bs\
 Y tį A Ė',


    '- cor, IIS\
I r I V 9\
Bopuat\
, 2 dUKRAINIETIŠKIVALGIAI \
{Irina Šauklienė}(FN) UAB {Ukrainietiški patiekalai}(ORG) \
. {Algirdo g. 5-2}(STREET), {LT-03219}(POSTCODE) {Vilnius}(CITY) \
{Restorano vadovė}(TITLE) Įm. kodas 302472497 PVM LT 100005329119 Mob {+37061805003}(TEL) "El.p. IrinaOborsch.lt 3 \
r {www.borsch.lt}(URL) ,',


    'Šš {sinerita}(ORG) Serviso centras p. \
e Spausdintuvų, kopijuoklių, fakso aparatų ks r \
remontas ir profilaktika i J \
\
e Meistro iškvietimas telefonu as j \
faks 52338826 el.p. servisasdsinerta.lt \
{Naugarduko g 41}(STREET), {03227}(POSTCODE) {Vilnius}(CITY)  {http://www.sinerta.lt}(URL) j',


    'AS {RAMIRENT}(ORG) VILNIAUS FILIALAS \
D {Titnago g. 19}(STREET), \
i , LT {02300}(POSTCODE) {Vilnius}(CITY) \
{Denis Kostyk}(FN) Tel +37052321778 {Klojinių ininierius}(TITLE) - Mobil {+37061540733}(TEL) projektuotojas Faks {+37052322141}(FAX) denis.kostykGramirent.lt \
{www.ramirent.lt}',


    '{Regina Nasickienė}(FN) {ERGO}(ORG) \
{Draudimo konsultantė}(TITLE) rem \
- UADB ERGO Lietuva \
 - 4. Kalvarijų atstovybė 3 Kalva a: A24 \
ies 7 {LT-08211}(POSTCODE) {Vilnius}(CITY) r \
Tek iB 52777939 set - Mob.tel {86126440514}(TEL) Faks {852685843}(FAX) Ę- ERGO draudimo grupės narė a a \
iek į Leg OS',


    'a E. a ia apr, Naoto sta a O o ŠE \
akiai RED pre ini SS Taetani Atia : š\
6 ralis. E Otaka ia ,\
Noe ET Ina Rs VS Rs sodai a EST\
Lia Te das O gi Makoto ŠE ES ss T Va OSA\
0 ae era De S į\
5 si Ė 52 a Kia e EA 47 07 votrenejjias\
20 marą p i iais se air Dai\
ata ES Sinai titano sa\
ek TS a mk Pitos. tirs . :\
is Par ua o Mia ia ia ra\
x 2 3 T o s a ą 4\
TaĖ : , I Ąą alis sai. a TT leirisio 00 skir,\
+ is 0 sd 4 a ar gacamamss LP Ara rai r Tpso\
t rrEZESTE S ar\
snd. T Toiilą ss ss a iai p i\
m Dai Load ni Fua --mm kū j a Ta Zaggtiimnis - m P - ms a\
P Az FSK FTUHRTO VERTINIMO\
saitų 20 a 000 aa Ššrsę- ap is as asų Aa Ki Fr B 4 j j j y j į k P\
"ELO gaa T T sr i šk kūnai , sa R Ė kinai m. r Fa\
a 08 mas\
a , ir m rą a\
ir ra , r i. F r 3\
2 m M. S P\
As ORE EEE Er Fm EK Et\
j X Fra Ša su a m. Ąą i\
į Mid t I I Gili a ka Rana" ad p. -\
Iokilnaaiamiaia. ir. kilnaimameais: tiertn vartinfniauc acichtantiao ,\
k + TKAT E TA Mt PIRSPTCEITE TAU TSS LAAELRSS VAL IR B Kia CL. DOC Fi.\
ai\
Š s - r i i ki m aa is AS a, Ma Ta Y\
arm EEST E EE DT TT 2 E to. bana r 54 PF AB ra E -.\
ai. 4i 6. M I , 7, a g. mv fr EL į 2 P\
SESI šį MR. + ir: IVECUJZ. LTE... 2 LE UL U+ 09\
Ą p - a - g i\
VvVIENIEUS 11 a vs EI Kai\
gai Press lr oriai f G fm t p. V. ima 4 0 Ja im,\
7 AA Tas Ei ia, ap Ša D k a. r B ra -iIia m T. r\
ast 0:8 S: ui 8 AO ė Aioll Niud a V. al s Jr dia: 5 a E a P ae\
ri š vėjas 32\
EE mų. abu E VA LT mą prie "ai. oiaa\
Di. D.. DtivabvčkaaAaITiaii. COm\
Eieoyko: Įidiaio ALT i A į Lt sr\
k Ea ė\
WI... TAM mi. 1\
k PARA i 8. BI\
WWW. TVD.lt\
x. p ,\
a 77\
k Fr me + FI r pras, t arenas r p ks šo E r iš x aa AP 8\
"LF EF K r TF i: Ar i į P, 18 FF iš A 8 į r s\
VLE FF NIE LL FN ROA LA EV OAS Vl, E NELAĖ NV PAST VE T NK E NV V\
a. s09 3 jp gpreinų Tal Pt pg G FS ar agiamaaii 3954 T. mai no\
i , į ED FK Y Elė V bob i FF J fam: ba EF FIAT ERA .\
p. i E FEVN E AP FREE Vv. V Lali VE Vu V Li Lo EEE VE EE EF Vt o 0\
6 ni aus Aialaita m. ar ZR Ri nr EE Er RPN ET EIK E KFNVYEB KA CC ai\
p pa FKE TTK E EEE E KFYEE EE NN. FEFF FK VA r.F Ąą i Vai Ą kų ta. .\
i KHR. FE FF EE Ft J. LBA XEC pie J FI VIN i FĮ CA VAL L FI Va E\
"A+ Vi a E FC J. LPA FEI i PT VY E TF. A š t\
kZ WP Vv L il E. ud albo L ta. Ragas" E Sp E Či w i j :\
si sr er a. šiai aa a p m i i T I - r: a\
FK KN EOS TEC SIERIERA Į DEBCY IE KT,\
avi Gp Na. E FC FN EF FT FX KN. i FR Ą\
"V V L. v E EFF VIFP NE RER B Šiam t i T 3\
k e , 8 Ė Či\
7 r k. 1\
D I. 7 r p\
par ji i Ravš g jj\
i k , č il',


    '. , a. 4 Ta AT\
š S\
t ir 3 aki\
t\
- Et ja\
Kati\
j 2 S\
s k 4 k\
j r as a i\
r io R\
ai\
P. 4 ui\
-\
i kr\
y LT\
šo Ė\
, as a\
j i\
8 4,\
t\
i akt\
ri sl KI V\
i M xi.\
r Jan\
iot a\
š ša kasis\
fi j\
Hai tai\
Ė r g 2 t kada AB na Kia k\
L , šį T S giš. I Lia i\
res i f 4. ET Urio B ja Ti\
į , į r Loa ei Yra IA\
kom , Aro p Ep j Mr - i i aa Vas\
Ę : Ee nadl tą. rija Či didi Bs Soso\
kų spa" , 5 r I- Tr iš Tik 8: seip "Taa Fo\
, f tt ja , Ų tani i Tata T. Ą 1 Ari A\
ę 1 p i. a sE Manic aa AE RS Ė pats Di GR ja Teų 2 8\
į z 7 r j diijaė I o AO atolų Mg ve ta a aa si arši JS9O I\
i p , i AGT G TE V ii aTa MS as\
ją Ake j į sirai L r s8:7 iais ŠIkials  I It V rs SS MS SE G as\
/ fa j Šai KT b airiai. Eik E BRT Bt moja ai AARC aaa E ES to MS A\
, r 190 Pr id, es sti Taa rs Za Jaeiiais Kaiasi ati son ra oi ikos" Jei sin\
4 gei s GMO Taa Ad Akis CE ii Pili šreko us" DIY t Es bri 2 Mintimis Ta,\
iz i į BO BAI, Ar TŲ p p namai Aira Ta R ai jai MKE "iptiai sosrssi t Kosos EEE\
p i ba ski salė 6 į i kas Skai Oo aa IO ero Ailaibi T ai ak ias Piiakėis T g į\
j sto gta k ats ečų pk akies S a S ro is. Za E tagai "Ana. Gas En D\
4 4 Ę kabo Edi Epakisė 2 5 T ss ai ia, 80 Ska sell akys T šanai Mila 7 JP akos I ar\
A , r r i Vartų, saitą af E tibia ali tia oi eo as , k E st a aaa pries Šis Eaaika AE sak si vio uno AP\
t ra r ats Aiks eriių ti 54 4 tia 6 kiek T Nagi anairnrėes - - J. ir io ta 0 oi sl ,\
A iz iais Kia P AE j "aiiaiidia AIA Oi sr ISK 5 eetisi Veseiyii aliss. ee ja 4 Tos Paiaa\
Ė ii , Ą 258 6 af atišias cooi ra na KES JP o r ui Ar 8 4 4 t vi Ta i aa eisi Too Cis p\
, , t Arija įnag 7iiOŲ AL efilaio a UE a Lat Saias "870 est ira Taranto Oita agto said iagpiaaniiaosi jo Kg 2O "as riai Gas aki i , 4\
+ Kk Si to gig Ska setai Talkos At a SiTe ta Ei e air hasiar S Titni Zak aut: T SE Ė Eiaii I ata, TER T ša is ai\
ą 4. 2 Ų 2 aso son kis nai ių Valo ciaiką E siaą ata si Iron Dos Yra, tao SE en 4 S Sai ane Euros 1 ini a To na\
AE są rs kasų Uri saaa. Pt oakis Drs Ėtte so Sr LU čia g at E sūris Šia sak okra LET Halis šau ša Kritinės S To 1:\
ais a Ą ar sc ki jr eat p Po Dale ra Adis. RI sai. v D naanajės S BBL CO vainikai eto ašis RE RS te +. 27" Atass p\
Serviso f 181 r g Pa vaad 2, lp Vršs t ais Aid sat Kk Ma ša ai iai AB I Pa, ap Seat ka ri am oras 4 itisči aa US A\
x "ns Ara Ek si Tai Ka ik S Ks rr ata Rais BTI I AS go o Do Makas I MS o arų\
i krona dos iaaki sptsters egkiniI anbditKre take Garso Jia S. VE sa os M MST T Tenka et S Ass 5 Asia. gos jo\
: narė Gizos Terasa oset gi bs S Es tas Jų rope O Tab Ms sara aaa aros MM NP S g aa TEO\
si ti sakai Kra RRKT iol Earn Mai rai Vina 2019 Aeiškii SE o asi ai ačių Taa vinių toi ses Nui d i\
Kt as in uoisi  Ns sai CpI Sp It Mirta S Sakei akis TAS i Kakas, MAS SDB Us Km ka S NE SE K gmT aig ai ais Ai ais r aa\
jį a 1 sr r 5 to Ąpsilks ai Sari tt, rs Sa ka ašS ak Ųų RS Muy I V Į sr Tais a 21" kasis is kN ia 2 p\
i iu atei Mais aaa atkasa KAUKAS TD ap Ero US TA LEI paie ri pik gos 5 -\
i "sė "tai Vo Gr ka kraitis Sk TT As ES TO Boa Ek BEE Kakas SS i\
a je , S V atioio sri Mai Kė js Morka ės JET ri Pasa as Kakas E r San m E S V EE GT k ros Est ais i\
i g Li A t Kanas k Irun Sea a ala GKLE as Rei a T Casi J ata Ziiias I atė ų raigia tatteis ora Dao Kiek į sri os\
š . 4 AX r niek setai asai Tj "te Saitas oO SAS M Eau asi č ia\
i Aaaa Mis Kk kia Ls IS pKsti Es eš xe taas darei ES GK ae ia\
a akiai, keis saaa Sis AAA ias aria sakai Oktanas DDT Aiks Tl AT ja Baro ja T eat Ap Uma Kappa 1\
Ei, ša ais VO AS aki Vi šo st ai arr Tos Tasas 2 Lb gaaki SE A K os ATI ao aa E AP ra ia ki ,\
ir. sa es SA Iš are Gia Ti TK G S GKS AR AE ESA\
j + t si aks st ep Jis Wypaias Sis TM sviiaki ao Pa Ainiai oda t Ta AT Aina sanis Mapas ganė p Eto ra\
4 i į ė Sin sro ae a Gas It a klija Aaaa Ki gai Tt ati is ala ia r y\
i j ogi aiste Latas "pi Anai iso o ESS Ss eis Pei ii osios Clap Aa KS J sių . pičias Uaė\
ti . į i Tais ai Eos aaa ata. ata akiai S ALŲ, A is aaa Pa , VS ma Zz  - i L. , i\
97 j Ius ias ji Ka Garis Ua Vi aiš aru, AE aa "a vis S ka io į sa Ei ji I ę i\
6:5 voniai od sači ass sių Bt masis id Aue S kata r g 8 lao a gta Ei į "Ak r r a A g į r\
o i Ti Manto Is i ri Aria šu 0 i šiai i Kai Ta T tas\
ų 4 7 gi Nurgg sfB star Kata ali varai, M Ta kr rata sy ak pyiia tolo i tail aaa ias Li Megė as rų i j j M nis ją\
r , sai ie ii iii i E ao j r ietal jogas A64f B YdA. as. getą Tania V i a 2 ,  YZ\
ai t g i tė Ir G aki Tas Tiot sat alūs 0 Jr SK if av a r 4719 ė\
. į k jj jr a iai sie i ala ska sein AST iĖ Epas ar sias A JS 2 / i j\
ao šalis adis arai ta GEĄ se šasi Tu a šlapi Mios Ha Iš CE ae E i :\
j ara Irakas. Aaa Opel Kas Eria "Bi S USS ads rdt Si Ai Ei a S IKS 57 atakas giigk i\
m keri Kg Sa EMS Traian Tas As aaa E ia :\
a . . as ios ien kAp Uris ši V tris S Attia, Lkskų Aroiiiis JS A i\
ik. pirkliutėsiiDerauto.lt T WWW. m\
"T A , p stati diiaai t Duaderke ais asai ri noios 0 Tso ti 0 ar g P\
2 k š Veino Tos a oriai, Kits Traagtkii tao kratas i į k\
p er desi a st Taka ss oMŲ Patri Al GR aa aaa\
a į Či ao ES eitu Tarit ae Abekršios nia sass a aa aka\
re y r Ka dkšioi al ims. ŠOKAS Da ar 4 evis T aklėn re Jasiiyka r\
i , į sans, tatoo tetis abato o ras tros Mo ius ki\
pome i šąfS Abi 0 tais, dk asi kepti o Eksa e Mesa nari Biko a 3\
ką, d r p S k sti 4877 Viso NE DNR Asi Ais Ve Palais ii ies Fint r\
2 Ke L pr ių. S p cats Aa Eau kos X 409 4\
"An as j š tar Asi si I AS E a an\
das ėvis i / i į sai isto a Stai ZA akis str sPuafi d e 4\
ra -. P i r ir sias "ai Airiui a arsoi a r j ,\
sa I ist 5 ci 1 asa sa sai Las E šs- aa 2 j p\
ia. di. i ar LD sis aa g 3 iui UI Toi Rją ia t sa f ar 5 r. y sr',


    'BFALOA LC "ti 00 AM Luis Rrekių {prieziūros vadybininkas}(TITLE) \
i {Vytauto g. 122}(STREET), LT {76340}(POSTCODE) {Šiauliai}(CITY), tel {+37041420640}(TEL) faks {+37041420639}(FAX) Mob. tel {+37068223672}(TEL) el. p.: balticOOsparinc.com, ww. {sparbaltic.com}(URL) \
r "T. M ĮOrarą i Wi ša F ,',


    'E. STANKEVIČ PF \
{Edvard Stankevič}(FN) \
\
{Imonės vadovas}(TITLE) \
\
Tel: mob. {86862620}(TEL) L T Ei \
\
El.p.: zibenaOone.lt ag ši',


    'Distribution 8 Logistics \
- {SERGEJ ŠUMAKOV}(FN) \
Vilniaus filialas \
{Padalinio vadovas}(TITLE) \
{Kirtimų g. 49}(STREET) \
{LT-02244}(POSTCODE) {Vilnius}(CITY) Tel./faks {852602187}(FAX) Lietuva Mobil. tel 86565 D 265 \
{www.sanitex.eu}(URL) i m. EI. paštas vil.retail1Osanitex.eu',


    'URMAS \
JŪSŲ SĖKMINGAM VERSLUI UAB ,{SENUKŲ PREKYBOS CENTRAS}(ORG) \
{RENATA SAVERINIENĖ}(FN) \
{Realizacijos projektų vadovė}(TITLE) \
V0LO Box Du ar \
br V Tel {852492374}(TEL) Mob. tel {865628277}(TEL) iais g. 244 Faksas 85252520107160 {Vilnius}(CITY) El. paštas rsaverinienedsenukai.lt \
{Lietuva}(COUNTRY) {www.senukai.lt}(URL) \
MB i K aa IM ORAI A" " P IS M" i r TP PA T LS T',


    'Kai \
Pernod Ricard \
i r o V \
{Lech Stankevič}(FN) \
{Tradicinės rinkos ir HoReCa pardavimų vadovas}(TITLE)/ \
Traditional trade and HoReCa sales manager \
UAB "{Pernod Ricard Lietuva}(ORG)" \
{Mėnulio g. 7}(STREET), {LT-04326}(POSTCODE) {Vilnius}(CITY), {Lietuva}(COUNTRY) \
Phone {+37052462277}(TEL) fax {+37052462278}(FAX) mob {+37061510018}(TEL) lech.stankevicaApernod-ricard.com',


    '7 ID \
or \
NAD \
"S šneao J \
{Rimvydas Valorka}(FN) \
{Pardavimo vadybininkas}(TITLE) \
 \
Tad 8521095355 UAB ,{Philip Morris Baltic}(ORG)" Faks {852756901}(FAX) {Jogailos g. 4}(STREET) Mob. rel {868731680}(TEL) {LT-01116}(POSTCODE) {Vilnius}(CITY) El. p. rimvydas.valotkaOpmintl.com',


    'r- Belcoro \
ja Softer feel for comfort \
FRUITiELOOM, \
- FRUIT OF THE LOOM šenklas - tai Jūsų \
 drabuio kokybės garantas. \
Mes įsipareigojame utikrinti kiekvieno \
gaminio kokybę, patvarumą, patikimumą \
beirekologinį priimtinumą. i',


    'Kara T saios PAS kio \
T Tan aa \
a Ls ao \
Lapis AS o \
Ya Pitakols ss maki si 6 ai \
Š oi. Las I. Irkani CIF ĖK \
Ė a P AB pi 078 \
ių. Plaaibšacių os 500 Mia \
Kratas aa aš V "E 4340 ix. k Jar 4 \
rima - . i \
r, \
i \
r \
g t \
j iš \
- 3 L i  -4 \
atiana Radzevič \
2a sv i į į EA \
21 EkKEnerio \
- i + t4an8 ad tmi o Nur \
i \
. D OSINNNAĄAS \
- ziighaoao rirotirnni mal \
8 DVYVDOES USjdciuūlUiitiao \
KTII.-D. + 15 Li UV 105 VIIIIIUS \
Ė. Sal są pa p į Pp PA 27 S EN OE \
sf a TF. e D R TaAaKkS ik FD E \
Č j j ZL 4 E" d Š Ą A T "a I T 23 , Ko. i AI Ar T 8 A eg \
. Ystą m a ps \
J , ke W se "si \
A sin iša ai aoi ia \
e Za ras j Izeviclo0Wgmali.L0I| \
, OAS Lo VIA 1 S \
-a',


    'VILNIAUS UNIVERSITETO \
 \
PRIĖMIMO KOMISIJA \
 \
pgYNI Vėtp \
 \
E. S e tel {852366231}(TEL) į \
 \
"Aš , KA {852366255}(FAX) m DB faksas {852366254}(TEL) IA s el. paštas kvieciamedvu.lt i \
 \
m Yras V 1 nė Et \
interneto svetainė i \
http//{www.studijos.cr.vu.lt/}(URL) p \
 \
M sw mų, E',


    'd 4 \
k 8 aa \
- aibė \
{Aljansas AIBE}(ORG), UAB \
epeisškis L. {Zamenhofo g. 5}(STREET), LT {06332}(POSTCODE) {Vilnius}(CITY) \
i i W pi Mor /a iai ia Ii \
epartamento vadvbininkas Mob {+37065949520}(TEL) k At 9 140 I 8 ii y. t Ai 8 į i tu i Rr \
andrius.tebelskisdaibe.lt \
{www.aibe.lt}(URL)',


    'įsi is \
pė E pė". i adenkrvgkjų 70 sava garso ta mą e pos atima \
i eggp ima saaia 0 GgptiiSO Tai T į t \
Katiaųs ABO ar ias Si Nisa tė t \
9 ta \
{Vyresnysis ininierius} id \
Tinklo eksploatavimo departamentas \
{Vilniaus tinklo eksploatavimo centras}(ORG) \
Tel {852368159}(TEL) Faks {852783340}(FAX) Mob +861880412 El. p. aleksandr.aleksandrovūteo.lt \
TEO .LT, AB, {PALANGOS G. 4}(STREET), {LT-01117}(POSTCODE) {VILNIUS}(CITY), {LIETUVA}(COUNTRY), {WWW.TEO.LT}(URL)',


    'i cinarbei cc... \
e Spausdintuvų, kopijuoklių, fakso aparatų \
Ta remontas ir profilaktika \
e Meistro iškvietimas telefonu 7 \
tel 52139310 el.p. servisasOsinerta.lt \
{Švitrigailos g. 11C}(STREET) {03228}(POSTCODE) {Vilnius}(CITY) http//{www.sinerta.lt}(URL)',


    'Tea a \
i sa ia \
"sarge ia ar Aroiaaajų, Rites \
"rikis t S mina Tauras penikgi pašoko \
ES AlHansa \
{Ieva Blaukonytė}(FN) \
{Investavimo vadybininkė}(TITLE). \
Lazdynų klientų aptarnavimo centras \
Sostinės regiono skyrius \
{Architektų g. 43}(STREET)/ {3104221}(POSTCODE) {Vilnius}(CITY), {Lietuva}(COUNTRY) . \
Tel {852168950}(TEL) Mob {861432573}(TEL) Faks {852450008}(FAX) El. paštas ieva.blazukonyteGhansa.lt {www.hansa.lt}(URL)',


    '. , a. 4 Ta AT \
š S \
t ir 3 aki \
t \
- Et ja \
Kati \
j 2 S \
s k 4 k \
j r as a i \
r io R \
ai \
P. 4 ui \
- \
i kr \
y LT \
šo Ė \
, as a \
j i \
8 4, \
t \
i akt \
ri sl KI V \
i M xi. \
r Jan \
iot a \
š ša kasis \
fi j \
Hai tai \
Ė r g 2 t kada AB na Kia k \
L , šį T S giš. I Lia i \
res i f 4. ET Urio B ja Ti \
į , į r Loa ei Yra IA \
kom , Aro p Ep j Mr - i i aa Vas \
Ę Ee nadl tą. rija Či didi Bs Soso \
kų spa" , 5 r I- Tr iš Tik 8- seip "Taa Fo \
, f tt ja , Ų tani i Tata T. Ą 1 Ari A \
ę 1 p i. a sE Manic aa AE RS Ė pats Di GR ja Teų 2 8 \
į z 7 r j diijaė I o AO atolų Mg ve ta a aa si arši JS9O I \
i p , i AGT G TE V ii aTa MS as \
ją Ake j į sirai L r s87 iais ŠIkials  I It V rs SS MS SE G as \
/ fa j Šai KT b airiai. Eik E BRT Bt moja ai AARC aaa E ES to MS A \
, r 190 Pr id, es sti Taa rs Za Jaeiiais Kaiasi ati son ra oi ikos" Jei sin \
4 gei s GMO Taa Ad Akis CE ii Pili šreko us" DIY t Es bri 2 Mintimis Ta, \
iz i į BO BAI, Ar TŲ p p namai Aira Ta R ai jai MKE "iptiai sosrssi t Kosos EEE \
p i ba ski salė 6 į i kas Skai Oo aa IO ero Ailaibi T ai ak ias Piiakėis T g į \
j sto gta k ats ečų pk akies S a S ro is. Za E tagai "Ana. Gas En D \
4 4 Ę kabo Edi Epakisė 2 5 T ss ai ia, 80 Ska sell akys T šanai Mila 7 JP akos I ar \
A , r r i Vartų, saitą af E tibia ali tia oi eo as , k E st a aaa pries Šis Eaaika AE sak si vio uno AP \
t ra r ats Aiks eriių ti 54 4 tia 6 kiek T Nagi anairnrėes - - J. ir io ta 0 oi sl , \
A iz iais Kia P AE j "aiiaiidia AIA Oi sr ISK 5 eetisi Veseiyii aliss. ee ja 4 Tos Paiaa \
Ė ii , Ą 258 6 af atišias cooi ra na KES JP o r ui Ar 8 4 4 t vi Ta i aa eisi Too Cis p \
, , t Arija įnag 7iiOŲ AL efilaio a UE a Lat Saias "870 est ira Taranto Oita agto said iagpiaaniiaosi jo Kg 2O "as riai Gas aki i , 4 \
+ Kk Si to gig Ska setai Talkos At a SiTe ta Ei e air hasiar S Titni Zak aut T SE Ė Eiaii I ata, TER T ša is ai \
ą 4. 2 Ų 2 aso son kis nai ių Valo ciaiką E siaą ata si Iron Dos Yra, tao SE en 4 S Sai ane Euros 1 ini a To na \
AE są rs kasų Uri saaa. Pt oakis Drs Ėtte so Sr LU čia g at E sūris Šia sak okra LET Halis šau ša Kritinės S To 1 \
ais a Ą ar sc ki jr eat p Po Dale ra Adis. RI sai. v D naanajės S BBL CO vainikai eto ašis RE RS te +. 27" Atass p \
Serviso f 181 r g Pa vaad 2, lp Vršs t ais Aid sat Kk Ma ša ai iai AB I Pa, ap Seat ka ri am oras 4 itisči aa US A \
x "ns Ara Ek si Tai Ka ik S Ks rr ata Rais BTI I AS go o Do Makas I MS o arų \
i krona dos iaaki sptsters egkiniI anbditKre take Garso Jia S. VE sa os M MST T Tenka et S Ass 5 Asia. gos jo \
narė Gizos Terasa oset gi bs S Es tas Jų rope O Tab Ms sara aaa aros MM NP S g aa TEO \
si ti sakai Kra RRKT iol Earn Mai rai Vina 2019 Aeiškii SE o asi ai ačių Taa vinių toi ses Nui d i \
Kt as in uoisi  Ns sai CpI Sp It Mirta S Sakei akis TAS i Kakas, MAS SDB Us Km ka S NE SE K gmT aig ai ais Ai ais r aa \
jį a 1 sr r 5 to Ąpsilks ai Sari tt, rs Sa ka ašS ak Ųų RS Muy I V Į sr Tais a 21" kasis is kN ia 2 p \
i iu atei Mais aaa atkasa KAUKAS TD ap Ero US TA LEI paie ri pik gos 5 - \
i "sė "tai Vo Gr ka kraitis Sk TT As ES TO Boa Ek BEE Kakas SS i \
a je , S V atioio sri Mai Kė js Morka ės JET ri Pasa as Kakas E r San m E S V EE GT k ros Est ais i \
i g Li A t Kanas k Irun Sea a ala GKLE as Rei a T Casi J ata Ziiias I atė ų raigia tatteis ora Dao Kiek į sri os \
š . 4 AX r niek setai asai Tj "te Saitas oO SAS M Eau asi č ia \
i Aaaa Mis Kk kia Ls IS pKsti Es eš xe taas darei ES GK ae ia \
a akiai, keis saaa Sis AAA ias aria sakai Oktanas DDT Aiks Tl AT ja Baro ja T eat Ap Uma Kappa 1 \
Ei, ša ais VO AS aki Vi šo st ai arr Tos Tasas 2 Lb gaaki SE A K os ATI ao aa E AP ra ia ki , \
ir. sa es SA Iš are Gia Ti TK G S GKS AR AE ESA \
j + t si aks st ep Jis Wypaias Sis TM sviiaki ao Pa Ainiai oda t Ta AT Aina sanis Mapas ganė p Eto ra \
4 i į ė Sin sro ae a Gas It a klija Aaaa Ki gai Tt ati is ala ia r y \
i j ogi aiste Latas "pi Anai iso o ESS Ss eis Pei ii osios Clap Aa KS J sių . pičias Uaė \
ti . į i Tais ai Eos aaa ata. ata akiai S ALŲ, A is aaa Pa , VS ma Zz  - i L. , i \
97 j Ius ias ji Ka Garis Ua Vi aiš aru, AE aa "a vis S ka io į sa Ei ji I ę i \
6-5 voniai od sači ass sių Bt masis id Aue S kata r g 8 lao a gta Ei į "Ak r r a A g į r \
o i Ti Manto Is i ri Aria šu 0 i šiai i Kai Ta T tas \
ų 4 7 gi Nurgg sfB star Kata ali varai, M Ta kr rata sy ak pyiia tolo i tail aaa ias Li Megė as rų i j j M nis ją \
r , sai ie ii iii i E ao j r ietal jogas A64f B YdA. as. getą Tania V i a 2 ,  YZ \
ai t g i tė Ir G aki Tas Tiot sat alūs 0 Jr SK if av a r 4719 ė \
. į k jj jr a iai sie i ala ska sein AST iĖ Epas ar sias A JS 2 / i j \
ao šalis adis arai ta GEĄ se šasi Tu a šlapi Mios Ha Iš CE ae E i \
j ara Irakas. Aaa Opel Kas Eria "Bi S USS ads rdt Si Ai Ei a S IKS 57 atakas giigk i \
m keri Kg Sa EMS Traian Tas As aaa E ia \
a . . as ios ien kAp Uris ši V tris S Attia, Lkskų Aroiiiis JS A i \
ik. pirkliutėsiiDerauto.lt T WWW. m \
"T A , p stati diiaai t Duaderke ais asai ri noios 0 Tso ti 0 ar g P \
2 k š Veino Tos a oriai, Kits Traagtkii tao kratas i į k \
p er desi a st Taka ss oMŲ Patri Al GR aa aaa \
a į Či ao ES eitu Tarit ae Abekršios nia sass a aa aka \
re y r Ka dkšioi al ims. ŠOKAS Da ar 4 evis T aklėn re Jasiiyka r \
i , į sans, tatoo tetis abato o ras tros Mo ius ki \
pome i šąfS Abi 0 tais, dk asi kepti o Eksa e Mesa nari Biko a 3 \
ką, d r p S k sti 4877 Viso NE DNR Asi Ais Ve Palais ii ies Fint r \
2 Ke L pr ių. S p cats Aa Eau kos X 409 4 \
"An as j š tar Asi si I AS E a an \
das ėvis i / i į sai isto a Stai ZA akis str sPuafi d e 4 \
ra -. P i r ir sias "ai Airiui a arsoi a r j , \
sa I ist 5 ci 1 asa sa sai Las E šs- aa 2 j p \
ia. di. i ar LD sis aa g 3 iui UI Toi Rją ia t sa f ar 5 r. y sr',


    'a E. a ia apr, Naoto sta a O o ŠE \
akiai RED pre ini SS Taetani Atia š \
6 ralis. E Otaka ia , \
Noe ET Ina Rs VS Rs sodai a EST \
Lia Te das O gi Makoto ŠE ES ss T Va OSA \
0 ae era De S į \
5 si Ė 52 a Kia e EA 47 07 votrenejjias \
20 marą p i iais se air Dai \
ata ES Sinai titano sa \
ek TS a mk Pitos. tirs . \
is Par ua o Mia ia ia ra \
x 2 3 T o s a ą 4 \
TaĖ , I Ąą alis sai. a TT leirisio 00 skir, \
+ is 0 sd 4 a ar gacamamss LP Ara rai r Tpso \
t rrEZESTE S ar \
snd. T Toiilą ss ss a iai p i \
m Dai Load ni Fua --mm kū j a Ta Zaggtiimnis - m P - ms a \
P Az FSK FTUHRTO VERTINIMO \
saitų 20 a 000 aa Ššrsę- ap is as asų Aa Ki Fr B 4 j j j y j į k P \
"ELO gaa T T sr i šk kūnai , sa R Ė kinai m. r Fa \
a 08 mas \
a , ir m rą a \
ir ra , r i. F r 3 \
2 m M. S P \
As ORE EEE Er Fm EK Et \
j X Fra Ša su a m. Ąą i \
į Mid t I I Gili a ka Rana" ad p. - \
Iokilnaaiamiaia. ir. kilnaimameais tiertn vartinfniauc acichtantiao , \
k + TKAT E TA Mt PIRSPTCEITE TAU TSS LAAELRSS VAL IR B Kia CL. DOC Fi. \
ai \
Š s - r i i ki m aa is AS a, Ma Ta Y \
arm EEST E EE DT TT 2 E to. bana r 54 PF AB ra E -. \
ai. 4i 6. M I , 7, a g. mv fr EL į 2 P \
SESI šį MR. + ir IVECUJZ. LTE... 2 LE UL U+ 09 \
Ą p - a - g i \
VvVIENIEUS 11 a vs EI Kai \
gai Press lr oriai f G fm t p. V. ima 4 0 Ja im, \
7 AA Tas Ei ia, ap Ša D k a. r B ra -iIia m T. r \
ast 0a87 Sui 8 AO ė Aioll Niud a V. al s Jr dia 5 a E a P ae \
ri š vėjas 32 \
EE mų. abu E VA LT mą prie "ai. oiaa \
Di. D.. DtivabvčkaaAaITiaii. COm \
Eieoykoi Įidiaio ALT i A į Lt sr \
k Ea ė \
WI... TAM mi. 1 \
k PARA i 8. BI \
WWW. TVD.lt \
x. p , \
a 77 \
k Fr me + FI r pras, t arenas r p ks šo E r iš x aa AP 8 \
"LF EF K r TF i Ar i į P, 18 FF iš A 8 į r s \
VLE FF NIE LL FN ROA LA EV OAS Vl, E NELAĖ NV PAST VE T NK E NV V \
a. s09 3 jp gpreinų Tal Pt pg G FS ar agiamaaii 3954 T. mai no \
i , į ED FK Y Elė V bob i FF J fam ba EF FIAT ERA . \
p. i E FEVN E AP FREE Vv. V Lali VE Vu V Li Lo EEE VE EE EF Vt o 0 \
6 ni aus Aialaita m. ar ZR Ri nr EE Er RPN ET EIK E KFNVYEB KA CC ai \
p pa FKE TTK E EEE E KFYEE EE NN. FEFF FK VA r.F Ąą i Vai Ą kų ta. . \
i KHR. FE FF EE Ft J. LBA XEC pie J FI VIN i FĮ CA VAL L FI Va E \
"A+ Vi a E FC J. LPA FEI i PT VY E TF. A š t \
kZ WP Vv L il E. ud albo L ta. Ragas" E Sp E Či w i j \
si sr er a. šiai aa a p m i i T I - r a \
FK KN EOS TEC SIERIERA Į DEBCY IE KT, \
avi Gp Na. E FC FN EF FT FX KN. i FR Ą \
"V V L. v E EFF VIFP NE RER B Šiam t i T 3 \
k e , 8 Ė Či \
7 r k. 1 \
D I. 7 r p \
par ji i Ravš g jj \
i k , č il',


    'a E. a ia apr, Naoto sta a O o ŠE \
akiai RED pre ini SS Taetani Atia š \
6 ralis. E Otaka ia , \
Noe ET Ina Rs VS Rs sodai a EST \
Lia Te das O gi Makoto ŠE ES ss T Va OSA \
0 ae era De S į \
5 si Ė 52 a Kia e EA 47 07 votrenejjias \
20 marą p i iais se air Dai \
ata ES Sinai titano sa \
ek TS a mk Pitos. tirs . \
is Par ua o Mia ia ia ra \
x 2 3 T o s a ą 4 \
TaĖ , I Ąą alis sai. a TT leirisio 00 skir, \
+ is 0 sd 4 a ar gacamamss LP Ara rai r Tpso \
t rrEZESTE S ar \
snd. T Toiilą ss ss a iai p i \
m Dai Load ni Fua --mm kū j a Ta Zaggtiimnis - m P - ms a \
P Az FSK FTUHRTO VERTINIMO \
saitų 20 a 000 aa Ššrsę- ap is as asų Aa Ki Fr B 4 j j j y j į k P \
"ELO gaa T T sr i šk kūnai , sa R Ė kinai m. r Fa \
a 08 mas \
a , ir m rą a \
ir ra , r i. F r 3 \
2 m M. S P \
As ORE EEE Er Fm EK Et \
j X Fra Ša su a m. Ąą i \
į Mid t I I Gili a ka Rana" ad p. - \
Iokilnaaiamiaia. ir. kilnaimameais tiertn vartinfniauc acichtantiao , \
k + TKAT E TA Mt PIRSPTCEITE TAU TSS LAAELRSS VAL IR B Kia CL. DOC Fi. \
ai \
Š s - r i i ki m aa is AS a, Ma Ta Y \
arm EEST E EE DT TT 2 E to. bana r 54 PF AB ra E -. \
ai. 4i 6. M I , 7, a g. mv fr EL į 2 P \
SESI šį MR. + ir IVECUJZ. LTE... 2 LE UL U+ 09 \
Ą p - a - g i \
VvVIENIEUS 11 a vs EI Kai \
gai Press lr oriai f G fm t p. V. ima 4 0 Ja im, \
7 AA Tas Ei ia, ap Ša D k a. r B ra -iIia m T. r \
ast 0a87 Sui 8 AO ė Aioll Niud a V. al s Jr dia 5 a E a P ae \
ri š vėjas 32 \
EE mų. abu E VA LT mą prie "ai. oiaa \
Di. D.. DtivabvčkaaAaITiaii. COm \
Eieoykoi Įidiaio ALT i A į Lt sr \
k Ea ė \
WI... TAM mi. 1 \
k PARA i 8. BI \
WWW. TVD.lt \
x. p , \
a 77 \
k Fr me + FI r pras, t arenas r p ks šo E r iš x aa AP 8 \
"LF EF K r TF i Ar i į P, 18 FF iš A 8 į r s \
VLE FF NIE LL FN ROA LA EV OAS Vl, E NELAĖ NV PAST VE T NK E NV V \
a. s09 3 jp gpreinų Tal Pt pg G FS ar agiamaaii 3954 T. mai no \
i , į ED FK Y Elė V bob i FF J fam ba EF FIAT ERA . \
p. i E FEVN E AP FREE Vv. V Lali VE Vu V Li Lo EEE VE EE EF Vt o 0 \
6 ni aus Aialaita m. ar ZR Ri nr EE Er RPN ET EIK E KFNVYEB KA CC ai \
p pa FKE TTK E EEE E KFYEE EE NN. FEFF FK VA r.F Ąą i Vai Ą kų ta. . \
i KHR. FE FF EE Ft J. LBA XEC pie J FI VIN i FĮ CA VAL L FI Va E \
"A+ Vi a E FC J. LPA FEI i PT VY E TF. A š t \
kZ WP Vv L il E. ud albo L ta. Ragas" E Sp E Či w i j \
si sr er a. šiai aa a p m i i T I - r a \
FK KN EOS TEC SIERIERA Į DEBCY IE KT, \
avi Gp Na. E FC FN EF FT FX KN. i FR Ą \
"V V L. v E EFF VIFP NE RER B Šiam t i T 3 \
k e , 8 Ė Či \
7 r k. 1 \
D I. 7 r p \
par ji i Ravš g jj \
i k , č il',


    '. , a. 4 Ta AT \
š S \
t ir 3 aki \
t \
- Et ja \
Kati \
j 2 S \
s k 4 k \
j r as a i \
r io R \
ai \
P. 4 ui \
- \
i kr \
y LT \
šo Ė \
, as a \
j i \
8 4, \
t \
i akt \
ri sl KI V \
i M xi. \
r Jan \
iot a \
š ša kasis \
fi j \
Hai tai \
Ė r g 2 t kada AB na Kia k \
L , šį T S giš. I Lia i \
res i f 4. ET Urio B ja Ti \
į , į r Loa ei Yra IA \
kom , Aro p Ep j Mr - i i aa Vas \
Ę Ee nadl tą. rija Či didi Bs Soso \
kų spa" , 5 r I- Tr iš Tik 8- seip "Taa Fo \
, f tt ja , Ų tani i Tata T. Ą 1 Ari A \
ę 1 p i. a sE Manic aa AE RS Ė pats Di GR ja Teų 2 8 \
į z 7 r j diijaė I o AO atolų Mg ve ta a aa si arši JS9O I \
i p , i AGT G TE V ii aTa MS as \
ją Ake j į sirai L r s87 iais ŠIkials  I It V rs SS MS SE G as \
/ fa j Šai KT b airiai. Eik E BRT Bt moja ai AARC aaa E ES to MS A \
, r 190 Pr id, es sti Taa rs Za Jaeiiais Kaiasi ati son ra oi ikos" Jei sin \
4 gei s GMO Taa Ad Akis CE ii Pili šreko us" DIY t Es bri 2 Mintimis Ta, \
iz i į BO BAI, Ar TŲ p p namai Aira Ta R ai jai MKE "iptiai sosrssi t Kosos EEE \
p i ba ski salė 6 į i kas Skai Oo aa IO ero Ailaibi T ai ak ias Piiakėis T g į \
j sto gta k ats ečų pk akies S a S ro is. Za E tagai "Ana. Gas En D \
4 4 Ę kabo Edi Epakisė 2 5 T ss ai ia, 80 Ska sell akys T šanai Mila 7 JP akos I ar \
A , r r i Vartų, saitą af E tibia ali tia oi eo as , k E st a aaa pries Šis Eaaika AE sak si vio uno AP \
t ra r ats Aiks eriių ti 54 4 tia 6 kiek T Nagi anairnrėes - - J. ir io ta 0 oi sl , \
A iz iais Kia P AE j "aiiaiidia AIA Oi sr ISK 5 eetisi Veseiyii aliss. ee ja 4 Tos Paiaa \
Ė ii , Ą 258 6 af atišias cooi ra na KES JP o r ui Ar 8 4 4 t vi Ta i aa eisi Too Cis p \
, , t Arija įnag 7iiOŲ AL efilaio a UE a Lat Saias "870 est ira Taranto Oita agto said iagpiaaniiaosi jo Kg 2O "as riai Gas aki i , 4 \
+ Kk Si to gig Ska setai Talkos At a SiTe ta Ei e air hasiar S Titni Zak aut T SE Ė Eiaii I ata, TER T ša is ai \
ą 4. 2 Ų 2 aso son kis nai ių Valo ciaiką E siaą ata si Iron Dos Yra, tao SE en 4 S Sai ane Euros 1 ini a To na \
AE są rs kasų Uri saaa. Pt oakis Drs Ėtte so Sr LU čia g at E sūris Šia sak okra LET Halis šau ša Kritinės S To 1 \
ais a Ą ar sc ki jr eat p Po Dale ra Adis. RI sai. v D naanajės S BBL CO vainikai eto ašis RE RS te +. 27" Atass p \
Serviso f 181 r g Pa vaad 2, lp Vršs t ais Aid sat Kk Ma ša ai iai AB I Pa, ap Seat ka ri am oras 4 itisči aa US A \
x "ns Ara Ek si Tai Ka ik S Ks rr ata Rais BTI I AS go o Do Makas I MS o arų \
i krona dos iaaki sptsters egkiniI anbditKre take Garso Jia S. VE sa os M MST T Tenka et S Ass 5 Asia. gos jo \
narė Gizos Terasa oset gi bs S Es tas Jų rope O Tab Ms sara aaa aros MM NP S g aa TEO \
si ti sakai Kra RRKT iol Earn Mai rai Vina 2019 Aeiškii SE o asi ai ačių Taa vinių toi ses Nui d i \
Kt as in uoisi  Ns sai CpI Sp It Mirta S Sakei akis TAS i Kakas, MAS SDB Us Km ka S NE SE K gmT aig ai ais Ai ais r aa \
jį a 1 sr r 5 to Ąpsilks ai Sari tt, rs Sa ka ašS ak Ųų RS Muy I V Į sr Tais a 21" kasis is kN ia 2 p \
i iu atei Mais aaa atkasa KAUKAS TD ap Ero US TA LEI paie ri pik gos 5 - \
i "sė "tai Vo Gr ka kraitis Sk TT As ES TO Boa Ek BEE Kakas SS i \
a je , S V atioio sri Mai Kė js Morka ės JET ri Pasa as Kakas E r San m E S V EE GT k ros Est ais i \
i g Li A t Kanas k Irun Sea a ala GKLE as Rei a T Casi J ata Ziiias I atė ų raigia tatteis ora Dao Kiek į sri os \
š . 4 AX r niek setai asai Tj "te Saitas oO SAS M Eau asi č ia \
i Aaaa Mis Kk kia Ls IS pKsti Es eš xe taas darei ES GK ae ia \
a akiai, keis saaa Sis AAA ias aria sakai Oktanas DDT Aiks Tl AT ja Baro ja T eat Ap Uma Kappa 1 \
Ei, ša ais VO AS aki Vi šo st ai arr Tos Tasas 2 Lb gaaki SE A K os ATI ao aa E AP ra ia ki , \
ir. sa es SA Iš are Gia Ti TK G S GKS AR AE ESA \
j + t si aks st ep Jis Wypaias Sis TM sviiaki ao Pa Ainiai oda t Ta AT Aina sanis Mapas ganė p Eto ra \
4 i į ė Sin sro ae a Gas It a klija Aaaa Ki gai Tt ati is ala ia r y \
i j ogi aiste Latas "pi Anai iso o ESS Ss eis Pei ii osios Clap Aa KS J sių . pičias Uaė \
ti . į i Tais ai Eos aaa ata. ata akiai S ALŲ, A is aaa Pa , VS ma Zz  - i L. , i \
97 j Ius ias ji Ka Garis Ua Vi aiš aru, AE aa "a vis S ka io į sa Ei ji I ę i \
6-5 voniai od sači ass sių Bt masis id Aue S kata r g 8 lao a gta Ei į "Ak r r a A g į r \
o i Ti Manto Is i ri Aria šu 0 i šiai i Kai Ta T tas \
ų 4 7 gi Nurgg sfB star Kata ali varai, M Ta kr rata sy ak pyiia tolo i tail aaa ias Li Megė as rų i j j M nis ją \
r , sai ie ii iii i E ao j r ietal jogas A64f B YdA. as. getą Tania V i a 2 ,  YZ \
ai t g i tė Ir G aki Tas Tiot sat alūs 0 Jr SK if av a r 4719 ė \
. į k jj jr a iai sie i ala ska sein AST iĖ Epas ar sias A JS 2 / i j \
ao šalis adis arai ta GEĄ se šasi Tu a šlapi Mios Ha Iš CE ae E i \
j ara Irakas. Aaa Opel Kas Eria "Bi S USS ads rdt Si Ai Ei a S IKS 57 atakas giigk i \
m keri Kg Sa EMS Traian Tas As aaa E ia \
a . . as ios ien kAp Uris ši V tris S Attia, Lkskų Aroiiiis JS A i \
ik. pirkliutėsiiDerauto.lt T WWW. m \
"T A , p stati diiaai t Duaderke ais asai ri noios 0 Tso ti 0 ar g P \
2 k š Veino Tos a oriai, Kits Traagtkii tao kratas i į k \
p er desi a st Taka ss oMŲ Patri Al GR aa aaa \
a į Či ao ES eitu Tarit ae Abekršios nia sass a aa aka \
re y r Ka dkšioi al ims. ŠOKAS Da ar 4 evis T aklėn re Jasiiyka r \
i , į sans, tatoo tetis abato o ras tros Mo ius ki \
pome i šąfS Abi 0 tais, dk asi kepti o Eksa e Mesa nari Biko a 3 \
ką, d r p S k sti 4877 Viso NE DNR Asi Ais Ve Palais ii ies Fint r \
2 Ke L pr ių. S p cats Aa Eau kos X 409 4 \
"An as j š tar Asi si I AS E a an \
das ėvis i / i į sai isto a Stai ZA akis str sPuafi d e 4 \
ra -. P i r ir sias "ai Airiui a arsoi a r j , \
sa I ist 5 ci 1 asa sa sai Las E šs- aa 2 j p \
ia. di. i ar LD sis aa g 3 iui UI Toi Rją ia t sa f ar 5 r. y sr',


    '. , a. 4 Ta AT \
š S \
t ir 3 aki \
t \
- Et ja \
Kati \
j 2 S \
s k 4 k \
j r as a i \
r io R \
ai \
P. 4 ui \
- \
i kr \
y LT \
šo Ė \
, as a \
j i \
8 4, \
t \
i akt \
ri sl KI V \
i M xi. \
r Jan \
iot a \
š ša kasis \
fi j \
Hai tai \
Ė r g 2 t kada AB na Kia k \
L , šį T S giš. I Lia i \
res i f 4. ET Urio B ja Ti \
į , į r Loa ei Yra IA \
kom , Aro p Ep j Mr - i i aa Vas \
Ę Ee nadl tą. rija Či didi Bs Soso \
kų spa" , 5 r I- Tr iš Tik 8- seip "Taa Fo \
, f tt ja , Ų tani i Tata T. Ą 1 Ari A \
ę 1 p i. a sE Manic aa AE RS Ė pats Di GR ja Teų 2 8 \
į z 7 r j diijaė I o AO atolų Mg ve ta a aa si arši JS9O I \
i p , i AGT G TE V ii aTa MS as \
ją Ake j į sirai L r s87 iais ŠIkials  I It V rs SS MS SE G as \
/ fa j Šai KT b airiai. Eik E BRT Bt moja ai AARC aaa E ES to MS A \
, r 190 Pr id, es sti Taa rs Za Jaeiiais Kaiasi ati son ra oi ikos" Jei sin \
4 gei s GMO Taa Ad Akis CE ii Pili šreko us" DIY t Es bri 2 Mintimis Ta, \
iz i į BO BAI, Ar TŲ p p namai Aira Ta R ai jai MKE "iptiai sosrssi t Kosos EEE \
p i ba ski salė 6 į i kas Skai Oo aa IO ero Ailaibi T ai ak ias Piiakėis T g į \
j sto gta k ats ečų pk akies S a S ro is. Za E tagai "Ana. Gas En D \
4 4 Ę kabo Edi Epakisė 2 5 T ss ai ia, 80 Ska sell akys T šanai Mila 7 JP akos I ar \
A , r r i Vartų, saitą af E tibia ali tia oi eo as , k E st a aaa pries Šis Eaaika AE sak si vio uno AP \
t ra r ats Aiks eriių ti 54 4 tia 6 kiek T Nagi anairnrėes - - J. ir io ta 0 oi sl , \
A iz iais Kia P AE j "aiiaiidia AIA Oi sr ISK 5 eetisi Veseiyii aliss. ee ja 4 Tos Paiaa \
Ė ii , Ą 258 6 af atišias cooi ra na KES JP o r ui Ar 8 4 4 t vi Ta i aa eisi Too Cis p \
, , t Arija įnag 7iiOŲ AL efilaio a UE a Lat Saias "870 est ira Taranto Oita agto said iagpiaaniiaosi jo Kg 2O "as riai Gas aki i , 4 \
+ Kk Si to gig Ska setai Talkos At a SiTe ta Ei e air hasiar S Titni Zak aut T SE Ė Eiaii I ata, TER T ša is ai \
ą 4. 2 Ų 2 aso son kis nai ių Valo ciaiką E siaą ata si Iron Dos Yra, tao SE en 4 S Sai ane Euros 1 ini a To na \
AE są rs kasų Uri saaa. Pt oakis Drs Ėtte so Sr LU čia g at E sūris Šia sak okra LET Halis šau ša Kritinės S To 1 \
ais a Ą ar sc ki jr eat p Po Dale ra Adis. RI sai. v D naanajės S BBL CO vainikai eto ašis RE RS te +. 27" Atass p \
Serviso f 181 r g Pa vaad 2, lp Vršs t ais Aid sat Kk Ma ša ai iai AB I Pa, ap Seat ka ri am oras 4 itisči aa US A \
x "ns Ara Ek si Tai Ka ik S Ks rr ata Rais BTI I AS go o Do Makas I MS o arų \
i krona dos iaaki sptsters egkiniI anbditKre take Garso Jia S. VE sa os M MST T Tenka et S Ass 5 Asia. gos jo \
narė Gizos Terasa oset gi bs S Es tas Jų rope O Tab Ms sara aaa aros MM NP S g aa TEO \
si ti sakai Kra RRKT iol Earn Mai rai Vina 2019 Aeiškii SE o asi ai ačių Taa vinių toi ses Nui d i \
Kt as in uoisi  Ns sai CpI Sp It Mirta S Sakei akis TAS i Kakas, MAS SDB Us Km ka S NE SE K gmT aig ai ais Ai ais r aa \
jį a 1 sr r 5 to Ąpsilks ai Sari tt, rs Sa ka ašS ak Ųų RS Muy I V Į sr Tais a 21" kasis is kN ia 2 p \
i iu atei Mais aaa atkasa KAUKAS TD ap Ero US TA LEI paie ri pik gos 5 - \
i "sė "tai Vo Gr ka kraitis Sk TT As ES TO Boa Ek BEE Kakas SS i \
a je , S V atioio sri Mai Kė js Morka ės JET ri Pasa as Kakas E r San m E S V EE GT k ros Est ais i \
i g Li A t Kanas k Irun Sea a ala GKLE as Rei a T Casi J ata Ziiias I atė ų raigia tatteis ora Dao Kiek į sri os \
š . 4 AX r niek setai asai Tj "te Saitas oO SAS M Eau asi č ia \
i Aaaa Mis Kk kia Ls IS pKsti Es eš xe taas darei ES GK ae ia \
a akiai, keis saaa Sis AAA ias aria sakai Oktanas DDT Aiks Tl AT ja Baro ja T eat Ap Uma Kappa 1 \
Ei, ša ais VO AS aki Vi šo st ai arr Tos Tasas 2 Lb gaaki SE A K os ATI ao aa E AP ra ia ki , \
ir. sa es SA Iš are Gia Ti TK G S GKS AR AE ESA \
j + t si aks st ep Jis Wypaias Sis TM sviiaki ao Pa Ainiai oda t Ta AT Aina sanis Mapas ganė p Eto ra \
4 i į ė Sin sro ae a Gas It a klija Aaaa Ki gai Tt ati is ala ia r y \
i j ogi aiste Latas "pi Anai iso o ESS Ss eis Pei ii osios Clap Aa KS J sių . pičias Uaė \
ti . į i Tais ai Eos aaa ata. ata akiai S ALŲ, A is aaa Pa , VS ma Zz  - i L. , i \
97 j Ius ias ji Ka Garis Ua Vi aiš aru, AE aa "a vis S ka io į sa Ei ji I ę i \
6-5 voniai od sači ass sių Bt masis id Aue S kata r g 8 lao a gta Ei į "Ak r r a A g į r \
o i Ti Manto Is i ri Aria šu 0 i šiai i Kai Ta T tas \
ų 4 7 gi Nurgg sfB star Kata ali varai, M Ta kr rata sy ak pyiia tolo i tail aaa ias Li Megė as rų i j j M nis ją \
r , sai ie ii iii i E ao j r ietal jogas A64f B YdA. as. getą Tania V i a 2 ,  YZ \
ai t g i tė Ir G aki Tas Tiot sat alūs 0 Jr SK if av a r 4719 ė \
. į k jj jr a iai sie i ala ska sein AST iĖ Epas ar sias A JS 2 / i j \
ao šalis adis arai ta GEĄ se šasi Tu a šlapi Mios Ha Iš CE ae E i \
j ara Irakas. Aaa Opel Kas Eria "Bi S USS ads rdt Si Ai Ei a S IKS 57 atakas giigk i \
m keri Kg Sa EMS Traian Tas As aaa E ia \
a . . as ios ien kAp Uris ši V tris S Attia, Lkskų Aroiiiis JS A i \
ik. pirkliutėsiiDerauto.lt T WWW. m \
"T A , p stati diiaai t Duaderke ais asai ri noios 0 Tso ti 0 ar g P \
2 k š Veino Tos a oriai, Kits Traagtkii tao kratas i į k \
p er desi a st Taka ss oMŲ Patri Al GR aa aaa \
a į Či ao ES eitu Tarit ae Abekršios nia sass a aa aka \
re y r Ka dkšioi al ims. ŠOKAS Da ar 4 evis T aklėn re Jasiiyka r \
i , į sans, tatoo tetis abato o ras tros Mo ius ki \
pome i šąfS Abi 0 tais, dk asi kepti o Eksa e Mesa nari Biko a 3 \
ką, d r p S k sti 4877 Viso NE DNR Asi Ais Ve Palais ii ies Fint r \
2 Ke L pr ių. S p cats Aa Eau kos X 409 4 \
"An as j š tar Asi si I AS E a an \
das ėvis i / i į sai isto a Stai ZA akis str sPuafi d e 4 \
ra -. P i r ir sias "ai Airiui a arsoi a r j , \
sa I ist 5 ci 1 asa sa sai Las E šs- aa 2 j p \
ia. di. i ar LD sis aa g 3 iui UI Toi Rją ia t sa f ar 5 r. y sr'
]