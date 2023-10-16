with open("flag.txt","rb") as f:
    flag = f.read().strip()

m = int.from_bytes(flag, "big")
e = 65537

from Crypto.Util.number import getPrime

for x in range(10):
    p = getPrime(1024)
    q = getPrime(1024)
    n = p * q
    c = pow(m, e, n)

    print("n =", n)
    print("c =", c)


'''
n = 17524722204224696445172535263975543817720644608816706978363749891469511686943372362091928951563219068859089058278944528021615923888948698587206920445508493551162845371086030869059282352535451058203615402089133135136481314666971507135484450966505425514285114192275051972496161810571035753943880190780759479521486741046704043699838021850105638224212696697865987677760179564370167062037563913329993433080123575434871852732981112883423565015771421868680113407260917902892944119552200927337996135278491046562185003012971570532979090484837684759828977460570826320870379601193678304983534424368152743368343335213808684523217
c = 6870605439714128574950893771863182370595667973241984289208050776870220326525943524507319708560433091378319367164606150977103661770065561661544375425887970907060665421562712515902428061727268441585629591525591001533188276465911918724808701356962871139957343861919730086334623932624184172272488406793955068827527130338853980609365042071290967556159598511667974987218999253443575482949258292953639729393456515185185102248985930422080581185292420347510600574229080211050520146551505605537486989306457793451086767402197128573781597156939709237045132856159368959981648969874765462190363842275826077556314448408825308218451
n = 24974121071274650888046048586598797033399902532613815354986756278905133499432183463847175542164798764762683121930786715931063152122056911933710481566265603626437742951648885379847799327315791800670175616973945640322985175516271373004547752061826574576722667907302681961850865961386200909397231865804894418194711076667760169256682834206788730947602211228930301853348503098156592000286467190760378847541148772869356389938999094673945092387627113807899212568399028514283219850734634544982646070106811651490010946670117927664594365986238107951837041859682547029079035013475238052160645871718246031144694712586073789250183
c = 10324627733161143472233272675096997859064721978612320424254305978486200326061730105384511258706433940176741256952824288120499229240005823611541292676234913505775165761543820764046537413943393325463602612485849366939102550336256797820440347815027443410399157963547486098366749815425187247171697678576246606105486928212486117878157055321965270364583625270716186820068538749425299073309429589410882809098930213978117176627031795312102177342499674234163614021182116065492884880492891668658240362567156235958605768725892407536211503981819707919444725863397622629226309480836486427388484176463279384813974310500625102568341
n = 14215826065753265334521416948225868542990756976323308408298887797364519400310818641526401662106853573185085731682502059761982246604277475488691297554851873224516934619888327644352138127883043558424300092247604877819821625587944308487310522092440517150600171819145803937177931473336108429889165189521078678397694303305705260759351843006130968234071638035667854938070597400634242396852782331461576526836227336952718230741560369621645218729592233657856104560425642219241082727756696967324334634822771842625681505869025740662258929200756109704988223034840699133778958569054445520305361142302393767439478256174414187983763
c = 415916446053083522663299405080903121619846594209033663622616979372099135281363175464579440520262612010099820951944229484417996994283898028928384268216113118778734726335389504987546718739928112684600918108591759061734340607527889972020273454098314620790710425294297542021830654957828983606433731988998097351888879368160881316237557097381718444193741788664735559392675419489952796677690968481917700683813252460912749931286739585465657312416977086336732056497161860235343155953578618273940135486362350057858779130960380833359506761436212727289297656191243565734621757889931250689354508999144817518599291078968866323093
n = 12221355905532691305226996552124162033756814028292708728711809229588190407700199452617060657420166395065565154239801465361510672853972152857415394695376825120759202857555325904640144375262531345320714166285999668052224661520834318497234299585219832943519644095197479639328120838919035625832361810964127485907587199925564724081163804724975965691571850962714258888527902920462746795712011579424322515292865504642938090200503979483095345893697972170153990274670257331483858538617460680462369680572833191232126527727222302641204529110948993583190295067970240051042000918629138767209918572311469915774910003970381965123241
c = 2248834602646305164283014556051672824689884721514190813323189875541899566338153534858709617544459297836048770439230174669883719627734394673012731609952869246171300132019334542245094425654362711870373095782083791160029789553806741967408922001051006100049326921742208757147339981269528740944842177729701945606827918253016001436218891580980192743564642120923356793292885805519110411357830040053435569937296612987581482128241218218550319154933831743819546558930918761162723110000328532730751591375727881221199739397698390594797621758011191224528339478784930214820615602510460640307707682865125229937141010351138099874025
n = 18152103454920389919231636321286527841833809319334215885641536161086810144890443857211776387914779781628740172079478910188540146498426564211851629962338413488555121865779016981727229209606498886170396500155102635962395243364899026418106378234307821492609778555173516000309435730752571818439328803899462791834490025768785383592935046996428331508608555503567191807692523852530836008436655164751054189301721070209363416058642811329040202582026786024825518381761299547703962502636888833428457116986351812252188468878701301184044948733274488264320930936362549028124581962244201377136969591119942276742760215403738913067567
c = 2797812094994121597295362327809389195134238119144547570610194659000554967367804835006774413888965325870488368112707535584687083342412367127561646136089638402907513075405746055834487062923240856950047936297155455745928810738711368950139327254040579266046642851362228893522740216519732851152162928545416236075387903789535000820423985522550638100049857678600662008021574841083416323980817348573062083159710189689337626277009675683473560325178417766400002763719953723259300977655801234386662217462862844994462505601804422871991694828697337752697234180117437785537788728412520613916334045368736691714704501962513954509705
n = 22877887459293720334652698748191453972019668578065068224653972884599636421200068659750242304040301306798039254241668648594556654589309801728248683586229288074709849246660525799452637187132633064172425677552176203292787732404537215347782229753837476655088638984496409603054524994383358547132112778403912563916886533181616856401929346567686400616307916690806467019665390260267596320840786982457521423178851498130935577260638269429250197050326097193841333205073650802709022947551398142692735680419453533128176592587955634333425401930362881423044363132586170013458300714163531162544301477356808388416864173949089028317961
c = 12271947322974809255127222556723394446467844330408506340843897575503534175121932185624776713618037572593449207329510171212097269297133492090526270770286000839978630002819714376964416081198925899119135271459404333829811516667576167576916805217016117373027245648473458331936273975110163065432285322832123169216976420362833557809289561705091817949915218278430834098156335989014645979633658818904753942786129126233956314517292746008579152368541316795082120147520597254020266752859205131887527661767589367756335766220841483940854397440079467053684289006956034944336788288196391829411432383541473132962783883758561108297747
n = 19844333358004073542783728196775487079202832688982038135532362073659058674903791697765527614270399097276261983744620537925712167578187109058145015032736796457938148615396547198728652435169126585595701228287449135664667959433491335769206692390262797325133960778920452511673878233190120432257482339068405290918739453464061987163074129048150451046315248186376609350095502130018696275764450248681787926130463463923862832714969425813770847493135627599129546112143050369344208092649256659330284904392961574494907186727388685504929586018639846040474616307662546605623294842316524163106100888851228858194942825157286544846177
c = 9531264751315473345056673937611382755236533664089452852716992791452558274873158812669513178040971923528201631609089069182049526587423864397527252061341857426422965190913745048414029690931254119437249218321954899956104589066479231204536856131403590472063496956452030342299863907499976917750846369802185896519725837163530049157920978007252920334447236842959033879772444475877613295594785710745889554296655932909212643500877218304116451889820444820534937901427158918411546484157737612926382420354101675658160847653151539420222526999426483473829341628599881460824765758346670633385844187252696874025582747177333702736465
n = 16956880944655068255446705024149899655327230949463546092744762226005904114738078692036960935391303255804754787864713189658290361949509917704853428701870609882427423574672772606814823959758208695540116440342488334213300943604780971422918744381486937517952553797134323570131582724393100092308466968491068503301604506186521656059375518680612292667310641047190088814753025794048591445267711939066523165042651430468971452726568222388482323097260496415484997546126185688914792795834046855221759289007609518312601640548469651358391745947588643697900883634533872314566389446271647587564348026861264979727062157272541149018781
c = 16110326928338602237561005337578085623028116490564329920738844771341250444164294693848130674347672763073995755532723894042946521372321947507527854966013459795492930736187058535665041545095683801386814190612817128504426590828954205050425979880047802547011117626354405687170961272200066258220699329112978151044633994329352673342582175349200008181837211288847301836681860817044391028992501763375849046751094019224570802498414368189170656992427042010362385494565216988561215657424755648213390551881450141899860811844684546992754530755092358644968088017107313907435586729574798046187046145596726569637758312033849476689378
n = 16472195897077185060734002588086375750797253422014472876266294484788862733424113898147596402056889527985731623940969291811284437034420929030659419753779530635563455664549165618528767491631867637613948406196511848103083967995689432928779805192695209899686072900265108597626632371718430059561807147486376536203800038054012500244392964187780217667805308512187849789773573138494622201856638931435423778275004491853486855300574479177472267767506041000072575623287557610576406578525902565241580838652860552046216587141709709405062150243990097835181557208274750462554811004137033087430556692966525170882625891516050207318491
c = 11867731823522211833301190385669833752050387304375114576570892885641949969365352586215693183003550684262313893105989683214739695968039039944442567581277252581988489020834299896625977474857889570528169919064941042132119301236852358823696947330423679033138054012027878783478922023431469564210485180679933264749281963405243082505688901662659030897104957499953192201440290084373968716271056483463909282407034181891901928790601973222643210525000717355062752079302291729448234374709852429885984987094307177760741403086538949190424454337896501402430653783597070178968921411867485584517214777073301007918941216316241784521708
n = 13890749889361612188368868998653029697326614782260719535555306236512452110708495623964530174188871342332417484996749651846510646453983388637377706674890018646246874688969342600780781646175634455109757266442675502522791531161284420286435654971819525519296719668701529481662071464145515727217108362496784024871976015116522898184301395037566514980846499856316532479656908169681719288258287756566886281183699239684997698487409138330229321935477734921670373632304542254938831218652340699024011371979519574576890581492623709896310465567043899767342676912434857372520308852745792360420376574037705943820090308501053778144141
c = 6250115196713939477947942995075509357173312813431601073354390451609559579925704891503987992181988654989477525811826607070378476102616752398280691012244301950194800995432882828020405062344160270290542566163969692748126314259624623341922057435728127596172871894887055305291345372720594481096374310285437492746765510292863238933163142677773310305789984897974266961231555124787205980411992251387207335655129551950825339766848166539671565212408741432649813058363660321480995187545006718837863674527475323414266732366507905974800565463011676462244368010182725161416783875646259625352308599198614681446394427674340328493047
n = 21457499145521259498911107987303777576783467581104197687610588208126845121702391694574491025398113729462454256070437978257494064504146718372095872819969887408622112906108590961892923178192792218161103488204912792358327748493857104191029765218471874759376809136402361582721860433355338373725980783308091544879562698835405262108188595630215081260699112737457564998798692048522706388318528370551365364702529068656665853097899157141017378975007689790000067275142731212069030175682911154288533716549782283859340452266837760560153014200605378914071410125895494331253564598702942990036163269043699029806343766286247742865671
c = 6269656777204332618433779865483197625538144405832409880710764183039800286008967127279281167109250083159801218370191973055663058165456565194979210256278526713608759141588082614531352489547674696723140599892318118960648862531538435596775798128845789504910467783731144808685373807716609662688064728614003904579841055786083326311313295311152563668422289435606771091246147867715987583149743032723028324394173498623642539175178996531881058274717907066845565199058931743481410454382746158558886667761300257488769795092777021292335562818583719708133179974425584610403335487082478848975656282384575767178925517257692365828720
'''